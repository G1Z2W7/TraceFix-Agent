# Delivery roadmap

The roadmap describes the current dependency order. Create only the next three Issues. Revisit later work after each milestone.

## Milestone 0: engineering contract

- PR-001 establishes the project charter, contribution process, templates, and documentation checks.
- PR-002 adds an executable FastAPI and PostgreSQL walking skeleton.

## Milestone 1: Order Sandbox

- Add the order aggregate and PostgreSQL persistence.
- Add lifecycle rules, transactions, and concurrency tests.
- Add Redis idempotency and coordination.
- Add the transactional outbox and RabbitMQ worker.

Exit result: a controlled business system with reproducible failure modes.

## Milestone 2: FlowPilot

- Normalize OpenAPI and establish a deterministic retrieval baseline.
- Compare the baseline with pgvector hybrid retrieval.
- Add typed tools and an allow-listed HTTP executor.
- Add a deterministic LangGraph workflow and generated pytest artifact.
- Add structured model planning, Langfuse traces, and a versioned evaluation set.

Exit result: a useful and measurable API workflow Agent.

## Milestone 3: TraceFix

- Derive protocol v1 from real FlowPilot traces.
- Add the Langfuse adapter and canonical trace storage.
- Add safe replay and evidence-based diagnosis.
- Add bounded candidate generation, regression evaluation, approval, and rollback.

Exit result: a local reliability workflow for FlowPilot failures.

## Milestone 4: integration kit

- Add the TraceFix CLI and machine-readable verification report.
- Add the `tracefix-integrate` Agent Skill.
- Integrate a second Agent without changing protocol semantics.

Exit result: a verified cross-repository integration path.

## Milestone 5: public release

- Decide whether the first release needs an operator console.
- Complete security and operations hardening.
- Test the quickstart and release documentation on a clean machine.

Release `v1.0.0` only after a repository outside this monorepo passes the integration contract without special handling.
