# Process steps block

> Numbered sequence showing how the service / engagement / order flow works. 3–7 steps, each with a label and short body.

## Purpose

De-mystify "what happens after I sign up?" Buyers convert better when they can see the steps. Replaces the abstract "we have a process" with concrete, observable milestones.

## Required elements

- **Section heading** — "How it works" / "Our process" / "What to expect"
- **3–7 numbered steps** — never fewer than 3 (too thin) or more than 7 (too much)
- Each step: step number, step name, 1–2 sentence body

## Optional elements

- **Timeline per step** — "Week 1: discovery, Week 2: build…"
- **Icon per step** — visual marker beyond the number
- **Connector line** between steps (visual flow)
- **Per-step CTA** — usually only on the last step (the conversion action)
- **Per-step image / illustration**

## Gutenberg + ACF default (primary)

**Block name:** `acf/process-steps`
**ACF field group:** `Process steps`

Fields:
- `heading` — text, required
- `dek` — textarea, optional
- `steps` — repeater, min 3, max 7:
  - `step_name` — text
  - `step_body` — textarea (1–2 sentences)
  - `timeline_label` — text, optional (e.g., `"Week 1"`)
  - `icon` — image or icon select, optional
  - `image` — image, optional (for image-led variant)
- `layout` — radio: `horizontal | vertical | zigzag`, default `horizontal`
- `show_numbers` — true_false, default true
- `show_connectors` — true_false, default true (visual line between steps)
- `final_step_cta` — group: `label` + `url`, optional

**Blade template:** `resources/views/blocks/process-steps.blade.php`

## Elementor fallback

Elementor's Icon Box widget (numbered icon + text) repeated, or Elementor's Flip Box widget for hover-reveal variants.

## Variations

- **Horizontal row** — desktop default, stacks on mobile
- **Vertical timeline** — single column with vertical connector line (more editorial)
- **Zigzag** — alternating image-text rows, one step per row (great for image-led processes)
- **With timeline** — adds "Week 1," "Week 2" labels per step
- **Compact icons** — minimal style for sites where the process is secondary

## Used on

- Service page (canonical)
- Service listing (overview variant — generic 3–4 step framework)
- Home page (variant — quick "how it works" strip)
- About page (variant — "how we work")
- Product page (variant — order / fulfillment process)

## Don'ts

- Don't have 2 steps — feels incomplete; reframe as a benefit or skip
- Don't have 10 steps — readers stop scanning; consolidate
- Don't write the same body for every step ("We'll work with you to…")
- Don't include steps the buyer doesn't experience ("internally we review and approve") — keep buyer-facing
- Don't use abstract step names ("Engage," "Synergize") — name what actually happens ("Kickoff call," "First draft delivered")
- Don't promise timelines you can't keep
- Don't include a process for a service that's truly bespoke and varies wildly per client
