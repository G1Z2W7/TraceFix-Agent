# ADR-0001: Derive protocol v1 from the reference Agent

- Status: Proposed
- Date: 2026-11-15
- Owners: `@G1Z2W7`

## Context

TraceFix aims to support Agent systems that use different languages, frameworks, and trace providers. Freezing a public protocol before observing a complete Agent workflow would encode assumptions that no running system has tested.

FlowPilot can produce real model, retrieval, tool, state, and failure events. Those events provide evidence for the first public trace and replay contracts.

## Decision

Build the Order Sandbox and a measurable FlowPilot workflow before freezing TraceFix protocol v1.

FlowPilot must still record internal run identifiers, Agent versions, configuration digests, and privacy markings from its first tracing change. These internal fields can change before protocol v1.

The public protocol remains provider neutral. Langfuse, LangGraph, storage rows, and queue messages stay inside adapters.

## Consequences

- The project delays the public integration kit until FlowPilot produces real traces.
- Early FlowPilot traces may require a migration before protocol v1.
- Protocol decisions gain concrete replay and failure evidence.
- A second independent Agent must pass the same contract before `v1.0.0`.

## Alternatives considered

### Freeze the protocol first

This order lets package work start sooner. It risks encoding speculative fields and FlowPilot-specific assumptions.

### Use Langfuse traces as the protocol

This order reduces the first adapter. It binds TraceFix to one provider and cannot require replay fields that Langfuse does not capture.

## Verification

Before accepting protocol v1:

1. Run the full FlowPilot workflow against Order Sandbox.
2. Capture success and failure traces.
3. Build a frozen-tool replay from one real failure.
4. Confirm that no protocol field names an Order Sandbox or LangGraph concept.
