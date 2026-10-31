# How to interpret this collection

This collection supports research on long-term video reasoning by vision-language models (VLMs) and multimodal large language models (MLLMs). Its central questions are: **What has happened? What state is the environment in? Which step is happening now? What should happen next? Has something gone wrong, and how could the agent recover?**

## Coverage and provenance

The initial collection contains 94 records in seven categories. A record can be an independent dataset, a benchmark derived from another dataset, a group of related versions, or a watchlist item. The count does **not** represent 94 independent video corpora. Categories follow application and research use; they are not mutually exclusive scientific taxonomies.

Descriptions, access notes, and license observations originate from a primary-source review dated **October 24, 2026**. Duration statements were audited separately on **October 31, 2026**. Each record retains these two dates. Five emerging entries received an additional [publication spot check](publication-checks.md) on October 31; their source-review dates were updated accordingly. Publication does not imply that all downloads were retried on the publication date. Where a later spot check changes a fact, the relevant record must identify that change explicitly.

Evidence comes from original papers, official project pages, author repositories, and selected released metadata. This was a documentation and metadata audit, not a complete download and media-duration measurement of every dataset. Missing statistics remain missing. Links are navigation and evidence pointers, not a guarantee of uninterrupted availability.

## Two independent axes

**Temporal extent** measures how far a sample extends in time. **Procedural dependency** measures how much a correct decision depends on earlier actions, persistent object states, prerequisites, alternative branches, or failure recovery. A several-minute assembly sequence may require substantial procedural reasoning. An hour-long entertainment video may provide little supervision for operational next-step decisions.

Some entries are deliberately short clips, static images, synthetic diagnostics, generic long-video QA, or conventional anomaly-detection datasets. They can support component evaluation and comparisons. They should not be described as full long-horizon procedural benchmarks without further evidence.

## Reading the duration fields

| Term | Interpretation |
| --- | --- |
| Range / min-max | A verified shortest-to-longest span for a specified unit and version. |
| Mean | An average; it does not imply every sample has that duration. |
| SD | Standard deviation; mean plus/minus SD is not a min-max range. |
| Inferred mean | Total time divided by a compatible count; rounding and unit assumptions remain relevant. |
| Upper bound / up to | A maximum or cap; the minimum and distribution can remain unknown. |
| Task means | Means for different tasks; the smallest and largest task means do not give the sample range. |
| Annotation interval | A labeled interval, potentially overlapping or repeated, not necessarily an independent video. |
| Evaluation window | A context or training slice; it need not describe the underlying full recording. |
| Memory / recall span | How far back evidence lies; not necessarily one continuous file. |
| Not verified | A value was not established by this audit; this does not claim it is unavailable elsewhere. |

Always specify the unit: independent execution, recording, synchronized camera stream, episode, clip, or annotation segment. Multi-view footage hours must not be divided by a count of independent executions to infer execution length. Parent-dataset duration must not automatically be assigned to a derivative benchmark.

Optional internal duration buckets are **under 1 minute**, **1-5 minutes**, **5-20 minutes**, **20-60 minutes**, and **at least 60 minutes**. These are proposed bookkeeping bins, not a community standard. Do not assign every sample to a bucket from its dataset mean.

## Editorial roles

| Role | Meaning |
| --- | --- |
| Core candidate | Worth inspecting for procedural understanding, state tracking, decisions, assistance, or failure analysis. This does not certify duration, label completeness, access, or benchmark readiness. |
| Auxiliary | Useful supervision or diagnostic evidence for a component of the overall task. |
| Comparison | A related baseline or evaluation setting whose task, length, or domain differs from the target. |
| Watchlist | Track the resource, but resolve availability, scope, or evidence gaps before inclusion. |

These roles are editorial judgments inherited from the initial survey. A project can have a promising role but still require new annotations. The suggested tasks are applications to investigate, not a claim that every task already has native ground-truth labels.

## Version, access, and rights

Freeze a release, source commit, annotation package, and download date before calculating statistics. Dataset access, code access, paper access, and permission to redistribute are separate questions. A repository license does not necessarily cover video files. Check the provider's current terms, consent restrictions, and upstream rights before using or sharing data.

This repository distributes original catalog descriptions and links. It contains no dataset videos, private industrial data, access credentials, or copied full papers. Dataset rights and citation requirements remain with their respective providers. No blanket license for the referenced datasets is granted by their inclusion here.

## Building an operational benchmark

1. Define the evaluation unit and maintain independent execution IDs across views and derivatives.
2. Split by execution, participant, site, task variation, and upstream video family as appropriate; avoid source-video leakage.
3. Track object and environment state alongside step boundaries, prerequisites, branches, and goals.
4. Separate online evaluation (past and present evidence only) from offline evaluation (future frames available).
5. Distinguish next-action prediction, choosing among valid alternatives, and executing a closed-loop policy.
6. Separate ordinary action recognition, execution errors, environmental hazards, and unusual events. Record onset, cause, severity, recoverability, and corrective action where possible.
7. Measure per-sample durations from the selected release and report min, max, median, percentiles, and independent hours. Keep annotation coverage and missing labels visible.

An incorrect or unexpected action is not automatically an anomalous video, and a surprising scene is not automatically a procedural error. Evaluate these distinctions explicitly.

