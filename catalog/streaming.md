# Long Video, Streaming, and Proactive Assistance

[Back to the collection](../README.md) · [Duration methodology](../docs/methodology.md) · [JSON data](../data/datasets.json)

Long-context memory, online understanding, causal reasoning, and timely assistance.

**13 records.** Suggested applications are editorial research directions; consult annotations and caveats before assuming native task support.

## Contents

- [STR-01 · Qualcomm Interactive Cooking](#qic)
- [STR-02 · EgoServe / Vinci2](#egoserve)
- [STR-03 · CausalVQA](#causalvqa)
- [STR-04 · EgoLife / EgoLifeQA](#egolife)
- [STR-05 · EgoMemReason v1.1](#egomemreason)
- [STR-06 · HourVideo](#hourvideo)
- [STR-07 · LongVideoBench](#longvideobench)
- [STR-08 · OVBench / VideoChat-Online](#ovbench)
- [STR-09 · OVO-Bench](#ovo-bench)
- [STR-10 · STORM-Bench](#storm-bench)
- [STR-11 · StreamingBench](#streamingbench)
- [STR-12 · Video-MME v1](#video-mme)
- [STR-13 · EgoStream (Forte, Lando, and Furnari)](#egostream)

---

<a id="qic"></a>

## STR-01 · Qualcomm Interactive Cooking

**Core candidate** · **Year / version:** 2025

Qualcomm Interactive Cooking adds timestamped step guidance, feedback, and remaining plans to CaptainCook4D cooking videos. Its main and advanced_planning configurations support task-progress reasoning, next-step assistance, and replanning, with recipe graphs in the advanced configuration.

- **Duration:** Complete CaptainCook4D cooking videos identified by video_id: minimum, maximum, mean, and typical duration unknown in this audit. The advanced_planning subset duration distribution is independently unknown.
- **Collection size:** Deduplicated video hours for main and advanced_planning are each unknown; parent-dataset hours cannot substitute for subset totals.
- **Potential applications:** Cooking progress estimation; Next-step guidance; Error feedback; Remaining-plan prediction and replanning.
- **Modalities / available information:** Text and timestamp annotations linked to parent CaptainCook4D video; fields include video_id, remaining_plan, output_timestamps, output_texts, output_types, and advanced recipe_graph annotations.
- **Dataset family:** CaptainCook4D
- **Access evidence:** As of 2026-10-24: Public Hugging Face annotations; videos must be obtained separately from CaptainCook4D. The original check inspected the dataset card and a 14-record test preview. Dataset downloads and playback were not tested.
- **License observations:** The dataset card specifies Research Use. Check the agreement text; the parent-video license does not automatically cover the added annotations.
- **Caveats:** The long-horizon characterization follows complete-recipe guidance and feedback structure, not proof that every video exceeds a duration threshold. Each row represents a video, not one feedback clip; message timestamps and the last feedback entry are not video endpoints. The main and advanced_planning configurations can reuse source videos and must not simply be added. Sampled output_actions fields were often empty, so do not assume one action per feedback message. Offline replay does not establish successful execution after a correction.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Qualcomm Interactive Cooking official dataset card: details, schema, and configurations](https://huggingface.co/datasets/qualcomm/qualcomm-interactive-cooking-dataset)

---

<a id="egoserve"></a>

## STR-02 · EgoServe / Vinci2

**Core candidate** · **Year / version:** 2026

EgoServe combines egocentric videos from EgoLife, HoloAssist, and CaptainCook4D with service-timing and response annotations. Semi-automatically generated and human-checked assistance supports evaluation of when to intervene and what guidance, reminders, or recovery advice to provide.

- **Duration:** Minimum and maximum durations are unknown for every source subset. HoloAssist subset mean approximately 4.59 minutes per video, derived as 14.6 hours * 60 / 191 videos; CaptainCook4D subset mean approximately 12.69 minutes, derived as 18.4 hours * 60 / 87 videos. EgoLife subset file/episode mean unknown; multiday history is not one video.
- **Collection size:** Source-specific video totals in Figure 2(c): EgoLife 95.3 hours, HoloAssist 14.6 hours, and CaptainCook4D 18.4 hours; summed total 128.3 hours.
- **Potential applications:** Intervention timing; Proactive guidance generation; Safety and tool-use reminders; Assistance using historical context.
- **Modalities / available information:** Egocentric video and service text with human-checked assistance timing and content annotations.
- **Dataset family:** EgoLife + HoloAssist + CaptainCook4D
- **Access evidence:** As of 2026-10-24: The official project links the SitongGong/EgoServe Hugging Face release; parent videos must be obtained under each source dataset's access conditions. Dataset downloads and playback were not tested.
- **License observations:** Licenses for the new annotations and all three parent datasets require separate checks; redistribution permission is unconfirmed.
- **Caveats:** Keep original videos, multiday memory histories, and model clip windows separate. Only HoloAssist and CaptainCook4D have matched video counts supporting derived means; do not construct a unified per-sample mean across all three sources. The Vinci2 paper, page 5 Figure 2(c) and section 3.2, reports 191 HoloAssist videos, 87 CaptainCook4D videos, and the first five days for three EgoLife participants; the plotted hours are subset totals. This mixes proactive assistance and everyday memory, not exclusively continuous manipulation. It is not an independent video collection, service appropriateness is not an industrial acceptance standard, and the unverified 547K-QA claim is not adopted.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoServe / Vinci2 official project](https://sitonggong.github.io/EgoServe-page/)
- [EgoServe official Hugging Face release](https://huggingface.co/datasets/SitongGong/EgoServe)
- [Vinci2 paper: page 5 Figure 2(c) and section 3.2 data sources](https://arxiv.org/pdf/2607.11523)

---

<a id="causalvqa"></a>

## STR-03 · CausalVQA

**Auxiliary** · **Year / version:** 2025

Meta's CausalVQA asks about physical behavior and its consequences using selected video clips. Descriptive, counterfactual, hypothetical, anticipation, and planning questions support evaluation of causal reasoning and alternative-action outcomes.

- **Duration:** Final QA clips: reported mean 24.8 seconds and maximum 288.9 seconds; minimum unknown, so the complete minimum-maximum range is unknown. Parent-video duration range and mean are unknown.
- **Collection size:** The original selection pool contains 298 parent videos totaling about 12 hours. Deduplicated hours of final QA clips are unknown; the source-pool total is not the final clip total.
- **Potential applications:** Causal video question answering; Counterfactual outcome reasoning; Action anticipation; Hypothetical and planning questions.
- **Modalities / available information:** Video clips and questions/answers about descriptive, counterfactual, hypothetical, anticipation, and planning scenarios.
- **Dataset family:** Ego4D / Ego-Exo licensing family
- **Access evidence:** As of 2026-10-24: The official repository provides download instructions requiring an EgoExo license application; test answers are withheld. Dataset downloads and playback were not tested.
- **License observations:** EgoExo License.
- **Caveats:** This record refers to Meta's 2025 CausalVQA. Longer parent recordings are cropped to the intervals needed for answers, yielding a mean of tens of seconds; a maximum near five minutes does not make the dataset uniformly long-horizon. Repeated questions and overlapping clips must not be added as independent video time. Paper v1 sections 2.2.1 and 2.2.2 describe the 12-hour source pool and cropping, and page 7 section 2.3.1 reports 24.8-second mean and 288.9-second maximum while noting that difficulty is not primarily long-video memory. A planning question category does not establish executable optimal-action labels.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [CausalVQA official repository and access conditions](https://github.com/facebookresearch/CausalVQA)
- [CausalVQA paper v1: sections 2.2 and 2.3.1](https://arxiv.org/pdf/2506.09943v1)

---

<a id="egolife"></a>

## STR-04 · EgoLife / EgoLifeQA

**Auxiliary** · **Year / version:** 2025

EgoLife records six people sharing a home, including chores, collaboration, conversation, and social activity over a week. Transcripts, dense captions, and long-term questions support retrieval of objects and events and assistance that uses personal history.

- **Duration:** Individual released video files or shards: minimum, maximum, and mean unknown. Each participant has approximately 50 hours of ordered recording history spanning 7 days; this does not mean one continuous 50-hour video file.
- **Collection size:** Approximately 50 hours per participant across 6 participants, yielding approximately 300 first-person hours (6 * approximately 50); simultaneous recordings from different participants are counted separately.
- **Potential applications:** Long-term episodic memory; Object and event retrieval; Cross-day task management; Multi-person activity understanding.
- **Modalities / available information:** Egocentric and synchronized multiview video and audio; the project also describes gaze, IMU, and 3D data, with full release correspondence still requiring verification.
- **Dataset family:** EgoLife
- **Access evidence:** As of 2026-10-24: Official Hugging Face video resources are available at the documented entry point; the matching release coverage of all described modalities remains unverified. Dataset downloads and playback were not tested.
- **License observations:** Hugging Face metadata specifies MIT while the project repository uses an S-Lab license. The scopes are inconsistent; check the agreement covering each specific file before fixing a release.
- **Caveats:** These are long everyday-life histories rather than a collection dedicated to continuous procedural tasks; household work, conversation, and social activity coexist. The project reports six participants, one week, and approximately 50 hours per person, without a released-shard duration range. Do not confuse searchable multiday history, individual file length, and synchronized-view totals, or assume uninterrupted overnight recording. Shared people and environments create identity/time leakage risks, and recording length is not the same as the evidence span required by a question.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoLife official project: daily-life history and recording scope](https://egolife-ai.github.io/)
- [EgoLife official Hugging Face data hosting](https://huggingface.co/datasets/lmms-lab/EgoLife)
- [EgoLife official repository](https://github.com/EvolvingLMMs-Lab/EgoLife)

---

<a id="egomemreason"></a>

## STR-05 · EgoMemReason v1.1

**Auxiliary** · **Year / version:** 2026

EgoMemReason adds cross-day questions and evidence annotations to existing EgoLife recordings. Entity, event, and behavior questions support reasoning about accumulated states, event order, and habits across multiple pieces of historical evidence.

- **Duration:** Individual video shards and actual input prefixes per question: minimum, maximum, and mean unknown. Mean memory backtracking/temporal certification is 25.9 hours, with a mean of 5.1 evidence segments per question; neither statistic is a video duration.
- **Collection size:** New independent recording hours are not applicable because this is an annotation benchmark over existing videos. Deduplicated video hours used by the benchmark are unknown.
- **Potential applications:** Cross-day state accumulation; Event ordering; Habit reasoning; Multi-evidence episodic memory.
- **Modalities / available information:** Parent EgoLife video, multiple-choice questions, and evidence annotations spanning entity, event, and behavior categories across six tasks.
- **Dataset family:** EgoLife
- **Access evidence:** As of 2026-10-24: The Ted412/EgoMemReason release provides 500 public questions; answers are withheld for evaluation. Dataset downloads and playback were not tested.
- **License observations:** Annotations: CC BY-NC 4.0. Video remains subject to EgoLife terms.
- **Caveats:** Version 1.1 evaluates cross-day life-memory reasoning, not one long procedural episode. Do not treat 25.9 hours as mean recording length or multiply 500 questions by backtracking hours to obtain video volume. The project reports 500 questions, 5.1 evidence segments per question, and 25.9-hour memory backtracking/temporal certification. The 2026-07-13 v1.1 update reordered answer-option letters; pin the version and do not reuse predictions expressed as old option letters without remapping.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoMemReason official project: v1.1 and memory-horizon statistics](https://egomemreason.github.io/)
- [EgoMemReason official 500-question release](https://huggingface.co/datasets/Ted412/EgoMemReason)

---

<a id="hourvideo"></a>

## STR-06 · HourVideo

**Auxiliary** · **Year / version:** 2024

HourVideo evaluates reasoning over long egocentric videos selected from Ego4D. Questions cover summarization, recall, tracking, spatial and causal reasoning, counterfactuals, and navigation across everyday scenes.

- **Duration:** Selected videos range from 20 to 120 minutes, with a reported mean of approximately 45.7 minutes.
- **Collection size:** 500 selected videos totaling a reported 381 hours; this is not the total duration of Ego4D.
- **Potential applications:** Long-video question answering; Historical evidence retrieval; Object and event tracking; Spatial, causal, and navigation reasoning.
- **Modalities / available information:** Video and language questions/answers; auxiliary captions are released separately.
- **Dataset family:** Ego4D
- **Access evidence:** As of 2026-10-24: Official repository, Hugging Face, and EvalAI entry points are documented; source videos follow Ego4D access conditions. Dataset downloads and playback were not tested.
- **License observations:** The benchmark and development annotations must not enter training corpora, and the canary must be retained. Other redistribution permissions require checking the dataset card; source video follows Ego4D terms.
- **Caveats:** All selected videos are long, but the 77 everyday scene categories include both procedures such as cooking/cleaning and nonprocedural activity such as eating or watching television. Prediction tasks may truncate inputs at query timestamps; one-minute caption windows are not source-video durations. Paper section 2.3 reports the 20-120-minute range, approximately 45.7-minute mean, and 381-hour total; section 3.1 describes prediction-time truncation. Do not count Ego4D-derived footage again as new recordings. Navigation QA is not closed-loop navigation, and the benchmark should remain isolated from training under its stated restrictions.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [HourVideo official repository and evaluation conditions](https://github.com/keshik6/HourVideo)
- [HourVideo paper](https://arxiv.org/abs/2411.04998)
- [HourVideo paper: section 2.3 statistics and section 3.1 protocol](https://arxiv.org/html/2411.04998)

---

<a id="longvideobench"></a>

## STR-07 · LongVideoBench

**Comparison** · **Year / version:** 2024

LongVideoBench pairs web videos with interleaved subtitles and multiple-choice questions requiring referring reasoning. Its mix of domains and duration groups supports evaluation of visual evidence retrieval and language understanding across different context lengths.

- **Duration:** Collection groups are 8-15 seconds, 15-60 seconds, 3-10 minutes, and 15-60 minutes. The design spans 8 seconds to 60 minutes, but exact observed minimum and maximum durations were not separately reported. Reported mean 473 seconds per video, equivalent to approximately 7.88 minutes.
- **Collection size:** Total hours unknown; the audited paper locations did not directly report a total. Do not multiply question counts by mean video duration.
- **Potential applications:** Referring video question answering; Long-context evidence retrieval; Video and subtitle reasoning; Comparison with and without subtitles.
- **Modalities / available information:** Video, interleaved subtitles, and multiple-choice referring questions.
- **Dataset family:** Multi-domain web video
- **Access evidence:** As of 2026-10-24: Official Hugging Face video/subtitle resources and a data loader are documented; the full release was not downloaded in the original check. Dataset downloads and playback were not tested.
- **License observations:** The data license was not verified in the original source check.
- **Caveats:** The four collection groups include many second-scale clips as well as minute-scale videos; movies, news, daily life, and knowledge content are not all procedural. Group boundaries do not establish that observed samples reach those exact endpoints. The introduction and section 3.1 define the groups, and Table 1 reports 3,763 videos with a 473-second mean. Interleaved subtitles and referenced evidence snippets are not complete-video durations. Subtitle access can bypass visual reasoning, so evaluate subtitle and video-only conditions separately.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [LongVideoBench paper](https://arxiv.org/abs/2407.15754)
- [LongVideoBench official repository and data loader](https://github.com/longvideobench/LongVideoBench)
- [LongVideoBench paper: Table 1 and section 3.1 duration groups](https://arxiv.org/html/2407.15754)

---

<a id="ovbench"></a>

## STR-08 · OVBench / VideoChat-Online

**Comparison** · **Year / version:** 2025

OVBench evaluates online understanding of past events, current observations, and future developments using multiple source datasets. Tasks include goal and step prediction, step verification, procedure recall, object localization, and motion prediction.

- **Duration:** Individual videos and evaluation prefixes: minimum, maximum, mean, and typical duration unknown.
- **Collection size:** Deduplicated video hours unknown.
- **Potential applications:** Online step prediction and verification; Procedure recall; Object localization; Motion and goal prediction.
- **Modalities / available information:** Video and image sequences with online task questions.
- **Dataset family:** Multiple video and image-sequence sources
- **Access evidence:** As of 2026-10-24: The official project provides a Hugging Face benchmark entry point and an evaluation repository. Dataset downloads and playback were not tested.
- **License observations:** The data license was not verified in the original source check.
- **Caveats:** The official project describes six core task categories and sixteen subtasks spanning multiple sources; the proportion of short and long inputs is unknown. Past, present, and future are relative to a query, not evidence of a long full input. Procedure recall is only part of the task mix, and no unified duration distribution was found on the checked page. No reliable official evidence was found for the claimed removal of Mistaken Step Detection on 2025-02-13, so that claim is not adopted.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [OVBench / VideoChat-Online official project and task taxonomy](https://videochat-online.github.io/)
- [VideoChat-Online data loading and evaluation repository](https://github.com/MCG-NJU/VideoChat-Online)

---

<a id="ovo-bench"></a>

## STR-09 · OVO-Bench

**Comparison** · **Year / version:** 2025

OVO-Bench evaluates backward tracing, real-time perception, and forward active responding in streaming video. Source-video and prechunked releases support protocols in which a model recalls history, interprets current evidence, or waits until sufficient future evidence arrives.

- **Duration:** For the repository version checked in the audit, source-video and prechunked-video minimum, maximum, and mean durations are unknown. The reported 263.42 seconds is the mean query timestamp, not mean video duration or a uniform clip length.
- **Collection size:** Deduplicated source-video hours unknown; the checked README reports 644 videos and 3,100 queries, which do not establish total hours.
- **Potential applications:** Historical event tracing; Real-time visual perception; Waiting for sufficient evidence; Streaming response timing.
- **Modalities / available information:** Video and text queries, distributed as source videos and prechunked video packages.
- **Dataset family:** Multi-source online video
- **Access evidence:** As of 2026-10-24: The official Hugging Face source-video and prechunked-video releases have documented download instructions; the original check verified instructions only. Dataset downloads and playback were not tested.
- **License observations:** Data: CC BY-NC-SA 4.0, with inherited source-dataset terms. Code: MIT.
- **Caveats:** This mixes current perception, historical tracing, and waiting for future evidence; the actual short/long-video proportions are unknown. Keep src_videos separate from chunked_videos because chunks may reuse the same source prefix and cannot simply be summed. The checked README explicitly labels 263.42 seconds as Average query timestamp and provides separate source and chunk packages. The repository version differs from the early arXiv version, so pin the release. Forward responding evaluates response timing, not recommended robot or human actions.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [OVO-Bench official README: repository-version statistics, data preparation, and licenses](https://github.com/JoeLeelyf/OVO-Bench)

---

<a id="storm-bench"></a>

## STR-10 · STORM-Bench

**Auxiliary** · **Year / version:** 2026

STORM-Bench tests reasoning from incomplete online evidence in real and simulated activities such as cooking, bicycle repair, health, music, and sports. Timestamped evidence, change-intensity labels, and Known/Uncertain judgments support state tracking and abstention when available observations are insufficient.

- **Duration:** Constructed compact episodes: minimum, maximum, mean, and typical duration unknown. Duration ranges and means of the upstream complete recordings are also unknown.
- **Collection size:** Deduplicated hours of constructed episodes unknown; upstream dataset totals must not be transferred to this benchmark.
- **Potential applications:** Online state tracking from video prefixes; Abstention under insufficient evidence; Historical evidence aggregation; Reasoning about state changes.
- **Modalities / available information:** Real and simulated video, questions/answers, temporal evidence, change-intensity annotations, and Known/Uncertain labels with reasons.
- **Dataset family:** HD-EPIC + Ego-Exo4D + AI2-THOR + VirtualHome
- **Access evidence:** As of 2026-10-24: GitHub provides annotations, manifests, and evaluation code, while Hugging Face provides media for six subsets. Episode IDs differ between the two releases. Dataset downloads and playback were not tested.
- **License observations:** A complete license was not verified; parent-data conditions require individual checks.
- **Caveats:** Chronologically ordered real clips are assembled into compact episodes and are not necessarily temporally continuous in their original recordings; the benchmark also includes simulation rollouts. Distinguish concatenated playback duration from original elapsed time with omitted gaps, and do not present all constructed episodes as original long videos. The official README documents both this construction and differences in episode IDs and media layout between GitHub and Hugging Face releases. This benchmark is distinct from industrial STORM-PSR.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [STORM-Bench official README: dataset construction and release layouts](https://github.com/siruzhong/STORM-Bench)

---

<a id="streamingbench"></a>

## STR-11 · StreamingBench

**Comparison** · **Year / version:** 2024

StreamingBench evaluates understanding and output timing across everyday and web video streams. Visual, audiovisual, sequential-question, and proactive-output settings support comparisons of real-time perception and use of preceding context.

- **Duration:** Complete videos: minimum, maximum, and mean unknown. The main evaluation uses the 60 seconds immediately preceding each query, a protocol window rather than a full-video range; the All Context setting uses a query-dependent prefix length.
- **Collection size:** Total hours for the 900 videos in the checked release are unknown; 4,500 QA items are not independent videos.
- **Potential applications:** Real-time video understanding; Audiovisual question answering; Sequential question answering; Proactive output timing.
- **Modalities / available information:** Video, audio, and text questions/answers.
- **Dataset family:** Multi-source streaming video
- **Access evidence:** As of 2026-10-24: Hugging Face resources and preprocessing scripts are documented; the full dataset was not downloaded in the original check. Dataset downloads and playback were not tested.
- **License observations:** Repository code: MIT. Licenses for benchmark data and source videos were not confirmed in the original check.
- **Caveats:** The main window is the 60 seconds before the query, not the first 60 seconds of the video. Real-time, audiovisual, and long-context settings are mixed; they do not all measure long-term memory or procedural tasks. The checked README reports 900 videos and five query timestamps per video, and distinguishes Main context from All Context (+ Long Context). Pin the version for task counts; the unverified 5,134-QA count is not adopted.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [StreamingBench official README: statistics and evaluation context](https://github.com/THUNLP-MT/StreamingBench)

---

<a id="video-mme"></a>

## STR-12 · Video-MME v1

**Comparison** · **Year / version:** 2024

Video-MME v1 evaluates video understanding with human-written multiple-choice questions across six domains and thirty subdomains. Short, medium, and long groups enable comparisons across input lengths and video, audio, and subtitle conditions.

- **Duration:** Version 1 videos range from 11 seconds to 1 hour. Mean approximately 16.93 minutes, derived as 254 hours * 60 / 900 videos. Evaluation groups: short under 2 minutes, medium 4-15 minutes, and long 30-60 minutes.
- **Collection size:** Version 1 contains 900 videos totaling 254 hours, as reported by the official project.
- **Potential applications:** Multi-domain video question answering; Short-, medium-, and long-context comparison; Audio and subtitle contribution analysis.
- **Modalities / available information:** Video, audio, subtitles, and human-written multiple-choice questions.
- **Dataset family:** General web video
- **Access evidence:** As of 2026-10-24: The official project provides code and data entry points. Dataset downloads and playback were not tested.
- **License observations:** Licenses for benchmark data and source videos were not verified in the original check.
- **Caveats:** The benchmark mixes short, medium, and long videos across domains; it is not uniformly long-horizon procedural content. This record and its duration statistics cover v1 only, not v2. The v1 introduction reports 11 seconds to 1 hour, 900 videos, and 254 hours; leaderboard groups define the three duration bands. Audio, subtitles, and multiple questions attached to one video do not add recording time. Global QA does not directly evaluate continuous procedural state tracking.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Video-MME v1 official project: introduction and duration groups](https://video-mme.github.io/home_page.html)

---

<a id="egostream"></a>

## STR-13 · EgoStream (Forte, Lando, and Furnari)

**Watchlist** · **Year / version:** 2026

EgoStream evaluates episodic memory in streaming egocentric video across seven memory dimensions. Evidence moments and Answer Validity Windows support analysis of whether an incorrect answer reflects forgetting or a subsequent change in the world.

- **Duration:** Individual source videos, evaluation subclips, and input prefixes: minimum, maximum, and mean unknown. Recall-delay regimes extend from immediate recall to more than 8 hours, but this is memory delay, not a video-duration range.
- **Collection size:** Deduplicated source-video hours unknown; totals from the multiple parent datasets must not be imported as this benchmark's total.
- **Potential applications:** Streaming episodic memory evaluation; Answer-validity tracking; Distinguishing forgetting from world-state changes.
- **Modalities / available information:** Egocentric video and questions/answers, evidence moments, and Answer Validity Window annotations.
- **Dataset family:** Multiple egocentric QA source datasets
- **Access evidence:** As of 2026-10-24: The original check verified the paper; availability of a complete usable dataset package and its license was not confirmed. Dataset downloads and playback were not tested.
- **License observations:** Unverified. A Creative Commons license on the paper does not establish a data license.
- **Caveats:** This is the EgoStream work by Forte, Lando, and Furnari; do not import statistics from namesakes or other Ego benchmarks. Not every question requires long memory, and the data are not a uniform collection of continuous procedural episodes. Record evidence moments, Answer Validity Windows, query delays, and input-video lengths separately. Paper section 3.1 draws from Ego4D, EgoLife, EgoTempo, Multi-Hop EgoQA, and HD-EPIC; appendix A.5 describes subclip cropping that preserves answer validity, and A.6 includes recall delays exceeding 28,800 seconds. Keep the watchlist status until release availability is confirmed.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoStream original paper](https://arxiv.org/abs/2605.31557)
- [EgoStream paper v1: sources, subclips, and recall-delay regimes](https://arxiv.org/html/2605.31557v1)
