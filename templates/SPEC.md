# Project specification

## Task definition

- Source requirements:
- Task goal and required result:
- Product/service intent: explicit / inferred — one sentence
- Explicit success conditions:
- User/audience, only if it changes behavior or UI:
- Required deliverables:
- Environment and available tools:
- Runtime/data facts: intended source, schema/sample, env var names, startup order, ports and unknowns
- Required end-to-end path:
- Out of scope:
- Deadline, if supplied:
- Verification reserve and expensive checks, if time-limited:

## Open ambiguities, omit if none

Keep only README ambiguities whose answers change scope, behavior or a costly choice.

- Q1: question — design impact; answer/source or provisional default and consequence; open / answered / assumed

## Key decisions, omit if none

Record only material choices. Do not invent alternatives after the fact.

- D1: choice over real alternative — basis/source and reason; accepted tradeoff; revisit when ...

## Requirements

### R1 — Requirement name

- Source section:
- Related question/decision IDs:
- Priority: required / optional
- Acceptance:
  - R1.A1: Given ..., when ..., the observable result is ...
- Failure/invariant, when relevant:
  - R1.F1: Given ..., the visible error/fallback is ... and ... remains unchanged
- Implementation:
  - [ ] Small implementation step
- Verification:
  - [ ] R1.A1 checked against the expected result
- Evidence/status: NOT RUN
- Implementation location:

Repeat for each requirement. Implementation checked does not mean verification passed.

## Implementation order

1. Smallest runnable end-to-end path
2. Remaining required paths and relevant failure states
3. Regression checks and required deliverables

Adapt this order when evidence or dependencies justify it. Do not treat the template as ceremony.

## Coordination, only if there are parallel writers

- Baseline commit:
- Work ownership by files/directories:
- Shared API/schema/type contract and its owner:
- Dependency, migration, data initialization and server/port owner:
- Integration order and handoff checks:

## UI choices, only if relevant

Main flow, screen states, layout, type scale, colors and concrete action labels.

## Decisions, evidence and remaining work

- Decision updates or invalidated assumptions:
- One real request trace: input -> validation -> handler -> data/query -> processing -> response -> consumer
- Evidence level: source / unit-command / fixture-mock / intended service-data / end-to-end
- Integration check on the combined checkpoint:
- Failed check, correction and recheck:
- Unimplemented:
- Unverified:
- Next action:
