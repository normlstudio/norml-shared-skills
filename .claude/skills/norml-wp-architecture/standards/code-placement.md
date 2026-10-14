# Code placement — plugin vs theme vs child theme vs mu-plugin

> Where does a given piece of code *live*? This is an architecture decision, not a style
> one, because it determines what survives a theme switch, what a client can break, and
> whether content gets orphaned. Builder-agnostic.

## The one principle: functionality vs presentation

> **Functionality** that should outlive the current look-and-feel goes in a **plugin.**
> **Presentation** — how things look and lay out — goes in the **theme.**

Presentation belongs to the theme; durable behavior belongs to a plugin. The test for any chunk of code: **if
the client switched to a completely different theme tomorrow, should this keep working?**

- "The site still needs *case studies to exist* as a content type" → **plugin** (survives
  the switch).
- "The site needs case studies to *look like this*" → **theme** (changes with the design).

This single rule resolves most placement questions. The rest of this file is its
consequences and This package's pragmatic exceptions.

---

## What goes where

| Code | Home | Why |
|---|---|---|
| CPT registration (`case_study`, `service`, …) | **Plugin** (principle) — see Package exception | Content must survive a re-theme |
| Custom taxonomy registration | **Plugin** (principle) — see Package exception | Same — terms + relationships are content |
| Shortcodes, custom REST endpoints, cron jobs | **Plugin** | Behavior, theme-independent |
| Third-party integrations (CRM, payment, API glue) | **Plugin** | Behavior, must not die with the theme |
| Templates (`single-`, `archive-`, page templates) | **Theme** | Pure presentation |
| Styles, scripts, fonts, images | **Theme** | Presentation |
| ACF **blocks** (registration + render) | **Theme** | Blocks are presentation/layout |
| ACF **field group definitions** (the field schema) | **Theme** (Package default) or plugin | See the ACF nuance below |
| Block patterns / synced patterns | **Theme** | Layout reuse |
| Global options pages (CTA, socials, footer) | **Theme** (ACF options) or plugin | Usually theme; plugin if cross-theme |
| Critical always-on glue that must never be off | **mu-plugin** | Can't be deactivated (see below) |

---

## Why CPT/taxonomy registration "wants" a plugin

This is the textbook rule, and the reason behind it is real and worth stating plainly:

**If you register a CPT in the theme and the client switches themes, the post type stops
being registered — and every case study becomes inaccessible.** The rows still sit in
`wp_posts` with `post_type = case_study`, but nothing registers that type anymore, so WP
won't route to them, won't show them in admin, won't query them. The content is *orphaned* —
not deleted, but invisible until the type is re-registered. For a client who owns their site
and might re-theme in two years, that is a latent landmine.

Putting CPT + taxonomy registration in a **site-specific "core" plugin** (e.g.
`{client}-core`) decouples the *content's existence* from the *current design*. Re-theme
freely; the content model persists. This is the portable, defensible default for any
long-lived client site where the current owner does **not** control all future theming.

---

## The Pragmatic default — and its honest tradeoff

One deliberately chosen option is **"CPTs registered via ACF JSON, not
PHP code"** — i.e. the post type and field groups are defined in ACF and **synced as JSON
inside the theme** (`acf-json/`, version-controlled). This is fast, gives a UI, keeps the
schema in git, and avoids spinning up a separate plugin for every small site.

**Be honest about what this costs.** ACF-JSON-in-theme has the **same coupling** the plugin
rule warns about, plus one more dependency:

- Field/CPT JSON schema in a theme couples its versioned definitions and loader to that
  theme and ACF. ACF-created registrations synced/persisted in the database may continue
  loading after a theme switch, depending on version and storage; test rather than assume.
- This is still a real ownership/portability tradeoff: the new theme/plugin must intentionally
  load and maintain the schema. Choose a durable site-core owner for long-lived content.
- A short-lived owner-controlled build may accept this coupling; record the choice explicitly.

**The escalation rule — when to put the CPT in a real plugin instead of ACF-JSON-in-theme:**

Escalate to a **site-core plugin** (PHP registration, or ACF's "export to PHP/plugin") when
**any** of these is true:

- The **client owns the site** and may re-theme or hire another agency later.
- The content corpus is **large or long-lived** (hundreds of case studies, years of events)
  — orphaning it later is a serious incident.
- **Content portability** matters contractually, or the site may be **migrated** between
  themes/hosts.
- Multiple themes/sites need to **share** the same content type (a network, a multi-brand
  setup).

When none of those hold — a fast owner-controlled build — **ACF-JSON-in-theme is the right,
pragmatic default.** State which one you're choosing in the architecture spec, and name the
tradeoff in one line. Don't silently pick the fast path on a site that needed the durable
one.

---

## Child themes — when and why

A **child theme** inherits everything from a **parent theme** and lets you override pieces
without editing the parent. Its entire reason to exist: **the parent theme is one you don't
own and will receive updates** (a marketplace theme, Divi, Astra, a starter) — and editing
the parent directly means the next update wipes your changes.

**Use a child theme when:**

- The project is built on a **third-party parent** (Divi, Elementor's Hello, Astra,
  GeneratePress, any ThemeForest theme) and you need custom templates, functions, or styles.
  The child holds your `functions.php` additions, template overrides, `assets/`, and your
  project's `.claude/`.
- You need a home for project code on a builder site where "the theme" is really the
  builder. (This is exactly the `elementor-child-with-git` / Divi-child pattern in
  `norml-ci-cd` and the the existing project stack documentation catalog — the child theme exists partly just to hold
  versioned project files.)

**Do NOT use a child theme when:**

- the owner **authored the theme from scratch** (Sage). There's no parent to protect against —
  *you are the theme.* A child theme on top of a Sage theme is pure overhead.

**Note:** a child theme is still a *theme* — so the functionality-vs-presentation rule still
applies *inside* it. CPT registration on a Divi child site still "wants" a plugin (or at
minimum a clearly-separated `inc/` include), for the same orphaning reason — putting it in
the child theme's `functions.php` couples your content to "this child theme staying active."

---

## mu-plugins (must-use) — the always-on tier

**mu-plugins** live in `wp-content/mu-plugins/` and are **always active — they cannot be
deactivated from the admin and have no on/off toggle.** They load before regular plugins.

**Use an mu-plugin for:**

- Critical site glue that **must never be turned off** — e.g. CPT/taxonomy registration on a
  site where you don't trust the admin (or a junior editor) not to deactivate a plugin and
  orphan the content.
- Infra-level mods that should apply unconditionally (security hardening, environment
  config, disabling something dangerous).

**Use sparingly.** Because they're invisible in the normal plugin list and can't be toggled,
they're easy to forget and harder to debug. This package reaches for a normal site-core plugin
first; mu-plugins are for the "this absolutely cannot be switched off" cases.

---

## Decision flow for placement

```
Is it presentation (how it looks / lays out)?
  └─ YES → theme  (or child theme, if the parent is third-party)
  └─ NO  → it's functionality:
        Must it survive a theme switch? (content existence, integrations, behavior)
          └─ YES → plugin
                Must it be impossible to deactivate? (untrusted admin, critical glue)
                  └─ YES → mu-plugin
                  └─ NO  → site-core plugin
          └─ NO (fast, owner-controlled, short-lived) →
                ACF-JSON-in-theme is an acceptable pragmatic home — state the tradeoff
```

Put the chosen home in the architecture spec, with the one-line tradeoff when you took the
pragmatic path. Where the code physically goes in *this* project's structure (which `inc/`
file, which Sage path) is the build skill's call, not this skill's — see
`norml-wp-developer/standards/` and the the existing project stack documentation catalog.
