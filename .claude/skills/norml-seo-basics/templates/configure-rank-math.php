<?php
/**
 * Idempotent Rank Math + WordPress Site Icon baseline.
 *
 * Copy this file into the project source of truth, replace the configuration
 * block from verified project facts, commit it, then run after Rank Math is
 * installed and active:
 *
 *   wp eval-file wp-content/themes/{theme}/scripts/configure-rank-math.php
 *
 * The script deliberately aborts while REPLACE_ME values remain.
 *
 * @package NormlSeoBasics
 */

declare(strict_types=1);

if (! defined('ABSPATH') || ! defined('WP_CLI') || ! WP_CLI) {
    return;
}

if (! defined('RANK_MATH_VERSION')) {
    WP_CLI::error('Rank Math must be installed and active before this script runs.');
}

/*
 * PROJECT CONFIG — replace only from approved project facts and visible content.
 * Relative image paths are resolved from the active theme directory.
 */
$config = [
    'site_name' => 'REPLACE_ME',
    'alternate_name' => '',
    'entity_type' => 'company', // company | person
    'entity_name' => 'REPLACE_ME',
    'seo_title' => 'REPLACE_ME',
    'seo_description' => 'REPLACE_ME',
    'focus_keyword' => '', // Keep empty unless verified by project research/context.
    'locale' => 'en-US',
    'site_icon_path' => 'assets/images/site-icon-512.png',
    'site_icon_filename' => 'site-icon-512.png',
    'site_icon_title' => 'REPLACE_ME site icon',
    'site_icon_identity_source' => 'REPLACE_ME approved identity source',
    'site_icon_is_organization_logo' => false,
    'organization_logo_path' => '',
    'organization_logo_filename' => '',
    'organization_logo_title' => '',
    'social_image_path' => 'assets/images/social-card.jpg',
    'social_image_filename' => 'social-card.jpg',
    'social_image_title' => 'REPLACE_ME social card',
    'social_image_width' => 1200,
    'social_image_height' => 630,
    'single_author_site' => true,
    'sitemap_post_types' => [
        'page' => true,
        'post' => true,
        'attachment' => false,
    ],
    'sitemap_taxonomies' => [
        'category' => true,
        'post_tag' => false,
    ],
];

$required_strings = [
    'site_name',
    'entity_name',
    'seo_title',
    'seo_description',
    'site_icon_path',
    'site_icon_filename',
    'site_icon_title',
    'site_icon_identity_source',
    'social_image_path',
    'social_image_filename',
    'social_image_title',
];

foreach ($required_strings as $required_key) {
    $value = isset($config[$required_key]) ? trim((string) $config[$required_key]) : '';
    if ($value === '' || strpos($value, 'REPLACE_ME') !== false) {
        WP_CLI::error(sprintf('Configure $config[%s] before running this script.', $required_key));
    }
}

if (! in_array($config['entity_type'], ['company', 'person'], true)) {
    WP_CLI::error('entity_type must be company or person.');
}

if (! is_array($config['sitemap_post_types']) || ! is_array($config['sitemap_taxonomies'])) {
    WP_CLI::error('Sitemap post-type and taxonomy maps must be arrays.');
}

$organization_logo_fields = [
    trim((string) $config['organization_logo_path']),
    trim((string) $config['organization_logo_filename']),
    trim((string) $config['organization_logo_title']),
];
$organization_logo_field_count = count(array_filter(
    $organization_logo_fields,
    static fn (string $value): bool => $value !== ''
));

if ($organization_logo_field_count !== 0 && $organization_logo_field_count !== 3) {
    WP_CLI::error('Set all organization_logo_* fields or leave all three empty.');
}

if ($config['site_icon_is_organization_logo'] && $organization_logo_field_count === 3) {
    WP_CLI::error('Choose either the approved Site Icon as logo or a separate Organization logo, not both.');
}

$homepage_id = (int) get_option('page_on_front');
if ($homepage_id < 1 || get_post_type($homepage_id) !== 'page') {
    WP_CLI::error('Configure a static front page before applying homepage SEO settings.');
}

$theme_directory = get_template_directory();

/**
 * Resolve a project asset path without assuming an OS-specific absolute path.
 */
$resolve_asset = static function (string $path) use ($theme_directory): string {
    if ($path === '') {
        return '';
    }

    $is_absolute_unix = substr($path, 0, 1) === '/';
    $is_absolute_windows = (bool) preg_match('/^[A-Za-z]:[\\\\\/]/', $path);

    return $is_absolute_unix || $is_absolute_windows
        ? $path
        : $theme_directory . '/' . ltrim($path, '/\\');
};

/**
 * Import a canonical asset once per content hash and role.
 */
$import_image = static function (
    string $source,
    string $filename,
    string $title,
    string $role
): int {
    if (! is_readable($source)) {
        WP_CLI::error(sprintf('Required image is missing or unreadable: %s', $source));
    }

    $sha256 = hash_file('sha256', $source);
    if (! is_string($sha256) || $sha256 === '') {
        WP_CLI::error(sprintf('Could not hash required image: %s', $source));
    }

    $wordpress_default_artwork = [
        ABSPATH . WPINC . '/images/w-logo-blue-white-bg.png',
        ABSPATH . 'wp-admin/images/w-logo-blue-white-bg.png',
        ABSPATH . 'wp-admin/images/wordpress-logo.svg',
    ];
    foreach ($wordpress_default_artwork as $default_artwork) {
        if (! is_readable($default_artwork)) {
            continue;
        }
        $default_sha256 = hash_file('sha256', $default_artwork);
        if (is_string($default_sha256) && hash_equals($default_sha256, $sha256)) {
            WP_CLI::error(sprintf('%s is WordPress default artwork, not an approved project asset.', $source));
        }
    }

    $existing = get_posts([
        'post_type' => 'attachment',
        'post_status' => 'inherit',
        'posts_per_page' => 1,
        'fields' => 'ids',
        'no_found_rows' => true,
        'meta_query' => [
            'relation' => 'AND',
            [
                'key' => '_norml_seo_asset_role',
                'value' => $role,
            ],
            [
                'key' => '_norml_seo_asset_sha256',
                'value' => $sha256,
            ],
        ],
    ]);

    if ($existing !== []) {
        return (int) $existing[0];
    }

    $filename_parts = pathinfo($filename);
    $filename_base = sanitize_file_name((string) ($filename_parts['filename'] ?? 'seo-asset'));
    $filename_extension = sanitize_key((string) ($filename_parts['extension'] ?? ''));
    $filename = $filename_base . '-' . substr($sha256, 0, 12)
        . ($filename_extension !== '' ? '.' . $filename_extension : '');

    require_once ABSPATH . 'wp-admin/includes/file.php';
    require_once ABSPATH . 'wp-admin/includes/image.php';
    require_once ABSPATH . 'wp-admin/includes/media.php';

    $temporary_file = wp_tempnam($filename);
    if (! $temporary_file || ! copy($source, $temporary_file)) {
        WP_CLI::error(sprintf('Could not stage %s for Media Library import.', $filename));
    }

    $attachment_id = media_handle_sideload([
        'name' => $filename,
        'tmp_name' => $temporary_file,
    ], 0, $title);

    if (is_wp_error($attachment_id)) {
        @unlink($temporary_file);
        WP_CLI::error($attachment_id->get_error_message());
    }

    $attachment_id = (int) $attachment_id;
    update_post_meta($attachment_id, '_norml_seo_asset_role', $role);
    update_post_meta($attachment_id, '_norml_seo_asset_sha256', $sha256);
    update_post_meta($attachment_id, '_wp_attachment_image_alt', $title);

    return $attachment_id;
};

$site_icon_id = $import_image(
    $resolve_asset((string) $config['site_icon_path']),
    (string) $config['site_icon_filename'],
    (string) $config['site_icon_title'],
    'site-icon'
);

$social_image_id = $import_image(
    $resolve_asset((string) $config['social_image_path']),
    (string) $config['social_image_filename'],
    (string) $config['social_image_title'],
    'social-card'
);

$organization_logo_id = 0;
if ($config['site_icon_is_organization_logo']) {
    $organization_logo_id = $site_icon_id;
} elseif ($organization_logo_field_count === 3) {
    $organization_logo_id = $import_image(
        $resolve_asset((string) $config['organization_logo_path']),
        (string) $config['organization_logo_filename'],
        (string) $config['organization_logo_title'],
        'organization-logo'
    );
}

update_post_meta(
    $site_icon_id,
    '_norml_seo_asset_identity_source',
    sanitize_text_field((string) $config['site_icon_identity_source'])
);

$site_icon_url = (string) wp_get_attachment_image_url($site_icon_id, 'full');
$social_image_url = (string) wp_get_attachment_image_url($social_image_id, 'full');
$organization_logo_url = $organization_logo_id > 0
    ? (string) wp_get_attachment_image_url($organization_logo_id, 'full')
    : '';

if ($site_icon_url === '' || $social_image_url === '') {
    WP_CLI::error('WordPress did not return URLs for the imported SEO images.');
}

$site_icon_metadata = wp_get_attachment_metadata($site_icon_id);
$site_icon_width = is_array($site_icon_metadata) ? (int) ($site_icon_metadata['width'] ?? 0) : 0;
$site_icon_height = is_array($site_icon_metadata) ? (int) ($site_icon_metadata['height'] ?? 0) : 0;
if ($site_icon_width < 512 || $site_icon_height < 512 || $site_icon_width !== $site_icon_height) {
    WP_CLI::error(sprintf(
        'WordPress Site Icon must be square and at least 512x512; imported asset is %dx%d.',
        $site_icon_width,
        $site_icon_height
    ));
}

$social_image_metadata = wp_get_attachment_metadata($social_image_id);
$social_image_width = is_array($social_image_metadata) ? (int) ($social_image_metadata['width'] ?? 0) : 0;
$social_image_height = is_array($social_image_metadata) ? (int) ($social_image_metadata['height'] ?? 0) : 0;
if (
    $social_image_width !== (int) $config['social_image_width']
    || $social_image_height !== (int) $config['social_image_height']
) {
    WP_CLI::error(sprintf(
        'Social image must be %dx%d; imported asset is %dx%d.',
        (int) $config['social_image_width'],
        (int) $config['social_image_height'],
        $social_image_width,
        $social_image_height
    ));
}

update_option('site_icon', $site_icon_id);
update_option('rank_math_registration_skip', true);
update_option('rank_math_wizard_completed', true);
// Preserve the existing module owner/scope. Disabling a module is a separate
// reviewed change; this baseline only adds its required modules idempotently.
$existing_modules = get_option('rank_math_modules', []);
if (! is_array($existing_modules)) {
    WP_CLI::error('Existing Rank Math modules are not an array; review them before applying this baseline.');
}
foreach ($existing_modules as $module) {
    if (! is_string($module) || $module === '') {
        WP_CLI::error('Existing Rank Math module IDs are invalid; review them before applying this baseline.');
    }
}
$baseline_modules = [
    'link-counter',
    'seo-analysis',
    'sitemap',
    'rich-snippet',
];
update_option('rank_math_modules', array_values(array_unique(array_merge(
    $existing_modules,
    $baseline_modules
))));

$general = get_option('rank-math-options-general', []);
$general = is_array($general) ? $general : [];
$general = array_replace($general, [
    'attachment_redirect_urls' => 'on',
    'attachment_redirect_default' => home_url('/'),
    'breadcrumbs' => 'off',
    'console_email_reports' => 'off',
    'frontend_seo_score' => 'off',
    'analytics_stats' => 'off',
    'new_window_external_links' => 'off',
    'setup_mode' => 'advanced',
]);
update_option('rank-math-options-general', $general);

$titles = get_option('rank-math-options-titles', []);
$titles = is_array($titles) ? $titles : [];
$titles = array_replace($titles, [
    'robots_global' => ['index'],
    'advanced_robots_global' => [
        'max-snippet' => '-1',
        'max-video-preview' => '-1',
        'max-image-preview' => 'large',
    ],
    'title_separator' => '-',
    'noindex_empty_taxonomies' => 'on',
    'capitalize_titles' => 'off',
    'twitter_card_type' => 'summary_large_image',
    'open_graph_image' => $social_image_url,
    'open_graph_image_id' => $social_image_id,
    'knowledgegraph_type' => (string) $config['entity_type'],
    'knowledgegraph_name' => (string) $config['entity_name'],
    'website_name' => (string) $config['site_name'],
    'website_alternate_name' => (string) $config['alternate_name'],
    'organization_description' => (string) $config['seo_description'],
    'url' => home_url('/'),
    'homepage_title' => (string) $config['seo_title'],
    'homepage_description' => (string) $config['seo_description'],
    'homepage_custom_robots' => 'off',
    'disable_author_archives' => $config['single_author_site'] ? 'on' : 'off',
    'author_custom_robots' => $config['single_author_site'] ? 'on' : 'off',
    'author_robots' => $config['single_author_site'] ? ['noindex'] : ['index'],
    'author_add_meta_box' => $config['single_author_site'] ? 'off' : 'on',
    'disable_date_archives' => 'on',
    'date_archive_robots' => ['noindex'],
    'noindex_search' => 'on',
    'noindex_archive_subpages' => 'on',
    'noindex_password_protected' => 'on',
    'pt_page_title' => '%title% %sep% %sitename%',
    'pt_page_description' => '%excerpt%',
    'pt_page_robots' => ['index'],
    'pt_page_custom_robots' => 'off',
    'pt_page_default_rich_snippet' => 'off',
    'pt_page_add_meta_box' => 'on',
    'pt_attachment_robots' => ['noindex'],
    'pt_attachment_custom_robots' => 'on',
    'pt_attachment_default_rich_snippet' => 'off',
    'pt_attachment_add_meta_box' => 'off',
]);

if ($organization_logo_id > 0 && $organization_logo_url !== '') {
    $titles['knowledgegraph_logo'] = $organization_logo_url;
    $titles['knowledgegraph_logo_id'] = $organization_logo_id;
} else {
    unset($titles['knowledgegraph_logo'], $titles['knowledgegraph_logo_id']);
}
update_option('rank-math-options-titles', $titles);

$sitemap = get_option('rank-math-options-sitemap', []);
$sitemap = is_array($sitemap) ? $sitemap : [];
$sitemap = array_replace($sitemap, [
    'items_per_page' => 200,
    'include_images' => 'on',
    'include_featured_image' => 'on',
    'html_sitemap' => 'off',
    'authors_sitemap' => $config['single_author_site'] ? 'off' : 'on',
    'authors_html_sitemap' => 'off',
    'include_authors_without_posts' => 'off',
]);

foreach ($config['sitemap_post_types'] as $post_type => $enabled) {
    $post_type = sanitize_key((string) $post_type);
    if ($post_type === '') {
        WP_CLI::error('A sitemap post-type key is empty or invalid.');
    }
    $sitemap['pt_' . $post_type . '_sitemap'] = $enabled ? 'on' : 'off';
}

foreach ($config['sitemap_taxonomies'] as $taxonomy => $enabled) {
    $taxonomy = sanitize_key((string) $taxonomy);
    if ($taxonomy === '') {
        WP_CLI::error('A sitemap taxonomy key is empty or invalid.');
    }
    $sitemap['tax_' . $taxonomy . '_sitemap'] = $enabled ? 'on' : 'off';
}

update_option('rank-math-options-sitemap', $sitemap);

$homepage_meta = [
    'rank_math_title' => (string) $config['seo_title'],
    'rank_math_description' => (string) $config['seo_description'],
    'rank_math_facebook_title' => (string) $config['seo_title'],
    'rank_math_facebook_description' => (string) $config['seo_description'],
    'rank_math_facebook_image' => $social_image_url,
    'rank_math_facebook_image_id' => $social_image_id,
    'rank_math_twitter_use_facebook' => 'on',
    'rank_math_twitter_card_type' => 'summary_large_image',
    'rank_math_rich_snippet' => 'off',
];

if (trim((string) $config['focus_keyword']) !== '') {
    $homepage_meta['rank_math_focus_keyword'] = trim((string) $config['focus_keyword']);
} else {
    delete_post_meta($homepage_id, 'rank_math_focus_keyword');
}

$homepage_meta_changed = false;
foreach ($homepage_meta as $meta_key => $meta_value) {
    if (get_post_meta($homepage_id, $meta_key, true) != $meta_value) {
        update_post_meta($homepage_id, $meta_key, $meta_value);
        $homepage_meta_changed = true;
    }
}

if ($homepage_meta_changed) {
    wp_update_post(['ID' => $homepage_id]);
}

clean_post_cache($homepage_id);
flush_rewrite_rules(false);

if (class_exists('RankMath\\Sitemap\\Cache')) {
    RankMath\Sitemap\Cache::invalidate_storage();
}

wp_cache_flush();

$stored_modules = get_option('rank_math_modules', []);
$stored_site_icon = (int) get_option('site_icon');
$stored_home_title = (string) get_post_meta($homepage_id, 'rank_math_title', true);

if ($stored_site_icon !== $site_icon_id || $stored_home_title !== $config['seo_title']) {
    WP_CLI::error('Post-write verification failed for the Site Icon or homepage title.');
}

WP_CLI::success(sprintf(
    'Configured Rank Math %s; homepage=%d site_icon=%d social_image=%d organization_logo=%d modules=%s.',
    RANK_MATH_VERSION,
    $homepage_id,
    $site_icon_id,
    $social_image_id,
    $organization_logo_id,
    implode(',', is_array($stored_modules) ? $stored_modules : [])
));
