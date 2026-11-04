# Project specification

## Goal and constraints

- Source requirements:
- User outcome:
- Intended user and decision this helps:
- Required deliverables:
- Environment and available tools:
- Runtime/data facts: intended source, schema/sample, env var names, startup order, ports and unknowns
- Required end-to-end path:
- Out of scope:
- Deadline, if supplied:

## Decisions and open questions

Separate user decisions from provisional assumptions. Record only choices that affect the work, with their reason. Keep unresolved acceptance questions visible.

## Requirements

### R1 — Requirement name

- Source section:
- Priority: required / optional
- Acceptance:
  - R1.A1: Given ..., when ..., the observable result is ...
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

## Coordination, only if there are parallel writers

- Baseline commit:
- Work ownership by files/directories:
- Shared API/schema/type contract and its owner:
- Dependency, migration, data initialization and server/port owner:
- Integration order and handoff checks:

## UI choices, only if relevant

Main flow, screen states, layout, type scale, colors and concrete action labels.

## Decisions, evidence and remaining work

- Significant decision and reason, including material AI proposal and adopted/modified/deferred/rejected status when applicable:
- One real request trace: input -> validation -> handler -> data/query -> processing -> response -> consumer
- Evidence level: source / unit-command / fixture-mock / intended service-data / end-to-end
- Integration check on the combined checkpoint:
- Failed check, correction and recheck:
- Unimplemented:
- Unverified:
- Next action:
