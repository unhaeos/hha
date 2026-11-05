---
name: hha-plan
description: Turn a project README or task brief into a checklist specification and implementation plan, asking the responsible person only about ambiguities that change the design. Supports empty projects and updating existing plans.
---

# Plan from requirements

Read [working guidance](../../AGENTS.md) if not already loaded. Determine the target project and permitted output path. Default to `hha-work/SPEC.md` in that project, using [this template](../../templates/SPEC.md). Preserve an existing plan's IDs and decisions.

## Read before interviewing

Read the task README, local instructions, supplied data and existing entry points, tests and run scripts. Exclude the downloaded harness from project discovery. Do not assume a framework, package manager or pre-existing app. If instructions conflict, record the conflict and follow the controlling instruction.

Record runtime and data facts that affect implementation: intended data source and location, relevant schema or sample shape, environment-variable names without secret values, startup order, ports, readiness signal and any unavailable dependency. Distinguish observed facts from assumptions. A server listening on a port does not prove that the required data path works.

Extract required behavior, constraints, deliverables and completion conditions. Assign stable IDs such as R1. Cite the source section for each. Separate explicit requirements, user decisions, assumptions and optional polish. A plan must not quietly invent requirements.

Before choosing a solution, summarize the task goal, required result and explicit success conditions from the README. Also state in one sentence what service or operational outcome the company appears to be building toward. Label that product intent explicit or inferred; use it to prioritize optional work and resolve ambiguity, never to replace stated requirements. Do not reopen a problem the brief already defines or force a stakeholder map. Identify the user or audience only when it changes observable behavior or UI. If relevance or selection matters, define useful inclusion and exclusion examples from the supplied domain data. Do not assume partial text matching establishes semantic suitability.

## Ask only about material ambiguities

Ask the responsible person one to three concise questions at a time only when the README and supplied files leave an ambiguity that affects scope, observable behavior or a costly implementation decision. High-value questions clarify priority between stated requirements, source of truth, a business rule, allowed state change, failure behavior or acceptance. For each question, know which design choice the answer changes. Give a recommendation and its practical tradeoff when useful. Do not ask for information already in the files or ask the person to choose an implementation detail that can be decided from evidence. If the user wants to plan together, iterate on the affected parts rather than re-interviewing everything.

Record the answer and its source in SPEC. If the relevant stakeholder is unavailable, keep the question with a provisional default, its consequence and whether it blocks work. Minor reversible choices can be stated assumptions. An unanswered question that changes acceptance behavior remains open; do not invent user agreement. Continue independent parts. No interview is needed when the task is already specified.

## Write an executable specification

For each requirement, record observable acceptance checks, a short implementation checklist, and a separate verification checklist. Expected results come from the brief or explicit decisions, not from whatever the implementation happens to do. For each meaningful risk, state the failure input or condition, the visible error or fallback, and the state that must remain unchanged. Include relevant normal and failure cases; do not add irrelevant defensive behavior.

Add a small service baseline proportional to the task even when the README does not spell it out: the documented app starts, the required path does not end in an unhandled failure, invalid input does not corrupt state, and a failed dependency does not masquerade as success. This is ordinary completion quality, not permission to add production infrastructure, load targets, broad concurrency design or speculative features.

Choose a short implementation order that reaches a working end-to-end path early. For an empty app, include the smallest runnable scaffold as the first step. Choose a stack from constraints and available tools; record the reason instead of scaffolding several alternatives.

If multiple writing sessions are explicitly intended, add a compact coordination section before implementation starts: baseline commit, each writer's owned files or directories, shared API/schema/type contracts, one owner for shared files and dependency changes, server ports and processes, integration order and handoff checks. Use the smallest number of writers that matches clearly separated slices; a fresh reviewer can be temporary rather than another permanent writer. Prefer boundaries that let each writer finish a coherent slice. Do not parallelize tightly coupled edits merely to keep sessions busy; the combined checkpoint must rerun the core path.

Name the required path that should remain complete if optional work is cut. Distinguish agent sessions used to build the app from any runtime AI integration requested by the app: runtime SDKs and services must be explicitly permitted and available, not inferred from another project's example. Label fixture, fallback and real external results separately. Do not drop a mandatory requirement because an anecdote describes a successful project that omitted it.

Treat MCP as an integration decision, not a default setup step. First test whether supplied files, APIs and terminal tools cover the requirement. If MCP would materially fill a missing capability, record its purpose, outbound data, authentication, configuration change, failure behavior and manual fallback, then confirm it is permitted before connecting. A visible JSON configuration option does not establish permission.

For UI work, read [hha-ui](../hha-ui/SKILL.md) and add the main user flow, screen states and compact visual system to this same document. Keep a planned feature distinct from an already implemented feature.

Finish with a self-check: every required README item has an ID; each ID has a testable end state; dependencies are ordered; optional work cannot block the required path; unknowns and required deliverables are visible. This is a same-session check, not an independent review.

The template is a memory aid, not a mandatory sequence. Omit empty optional sections, combine notes that serve the same decision, and change implementation order when new evidence justifies it.

## Keep it useful

Update the SPEC as decisions or evidence change. Keep a decision record only for choices that change behavior, architecture, scope, data handling or a costly/reversible path. Record the alternatives considered, chosen option, source or evidence, reason, accepted tradeoff and condition that would reopen it. A responsible-person answer, user decision, task rule, observed data and AI proposal are different sources; label them honestly. Do not manufacture a disagreement or claim an unrun check. Record reasons for changed requirements and preserve their source; failing code is not a reason to weaken acceptance. Mark implementation complete separately from verified complete. Keep one clear next action. Planning-only requests stop here; otherwise continue the authorized workflow.
