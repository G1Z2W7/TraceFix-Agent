# Project charter

## Problem

Agent traces record model calls, retrieval results, and tool calls. A trace does not prove that a failure can be reproduced or that a proposed fix avoids regressions.

TraceFix converts observed failures into versioned replay cases. It evaluates a bounded candidate against both failed and successful cases. A human approves or rejects the candidate.

## Users

TraceFix serves:

- Agent developers who need to reproduce failures;
- reviewers who need evidence before accepting a Prompt or Tool Schema change;
- maintainers who need a repeatable integration contract for an existing Agent.

## Product boundaries

TraceFix owns:

- a provider-neutral trace and replay protocol;
- safe replay with fixed tool responses;
- failure evidence and evaluation reports;
- candidate boundaries, approval records, and rollback data;
- a CLI and Agent Skill that integrate another repository.

TraceFix does not own:

- production model hosting;
- a replacement for Langfuse or OpenTelemetry;
- arbitrary source-code changes;
- automatic merge or deployment;
- production credentials or destructive replay.

## Reference systems

Order Sandbox provides a controlled business system. FlowPilot is the reference Agent that acts on the Sandbox. These systems create realistic traces and failure cases before TraceFix freezes a public protocol.

## Delivery rules

- Each change starts from a GitHub Issue.
- Each Pull Request changes one public behavior or one architecture boundary.
- Local and CI checks use the same commands.
- CI does not depend on a paid or stochastic model.
- The repository adds a module only when a merged behavior needs that owner.
- The user reviews and merges every Pull Request.

## Success criteria

The first public release requires all of the following evidence:

1. FlowPilot completes and verifies a multi-step API workflow.
2. TraceFix reproduces a real FlowPilot failure without external side effects.
3. A regression gate rejects a candidate that breaks a critical historical case.
4. The integration CLI verifies FlowPilot and one independent Agent with the same protocol.
5. A clean machine completes the documented quickstart.
