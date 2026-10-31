# Emerging Benchmarks and Watchlist

[Back to the collection](../README.md) · [Duration methodology](../docs/methodology.md) · [JSON data](../data/datasets.json)

Recent egocentric reasoning, assistance, grounding, and synthetic diagnostics; access and task scope vary.

**8 records.** Suggested applications are editorial research directions; consult annotations and caveats before assuming native task support.

## Contents

- [FRO-01 · EgoSafetyBench](#egosafetybench)
- [FRO-02 · EgoSAT](#egosat)
- [FRO-03 · EgoTL](#egotl)
- [FRO-04 · LongEgoRefer](#longegorefer)
- [FRO-05 · Minerva-Ego](#minerva-ego)
- [FRO-06 · EgoGapBench](#egogapbench)
- [FRO-07 · EgoVoice](#egovoice)
- [FRO-08 · ObjChangeVR](#objchangevr)

---

<a id="egosafetybench"></a>

## FRO-01 · EgoSafetyBench

**Auxiliary** · **Year / version:** 2026; v1 submitted 2026-06-30; v2 submitted 2026-10-04

The main benchmark contains 1,200 synthetic robot-view scenarios for detecting hazards, avoiding false alarms, and resisting misleading visual signs. Paper v2 additionally describes a separate 20-clip real-video sanity check whose release was not established.

- **Duration:** Main synthetic benchmark: generated full clips are fixed at 5 seconds by paper design (minimum = maximum = 5 seconds), each divided into ten nonoverlapping 0.5-second chunks. Media-container durations were not measured file by file; no duration is established here for the separate real-video check.
- **Collection size:** Main full set: 1,200 five-second clips, implying 6,000 seconds = 100 minutes, approximately 1.667 hours. It comprises 800 situational clips and 400 visual-channel clips arranged as 200 true/false-sign pairs; paired variants are not independent executions. The card lists core800, standard1000, and full1200 variants. Paper v2 separately reports 20 real-video check clips, not an addition to the main 1,200.
- **Potential applications:** Hazard detection; False-alarm control; Hazard-onset alerting; Robustness to misleading visual text.
- **Modalities / available information:** Main set: synthetic egocentric robot chest-view video, textual signs, chunk-level labels, and explanations. Paper v2 also describes a separate real-video check.
- **Dataset family:** Independent synthetic robot-view benchmark, with a separately described real-video sanity check in paper v2.
- **Access evidence:** As of 2026-10-31: Gated; the official Hugging Face API verifies a nonprivate repository with automatic gating and 1,200 MP4 filenames plus annotations. Access requires login and agreement to share account information. No gate was accepted and no media were downloaded; file integrity and completeness against the specification were not verified. Release of the separate 20-clip real-video check is unconfirmed.
- **License observations:** The official Hugging Face data card declares CC BY 4.0 for the dataset. The official GitHub README and LICENSE establish Apache-2.0 for the code repository; these are separate licenses.
- **Caveats:** Use paper v2, available at the 2026-10-31 cutoff, to qualify the original v1 account. The canonical 5-second duration is the full clip; 0.5 seconds is a chunk. The verified 1,200-file manifest supersedes the earlier uncertainty about listed media, but it does not prove successful downloads or decoding. Short synthetic contexts do not establish long procedural dependencies or recovery planning. The HF history and raw-card endpoints returned HTTP 401 without authentication, which is an access limitation rather than evidence of missing data. Repository timestamps do not prove an exact first-public-release date.

**Primary links** · Source review: 2026-10-31 · Duration audit: 2026-10-31

- [EgoSafetyBench paper v1: full-clip and chunk design](https://arxiv.org/html/2607.00218v1)
- [EgoSafetyBench official gated dataset and declared data license](https://huggingface.co/datasets/AIM-Intelligence/EgoSafetyBench)
- [EgoSafetyBench official Hugging Face API: gating and 1,200-video manifest](https://huggingface.co/api/datasets/AIM-Intelligence/EgoSafetyBench)
- [EgoSafetyBench arXiv submission and revision history](https://arxiv.org/abs/2607.00218)
- [EgoSafetyBench paper v2: synthetic benchmark and separate real-video check](https://arxiv.org/html/2607.00218v2)
- [EgoSafetyBench official code repository](https://github.com/AIM-Intelligence/EgoSafetyBench)
- [EgoSafetyBench official Apache-2.0 code license](https://raw.githubusercontent.com/AIM-Intelligence/EgoSafetyBench/main/LICENSE)
- [EgoSafetyBench official HF history endpoint, access limited during audit](https://huggingface.co/api/datasets/AIM-Intelligence/EgoSafetyBench/commits/main)
- [EgoSafetyBench official raw data card endpoint, access limited during audit](https://huggingface.co/datasets/AIM-Intelligence/EgoSafetyBench/raw/main/README.md)

---

<a id="egosat"></a>

## FRO-02 · EgoSAT

**Core candidate** · **Year / version:** 2026

Ego4D-derived interaction sessions support streaming questions about current events, past evidence, and future actions. Visibility-switch labels and multiple-choice queries evaluate narration, retrieval, prediction, and answerability as the observed prefix grows.

- **Duration:** Constructed interaction sessions are roughly 230-300 seconds (approximately 3.83-5 minutes), with a paper-reported mean of 296.8 seconds (approximately 4.947 minutes). The range is the authors' rough description, not measured exact extrema, and does not describe original full Ego4D recordings.
- **Collection size:** The paper reports 1,997 sessions, approximately 165 hours, and about 4,800 QA items. Mean duration x count gives approximately 164.64 hours, consistent with the rounded total. Footage comes from Ego4D; reused question prefixes do not add independent hours. The main release candidate contains approximately 264 MB of annotations/manifests.
- **Potential applications:** Streaming current-action narration; Interaction visibility-switch detection; Short-term and multistep prediction; Past-event retrieval; Answerability and confidence analysis.
- **Modalities / available information:** Egocentric video, textual QA, interaction-visibility labels, and separately released ROI caches.
- **Dataset family:** Constructed sessions and new annotations derived from Ego4D footage, not 165 newly recorded hours.
- **Access evidence:** As of 2026-10-24: Public Hugging Face annotations and the file tree were verified. Raw RGB is not redistributed and requires separate Ego4D authorization; videos were not downloaded and evaluation was not run.
- **License observations:** The Hugging Face card uses other and specifies research use. Code is separately MIT, while Ego4D media retain the upstream agreement.
- **Caveats:** The canonical audit adds approximate session lengths; streaming and a 165-hour total do not imply hour-long individual samples. State switches concern interaction visibility rather than every physical object-state change. Confidently wrong describes model errors, not verified human execution failures. Some release-candidate sample files are intentionally empty; use effective querysets rather than raw file counts. Original RGB access and full release completeness were not tested.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoSAT paper v1, Section 3.4: benchmark construction](https://arxiv.org/html/2606.24422v1)
- [EgoSAT official release candidate, schema, and terms](https://huggingface.co/datasets/YijiaLeithu/EgoSAT)
- [EgoSAT official published file tree](https://huggingface.co/datasets/YijiaLeithu/EgoSAT/tree/main)

---

<a id="egotl"></a>

## FRO-03 · EgoTL

**Core candidate** · **Year / version:** 2026; paper submitted 2026-04-10

Participants navigate homes and manipulate objects while speaking their intentions before acting. Separate environment walkthroughs provide memory context for planning, action prediction, direction recognition, and distance estimation.

- **Duration:** The paper describes task episodes lasting 2-4 minutes; this is a collection-protocol range, not independently remeasured exact minimum and maximum. A separate memory-bank environment walkthrough lasts approximately 2 minutes and must not be added as if it were one continuous task video.
- **Collection size:** Paper scope: 400 episodes, over 100 task types, and 50 participants; actual cumulative episode hours are unknown. The public partial-release manifest lists 19 episode-annotation JSON files and 256 MP4 clips, not 256 or 400 released episodes. Task videos and walkthroughs require separate duration accounting.
- **Potential applications:** Memory-conditioned planning; Environment-conditioned action reasoning; Next-action prediction; Action recognition; Direction recognition; Distance estimation.
- **Modalities / available information:** Egocentric RGB, synchronized speech, word-level timestamps, spatial measurements, and separate environment-memory videos.
- **Dataset family:** Independent EgoTL collection, with task episodes and separately recorded environment walkthroughs.
- **Access evidence:** As of 2026-10-31: Open, partial release; the author-linked Hugging Face repository is public and ungated, and its card explicitly describes selected episodes. The API lists 19 episode-annotation JSON files and 256 MP4 clips. Upload history includes commit a817cb36d7b3e0f4d4dd3f8a1716b29ed90a4ea6 dated 2026-04-14 17:19:41 UTC. Media downloading and full release of the paper's 400 episodes were not verified.
- **License observations:** The Hugging Face card declares license: other. Specific usage and redistribution permissions were not established; MIT must not be assumed.
- **Caveats:** The canonical 2-4-minute range is retained, but multiplying 400 by its endpoints does not establish actual total duration. Manifest file counts supersede ambiguous viewer-row counts and are not independent-episode counts or duration measurements. Complete paper-version splits and exact released-media duration remain unverified. The April 14 upload commit documents repository history, not necessarily the first moment of public availability. Spoken-intention collection affects behavior; model omission/hallucination diagnostics do not establish human failure-and-recovery labels.

**Primary links** · Source review: 2026-10-31 · Duration audit: 2026-10-31

- [EgoTL paper v1: collection statistics and task definitions](https://arxiv.org/html/2604.09535v1)
- [EgoTL official project](https://ego-tl.github.io/)
- [EgoTL official linked data card](https://huggingface.co/datasets/luuuulinnnn/EgoTL-DATA)
- [EgoTL published file tree](https://huggingface.co/datasets/luuuulinnnn/EgoTL-DATA/tree/main)
- [EgoTL arXiv submission history](https://arxiv.org/abs/2604.09535)
- [EgoTL official raw data card: selected episodes and license declaration](https://huggingface.co/datasets/luuuulinnnn/EgoTL-DATA/raw/main/README.md)
- [EgoTL official HF API: public status and annotation/video file counts](https://huggingface.co/api/datasets/luuuulinnnn/EgoTL-DATA)
- [EgoTL official HF history: April 14, 2026 partial upload](https://huggingface.co/api/datasets/luuuulinnnn/EgoTL-DATA/commits/main)

---

<a id="longegorefer"></a>

## FRO-04 · LongEgoRefer

**Auxiliary** · **Year / version:** 2026; paper submitted 2026-07-02

Natural-language expressions identify object occurrences within long egocentric videos using interaction and state-change clues. Temporal coordinates, bounding-box trajectories, and inherited object attributes support spatiotemporal referring-expression comprehension.

- **Duration:** Full Ego4D source videos were selected to be at least 20 minutes long; the paper reports a mean of 2,714.9 seconds (approximately 45.248 minutes) across 433 videos. Exact minimum and maximum were not independently established, and the maximum remains unknown in the canonical audit. Object occurrences are localized intervals within these videos, not complete procedural sessions.
- **Collection size:** 433 unique source videos, 1,498 object occurrences/referring expressions, 769 clips, and 442 object titles. Independent media hours were not directly verified and are not newly derived from the mean. Existing Ego4D/EgoTracks footage adds no new recording hours. The public annotation file is 103,537,195 bytes (approximately 98.74 MiB).
- **Potential applications:** Long-video referring-expression comprehension; Temporal object localization; Spatial object grounding; State-aware object retrieval.
- **Modalities / available information:** Long RGB video, referring expressions, temporal coordinates, bounding-box tracks, interaction labels, and object-state attributes.
- **Dataset family:** Annotations derived from Ego4D and EgoTracks; shared source footage must not be counted as additional independent media.
- **Access evidence:** As of 2026-10-31: The annotation JSON and documentation are public; source videos are excluded from the repository and must be obtained separately under Ego4D/EgoTracks terms. File API metadata and an annotation commit dated 2026-06-23 10:49:28 UTC were verified. The large JSON and source media were not downloaded; full integrity and video availability after authorization remain unverified.
- **License observations:** The repository README says annotations follow upstream Ego4D/EgoTracks terms. This establishes a stated upstream terms relationship, not a separate permissive annotation license or an MIT code license; source video remains subject to upstream access terms.
- **Caveats:** The publication audit verifies an existing annotation artifact and corrects the earlier 98.7 MB description to 103,537,195 bytes, approximately 98.74 MiB. The README reports roughly 20-118-minute source videos, but the canonical audit does not independently verify those exact endpoints or the earlier 10-443-second occurrence range; retain that uncertainty. The annotation commit 09f49e6499c0ddc1a192d5611f7b3a904e4d0ec5 predates the arXiv submission but does not establish a first-public-release date. Long object retrieval is not full-procedure tracking, next-action decision supervision, or failure/recovery annotation.

**Primary links** · Source review: 2026-10-31 · Duration audit: 2026-10-31

- [LongEgoRefer paper and submission history](https://arxiv.org/abs/2607.02096)
- [LongEgoRefer official repository and upstream terms](https://github.com/shunya-kato/LongEgoRefer)
- [LongEgoRefer official annotation statistics and schema](https://raw.githubusercontent.com/shunya-kato/LongEgoRefer/main/dataset/README.md)
- [LongEgoRefer public annotation file](https://github.com/shunya-kato/LongEgoRefer/blob/main/dataset/longegorefer.json)
- [LongEgoRefer paper v1, Sections 3.2-3.3 and Table 1](https://arxiv.org/html/2607.02096v1)
- [LongEgoRefer official annotation file API: exact byte size](https://api.github.com/repos/shunya-kato/LongEgoRefer/contents/dataset/longegorefer.json)
- [LongEgoRefer official annotation-file commit history](https://api.github.com/repos/shunya-kato/LongEgoRefer/commits?path=dataset/longegorefer.json&per_page=100)
- [LongEgoRefer annotation upload commit dated June 23, 2026](https://github.com/shunya-kato/LongEgoRefer/commit/09f49e6499c0ddc1a192d5611f7b3a904e4d0ec5)

---

<a id="minerva-ego"></a>

## FRO-05 · Minerva-Ego

**Auxiliary** · **Year / version:** 2026

Expert-written questions require combined temporal, counting, causal, goal, spatial, event, and state-change reasoning over HD-EPIC footage. Answers and reasoning traces are paired with timestamps and, in the paper, object-mask evidence.

- **Duration:** The paper reports video contexts from 10 seconds to 75 minutes, with a mean of 20 minutes, for 1,160 questions covering 156 unique videos. These are question-context video lengths, not the duration of each question's supporting evidence segment.
- **Collection size:** 1,160 five-choice questions across 156 unique videos. Independent benchmark media hours are unknown; upstream HD-EPIC reports 41.3 hours. Multiplying 156 by 20 minutes to obtain 52 hours would not establish a verified total because the difference from HD-EPIC's 15.9-minute mean is unexplained.
- **Potential applications:** Multistep video question answering; Temporal and spatial evidence reasoning; Object state-change reasoning; Goal and causal reasoning.
- **Modalities / available information:** Egocentric video, textual questions/answers and reasoning chains, timestamps, and paper-described object segmentation masks; mask-release completeness is unverified.
- **Dataset family:** Derived reasoning evaluation on HD-EPIC footage; only the new questions and evidence annotations are additional.
- **Access evidence:** As of 2026-10-24: A public annotation JSON file page was verified in the official repository, but the raw response exceeded 4 MB and was not parsed. HD-EPIC video must be obtained separately and was not downloaded. Video absence from this repository does not imply annotations are unpublished.
- **License observations:** The repository carries Apache-2.0, but the README's data-license scope still requires distinction. This record did not verify upstream-media or mask-package terms; the separately cataloged HD-EPIC record documents its Bristol data license.
- **Caveats:** The canonical audit retains the paper's range and mean while recording their unexplained mismatch with upstream HD-EPIC statistics; it does not decide which is wrong. A public JSON artifact does not verify completeness of the entire release or mask files. This is offline reasoning evaluation without native online action execution, error intervention, or confirmed real failure labels.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Minerva-Ego paper: scale and duration distribution](https://arxiv.org/html/2605.15342v1)
- [Official Minerva dataset collection](https://github.com/google-deepmind/neptune)
- [Released Minerva-Ego annotations](https://github.com/google-deepmind/neptune/blob/main/minerva-ego_20260205.json)
- [HD-EPIC paper, Sections 3 and B.2: upstream duration statistics](https://arxiv.org/html/2502.04144v2)

---

<a id="egogapbench"></a>

## FRO-06 · EgoGapBench

**Watchlist** · **Year / version:** 2026; paper submitted 2026-07-01

Single-image multiple-choice questions test which action the observer should take in multi-agent scenes lacking clear own-body cues. Distractors diagnose copying another person's action instead of selecting an action from the correct egocentric perspective.

- **Duration:** Not applicable: each sample is an action-selection question on a single static image. There is no video or continuous-session duration.
- **Collection size:** The independently parsed main default JSONL contains 440 image bundles and 1,000 multiple-choice questions, including 650 direct and 350 indirect questions reported in the paper. The alternate egoplan file has 440 bundles and the Wikimedia variant has 44; variants must not be summed as independent main-set images. Video hours are not applicable.
- **Potential applications:** Egocentric action selection; Perspective-sensitive action reasoning.
- **Modalities / available information:** Static images and textual action options; no temporal video stream.
- **Dataset family:** Independent static-image action-selection benchmark with alternate benchmark variants and externally acquired images.
- **Access evidence:** As of 2026-10-31: Public benchmark JSONL annotations were fetched and structurally verified. The main default file has 440 bundles and 1,000 mcq_items; two alternate benchmark files were also parsed. The inspected repository tree contains scripts, a Wikimedia manifest, and image credits but no bundled image binaries. Image acquisition from external sources was not tested.
- **License observations:** No top-level LICENSE file was present in the inspected tree. Data/code permissions and external-image rights remain unverified; public accessibility does not establish MIT or a blanket dataset license.
- **Caveats:** Retain watchlist because static-image action selection does not match long-video procedural tasks and image acquisition, completeness, and permissions remain untested. The publication audit supersedes the registry and duration-audit statements that benchmark files were unverified. Commit 6d2d95b67a9834eecf022194f429f78647ae87e4 records an upload at 2026-08-05 00:51:28 UTC, not a proven first-public-release date. The main scale is 1,000 questions on 440 images, not 9,000 questions on 3,000 images. Wrong options and perspective errors are not recordings of real procedural failures.

**Primary links** · Source review: 2026-10-31 · Duration audit: 2026-10-31

- [EgoGapBench paper v1: sample unit and main-set statistics](https://arxiv.org/html/2607.00547v1)
- [EgoGapBench official repository](https://github.com/jhCOR/EgoGapBench)
- [EgoGapBench arXiv submission history](https://arxiv.org/abs/2607.00547)
- [EgoGapBench official repository commit history](https://api.github.com/repos/jhCOR/EgoGapBench/commits?per_page=100)
- [EgoGapBench complete tree at the benchmark-upload commit](https://api.github.com/repos/jhCOR/EgoGapBench/git/trees/6d2d95b67a9834eecf022194f429f78647ae87e4?recursive=1)
- [EgoGapBench main default benchmark JSONL, independently parsed](https://raw.githubusercontent.com/jhCOR/EgoGapBench/6d2d95b67a9834eecf022194f429f78647ae87e4/Data/benchmark/egogapbench/bench_default.bundles.jsonl)
- [EgoGapBench alternate egoplan benchmark JSONL, independently parsed](https://raw.githubusercontent.com/jhCOR/EgoGapBench/6d2d95b67a9834eecf022194f429f78647ae87e4/Data/benchmark/egogapbench/bench_egoplan.bundles.jsonl)
- [EgoGapBench Wikimedia benchmark JSONL, independently parsed](https://raw.githubusercontent.com/jhCOR/EgoGapBench/6d2d95b67a9834eecf022194f429f78647ae87e4/Data/benchmark/egogapbench_wikimedia/bench_default.bundles.jsonl)

---

<a id="egovoice"></a>

## FRO-07 · EgoVoice

**Watchlist** · **Year / version:** 2026; paper submitted 2026-10-08

HoloAssist-derived collaborative task recordings pair real egocentric video with separated background audio and resynthesized user and instructor speech. The benchmark studies when an assistant should remain silent or speak, what guidance to give, and how guidance relates to subsequent actions.

- **Duration:** Processed full-session minimum and maximum are unknown. Derived means are approximately 4.405 minutes for training (91.7 hours x 60 / 1,249 sessions) and 4.553 minutes for held-out evaluation (12.9 hours x 60 / 170 sessions). One second is the streaming-chunk unit, not session duration.
- **Collection size:** Training: 1,249 sessions and 91.7 hours. Held-out: 170 sessions and 12.9 hours. Combined processed set: 1,419 sessions and 104.6 hours. The selected upstream HoloAssist subset contains 1,673 sessions and 124.8 hours; it is not the full HoloAssist collection and must not be added to processed hours.
- **Potential applications:** Proactive speech timing; Silence-versus-intervention prediction; Instruction-content generation; Guidance and subsequent-action alignment.
- **Modalities / available information:** Real egocentric video, resynthesized user speech, resynthesized instructor speech, and separated background audio.
- **Dataset family:** Processed derivative of a selected HoloAssist subset, with resynthesized speech rather than new independent video collection.
- **Access evidence:** As of 2026-10-31: Announced; release was not established by the cutoff. The official project still schedules code, models, and dataset for November 2026, which is after 2026-10-31. No specific November release day or completed release is confirmed; no dataset package was downloaded.
- **License observations:** The paper identifies upstream HoloAssist as CDLAv2 and describes speech resynthesis. A separate license for the planned derivative package was not verified.
- **Caveats:** Retain watchlist: the paper is available, but November 2026 remains a future release plan at the October 31 cutoff. The canonical duration means are split-specific derivations, and 12.9 hours is the held-out total, not one video. The publication audit did not remeasure sessions or verify a released package. Audio processing differs from natural speech; analyses of incorrect or late assistant guidance do not establish a complete set of human execution-error and recovery labels.

**Primary links** · Source review: 2026-10-31 · Duration audit: 2026-10-31

- [EgoVoice paper and submission history](https://arxiv.org/abs/2610.12248)
- [EgoVoice paper v1, Sections 3.1-3.2: construction and statistics](https://arxiv.org/html/2610.12248v1)
- [EgoVoice official November 2026 release plan](https://egocentricvoice.github.io/)

---

<a id="objchangevr"></a>

## FRO-08 · ObjChangeVR

**Watchlist** · **Year / version:** 2026

Synthetic VR exploration sequences test whether an object disappeared, remained present, or never appeared as the viewpoint moves. Scenes include homes, restaurants, markets, museums, and villages, emphasizing background changes that need not result from the observer's actions.

- **Duration:** Typical trajectories are approximately 60 seconds for short sequences and approximately 180 seconds for long sequences; these are not measured minima or maxima. The sample unit is a VR viewpoint trajectory with poses at 5 Hz and images at 1 Hz. Independent trajectory counts and exact endpoints are unknown.
- **Collection size:** Cumulative independent-trajectory duration is unknown. The paper reports 3,000 short-trajectory questions and 2,000 long-trajectory questions across 5 VR scenes, 35 scene regions, and 729 target objects. QA counts cannot be multiplied by 60 or 180 seconds to establish deduplicated video hours.
- **Potential applications:** Object-presence state question answering; Cross-view temporal object memory; Disappearance-versus-occlusion reasoning.
- **Modalities / available information:** Simulated RGB image sequences, camera positions/poses, timestamps, and textual QA.
- **Dataset family:** Synthetic Unity VR environments and generated viewpoint trajectories, not recorded human procedural sessions.
- **Access evidence:** As of 2026-10-24: Links only; the official repository provides a SharePoint data link, but the target contents and downloadable status were not verified. No media download was tested, so the record remains watchlist.
- **License observations:** Paid Unity Asset Store scenes cannot be redistributed; the repository provides generation scripts. A separate license for generated images and QA was not verified.
- **Caveats:** The canonical audit adds typical 60/180-second durations from paper Section 3 and Table 8, not guesses from repository defaults. These values are not exact range endpoints, and question counts are not independent trajectory counts. Actual full-trajectory release and usable media totals remain unverified. Controlled object appearance/disappearance is synthetic state-change evidence, not real operation failures or recovery behavior.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [ObjChangeVR paper v1, Section 3 and Table 8](https://arxiv.org/html/2603.06648v1)
- [ObjChangeVR official repository, data link, and asset restrictions](https://github.com/sding11/ObjChangeVR)
