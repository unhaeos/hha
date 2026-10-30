---
name: hha-ui
description: Plan, build or review polished product interfaces with a subject-specific visual direction, consistent spacing and components, readable Korean or English typography, responsive states and concrete copy. Use for any screen work or visual quality review.
license: Apache-2.0; see LICENSE.txt
---

# UI with a clear point of view and disciplined detail

Read [working guidance](../../AGENTS.md) if not loaded. Modified adaptation of selected frontend-design ideas, with hha-specific typography, Korean copy and environment rules. See [attribution](../../THIRD_PARTY.md) and [license](LICENSE.txt).

## Start with the user's task

Name the audience, primary action, information needed to take it, and observable outcome. Use actual domain content. Preserve a good existing design system unless asked to change it. For a new screen, write a compact visual direction in SPEC before building:

- one sentence describing the intended character and why it fits this audience;
- a 4–6 color palette with roles and hex values, including surfaces, text and accent;
- font families that are actually available, a type scale, weights, line heights and letter spacing;
- a spacing scale, content width, grid/alignment rule and component geometry;
- imagery or illustration treatment when content needs it;
- a small ASCII wireframe for the main narrow and wide layouts.

Reject a direction that could be pasted onto any unrelated product. Customer and operator surfaces may share tokens but need different composition because their jobs differ.

Make the main content easy to find. Use spacing, alignment and headings before adding containers. Cards are appropriate for independently selectable or repeated objects, such as products; they are not the default wrapper for every paragraph, label and metric. Avoid nested bordered panels, identical tiles for unrelated information, gratuitous badges and dashboard statistics with no user purpose.

When customers and operators have different jobs, design their flows separately: a browsing surface should support choosing, while an operator surface should support inspection, correction and explicit state changes. Reuse shared tokens where appropriate without forcing both into the same dashboard. Use supplied brand references when available; explain choices from the audience and content, not an imitation of a fashionable template.

Choose one memorable visual idea tied to the content: composition, imagery, type treatment, color field or interaction. Let it carry the identity while the surrounding system stays coherent. Gradients, unusual grids, large type, illustration and motion are valid when they support that idea. Do not remove all character in the name of restraint, and do not scatter several unrelated effects across the same screen.

## Spacing, layout and component consistency

- Start from a 4px base and use a deliberate scale such as 4, 8, 12, 16, 24, 32, 48 and 64px. Existing design-system tokens win. Do not accumulate arbitrary 13/17/22px gaps to patch individual screens.
- Encode relationship through distance: 4–8px within a label/value or icon/text pair, 12–16px between related controls, 20–32px between groups, and 40–64px between major sections as a starting point. Adjust for density and type size, then keep the choice consistent.
- Repeated components with the same role use the same height, horizontal padding, border, radius, icon size, label placement and focus treatment. Avoid near-duplicates such as 40/42/44px buttons without a semantic size system.
- Align content edges, text baselines and control centers. Pick a grid and use it. Do not center isolated elements inside otherwise left-aligned content without a compositional reason.
- Use whitespace to group information before adding borders or tinted containers. Cards still need consistent internal padding and alignment; a card grid is not polished when each card has different vertical rhythm.
- Use integer token values or rem equivalents for structural dimensions. Inspect one-pixel borders, SVG viewBoxes, transforms and device scaling before diagnosing blurry or clipped rendering.

## Typography and color

- Prefer available fonts with reliable glyph coverage. For Korean, use an existing Korean-capable family or a system stack and confirm the requested weights exist. Deliberate display type is welcome when available; mixed fallback glyphs are not.
- Use a named, consistent scale. A practical starting point is 14px supporting, 16px body, and 20/24/32/44px display steps, adapted to the product. Pair size with explicit line height: roughly 1.5–1.7 for Korean body copy and 1.15–1.35 for headings, then inspect the render.
- Keep Korean body letter spacing near the font default. Avoid wide tracking and all-caps-style spacing. Slight negative tracking may suit large headings only after visual inspection; do not apply one negative value to every text style.
- Use real supported font weights and natural line breaks. Do not scale text with CSS transforms to fit a box. Define readable measure for prose and prevent headings from leaving a single orphan syllable when a reasonable width or copy edit fixes it.
- Distinguish primary, secondary and disabled text intentionally. Secondary text must still be readable; low opacity is not a substitute for hierarchy. Check text/background contrast with an available contrast tool or calculation; aim for at least 4.5:1 for ordinary text. Never encode state only through color.
- Keep label, value and action alignment consistent. Respect zoom, focus visibility and reduced-motion settings. Prevent narrow-screen horizontal overflow and truncation of essential actions.

## Product copy

Read [hha-writing](../hha-writing/SKILL.md) for labels, notifications and other copy, even when writing is only a small part of a UI task.

Say what exists, what changed and what the user can do. Prefer specific nouns and verbs. Examples: `상품 6개를 선택했어요`, `상품 바꾸기`, `저장하지 못했어요. 다시 시도해 주세요.`

Do not use inflated framing such as `건강한 미래 위에 서 있다`, `이것이 우리가 갈린 지점이다`, `단순한 X가 아닌 Y`, or promises of transformation without concrete meaning. Do not put model, prompt, pipeline or harness terminology in the UI unless users need it to make a decision.

Do not join short labels or slogans with floating middle dots (`정교함 · 혁신`, `분석 · 추천 · 성장`). Use a plain sentence, a meaningful heading, or distinct properly labeled controls. Avoid ornamental all-caps eyebrows, invented category names, decorative numbered sections, and arrows appended to every button. Symbols in legitimate data, mathematics or user content are not banned.

Keep action names stable throughout the flow. Show useful guidance for empty and error states, not decorative slogans. Clearly label sample data and simulated results; do not invent testimonials, precision scores or live-AI claims.

## Behavior is part of the design

Plan applicable loading, empty, success, validation-error and retry states. Include editing, canceling and feedback only where required. For a feedback loop, explain what input was recorded and how it affects the next result; a confirmation toast alone does not prove the loop works.

Use semantic controls, visible labels and keyboard-operable flows. Avoid re-creating standard controls without a reason. Map required interactions and states into the verification feature map.

## Review the result

Review the rendered main flow with realistic short and long content at a narrow and wide viewport when allowed. Compare repeated controls side by side. Check outer gutters, section rhythm, component padding, baseline alignment, type hierarchy, letter spacing, contrast, glyph fallback, wrapping, overflow, loading/empty/error states and keyboard focus. Fix systemic token or component problems before one-off margins.

When fresh subagents or sessions are permitted, give one read-only UI critic the brief, SPEC and rendered surface after the writer reaches a stable checkpoint. Ask it to identify the three highest-impact visual problems with concrete locations and evidence. The critic does not edit; the coordinator accepts or rejects each finding and applies coherent fixes. A second opinion on source alone is not a visual review.

Use visual inspection or browser tools only when the environment permits them. In a restricted environment, inspect code and allowed runtime evidence and explicitly leave layout, actual font rendering and visual polish unverified. Do not claim that lint, build or HTTP success proves the screen looks correct.
