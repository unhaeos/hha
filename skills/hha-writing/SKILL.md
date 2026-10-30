---
name: hha-writing
description: Write or refine user-facing wording of any length, including buttons, labels, empty states, errors, notifications, README text and result summaries. Use concrete Korean or English and remove vague metaphors, formulaic AI prose and unnecessary structure.
---

# Clear product and technical wording

Apply to a single label as well as a document. Read [AGENTS.md](../../AGENTS.md) if not loaded. Keep the product's established terminology and the user's intended meaning.

## Write the information the reader needs

Name the thing, the action and the result. Use concrete verbs and ordinary sentences. Remove sentences that neither explain a fact nor help the reader act. Keep useful context; brevity does not justify ambiguity.

Avoid abstract metaphors and staged revelations: `여기서 갈린다`, `그 위에 서 있다`, `새로운 가능성을 열다`, `진정한 가치를 실현하다`. Do not automatically write `단순한 X가 아닌 Y`, question-and-answer hooks, or three-part slogans. Replace them with the specific behavior or decision; if the fact is unknown, do not invent it.

Do not decorate content with middle-dot chains such as `속도 · 혁신 · 연결`, repeated eyebrow labels, gratuitous bold text or a heading for each sentence. A real comparison or technical distinction is fine when it conveys necessary information. Do not alter exact quotes, identifiers, user-entered text or legitimate mathematical notation just to satisfy style.

## Match the surface

- Buttons: name the action and object when needed, such as `상품 저장` or `선택 해제`. Distinguish saving a draft from publishing.
- Empty states: say what is missing and the available next action. `등록된 상품이 없어요. 상품을 추가해 주세요.`
- Errors: state the failed action and a real recovery option. Do not promise data was preserved unless the app guarantees it.
- Success messages: report only what completed. A submitted job is not a completed result.
- Supporting text: explain a choice or consequence, not the application's internal pipeline.
- README and reports: lead with the useful outcome, then evidence, limitations and next steps only where needed. Do not turn a small change into an essay.

## Edit examples

`건강한 선택이 시작되는 지점` → use the actual task, for example `내 조건에 맞는 상품 찾기`.
`추천과 운영은 여기서 갈리지 않습니다` → if this is the implemented behavior, `추천 상품을 수정한 뒤 발행할 수 있어요`.
`정교함 · 신뢰 · 혁신` → remove it or state a supported fact, such as `발행 전에 상품과 문구를 확인하세요`.

These are patterns, not mandatory replacement strings. Read nearby UI and confirm the suggested wording matches actual behavior. After editing, check terminology, button length, claims and the recovery path. Actual line wrapping and visual fit require permitted visual inspection; source review alone cannot prove them.
