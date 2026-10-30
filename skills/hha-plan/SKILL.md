---
name: hha-plan
description: Turn a project README or task brief into a checklist specification and implementation plan, using a short interview for material unresolved choices. Supports empty projects and updating existing plans.
---

# Plan from requirements

Read [working guidance](../../AGENTS.md) if not already loaded. Determine the target project and permitted output path. Default to `hha-work/SPEC.md` in that project, using [this template](../../templates/SPEC.md). Preserve an existing plan's IDs and decisions.

## Read before interviewing

Read the task README, local instructions, supplied data and existing entry points, tests and run scripts. Exclude the downloaded harness from project discovery. Do not assume a framework, package manager or pre-existing app. If instructions conflict, record the conflict and follow the controlling instruction.

Extract required behavior, constraints, deliverables and completion conditions. Assign stable IDs such as R1. Cite the source section for each. Separate explicit requirements, user decisions, assumptions and optional polish. A plan must not quietly invent requirements.

Describe who uses the result and which concrete decision or task it improves. A business-purpose interpretation is a hypothesis until supported by the brief or user; it does not override required behavior. If relevance or selection matters, define useful inclusion and exclusion examples from the supplied domain data. Do not assume partial text matching establishes semantic suitability.

## Interview only what changes the work

Ask one to three concise questions at a time when answers affect scope, observable behavior or a costly implementation decision. Give a recommendation and its practical tradeoff when useful. Do not ask for information already in the files. If the user wants to plan together, iterate on the affected parts rather than re-interviewing everything.

Minor reversible choices can be stated assumptions. An unanswered question that changes acceptance behavior remains open; do not invent user agreement. Continue independent parts. No interview is needed when the task is already specified.

## Write an executable specification

For each requirement, record observable acceptance checks, a short implementation checklist, and a separate verification checklist. Expected results come from the brief or explicit decisions, not from whatever the implementation happens to do. Include relevant normal and failure cases; do not add irrelevant defensive behavior.

Choose a short implementation order that reaches a working end-to-end path early. For an empty app, include the smallest runnable scaffold as the first step. Choose a stack from constraints and available tools; record the reason instead of scaffolding several alternatives.

Name the required path that should remain complete if optional work is cut. Distinguish agent sessions used to build the app from any runtime AI integration requested by the app: runtime SDKs and services must be explicitly permitted and available, not inferred from another project's example. Label fixture, fallback and real external results separately. Do not drop a mandatory requirement because an anecdote describes a successful project that omitted it.

Treat MCP as an integration decision, not a default setup step. First test whether supplied files, APIs and terminal tools cover the requirement. If MCP would materially fill a missing capability, record its purpose, outbound data, authentication, configuration change, failure behavior and manual fallback, then confirm it is permitted before connecting. A visible JSON configuration option does not establish permission.

For UI work, read [hha-ui](../hha-ui/SKILL.md) and add the main user flow, screen states and compact visual system to this same document. Keep a planned feature distinct from an already implemented feature.

Finish with a self-check: every required README item has an ID; each ID has a testable end state; dependencies are ordered; optional work cannot block the required path; unknowns and required deliverables are visible. This is a same-session check, not an independent review.

## Keep it useful

Update the SPEC as decisions or evidence change. Record reasons for changed requirements and preserve their source; failing code is not a reason to weaken acceptance. Mark implementation complete separately from verified complete. Keep one clear next action. Planning-only requests stop here; otherwise continue the authorized workflow.
