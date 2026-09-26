---
name: mayer-taste
description: Use when designing, building, redesigning, or auditing any website or interface, in any industry or stack, when the goal is to look intentionally designed rather than templated, symmetric-by-default, or AI-generated. Use when the user references a past site as a quality bar, asks for a site to not look pixel-perfect/cookie-cutter, wants structural variety instead of a generic hero-features-CTA layout, or asks to check a design against the owner's taste. Not tied to any single palette, font, or industry — this is the transferable philosophy, not a locked theme.
version: 1.0.0
---

# Mayer Taste

A universal design-taste skill. Distilled from studying one well-designed site, but the rules here are the *transferable* lessons, not that site's specific hex codes or fonts. Use this on any project: SaaS, e-commerce, portfolio, B2B, whatever.

**The core insight:** a site reads as "designed" not because every pixel is symmetric and perfect, but because of the opposite — deliberate asymmetry, restraint spent in the right places, and one or two signature choices executed with total conviction instead of ten trendy effects executed halfway. Pixel-perfect symmetry is the tell of a template, not the mark of quality. Two projects built under this skill should never look like reskins of each other.

## The core law: never the same site twice

This is the law everything else serves. If you're building a second, third, or tenth project under this skill and it shares a hero pattern, a color temperature, a spacing rhythm, or a "signature move" with a previous one, that's a failure of this skill, not a coincidence.

Before designing anything, name three things out loud (to yourself, in the plan, or in a comment — but name them):

1. **Register** — is design *the* product (marketing/brand/portfolio) or does it *serve* the product (dashboard/tool/app)? This changes how much visual risk is affordable.
2. **One physical scene sentence** — who uses this, where, under what light, in what mood? ("A procurement manager comparing three quotes on a laptop in a warehouse office" reads nothing like "a teenager scrolling a sneaker drop on a phone at midnight.") If the sentence doesn't force a concrete answer on theme/mood, it's too vague — add detail until it does.
3. **One deliberate signature move, unique to this project** — the one thing this site does that a generic template in this category wouldn't. Pick it on purpose before writing any code. Everything else stays disciplined so this one thing can stand out.

If you can't answer #3, you're about to build a template. Stop and pick one.

## Universal principles (transferable, not locked to any theme)

These are *how* to execute, not *what* colors/fonts to use — the specifics are chosen per-project in the calibration step below.

1. **Conservative skeleton, uncommon execution.** The page structure (nav → hero → content → footer, or whatever the genre's honest skeleton is) is allowed to be ordinary. Spend the designed-feeling budget on execution — typography, color depth, motion — not on reinventing information architecture for its own sake. A wildly unconventional skeleton with generic execution reads worse than a plain skeleton executed with conviction.

2. **One signature typographic move, one job only.** Pick exactly one place where type does something no default stack would (a genuinely distinct display face, an unusual scale jump, a texture in the headline treatment). Use it in exactly one role — usually the H1 — and nowhere else. The moment the signature move shows up in a second, unrelated role, the contrast that made it feel special collapses. Everything that isn't the signature move should be typographically boring on purpose.

3. **Context-tuned color, not one-size palette.** A single color token forced to work against both a light background and a dark hero always looks slightly wrong on one of them. Tune the same hue differently per lighting context (a deeper/richer variant for dark sections, a flatter/more legible variant for light sections) rather than compromising one value to cover both. Reduce chroma as lightness approaches 0 or 100 — high chroma at the extremes looks garish, cheap, or "AI purple."

4. **Motion as sequence, not simultaneity.** Elements should arrive in an order that tells the eye where to look first, not all at once. Stagger reveals in small, consistent increments. Ease out, never bounce or elastic — a spring-physics hero reads as a demo reel, not a considered interface. Motion should feel confident and quiet, not like it's trying to prove the site is "alive."

5. **Atmospheric restraint.** Depth cues (background glows, gradients, texture, blur) exist to suggest depth, not to announce themselves. If someone notices the glow before they notice the content, it's too strong. Low-opacity, off-canvas-positioned, `pointer-events: none` — atmosphere should be felt, not seen.

6. **Deliberate asymmetry over reflexive centering.** Centered text over a symmetric hero is the default every LLM and every template reaches for first. Before centering anything, ask whether an asymmetric split, an off-center focal point, or a varied-rhythm layout serves the content better. Symmetry is a valid choice sometimes — but it should be chosen, never defaulted into.

## Absolute bans

Match-and-refuse. If you're about to ship one of these, stop and rebuild that element with a different structure — these are the patterns that make any site, regardless of industry, read as templated or AI-generated:

- **Eyebrow/pill badges above headlines** — small rounded-full badges with a dot + uppercase tracked-out label ("SINCE 2002", "TRUSTED BY 500+ TEAMS"). The single most recognizable AI-slop tell. If a label genuinely earns its place, it needs its own specific treatment, not a copy-pasted pill.
- **Symmetric, dead-centered hero as an unexamined default.** Fine if chosen deliberately for the register; a failure if it's just what got typed first.
- **The generic 3-card feature grid** — identical-sized cards, icon + heading + one line of text, repeated 3-6 times in a row. If a features section needs it, vary card size, break the grid, or use a different pattern entirely (zig-zag, asymmetric bento, list with leading numerals).
- **Gradient text (`background-clip: text`) on more than one phrase per page**, or on body copy. It's a spotlight, not a paint bucket.
- **Glow/blur opacity above ~12%**, or more than two glow blobs per section. Past that threshold it reads as generic SaaS-hero glow or "AI purple" cliché, not atmosphere.
- **Bounce, elastic, or spring-physics easing** on anything. Ease-out curves only.
- **Identical spacing everywhere.** Uniform padding on every section is monotony dressed up as consistency. Vary spacing deliberately for rhythm.
- **Pure black (`#000`) or pure white (`#fff`).** Tint every neutral toward the project's hue, even slightly.
- **Reusing the signature typographic move outside its one assigned role.**
- **Converging on a previous project's palette temperature, hero pattern, or signature move.** If it's been done before under this skill, it's off the table for the next one unless the brief genuinely calls back to it (e.g., a sequel site for the same client).

## Per-project calibration (do this first, every time — before any code)

1. Answer Register / Scene / Signature Move (above) explicitly.
2. Pick a color strategy on purpose, not by reflex: restrained (tinted neutrals + one accent), committed (one saturated color carries 30-60% of the surface), full palette (3-4 named roles), or drenched (the surface IS the color). Match it to the scene sentence, not the industry category.
3. Decide the asymmetry level on purpose: could this layout be guessed from the category alone (e.g., "B2B → navy and centered," "fintech → dark and glowing")? If yes, rework the structural choice until it isn't guessable from the category, so it doesn't read as a generic template for its category.
4. Name the one signature move (typographic, structural, or motion) that will carry the "designed" feeling, and hold everything else disciplined around it.

## Case study (anonymized)

A worked example, not a locked ruleset.

- **Register/scene:** B2B industrial supplier, procurement audience, trust-driven: conservative skeleton, restrained color.
- **Signature move:** one custom display font, used only on H1s; everything else stays deliberately unremarkable.
- **Motion:** ~80ms staggered fade reveals, ease-out only, no bounce.
- **What got cut:** an eyebrow-pill badge copy-pasted onto every hero. Caught only by grepping every page, since there was no shared Hero component.

## Pre-flight checklist

Before shipping any page under this skill:

- [ ] Register, scene sentence, and one signature move were named before writing code
- [ ] Color strategy was chosen on purpose, not defaulted; neutrals are tinted, not pure black/white
- [ ] The signature move appears in exactly one role and nowhere else
- [ ] No eyebrow/pill badge, no generic 3-card grid, no gradient text on more than one phrase
- [ ] Glow/atmosphere effects are ≤12% opacity, ≤2 per section, non-interactive
- [ ] Motion is staggered and ease-out only — no bounce, no simultaneity
- [ ] Spacing rhythm varies deliberately; nothing is uniform by default
- [ ] Layout and palette were checked against "could this be guessed from the category alone?" — and reworked if yes
- [ ] This project's structural choices don't converge with a previous project built under this skill
