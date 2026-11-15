# Contributing

Every change starts from a GitHub Issue and enters `main` through a Pull Request.

## Start a change

1. Search existing Issues.
2. Create or claim an Issue with a problem, scope, non-goals, and acceptance criteria.
3. Branch from the latest `main`.

Use a branch name that includes the change type, Issue number, and topic:

```text
feat/12-flowpilot-evals
fix/16-replay-idempotency
docs/1-project-charter
```

## Make the change

- Add a failing public-boundary test before product code.
- Keep the Pull Request focused on one behavior or one architecture boundary.
- Record larger discoveries as separate Issues.
- Do not commit credentials, production traces, personal data, or `.env` files.
- Update the documentation in the same Pull Request as the behavior.

Run the checks that apply to the current repository state:

```powershell
python tools/check_docs.py
python -m unittest discover -s tests/tools -p "test_*.py"
git diff --check
```

## Commit the change

Use Conventional Commit subjects:

```text
docs: establish project charter
feat(flowpilot): add typed call plan
fix(replay): reject duplicate side effects
```

Commits may show the order of the work. The Pull Request will use a squash merge after review.

## Open the Pull Request

Complete the Pull Request template. Link the Issue with `Closes #N`. Include commands and observable results that prove the acceptance criteria.

The repository owner reviews the change and decides whether to merge it. The author must resolve every review thread and rerun required checks after material changes.

## Record architecture decisions

Add an ADR when a change affects a public protocol, state ownership, a durable store, a message contract, or a security boundary. Follow the [ADR guide](docs/adr/README.md).
