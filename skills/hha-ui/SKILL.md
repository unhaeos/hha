---
name: hha-ui
description: Plan, build or review restrained product interfaces with readable typography, clear actions and concrete Korean or English copy. Use for screen work; avoids excessive cards, decorative labels and formulaic AI prose.
license: Apache-2.0; see LICENSE.txt
---

# UI that is easy to read and use

Read [working guidance](../../AGENTS.md) if not loaded. Modified adaptation of selected frontend-design ideas, with hha-specific typography, Korean copy and environment rules. See [attribution](../../THIRD_PARTY.md) and [license](LICENSE.txt).

## Start with the user's task

Name the primary action, the information needed to take it, and the observable outcome. Use the actual domain content. Preserve an existing design system unless asked to change it. For a new screen, put a short flow and small set of type, spacing and color choices in SPEC before building; do not create a separate design bureaucracy.

Make the main content easy to find. Use spacing, alignment and headings before adding containers. Cards are appropriate for independently selectable or repeated objects, such as products; they are not the default wrapper for every paragraph, label and metric. Avoid nested bordered panels, identical tiles for unrelated information, gratuitous badges and dashboard statistics with no user purpose.

When customers and operators have different jobs, design their flows separately: a browsing surface should support choosing, while an operator surface should support inspection, correction and explicit state changes. Reuse shared tokens where appropriate without forcing both into the same dashboard. Use supplied brand references when available; explain choices from the audience and content, not an imitation of a fashionable template.

Choose one useful visual emphasis that suits the product. Do not add gradients, glows, oversized hero copy or animation merely to look designed. A work tool can start directly with the work.

## Typography and color

- Prefer available fonts with reliable glyph coverage. For Korean, use an existing Korean-capable family or a system stack. Do not fetch a decorative font or mix fallback glyphs just for novelty.
- Use a small consistent scale. A reasonable new-app starting point is 16px-equivalent body text, 14px supporting text, and 20/24/32px headings using rem units. Adapt to the existing system and viewport rather than scattering arbitrary sizes. Avoid tiny labels and oversized marketing headings.
- Use comfortable line height, real supported font weights and natural line breaks. Do not scale text with CSS transforms to fit a box. Fractional CSS values alone do not prove a rendering defect: inspect clipping, zoom, font loading and the actual rendering when permitted.
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

Review the main screen with realistic content at a narrow and wide viewport when allowed. Look for unnecessary boxes, vague copy, faint or tiny text, broken glyphs, clipped actions and awkward wrapping. Fix the largest readability issue first.

Use visual inspection or browser tools only when the environment permits them. In a restricted environment, inspect code and allowed runtime evidence and explicitly leave layout, actual font rendering and visual polish unverified. Do not claim that lint, build or HTTP success proves the screen looks correct.
