# Share with AI block (reader assistance)

> A three-button strip at the end of a blog post that lets readers pipe the article into ChatGPT (or another LLM) with a pre-baked prompt — "give me the takeaway," "summarize it," "explain it simply." Increases time-on-content even if the reader leaves the page, and signals AI-fluency in the brand voice.

## Purpose

The 2026 reader-engagement equivalent of social-share buttons. Lets a reader continue working with the article inside an LLM without copy-pasting. Three canonical jobs-to-be-done: extract the gist (Takeaway), get a structured summary (Summarize), demystify a complex topic (Explain like I'm a kid). This is a reusable reader-assistance pattern. On blog singles it is followed by the [Google Preferred Source](preferred-source.md) control, then social sharing.

## Required elements

- **Section heading** — "Share with AI" (H3)
- **Three buttons**, in this fixed order:
  1. **One-minute takeaway**
  2. **Summarize**
  3. **Explain like I'm a kid**
- Each button is a real `<a>` with `target="_blank"` opening the chosen AI destination with the pre-baked prompt URL-encoded in the query string. No JS handlers, no modals, no clipboard — direct URL navigation.

## Optional elements

- Custom button order (per project) — but default to the three above
- Custom 4th button (e.g., "Translate to Spanish," "Convert to LinkedIn post") — rare, only when the audience clearly wants it
- Icon per button (small emoji or SVG) — disabled by default, allowed by spec
- Per-project AI destination — defaults to ChatGPT (`https://chat.openai.com/?q=...`), can be switched to Claude (`https://claude.ai/new?q=...`) or Gemini (`https://gemini.google.com/app?q=...`) globally via Theme Options
- Above-fold variant — same block in a more compact form at the top of the article (rare; only on long-form how-tos)

## Illustrative implementation

Portable example HTML; adapt and verify destination links before shipping:

```html
<div class="blog-social-ai-section">
  <h3 class="blog-social-share-title">Share with AI</h3>
  <div class="blog-social-ai-buttons">

    <!-- One-minute takeaway -->
    <a href="https://chat.openai.com/?q={URL_ENCODED_PROMPT_1}"
       class="blog-ai-btn"
       target="_blank"
       rel="noopener noreferrer"
       aria-label="One-minute takeaway with ChatGPT">
      <span>One-minute takeaway</span>
    </a>

    <!-- Summarize -->
    <a href="https://chat.openai.com/?q={URL_ENCODED_PROMPT_2}"
       class="blog-ai-btn"
       target="_blank"
       rel="noopener noreferrer"
       aria-label="Summarize article with ChatGPT">
      <span>Summarize</span>
    </a>

    <!-- Explain like I'm a kid -->
    <a href="https://chat.openai.com/?q={URL_ENCODED_PROMPT_3}"
       class="blog-ai-btn"
       target="_blank"
       rel="noopener noreferrer"
       aria-label="Explain like I'm a kid with ChatGPT">
      <span>Explain like I'm a kid</span>
    </a>

  </div>
</div>
```

Position on page: after the article body, before Google Preferred Source and the standard social-share row, and before "Related articles."

### Canonical prompt templates (project-tunable)

Each prompt is constructed at render time with two variables substituted: `{POST_TITLE}` (post's H1) and `{POST_URL}` (canonical URL). The output is URL-encoded and dropped into the AI destination's `?q=` parameter. **Always include the post URL in the prompt** so the LLM can fetch the article; actual URL-fetch capability depends on the user’s provider/account.

**Prompt 1 — One-minute takeaway** (3-bullet summary)
```
Provide a one-minute takeaway of this article: "{POST_TITLE}" ({POST_URL})

Requirements:
– 3 short bullet points
– Each bullet under 20 words
– Focus on what the reader should understand after reading
```

**Prompt 2 — Summarize** (clear, neutral overview)
```
Summarize this article into a clear, neutral overview: "{POST_TITLE}" ({POST_URL})

Requirements:
– Maximum 5 bullet points
– Focus on what changed, why it matters, and who it affects
– No speculation or opinion
```

**Prompt 3 — Explain like I'm a kid** (simple-language explainer)
```
Explain this article in very simple terms, as if speaking to a curious kid: "{POST_TITLE}" ({POST_URL})

Requirements:
– Friendly tone
– Simple explanations
– No sarcasm or jokes
– No invented examples outside the article
```

**Per-project guardrail clauses** — append industry-specific safety lines to each prompt as needed. A regulated-industry project can choose `"– No legal recommendations"` on Prompt 2 because supplements have legal/health exposure. For a different project, swap or remove. Configure these per-project in Theme Options (see ACF fields below).

### URL encoding rule

When building the `?q=` value, use `encodeURIComponent(prompt)` (or PHP `urlencode($prompt)`). Spaces become `+` or `%20`; quotes become `%22`; en-dashes become `%E2%80%93`; the URL inside the prompt is itself URL-encoded inside the outer query.

Keep whitespace/newlines between title, URL and requirements. Test the decoded prompt at the actual provider; query-prefill behavior is not guaranteed.

## Gutenberg + ACF default (primary)

**Block name:** `acf/share-ai`
**ACF field group:** `Share with AI`

Fields:
- `heading` — text, required, default `"Share with AI"`
- `enabled` — true_false, default `true` (toggle per-post override; theme default also exists)
- `ai_destination` — select: `chatgpt | claude | gemini | custom`, default `chatgpt` — overrides Theme Options default if set per-post
- `custom_destination_url_pattern` — text, conditional on `ai_destination = custom`, default `https://chat.openai.com/?q=`
- `prompts` — group with three sub-groups (one per button), each:
  - `enabled` — true_false, default true (lets editor hide one button per post if irrelevant)
  - `button_label` — text, default per canonical order above
  - `prompt_template` — textarea, default per canonical template above (with `{POST_TITLE}` / `{POST_URL}` placeholders)
  - `aria_label` — text, default `"{button_label} with {AI_DESTINATION_NAME}"`

**Theme Options page** (`ACF Options → Site → Share with AI`):
- `default_heading` — text, default `"Share with AI"`
- `default_ai_destination` — select (same options as per-post), default `chatgpt`
- `default_prompts` — group of three (One-minute takeaway / Summarize / Explain like I'm a kid), each with `button_label` + `prompt_template` + `aria_label`
- `industry_guardrails` — textarea, multi-line; appended to ALL prompts when set (e.g., `"– No legal recommendations"` for legal/health clients)
- `enabled_globally` — true_false, master toggle to disable across all posts

**Blade template:** `resources/views/blocks/share-ai.blade.php`

Skeleton:
```php
@php
  $heading = get_field('heading') ?: get_field('default_heading', 'option');
  $dest    = get_field('ai_destination') ?: get_field('default_ai_destination', 'option');
  $base    = [
      'chatgpt' => 'https://chat.openai.com/?q=',
      'claude'  => 'https://claude.ai/new?q=',
      'gemini'  => 'https://gemini.google.com/app?q=',
      'custom'  => get_field('custom_destination_url_pattern'),
  ][$dest];
  $name  = ['chatgpt'=>'ChatGPT','claude'=>'Claude','gemini'=>'Gemini','custom'=>'AI'][$dest];
  $title = get_the_title();
  $url   = get_permalink();
  $guard = get_field('industry_guardrails', 'option');
  $prompts = get_field('prompts') ?: get_field('default_prompts', 'option');
@endphp

<div class="share-ai">
  <h3 class="share-ai__heading">{{ $heading }}</h3>
  <div class="share-ai__buttons">
    @foreach ($prompts as $p)
      @if ($p['enabled'])
        @php
          $body = str_replace(['{POST_TITLE}','{POST_URL}'], [$title, $url], $p['prompt_template']);
          if ($guard) $body .= "\n" . $guard;
          $href = $base . urlencode($body);
        @endphp
        <a href="{{ $href }}"
           class="share-ai__btn"
           target="_blank"
           rel="noopener noreferrer"
           aria-label="{{ $p['aria_label'] ?: ($p['button_label'].' with '.$name) }}">
          <span>{{ $p['button_label'] }}</span>
        </a>
      @endif
    @endforeach
  </div>
</div>
```

(Non-Sage projects: equivalent PHP partial inside the child theme; same logic.)

## Elementor fallback

Use Elementor's Button group widget with three buttons. Manually paste the URL-encoded `chat.openai.com/?q=...` href on each button. Set `target="_blank"`. Loses the per-post prompt customization Theme Options gives you in the ACF path — only do this if the rest of the site is already Elementor.

## Variations

- **3-button horizontal row** — default, matches the manufacturer example
- **3-button vertical stack** — for narrow sidebars / mobile-only positions
- **1-button compact** — only Takeaway, for above-the-fold placement on long posts
- **Boxed card** — buttons inside a tinted card with section title + tiny tagline ("Want the gist?")
- **Multi-destination** — let the reader pick ChatGPT vs Claude vs Gemini at click time (3×3 grid). Only meaningful on AI-industry blogs.

## Used on

- Blog post (canonical) — see [blog-post.md](../pages/blog-post.md)
- Long-form service page (rare — only when content reads like an article)
- News / press release pages
- Knowledge base / docs (when content is dense enough that summarization helps)

## Don'ts

- Don't ship without the post URL in the prompt — ChatGPT can't fetch the article without it, and the summary degrades to "Based on the title alone…"
- Don't open the AI destination in the same tab — the reader loses the article
- Don't hardcode the prompt strings in PHP without giving editors a Theme Options override — projects need to tune guardrails per industry
- Don't add 6+ buttons — three is the right cognitive load; more dilutes the choice
- Don't translate the prompts into the article's language automatically without testing — many LLMs degrade when prompted in non-English. Default English prompts even on multilingual sites; expose per-language prompt overrides as an opt-in per project.
- Don't use this block on a 300-word announcement — there's nothing to summarize
- Don't write industry guardrails as a question ("Should this exclude legal advice?") — write them as instructions ("No legal recommendations") so the LLM follows them as constraints
- Don't expose the raw `?q=` URL to the editor as the configurable field — it'll get URL-encoded twice. Configure the prompt template as plain text and let the Blade do the encoding once.
