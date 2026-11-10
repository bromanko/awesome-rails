# Rails catalog inventory review

This opt-in, manually triggered UM workflow investigates three catalog entries and
previews evidence-backed corrections. It reports current descriptions, names,
canonical destinations and Rails-version labels. It never edits the catalog,
opens correction PRs, comments, schedules itself or merges changes.

## Review and output

The seven stages retain the existing inventory workflow design: prepare the pinned
catalog, investigate selected entries, collect prior discussions, review that
history, build bounded corrections, validate them, and render the preview. GitHub
Actions invokes UM once, displays its report and saves the proposed-changes ZIP.

Each correction changes one native README entry. Inline and reference-style bullets,
including existing secondary links, retain their order and formatting. Reference
URL corrections affect only the selected entry. Generator-table name/URL corrections
preserve the other columns; table-description rewrites require manual editing and
are withheld. Every selected entry receives a recommendation, evidence and uncertainty.

Version evidence comes from official dependency files and documentation. It does
not establish runtime compatibility. Historical articles, old versions, archived
projects and existing deprecation labels are not automatically removal candidates.
The model gathers evidence and the maintainer decides what belongs.

Prior-discussion searches include the upstream repository and the executing fork.
Incomplete searches, unresolved objections or already-proposed corrections hold a
patch. Limits are 30 results per query, 10 discussions per candidate and 100 records
per discussion-detail request. The catalog is rechecked against upstream `master`;
a changed or inaccessible catalog prevents a ready patch.

Validation checks patch applicability, exact one-entry structure and positive
Lychee success for destinations in the changed entry. This repository has no native
lint/test workflow in the source snapshot, so no other catalog's lint, spelling or
ordering rules are imposed. This is not a whole-catalog link audit. Missing tools,
timeouts and missing link-success evidence hold the patch. Removal recommendations
still require affirmative source evidence and maintainer judgment; structural
validation cannot prove a removal's factual merits.

## Enable a fork trial

1. Review and merge the integration into the fork's default branch when ready.
2. Configure the `awesome-rails-review` environment with required reviewers and an
   `ANTHROPIC_API_KEY` environment secret.
3. Set repository variable `UM_FRESHNESS_ENABLED=true`.
4. Dispatch **UM freshness review** with a zero-based slice number.

The pilot uses published UM 0.72.1, official Claude Code 2.1.284 and Opus 5.5 at
medium effort. It has a 45-minute job timeout, no production dollar cap and no
automatic schedule; enabling it incurs provider usage. GitHub permissions are
read-only and checkout does not persist credentials. Agent tools remain available;
read-only instructions are not an execution sandbox. The admitted read-only GitHub
token supports public history queries; it is not a write credential.

A slice consists of three parsed resource entries. Catalog edits can shift slices;
record reviewed entries manually. This is not persisted recurring coverage.

## Validate locally

```sh
python3 -m unittest discover -s .um/freshness/tests -v
um workflow validate --source-root .um/freshness --json .um/freshness/workflow.yaml
actionlint .github/workflows/um-freshness.yml .github/workflows/um-freshness-checks.yml
```

The integration adapts the existing inventory workflow at
[bromanko/awesome-ratatui, 91ec0be](https://github.com/bromanko/awesome-ratatui/commit/91ec0be3aecb93d17b6f18e771ea86b52022f2de).
Its earlier results do not establish this Rails adaptation's behavior. See
[BACKTEST.md](BACKTEST.md) for this adaptation's actual local results and limits.
A GitHub-hosted trial remains separate from local validation.
