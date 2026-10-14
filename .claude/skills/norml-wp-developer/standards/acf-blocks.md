# ACF and native block registration

Discover the project's WordPress/ACF versions, native-versus-ACF block style, existing keys,
JSON save/load paths, and editor context before creating a block. Never replace an inherited
registration pattern implicitly. ACF PRO licensing/access is supplied by the project.

## Metadata registration (new compatible ACF work)

Use supported `register_block_type()` metadata and a dedicated `block.json` directory.
Verify the installed ACF supports the chosen properties; preserve the project's API version.
Example structure: `blocks/benefits/block.json` and `blocks/benefits/render.php`.

```json
{
  "apiVersion": 3,
  "name": "acf/benefits",
  "title": "Benefits",
  "category": "design",
  "icon": "star-filled",
  "supports": {"anchor": true},
  "acf": {"mode": "preview", "renderTemplate": "render.php"},
  "example": {"attributes": {"data": {"is_example": true}}}
}
```

```php
add_action('init', function () {
    if (! function_exists('get_field')) {
        return;
    }
    register_block_type(__DIR__ . '/../blocks/benefits');
});
```

The example flag is a preview fixture, not evidence that production fields exist.
If the selected version uses different block/editor options, consult current official ACF
and WordPress docs before implementation. Declare CSS/JS assets through supported metadata
or the existing enqueue pipeline and ensure editor styles load in its iframe/context.

## Legacy PHP callback route (inherited compatible projects)

```php
add_action('acf/init', function () {
    if (! function_exists('acf_register_block_type')) {
        return;
    }
    acf_register_block_type([
        'name' => 'benefits',
        'title' => __('Benefits', 'project-textdomain'),
        'category' => 'design',
        'mode' => 'preview',
        'supports' => ['anchor' => true],
        'example' => ['attributes' => ['mode' => 'preview', 'data' => ['is_example' => true]]],
        'render_callback' => function ($block, $content = '', $is_preview = false, $post_id = 0) {
            get_template_part('template-parts/sections/benefits', null, [
                'block' => $block, 'is_preview' => $is_preview, 'post_id' => $post_id,
            ]);
        },
    ]);
});
```

A Sage callback can render the project's Blade view with the same explicit data boundary.
Keep render markup outside registration. Follow existing keys and duplicate-field detection.

## Field schema and values

Typed image/link/repeater/relationship fields need correct return-format normalization.
Define field groups in the existing admin/PHP/local JSON workflow. JSON definitions ship as
source code; values remain WordPress content. Sync UI detection must be checked deliberately.
Do not assume ACF provides a `wp acf sync` CLI namespace; inspect installed command extensions.

## Preview contract

Live preview detects `is_example` and uses realistic sample data; live content uses actual
stored values. A heavy or remote-data block can render a bundled screenshot only in example
mode. Derive the file slug safely from the actual registered block, not `acf/name` as a path.
Keep screenshots current and document fallbacks. Check inserter, initial insertion, saved
fields, empty states, editor styles and frontend preview on staging/local authorized fixtures.

## Acceptance

- Block registration exists once and degrades safely if the dependency is absent.
- Fields load, save and read back with correct type/key/return format.
- Editor can find the block, see its preview and edit required content.
- Rendered markup escapes output and uses actual production content.
- Assets load in frontend and editor, including nested/synced blocks where applicable.
- Keyboard interaction and responsive layout work; no sample data leaks into live content.
