# Errors, Anomalies, and Safety

[Back to the collection](../README.md) · [Duration methodology](../docs/methodology.md) · [JSON data](../data/datasets.json)

Procedural mistakes, unintentional actions, quality assessment, traffic incidents, and surveillance comparisons.

**18 records.** Suggested applications are editorial research directions; consult annotations and caveats before assuming native task support.

## Contents

- [ERR-01 · Ego-MC-Bench](#qualcomm-mistake-corrections)
- [ERR-02 · EgoPER](#egoper)
- [ERR-03 · Anomalous Toy Assembly (ATA)](#ata)
- [ERR-04 · AQA-7](#aqa7)
- [ERR-05 · Assembly101-O](#assembly101-o)
- [ERR-06 · DADA-2000](#dada-2000)
- [ERR-07 · DoTA](#dota)
- [ERR-08 · Ego-CoMist](#qualcomm-counterfactual-mistakes)
- [ERR-09 · EgoErrorVQA](#egoerrorvqa)
- [ERR-10 · EgoOops](#egooops)
- [ERR-11 · EgoProceL](#egoprocel)
- [ERR-12 · EPIC-Tent / Epic-tent-O](#epic-tent-o)
- [ERR-13 · FineDiving](#finediving)
- [ERR-14 · MATT-Bench](#matt-bench)
- [ERR-15 · OOPS!](#oops)
- [ERR-16 · ProceL](#procel)
- [ERR-17 · UCF-Crime](#ucf-crime)
- [ERR-18 · XD-Violence](#xd-violence)

---

<a id="qualcomm-mistake-corrections"></a>

## ERR-01 · Ego-MC-Bench

**Core candidate** · **Year / version:** 2026; first paper submitted 2026-06-08

Egocentric recordings show participants completing interactive cooking tasks with instructions, feedback, and clarification. Participants rehearsed deliberate mistakes before filming, and the recordings include responses intended to make corrections realistic.

- **Duration:** Recording-session minimum and maximum are unknown; the reviewed paper does not report them. The inferred mean is approximately 15 minutes per recording session, calculated as approximately 10 hours x 60 / 40 sessions. This is not a measured per-video mean and establishes no minimum or maximum.
- **Collection size:** The paper reports approximately 10 hours across 40 recordings. The dataset card lists 40 videos and 1,597 text annotations, but its YAML split lists 39; the discrepancy is unresolved.
- **Potential applications:** Streaming mistake detection; Timely intervention; Corrective feedback generation.
- **Modalities / available information:** Egocentric video, timestamped text, and speech in the original recordings; the dataset card lists text annotations and MP4 files.
- **Dataset family:** Ego-MC-Bench: independently recorded interactive sessions released under the QIC brand; not reused CaptainCook4D videos from base QIC.
- **Access evidence:** As of 2026-10-24: Public entry point: Hugging Face API metadata reported gated=false and private=false; the card listed videos and annotations. Repository creation was 2026-04-30 and its last modification was 2026-10-22. Media downloads and complete package availability were not tested.
- **License observations:** Research-only under QIC LICENSE.pdf; the full terms were not reviewed, so redistribution permission is not established.
- **Caveats:** The inferred mean applies only to the paper's 40 recording sessions, not to base QIC, CaptainCook4D, or Ego-CoMist. Text annotations are not video or error-event counts. Release-package counts may differ from the paper; individual MP4 durations were not inspected. Preserve the unresolved 39-versus-40 count. A 401 response from an older short URL did not establish gated access. These are staged mistakes in real recordings, not verified optimal plans or evidence of causal intervention benefits. EgoOops and EgoMCEC are separate datasets.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Qualcomm Ego Mistake Corrections: official dataset card](https://huggingface.co/datasets/qualcomm/qualcomm-interactive-cooking-dataset-ego-mistake-corrections)
- [Qualcomm Ego Mistake Corrections: Hugging Face API metadata](https://huggingface.co/api/datasets/qualcomm/qualcomm-interactive-cooking-dataset-ego-mistake-corrections)
- [Streaming Interventions: Ego-MC-Bench statistics and Ego-CoMist](https://arxiv.org/html/2606.09547)
- [Streaming Interventions: submission history](https://arxiv.org/abs/2606.09547)

---

<a id="egoper"></a>

## ERR-02 · EgoPER

**Core candidate** · **Year / version:** 2024; repository updated 2025-09-16

Egocentric cooking videos show people preparing pinwheels, quesadillas, oatmeal, coffee, and tea. Normal and erroneous executions follow prepared task transcripts and include omissions, additions, modifications, physical slips, and corrections.

- **Duration:** Per-video minimum and maximum are unknown. Table 1 reports task-group means for normal/error videos in minutes: Coffee 8.4/9.3, Pinwheels 5.6/4.2, Tea 2.6/2.5, Quesadilla 1.6/1.8, and Oatmeal 4.2/4.3. The inferred overall mean is approximately 4.35 minutes, calculated as 28 hours x 60 / 386 videos. The 1.6-9.3 minute span describes group means, not a per-video range.
- **Collection size:** The paper reports 28 hours and 386 videos: 213 normal and 173 erroneous, involving 11 people, two environments, and five tasks. The released trimmed RGB package has no independently verified total duration.
- **Potential applications:** Procedural step segmentation; Procedural error detection; Correction event recognition.
- **Modalities / available information:** RGB, depth, audio, gaze, and hand tracking described for the dataset; the release instructions describe trimmed RGB videos.
- **Dataset family:** EgoPER
- **Access evidence:** As of 2026-10-24: Request required: email institutional affiliation, supervisor, status, OneDrive email address, and intended use. Shared links are valid for two weeks. Media downloads and complete package availability were not tested.
- **License observations:** Dataset license not verified; a code license must not be extended to the videos.
- **Caveats:** The paper describes untrimmed videos, while the official repository explicitly describes trimmed RGB and supplies trim_start_end.txt. Paper statistics must not be assumed to describe the release package or pre-trim source files. Table 1's Min. denotes average minutes, not a minimum. Task durations vary and not every video is long. Prepared transcripts mean the errors are not purely spontaneous. Omission evaluation requires task graphs and temporal boundaries. The paper describes object boxes on at least three frames per step, whereas the repository says frame-wise; density needs package inspection. The 2025 task-graph and language-description additions do not automatically incorporate the separate EgoPED omission task.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Error Detection in Egocentric Procedural Task Videos: CVPR 2024, Table 1 and Section 3.2](https://openaccess.thecvf.com/content/CVPR2024/papers/Lee_Error_Detection_in_Egocentric_Procedural_Task_Videos_CVPR_2024_paper.pdf)
- [EgoPER: official release instructions](https://github.com/robert80203/EgoPER)
- [EgoPER official README: preparation and dataset files](https://github.com/robert80203/EgoPER_official/blob/main/README.md)

---

<a id="ata"></a>

## ERR-03 · Anomalous Toy Assembly (ATA)

**Core candidate** · **Year / version:** 2023

Four synchronized external cameras record people assembling toy airplanes, tables, and record players in a laboratory. Participants follow prepared action transcripts with spoken prompts, producing familiar and unseen sequences as well as predefined assembly errors.

- **Duration:** Per-view video and synchronized-episode minima and maxima are unknown; the readable official page did not report them. The inferred mean is approximately 1.292 minutes, or 77.5 seconds per view video, calculated as 24.8 hours x 3,600 / 1,152 videos. Synchronized episode elapsed time must not be multiplied by four.
- **Collection size:** The official page reports 24.8 hours summed over 1,152 view videos. The inferred independent episode count is 288 (32 people x three tasks x three repetitions). Assuming four complete views of equal length, deduplicated elapsed duration is approximately 6.2 hours.
- **Potential applications:** Action segmentation; Unseen sequence anomaly detection; Assembly error detection.
- **Modalities / available information:** Four external RGB views, human keypoints, and interacting-object boxes; audio is muted and faces are blurred.
- **Dataset family:** ATA; separate from Assembly101
- **Access evidence:** As of 2026-10-24: Request required through a university affiliation and university email address; use is non-commercial. Media downloads and complete package availability were not tested.
- **License observations:** The official page specifies non-commercial use. The full application agreement was not obtained; open redistribution is not established.
- **Caveats:** These are complete toy assemblies on a minute scale, not atomic action snippets. The audit's short-clip classification is conservative about temporal scale; untrimmed does not establish long-horizon duration. The 1,152 view videos are not 1,152 independent executions. The registry's 0.6-2.1 minute range was not confirmed by readable primary evidence in the canonical audit and remains unverified. An unseen but valid ordering is not necessarily an assembly failure; use the 11 error classes separately from sequence novelty. State and recovery-policy labels are not established.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Honda Research Institute: Anomalous Toy Assembly official page](https://usa.honda-ri.com/ata)
- [Weakly-Supervised Action Segmentation and Unseen Error Detection in Anomalous Instructional Videos: ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/papers/Ghoddoosian_Weakly-Supervised_Action_Segmentation_and_Unseen_Error_Detection_in_Anomalous_Instructional_ICCV_2023_paper.pdf)

---

<a id="aqa7"></a>

## ERR-04 · AQA-7

**Auxiliary** · **Year / version:** 2018 preprint; 2019 paper

Clips extracted from sports broadcasts show individual performances across seven action categories. Expert judging scores describe performance quality, including trampoline routines with multiple phases.

- **Duration:** Per-video minimum, maximum, and overall mean in seconds are unknown. The paper describes typical individual sports actions as shorter than five seconds except trampoline, which lasts approximately 20 seconds and has multiple phases; these are typical action scales, not measured video extrema. Table 1 gives category mean sequence lengths of 87-156 frames for six actions and 634 frames for trampoline. No conversion to seconds is made without verified frame rates.
- **Collection size:** Total video duration is unknown. The abstract reports 1,106 samples across seven actions, while Table 1 separately lists 83 trampoline samples; the counting scopes are inconsistent.
- **Potential applications:** Action quality assessment; Cross-action quality learning.
- **Modalities / available information:** Video and expert quality scores; additional modalities not verified.
- **Dataset family:** AQA-7; distinct from MTL-AQA and FineDiving
- **Access evidence:** As of 2026-10-24: Links only: the paper points to a UNLV dataset page; media download status was not verified. Media downloads and complete package availability were not tested.
- **License observations:** Dataset license not verified.
- **Caveats:** Samples are individual sports performances, not full competitions or continuous procedural tasks. Experiments exclude trampoline, and the abstract/table counting discrepancy prevents estimating total duration by multiplying 1,106 by a mean. Fixed model input frame counts do not specify source-clip duration. Low scores do not establish procedural errors or their causes; omission, ordering, and recovery labels were not found.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Action Quality Assessment Across Multiple Actions: paper](https://arxiv.org/abs/1812.06367)
- [Action Quality Assessment Across Multiple Actions: Section 3.1, Table 1, and experimental setup](https://arxiv.org/pdf/1812.06367)

---

<a id="assembly101-o"></a>

## ERR-05 · Assembly101-O

**Core candidate** · **Year / version:** 2024

A derived Assembly101 protocol uses one egocentric view of people assembling and disassembling toy vehicles. It reuses action and error annotations and evaluates erroneous procedures only up to the first dependency error.

- **Duration:** Assembly101-O evaluation-sequence minimum, maximum, mean, and typical duration are unknown. The paper supplies no duration statistics independently attributable to this derived version.
- **Collection size:** Assembly101-O total duration is unknown. PREGO reorganizes 362 procedures and uses 190 error-free procedures for training; parent Assembly101 hours are excluded.
- **Potential applications:** Online open-set mistake detection; One-class mistake detection; Step recognition and prediction.
- **Modalities / available information:** One egocentric RGB view per procedure and TSN features; parent multi-view and pose data are not established as inputs to this protocol.
- **Dataset family:** Assembly101: derived evaluation protocol using existing recordings
- **Access evidence:** As of 2026-10-24: Public feature entry point: PREGO lists TSN features and target_perframe. RGB videos require the parent dataset channel. Media downloads and complete package availability were not tested.
- **License observations:** Extension data license not verified; videos remain subject to the parent dataset terms.
- **Caveats:** Normal and erroneous procedures retain different evaluation lengths. Do not fill missing statistics with parent means, ranges, or totals summed over all views. Logical evaluation truncation does not necessarily mean physical video files are trimmed. The protocol reorganizes existing labels and splits rather than collecting new videos or comprehensively reannotating errors. Truncation removes later recovery from evaluation, so complete error-recovery trajectories require a separate parent-data protocol. The natural-versus-induced error proportion was not independently verified. Deduplicate against Assembly101; family membership does not establish aligned source video IDs.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [PREGO: Online Mistake Detection in PRocedural EGOcentric Videos, CVPR 2024, Section 3.1](https://openaccess.thecvf.com/content/CVPR2024/papers/Flaborea_PREGO_Online_Mistake_Detection_in_PRocedural_EGOcentric_Videos_CVPR_2024_paper.pdf)
- [PREGO: official repository](https://github.com/aleflabo/PREGO)
- [PREGO: Section 3.1.1, Assembly101-O](https://arxiv.org/html/2404.01933)

---

<a id="dada-2000"></a>

## ERR-06 · DADA-2000

**Comparison** · **Year / version:** 2019; related DADA journal paper in 2022

Driving accident clips show traffic incidents across different roads, weather conditions, and times of day. They include context before and after accidents, with attention annotations collected from people watching the footage in a laboratory.

- **Duration:** Per-video minimum and maximum are unknown. The inferred mean is approximately 10.98 seconds, calculated from Table II as 658,476 frames / 30 fps / 2,000 videos. Table I separately gives a rounded mean of 325 frames, corresponding to approximately 10.83 seconds; this is not the same precise statistic.
- **Collection size:** Table III reports 6.1 hours across 2,000 clips. Table II's 658,476 frames at 30 fps imply approximately 6.097 hours; the original benchmark covers 54 accident types.
- **Potential applications:** Accident attention prediction; Hazard warning research; Accident temporal and spatial localization.
- **Modalities / available information:** RGB, fixation maps, saccade scan paths, and focusing time.
- **Dataset family:** DADA-2000; separate accounting from later DADA extensions
- **Access evidence:** As of 2026-10-24: Public entry points: the author repository lists Baidu and Google Drive links, separating early train/test packages from the later full benchmark. File versions were not verified. Media downloads and complete package availability were not tested.
- **License observations:** Explicit dataset license not verified; an invitation to use or share does not replace complete license terms.
- **Caveats:** These are second-scale traffic events, not complete driving journeys or procedural executions. Preserve the discrepancy between Table I's 650,000 total frames and Table II's 658,476. Do not mix the original benchmark with later DADA releases. Viewer attention is not automatically ground truth for the driver's real-time gaze, causal accident explanations, liability, avoidability, or optimal driving decisions. Procedural-step and recovery supervision are not established.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [DADA-2000: original benchmark paper](https://arxiv.org/abs/1904.12634)
- [DADA: author repository and downloads](https://github.com/JWFangit/LOTVS-DADA)
- [DADA-2000: Section III-A and Tables I-III](https://arxiv.org/html/1904.12634)

---

<a id="dota"></a>

## ERR-07 · DoTA

**Comparison** · **Year / version:** 2020; media-sharing updates in 2021 and 2023

Moving dashcam footage captures real traffic anomalies and their surrounding context. Extracted clips include events before, during, and after incidents, with temporal boundaries, spatial annotations, and anomaly categories.

- **Duration:** Per-clip minimum and maximum are unknown; extrema were not inferred from distribution plots. The inferred mean is approximately 15.65 seconds, calculated as 731,932 frames / 10 fps / 4,677 videos.
- **Collection size:** Inferred total duration is approximately 20.33 hours, calculated as 731,932 frames / 10 fps / 3,600, across 4,677 videos.
- **Potential applications:** Traffic anomaly temporal localization; Traffic anomaly spatial localization; Traffic anomaly classification.
- **Modalities / available information:** Dashcam RGB, object boxes and trajectories, and optical-flow-related derived features.
- **Dataset family:** DoTA
- **Access evidence:** As of 2026-10-24: Public media entry points: authors reported permission from source channels to share clips and frames in 2021 and offered split archives of the same data in 2023. The 55 GB package was not downloaded. Media downloads and complete package availability were not tested.
- **License observations:** Author permission to share source footage does not establish unrestricted downstream use or redistribution; an explicit standard dataset license was not verified.
- **Caveats:** Source videos were 30 fps, but the paper's release and annotation statistics are at 10 fps: divide 731,932 frames by 10, not 30. These traffic-event clips are not long procedural episodes; original web-video and complete-journey durations are unknown. An accident need not result from the ego vehicle's procedural mistake. Anomaly annotations do not supply control policies or recovery actions; future anomaly prediction would be a derived application.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [When, Where, and What? DoTA: original paper](https://arxiv.org/abs/2004.03044)
- [DoTA: official release and updates](https://github.com/MoonBlvd/Detection-of-Traffic-Anomaly)
- [When, Where, and What? DoTA: Section 3 and Table 1](https://arxiv.org/html/2004.03044)

---

<a id="qualcomm-counterfactual-mistakes"></a>

## ERR-08 · Ego-CoMist

**Auxiliary** · **Year / version:** 2026 associated paper; dataset card still cites the NeurIPS 2025 QIC parent

Real cooking footage from CaptainCook4D, Ego4D, and Ego-Exo4D is paired with counterfactual instructions and corrective feedback. The text describes mismatches between an instruction and the action actually shown, rather than newly filmed accidents.

- **Duration:** Annotation-row interval durations were computed in the canonical audit as end_time minus start_time on the seconds timeline: minimum 10 seconds, maximum 1,054.969 seconds (approximately 0.167-17.583 minutes), mean 34.2708 seconds, and median 22.7102 seconds. The 25,087 rows are not independent videos; deduplication by (dataset, video_id, start_time, end_time) yields 13,737 intervals. Original full-video minimum, maximum, and mean durations are unknown.
- **Collection size:** Unique original-video total duration is unknown. The computed sum of annotation-row intervals is 238.8201 hours, including duplicates and overlaps; it is not unique footage duration. There are 25,087 rows and 1,110 unique (dataset, video_id) source identifiers: 4,969 rows from CaptainCook4D, 13,847 from Ego4D, and 6,271 from Ego-Exo4D.
- **Potential applications:** Counterfactual instruction-action mismatch training; Corrective feedback generation; Synthetic supervision for mistake intervention.
- **Modalities / available information:** References to real parent-dataset videos, synthetic text, mistake types, and timestamps.
- **Dataset family:** CaptainCook4D; Ego4D; Ego-Exo4D: annotation extension released under the QIC brand
- **Access evidence:** As of 2026-10-24: Public annotation entry point: the card lists annotations.json only. Videos must be obtained through the three parent datasets under their respective access conditions. Media downloads and complete package availability were not tested.
- **License observations:** The card specifies research-only use under QIC LICENSE.pdf; parent videos retain their own licenses. YAML metadata marked other is not an open license.
- **Caveats:** Most annotations cover short steps, but some intervals last minutes; the collection is not uniformly long-horizon. Neither 25,087 rows nor 13,737 deduplicated intervals are independent-video counts. The 1,110 source identifiers do not establish unique-video hours. Do not use the overlapping interval sum to estimate full-video means, or inherit parent duration statistics. These figures audit annotation timestamps, not individual MP4 durations; sources establish provenance and schema, while numerical results come from the canonical audit's local file calculation. Qwen3-VL-32B-Instruct and Gemini-2.5-Pro generated text, not the footage. Error coverage differs across parents; the paper restricts parts of Ego4D/Ego-Exo4D generation to preparation and technique errors. Natural failure rates and recovery efficacy require separate evaluation. EgoMMM and PaLM are not verified aliases.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Qualcomm Ego Counterfactual Mistakes: official dataset card](https://huggingface.co/datasets/qualcomm/qualcomm-interactive-cooking-dataset-counterfactual-mistakes)
- [Streaming Interventions: Section 4, Ego-CoMist construction](https://arxiv.org/html/2606.09547)
- [Official annotations.json: downloaded and computed in the canonical duration audit](https://huggingface.co/datasets/qualcomm/qualcomm-interactive-cooking-dataset-counterfactual-mistakes/resolve/main/annotations.json)

---

<a id="egoerrorvqa"></a>

## ERR-09 · EgoErrorVQA

**Auxiliary** · **Year / version:** 2026-08-25 preprint; repository lists EMNLP 2026, proceedings not independently verified

Selected procedural video clips cover cooking, tent assembly, crafts, and assembly tasks from four existing datasets. Open-ended and multiple-choice questions ask about errors visible in these clips, using machine-assisted question construction with human additions and checks.

- **Duration:** VQA input-clip minimum, maximum, mean, and typical duration are unknown. The reviewed paper reports clip and question counts but no directly usable clip-duration statistics in seconds.
- **Collection size:** Unique benchmark-clip total duration is unknown. Table 2 reports 3,560 open-ended QA pairs and 1,857 multiple-choice QA pairs; these are not independently verified counts of distinct original videos.
- **Potential applications:** Procedural error visual question answering; Error-type identification.
- **Modalities / available information:** Parent-dataset video clips and open-ended or multiple-choice question-answer JSON; evaluation uses a language-model judge.
- **Dataset family:** CaptainCook4D; EgoOops; EPIC-Tent; Assembly101: derived question-answer annotations
- **Access evidence:** As of 2026-10-24: Public annotation and evaluation-code entry points. Videos require separate acquisition from CaptainCook4D, EgoOops, EPIC-Tent, and Assembly101; JSON completeness was not tested. Media downloads and complete package availability were not tested.
- **License observations:** Derived QA license not verified; each parent dataset's video license remains applicable.
- **Caveats:** The input unit is a selected step clip, not a complete parent procedure; no parent duration may be inherited. The 1,857 multiple-choice figure is a QA count in Table 2, although its source-clip counts also sum to 1,857; media deduplication is required before treating it as an independent-video denominator. Do not add the two QA totals as non-overlapping video counts. Whether these inputs meet a long-horizon duration criterion remains unknown. Video errors inherit a mixture of real and staged parent data, while text is machine-assisted. Parent test videos may overlap other error benchmarks. The benchmark does not directly evaluate online detection latency or executed recovery.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoErrorVQA: original preprint and submission date](https://arxiv.org/abs/2608.24134)
- [EgoErrorVQA: Table 2 and Appendices A and C](https://arxiv.org/html/2608.24134)
- [EgoErrorVQA: official repository](https://github.com/z1oong/EgoErrorVQA)

---

<a id="egooops"></a>

## ERR-10 · EgoOops

**Core candidate** · **Year / version:** 2024 preprint; ICCV Workshops 2025

People follow written procedures involving electrical circuits, color mixing, ion reactions, building blocks, and cardboard crafts. Half the recordings in each task ask participants to make deliberate mistakes, while the other half ask them to avoid mistakes but still include occasional slips.

- **Duration:** Per-video minimum and maximum are unknown. The paper reports an overall video mean of 8.2 minutes and task means of EC 3.2, CM 4.4, IR 5.4, BB 1.9, and CB 26.1 minutes. The 1.9-26.1 minute span is a range of task means, never individual-video extrema. The overall mean for annotated step segments is 40.7 seconds.
- **Collection size:** Table 1 reports 6.8 hours across 50 videos, with ten videos per domain across five domains and 538 annotated step segments. The 8.2 minute video mean and 6.8 hour total are rounded paper statistics.
- **Potential applications:** Text-conditioned mistake recognition; Mistake explanation; Video-step alignment.
- **Modalities / available information:** 720p RGB video, procedure text, temporal step alignments, mistake classes, and segment-level explanations.
- **Dataset family:** EgoOops: Kyoto University dataset; separate from Qualcomm datasets
- **Access evidence:** As of 2026-10-24: Public entry points: the laboratory provides a 720p video ZIP and GitHub annotations. The repository video list still contains TODO entries. Media downloads and complete package availability were not tested.
- **License observations:** The official project and annotation repository explicitly specify CC BY-SA 4.0.
- **Caveats:** Complete procedures span shorter and longer tasks. Distinguish the 8.2 minute whole-video mean from the 40.7 second mean over 538 step segments; step-sliced training examples are not full procedures. The dataset is small, and deliberately induced versus incidental mistakes should be separated. The repository task-name mapping repeats blacklight/ion text and needs checking against paper tasks and metadata. Next-step selection and recovery plans are not independent native evaluation targets.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoOops: official project page](https://y-haneji.github.io/EgoOops-project-page/)
- [EgoOops: official annotation repository](https://github.com/Y-Haneji/EgoOops-annotations)
- [EgoOops: Tables 1 and 2, Section 3.5, and recording protocol](https://arxiv.org/html/2410.05343)

---

<a id="egoprocel"></a>

## ERR-11 · EgoProceL

**Auxiliary** · **Year / version:** 2022

Egocentric procedural videos cover cooking, tent setup, toy-bicycle assembly, and computer assembly and disassembly. The benchmark combines existing datasets with newly recorded computer tasks and retains background activity and repeated steps.

- **Duration:** Per-video minimum and maximum are unknown. Table 1 directly reports a mean video length of 769.2 seconds, approximately 12.82 minutes; the overview rounds this to approximately 13 minutes.
- **Collection size:** The original paper reports 62 hours across 16 tasks and 130 participants. Key-step annotation counts are not video counts.
- **Potential applications:** Procedure learning; Step ordering; Temporal step alignment.
- **Modalities / available information:** Egocentric RGB and CSV key-step start times, end times, and names; extra parent modalities are not guaranteed across the release.
- **Dataset family:** CMU-MMAC; EGTEA Gaze+; MECCANO; EPIC-Tent; newly recorded PC assembly and disassembly
- **Access evidence:** As of 2026-10-24: Public entry points with mixed parent-dataset conditions: official mirrors and download instructions are listed. The old OneDrive link is explicitly expired; Google Drive was the recommended entry point at the original check. Media downloads and complete package availability were not tested.
- **License observations:** The code's MIT license is not a dataset license. Parent datasets retain their respective terms; terms for new computer-task footage were not verified.
- **Caveats:** Use the directly reported 769.2 second mean, not estimates from participant counts, step counts, or video counts from other versions. Full-procedure duration differs from model sampling windows and does not guarantee every video exceeds a long-video threshold. The reported mean missing-step ratio of 0.12 and repeated-step ratio of 0.49 are not procedural error rates. Dedicated error-type, failure-cause, and recovery labels were not verified. Deduplicate overlapping parent footage, including EPIC-Tent and MECCANO; family membership alone does not align source IDs.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoProceL: author project page](https://sid2697.github.io/egoprocel/)
- [EgoProceL: download instructions and annotation schema](https://github.com/Sid2697/EgoProceL-egocentric-procedure-learning/blob/main/EgoProceL-download-README.md)
- [My View is the Best View: Procedure Learning from Egocentric Videos, Table 1 and Section 3](https://arxiv.org/html/2207.10883)

---

<a id="epic-tent-o"></a>

## ERR-12 · EPIC-Tent / Epic-tent-O

**Core candidate** · **Year / version:** 2019; PREGO extension in 2024

Head-mounted recordings show participants assembling tents outdoors while handling flexible parts, consulting instructions, and using tools. The Epic-tent-O protocol selects procedural errors from these recordings and limits test evaluation to the last frame of the first error.

- **Duration:** For the Epic-tent-O derivative, per-video or evaluation-sequence minimum, maximum, mean, and typical duration are all unknown; no independent duration statistics were reported. Full-recording durations from parent EPIC-Tent must not be assigned to Epic-tent-O. Parent 2019 and 2020 version statistics are tracked separately in EGO-02.
- **Collection size:** Epic-tent-O total duration is unknown; it has 29 videos split into 14 training and 15 test videos. Separately, the updated parent website reports 29 participants and over seven hours, striking out the older 24-participant, 5.4-hour figures. PREGO still cites those older parent figures.
- **Potential applications:** Online procedural mistake detection; Step recognition; Order and omission detection; Correction and repetition recognition.
- **Modalities / available information:** Parent: GoPro RGB, a second head-mounted eye-tracking camera, gaze, and self-reported uncertainty. The O protocol primarily uses GoPro video or features.
- **Dataset family:** EPIC-Tent: parent dataset and Epic-tent-O derived evaluation protocol
- **Access evidence:** As of 2026-10-24: Public entry points: the parent project lists video, annotation, and script downloads; PREGO lists TSN features and per-frame targets. Files behind the links were not tested. Media downloads and complete package availability were not tested.
- **License observations:** Not verified; parent video rights and PREGO code or feature terms must be handled separately.
- **Caveats:** This registry ID covers both the parent and its derivative; the canonical mixed classification reflects these different version scopes. The parent records complete tent procedures, while O retains selected material and truncates test evaluation after the first error. Whether retained O sequences are still long-horizon is unknown. Neither the parent's over-seven-hour total nor any parent-derived mean applies to O. O includes order, omit, correction, and repeat errors but excludes slow, search, misuse, motor, and failure categories. Higher self-reported confidence guides the training split and does not guarantee error-free training. The single task and truncation limit recovery and strict one-class interpretations; recovery requires returning to parent recordings.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EPIC-Tent: official dataset page and updated statistics](https://sites.google.com/view/epic-tent)
- [PREGO: Online Mistake Detection in PRocedural EGOcentric Videos, CVPR 2024, Section 3.1](https://openaccess.thecvf.com/content/CVPR2024/papers/Flaborea_PREGO_Online_Mistake_Detection_in_PRocedural_EGOcentric_Videos_CVPR_2024_paper.pdf)
- [PREGO: official repository](https://github.com/aleflabo/PREGO)
- [PREGO: Section 3.1.2, Epic-tent-O](https://arxiv.org/html/2404.01933)

---

<a id="finediving"></a>

## ERR-13 · FineDiving

**Auxiliary** · **Year / version:** 2022

Competition footage shows complete individual dives with fine-grained action phases and judging scores. Samples are trimmed to dive boundaries, with incomplete actions and slow-motion footage filtered out.

- **Duration:** Per-dive video minimum, maximum, mean, and typical duration are unknown. The reviewed primary paper and repository provide no directly usable duration statistics in seconds.
- **Collection size:** Total video duration is unknown for the 3,000 samples, which cover 52 action types, 29 sub-actions, and 23 difficulty-level types.
- **Potential applications:** Action quality assessment; Fine-grained dive phase recognition; Procedure-aware quality scoring.
- **Modalities / available information:** RGB, action and sub-action labels, transition frames, judge scores, dive scores, and difficulty.
- **Dataset family:** FineDiving
- **Access evidence:** As of 2026-10-24: Request required: sign a Release Agreement and email the authors. The official description lists untrimmed competition videos, trimmed frames, and annotations. Media downloads and complete package availability were not tested.
- **License observations:** A Release Agreement is required; detailed use and redistribution restrictions were not fully reviewed.
- **Caveats:** A sample is a complete individual dive extracted from a competition, not a full event or sustained assembly or cooking procedure. The paper's 96-frame input is a sampling strategy, not original video length; no seconds conversion is justified without a consistent verified source frame rate. Quality variation and low scores do not establish procedural omissions, recovery behavior, safety violations, or causal failure explanations. Separate skill quality from task success or failure.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [FineDiving: official README, lexicon, annotation, and statistics](https://github.com/xujinglin/FineDiving)
- [FineDiving: original paper, Section 5.2](https://arxiv.org/pdf/2204.03646.pdf)

---

<a id="matt-bench"></a>

## ERR-14 · MATT-Bench

**Auxiliary** · **Year / version:** 2025-11-25 preprint; revised 2026-03-25; CVPR 2026

Real egocentric manipulation clips are paired with altered instructions to create predicate, object, or combined mismatches. Derived annotations cover Ego4D-M and EPIC-KITCHENS-M, with an additional HoloAssist-M release outside the paper's two main evaluation datasets.

- **Duration:** Per-clip minimum and maximum are unknown for the complete benchmark and each of its three subsets. The Ego4D-M temporal-attribution/point-of-no-return experiment reports a mean clip length of approximately eight seconds (240 frames at 30 fps), applicable only to that experimental scope. Independent mean or typical durations for EPIC-KITCHENS-M and HoloAssist-M are unknown.
- **Collection size:** Unique video duration is unknown for MATT-Bench and each subset. The card lists Ego4D-M: 220,800 samples / 19,467 instructions; EPIC-KITCHENS-M: 299,715 / 12,283; HoloAssist-M: 562,209 / 1,786. These are not independent-video counts and must not be multiplied by eight seconds.
- **Potential applications:** Semantic mistake attribution; Ego4D-M temporal mistake attribution; Ego4D-M spatial mistake attribution.
- **Modalities / available information:** Real RGB action-attempt clips, instructions, semantic roles, and inherited Ego4D point-of-no-return and spatial-box annotations; XLSX and Parquet annotation releases.
- **Dataset family:** Ego4D; EPIC-KITCHENS; HoloAssist: derived annotation extensions
- **Access evidence:** As of 2026-10-24: Public annotations: the Hugging Face card explicitly states that videos are not hosted. Parent video downloads and access conditions are separate. Media downloads and complete package availability were not tested.
- **License observations:** The Hugging Face annotation card specifies CC BY 4.0; original videos retain upstream licenses.
- **Caveats:** The confirmed Ego4D-M experiment uses short action-attempt clips, but longer-sample coverage elsewhere is unverified. Eight seconds must not be generalized to all MATT-Bench or to other subsets. Parent full-video duration is not benchmark input duration, and HoloAssist-M must not inherit HoloAssist statistics. MisEngine pairs real actions with different instructions to synthesize labels; human validity studies do not make these naturally occurring mistakes. Large combinatorial row counts are not counts of natural failures. Temporal and spatial supervision is inherited for Ego4D-M; the other parts provide semantic attribution only. An inherited point-of-no-return label is not automatically the irreversible point of an actual failure. Full-procedure omissions and recovery trajectories are not native supervision.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [MATT-Bench: official Hugging Face dataset card](https://huggingface.co/datasets/mistakeattribution/MATT-Bench)
- [Mistake Attribution: paper dates and venue](https://arxiv.org/abs/2511.20525)
- [Mistake Attribution: MisEngine construction and Section 4.2 temporal attribution](https://arxiv.org/html/2511.20525v2)

---

<a id="oops"></a>

## ERR-15 · OOPS!

**Comparison** · **Year / version:** 2019 preprint; CVPR 2020

Short scenes from online fail compilations show everyday sports, social situations, falls, and other physical mishaps. Temporal annotations mark transitions from intentional activity to unintended outcomes.

- **Duration:** The paper's scene-selection protocol retains clips of 3-30 seconds, rejecting scenes shorter than three or longer than 30 seconds. Exact measured minimum and maximum are unknown; selection bounds are not observed extrema. The reported mean is 9.4 seconds and the median is 7.6 seconds.
- **Collection size:** The paper reports over 50 hours across 20,338 clips.
- **Potential applications:** Unintentional action recognition; Intentional-to-unintentional transition localization; Short-term accident anticipation.
- **Modalities / available information:** RGB; optical flow and pose were proposed in the paper, but availability of those files was not verified.
- **Dataset family:** OOPS!
- **Access evidence:** As of 2026-10-24: Media availability unknown: the paper was read, but its linked oops.cs.columbia.edu project site returned 404 during the original check. The paper's release commitment does not establish an available download. Media downloads and complete package availability were not tested.
- **License observations:** Not verified; online source footage does not establish redistribution rights.
- **Caveats:** Scenes are extracted from longer web compilations; compilation lengths must not be used as sample durations. These broad unintended-action clips need not contain complete multistep goals. Online fail compilations introduce selection bias, and the paper does not individually establish that every scene is unstaged. Step dependencies, omission judgments, and corrective-action labels are absent. Temporal accident transitions do not establish long-horizon procedural state understanding; the unavailable project entry point needs separate follow-up.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Oops! Predicting Unintentional Action in Video: original paper](https://arxiv.org/abs/1911.11206)
- [Oops! Predicting Unintentional Action in Video: Section 3.1, Figure 3, and tasks](https://arxiv.org/html/1911.11206)

---

<a id="procel"></a>

## ERR-16 · ProceL

**Auxiliary** · **Year / version:** 2019 original website citation; used by later methods in 2020

Online instructional videos demonstrate physical and virtual tasks such as tying a tie, assembling a clarinet, and setting up Chromecast. Key-step boundaries, task grammars, and manually cleaned speech transcripts describe the demonstrated procedures.

- **Duration:** Per-video minimum and maximum are unknown. Table 1 reports a mean of 251.5 seconds (approximately 4.19 minutes). The website and paper-body totals imply a different mean of approximately 236.5 seconds, or 3.94 minutes, calculated as 47.3 hours x 3,600 / 720 videos. The aggregation or population difference is unresolved, and the values do not corroborate each other.
- **Collection size:** The original author website reports 47.3 hours, 720 videos, and 12 tasks, with approximately 60 YouTube videos per task.
- **Potential applications:** Procedure learning; Key-step localization; Video-language procedural alignment.
- **Modalities / available information:** RGB video, manually cleaned automatic speech-recognition transcripts, task grammars, and temporal step annotations.
- **Dataset family:** ProceL
- **Access evidence:** As of 2026-10-24: Video URLs only, plus a public annotation-download entry point and a separate annotation-license link. The official page was readable with curl; a Python certificate-chain error did not establish site unavailability. Media downloads and complete package availability were not tested.
- **License observations:** A separate annotation-license file is linked, but its contents were not verified. YouTube media rights are separate.
- **Caveats:** The official readme.txt specifies trimming start and end times for original YouTube videos; data.mat describes the trimmed videos. Original upload lengths are unknown. Preserve the reported 251.5 second mean and the aggregate-derived 236.5 second mean separately; do not merge them into a sample range or assume identical weighting. Minute-scale multistep tutorials are long-horizon candidates, but not every sample is necessarily long or continuously recorded. Editing and narration can reveal steps. Missing or edited-out steps are not verified omission errors; native error, recovery, and optimal next-action supervision were not found.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [ProceL: original official page, overview, and annotations](https://www.khoury.northeastern.edu/home/eelhami/procel.htm)
- [Unsupervised Procedure Learning via Joint Dynamic Summarization: Table 1 and dataset description](https://openaccess.thecvf.com/content_ICCV_2019/papers/Elhamifar_Unsupervised_Procedure_Learning_via_Joint_Dynamic_Summarization_ICCV_2019_paper.pdf)

---

<a id="ucf-crime"></a>

## ERR-17 · UCF-Crime

**Comparison** · **Year / version:** 2018

Surveillance videos show normal activity and public-safety anomalies such as fights, robberies, burglaries, and traffic accidents. The footage retains surrounding context and supports weakly supervised anomaly detection and temporal localization.

- **Duration:** Per-video minimum and maximum are unknown. The inferred mean is approximately 4.04 minutes, calculated as 128 hours x 60 / 1,900 videos. The paper describes videos as long and untrimmed, which does not guarantee a minimum duration for every sample.
- **Collection size:** The original paper reports 128 hours across 1,900 videos, covering 13 anomaly categories plus normal activity.
- **Potential applications:** Weakly supervised anomaly detection; Temporal anomaly localization.
- **Modalities / available information:** RGB and video features; original audio is not a consistent native benchmark input.
- **Dataset family:** UCF-Crime
- **Access evidence:** As of 2026-10-24: Public entry points: the author repository lists UNC Charlotte and Dropbox media links plus test temporal annotations. Linked package contents were not verified. Media downloads and complete package availability were not tested.
- **License observations:** Dataset license not verified; code licenses do not establish rights to source surveillance videos.
- **Caveats:** Continuous surveillance context is not a multistep task-completion episode. Multiple-instance learning splits videos into instances as a training representation; instance lengths must not be conflated with original surveillance-video lengths. Training uses video-level weak labels, while test temporal annotations are provided. Category semantics may dominate detection. Native step, omission, correction, or optimal next-action annotations are absent, so performance does not establish long-horizon procedural state understanding.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Real-world Anomaly Detection in Surveillance Videos: original paper](https://arxiv.org/abs/1801.04264)
- [UCF-Crime: original code, data links, and test annotations](https://github.com/WaqasSultani/AnomalyDetectionCVPR2018)
- [Real-world Anomaly Detection in Surveillance Videos: abstract and dataset description](https://arxiv.org/html/1801.04264)

---

<a id="xd-violence"></a>

## ERR-18 · XD-Violence

**Comparison** · **Year / version:** 2020

Audiovisual footage contains abuse, car accidents, explosions, fighting, riots, and shootings alongside normal context. The collection uses mixed filmed sources, including movie and online material, rather than a uniform set of task-oriented procedures.

- **Duration:** Per-video minimum and maximum are unknown; extrema were not guessed from the website's length-distribution plot. The inferred mean is approximately 2.74 minutes, calculated as 217 hours x 60 / 4,754 videos.
- **Collection size:** The official website reports 217 hours across 4,754 untrimmed videos.
- **Potential applications:** Audiovisual violence detection; Weakly supervised temporal anomaly localization.
- **Modalities / available information:** RGB and audio, with entry points for I3D and VGGish features; video-level weak labels and test annotations.
- **Dataset family:** XD-Violence
- **Access evidence:** As of 2026-10-24: Public entry points for videos, features, and test annotations across multiple storage services. The Baidu training entry is explicitly marked Disabled; other packages were not individually verified. Media downloads and complete package availability were not tested.
- **License observations:** Media license not verified; do not infer video rights from a code license.
- **Caveats:** Untrimmed means that context beyond anomaly windows is retained, not that every sample is a long video. Original web-source lengths and model snippet windows cannot replace released-video durations. The 217-hour collection is not organized around procedural goals and steps. The reviewed primary page did not establish real-event versus enacted provenance for every video, so the dataset is not labeled purely natural accidents. Procedural dependencies and recovery labels are absent; source distribution differs from continuous task execution.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [XD-Violence: official project, release, abstract, and dataset statistics](https://roc-ng.github.io/XD-Violence/)
