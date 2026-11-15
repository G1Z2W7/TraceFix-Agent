# Security policy

## Report a vulnerability

Do not report a vulnerability in a public Issue.

Use [GitHub private vulnerability reporting](https://github.com/G1Z2W7/TraceFix-Agent/security/advisories/new). Include the affected revision, reproduction steps, impact, and any suggested mitigation.

Do not include live credentials, personal data, or production traces. Replace sensitive values with test fixtures.

## Supported versions

The project has not published a stable release. Security fixes currently target the latest `main` revision.

## Security boundaries

- Replay denies external network access by default.
- Trace adapters remove configured secrets and personal data before transmission.
- Candidate generation can change only registered artifacts.
- Human approval controls promotion.

These boundaries describe the target design. A release note will identify which controls are implemented in each version.
