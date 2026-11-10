# Rails inventory backtest — November 9, 2026

The adapted seven-stage workflow reproduced the narrow version-label correction in
[awesome-rails #150](https://github.com/gramantin/awesome-rails/pull/150), then left
its corrected counterpart unchanged. Both runs kept the official Rails website and
source-code entries. This is a small, purposefully selected retrospective fixture,
not a blinded discovery test or an accuracy estimate.

| Catalog | Expected | Observed | Patch | Time | Estimated cost |
| --- | --- | --- | --- | --- | --- |
| Before #150 | Correct Lobsters' Rails 7.0 label | Update to Rails 8.1; preserve both URLs and surrounding entries | One ready historical patch; applicability, structure and changed-entry links passed | 24.82s | $0.695826 |
| After #150 | Keep corrected Lobsters entry | Keep all three entries | No patch | 22.16s | $0.657258 |

Provider-reported historical-pair total: **$1.353084**; including the current run, **$1.965593**. Costs are estimates, not invoices. The two
historical runs used Opus 5.5, medium effort, official Claude Code 2.1.284 and
published UM 0.72.1. The adaptation's executable production files were frozen
before both runs; no tuning occurred between them.

## Inputs and limits

The historical catalog revisions were
[`d7d31c7`](https://github.com/gramantin/awesome-rails/commit/d7d31c76c45a814e22963b9cf4ee1e751501460e)
and [`e1d0523`](https://github.com/gramantin/awesome-rails/commit/e1d052387f26e352373c0afe6f66b8831f599b04).
Each execution checkout had a synthetic commit containing that catalog snapshot.
The selected entries were Lobsters, Rails Official Website and Rails Source Code.

Both runs received the same independently fetched, pinned
[Lobsters Gemfile.lock](https://github.com/lobsters/lobsters/blob/2f385d149e67f5ff78643dcf6d3cab0b24c0117c/Gemfile.lock),
which declares Rails 8.1.3.1. Supplying that relevant source makes this a test of
interpreting evidence and constructing the correction, **not proof of discovering
the mismatch unaided**. The agents separately fetched official Rails and Lobsters
pages for identity/relevance checks. Dependency declarations do not prove runtime
compatibility, and current page content is not a reconstruction of the historical web.

Expected labels, target PR outcomes/discussion and other runs were withheld from
the model input. The audited tool requests only accessed the official Rails site,
Rails repository and Lobsters repository; no target catalog outcome exposure was
detected. Prompt restrictions and a clean trace are not a guarantee of isolation.

Evaluation-only adapters selected the three entries, supplied the pinned source,
limited history queries to records created and last updated before
2026-08-18T20:37:28Z, and checked freshness against the frozen checkout. The latter
permits an evaluated historical patch but **cannot authorize a current correction**.
The production workflow retains its current upstream `master` recheck. Excluding
records updated after the cutoff can omit legitimate older discussion; this is not
a complete reconstruction of history. The reports' displayed query strings omit
the adapter-added cutoff, which is recorded here and in the retained protocol.

## Separate current-source trial

The predeclared current sample used FAE, canvas-lms and Rails Official Guide from
upstream revision `7bbd6fbe39d889ce38ae0fc6b3026bb63eb75570`. It supplied no source
snapshots, expected answers, history cutoff or freshness override. The agent found
FAE's stale Rails 5.2 label and proposed Rails 7.0, while retaining Canvas and the
Rails Guides unchanged. The production history stage found the original FAE addition
and an unrelated typo discussion; it did not mistake them for a duplicate correction.
The one-entry patch passed structure, destination and current-upstream checks.
Runtime: **42.41s**; provider estimate: **$0.612509**.

Independent inspection confirms [FAE's Gemfile](https://github.com/wearefine/fae/blob/master/Gemfile)
uses Rails `~> 7.0.2` for the dummy app, its lockfile resolves `7.0.2.3`, and its
[README](https://github.com/wearefine/fae/blob/master/README.md) distinguishes Fae 3.x's
Rails 7 support from legacy Fae 2.x's Rails 5.0–5.2 support. The broad gemspec floor is
not a reason to keep the old label. This verifies documentary consistency, not
runtime compatibility. Canvas's official README supports its LMS description, and
[the official Rails Guides](https://guides.rubyonrails.org) support that keep decision.
The two keeps were not exhaustively audited beyond their listed claims.

One raw history explanation says the old 5.2 label was accurate when added in 2021.
The retrieved history establishes that it was listed then, not that it was correct;
that historical assertion is **not independently verified**. It does not change the
current version evidence. Raw output remains retained rather than silently rewritten.

Two earlier attempts at this current sample failed at UM's command-launch phase,
before either model stage started. A model-free A/B check reproduced failure with a
long temporary path and success with a short one; the shared runner was corrected.
Both failures and their missing model receipts remain retained, with explicit
no-model reconciliation. They are not counted as successful tests or fabricated
zero-dollar receipts. The final current-source run used the corrected runner.

Between the paired and current runs, review found that valid parentheses in 18 existing
catalog labels could abort an unrelated correction. The guard now accepts parentheses
while retaining bracket/newline injection checks; a focused regression covers it.
No prompt or judgment tuning followed the historical outputs. The retained paired
runs use their original guard, and the current run uses the final guard. Source hashes
and this exact difference are recorded locally. The paired selected labels contain
no parentheses, so their observed correction is unaffected by that guard fix.

## Retained evidence and checks

- [Before report](backtests/before.md), [historical patch](backtests/before.patch).
- [Corrected control report](backtests/after.md), [current report](backtests/current.md),
  [current proposed patch](backtests/current.patch), [compact results](backtests/summary.json).
- Ten offline adapter tests passed; UM validated all seven stages; actionlint
  passed both GitHub workflow files. Current-catalog packet preparation recognized
  417 resource entries in 139 slices.

Full local run receipts, tool audits, inputs, source snapshots, protocol and hashes
are retained in the acquisition workspace. They contain no upstream publication.
The GitHub-hosted integration has not been run. The historical pair and current finding support a
reviewable fork trial, not general accuracy, autonomous editing or claimed hours saved.
