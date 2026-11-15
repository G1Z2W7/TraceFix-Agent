# Architecture decision records

An architecture decision record, or ADR, explains one decision that changes ownership, a public contract, a data model, or an operational boundary.

Create an ADR when a change:

- defines or changes a public protocol;
- moves state ownership between modules;
- introduces a durable data store or message contract;
- changes a security or replay boundary;
- rejects a viable architecture alternative.

Do not create an ADR for a local implementation detail that a future Pull Request can replace without migration.

Copy [`0000-template.md`](0000-template.md) to the next numbered file. Set the status to `Proposed`. A reviewer changes the status through the Pull Request that accepts or rejects the decision.
