# Egocentric and Instructional Procedures

[Back to the collection](../README.md) · [Duration methodology](../docs/methodology.md) · [JSON data](../data/datasets.json)

Cooking, daily activities, skill learning, instructional videos, and first-person task progress.

**18 records.** Suggested applications are editorial research directions; consult annotations and caveats before assuming native task support.

## Contents

- [EGO-01 · CaptainCook4D](#captaincook4d)
- [EGO-02 · EPIC-Tent](#epic-tent)
- [EGO-03 · HoloAssist](#holoassist)
- [EGO-04 · Ego-Exo4D](#ego-exo4d)
- [EGO-05 · Ego4D Goal-Step](#ego4d-goal-step)
- [EGO-06 · HD-EPIC](#hd-epic)
- [EGO-07 · 50Salads](#50salads)
- [EGO-08 · Breakfast Actions](#breakfast)
- [EGO-09 · COIN](#coin)
- [EGO-10 · CrossTask](#crosstask)
- [EGO-11 · Ego4D](#ego4d)
- [EGO-12 · EgoPlan / EgoPlan-IT / EgoPlan-Bench](#egoplan)
- [EGO-13 · EgoPlan-Bench2](#egoplan-bench2)
- [EGO-14 · EPIC Fields](#epic-fields)
- [EGO-15 · EPIC-KITCHENS-100](#epic-kitchens)
- [EGO-16 · HowTo100M](#howto100m)
- [EGO-17 · HT-Step](#ht-step)
- [EGO-18 · YouCook2](#youcook2)

---

<a id="captaincook4d"></a>

## EGO-01 · CaptainCook4D

**Core candidate** · **Year / version:** 2023 preprint; 2024

Head-mounted recordings capture complete recipe executions in home kitchens, including deliberate deviations and unintentional mistakes. Step and fine-grained action annotations, seven error categories, and recipe dependency graphs support procedural understanding and error analysis.

- **Duration:** Recording minimum and maximum are unknown; the derived mean is approximately 14.766 minutes (94.5 hours x 60 / 384 recordings). This is the recording mean, not the mean step-clip duration.
- **Collection size:** 384 recordings totaling 94.5 hours; 24 recipes, 8 participants, and 10 kitchens. Approximately 5.3K step and 10K action annotations; their cumulative annotated duration is unknown. Synchronized modalities do not add independent recording hours.
- **Potential applications:** Procedural error recognition; Step localization; Procedure learning; Dependency-aware order analysis.
- **Modalities / available information:** Head-mounted GoPro Hero11 and HoloLens2 RGB, depth, audio, IMU, and head/hand tracking.
- **Dataset family:** Independent CaptainCook4D collection; synchronized sensor streams represent the same executions.
- **Access evidence:** As of 2026-10-24: Open; the official site lists a downloader and annotation repository. Media and annotation packages were not downloaded or tested.
- **License observations:** The official data section explicitly states Apache License 2.0 for the data; this is not inferred from the code license.
- **Caveats:** The duration mean is derived from published collection totals. Recipe selection based on preparation times of at most 30 minutes does not establish a recording maximum; complete-process coverage needs sample-level screening. Errors combine staged deviations and unintended mistakes. Split by recipe, operator, and kitchen as appropriate; dependency graphs permit alternative valid orders. Counterfactual correction outcomes are not established by the native benchmark.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [CaptainCook4D official project: data license and collection statistics](https://captaincook4d.github.io/captain-cook/)
- [CaptainCook4D paper: collection protocol, error categories, and statistics](https://arxiv.org/html/2312.14556)

---

<a id="epic-tent"></a>

## EGO-02 · EPIC-Tent

**Core candidate** · **Year / version:** ICCV Workshops 2019; Bristol release 2020-08-10

Participants assemble a tent outdoors while synchronized egocentric cameras and eye tracking record the process. Action, error, uncertainty, and gaze annotations support analysis of assembly progress, hesitation, and recovery.

- **Duration:** 2019 paper, 24-participant version: full recordings average 13.6 minutes, with minimum and maximum unknown; task-completion segments range from 4.3 to 24.1 minutes and average 12.1 minutes. For the 2020 repository version with 29 participants, per-video minimum, maximum, and mean are unknown; the older mean does not transfer to this version.
- **Collection size:** 2019 paper version: 24 participants and approximately 5.4 hours. Bristol release dated 2020-08-10: 29 participants, over 7 hours, and 166.8 GiB. GoPro, SMI, and gaze-overlay renderings are synchronized views or representations, not two or three times as many independent session hours.
- **Potential applications:** Action recognition and detection; Step tracking; Assembly error analysis; Uncertainty and recovery analysis.
- **Modalities / available information:** Synchronized egocentric GoPro and SMI video with eye tracking; a third-person overview is not guaranteed.
- **Dataset family:** Independent EPIC-Tent collection with distinct 2019 paper and 2020 hosted versions.
- **Access evidence:** As of 2026-10-24: Open; hosted Bristol files and the official annotation repository were visible. Media were not downloaded.
- **License observations:** Hosted data use the Non-Commercial Government Licence for public sector information, not CC BY. The annotation repository code license was not verified.
- **Caveats:** The 2020 figures of 29 participants and over 7 hours remain valid; do not combine them with the 2019 duration statistics. The 4.3-24.1-minute range describes task-completion segments, not full recordings. Omission annotations lack usable end times; order-error intervals describe the action being performed. Treating all error types as ordinary temporal intervals would misrepresent their semantics.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Bristol EPIC-Tent official 2020 data release and license](https://data.bris.ac.uk/data/dataset/2ite3tu1u53n42hjfh3886sa86)
- [EPIC-Tent official action and error annotation repository](https://github.com/youngkyoonjang/EPIC_Tent2019)
- [EPIC-Tent 2019 paper, Sections 3.1-3.2](https://research-information.bris.ac.uk/ws/files/208376241/PID6108907.pdf)

---

<a id="holoassist"></a>

## EGO-03 · HoloAssist

**Core candidate** · **Year / version:** ICCV 2023; official-site version documented in 2026

A performer manipulates physical objects while a remote instructor provides spoken guidance. Multimodal recordings include hierarchical actions, dialogue, and mistake/correction attributes for studying collaborative assistance.

- **Duration:** Full task-session minimum and maximum are unknown. The derived mean is approximately 4.484 minutes using the internally matched 2023 paper figures of 166 hours and 2,221 sessions; fine-grained action durations in seconds do not describe entire sessions.
- **Collection size:** 2023 paper: 166 hours across 2,221 sessions. Official site: 169 hours and 350 instructor-performer pairs. These are separate reporting bases: do not divide 169 hours by 2,221 or treat participant pairs as sessions. Seven synchronized streams do not add independent hours.
- **Potential applications:** Mistake detection; Intervention-type prediction; Hand-motion prediction; Collaborative correction analysis.
- **Modalities / available information:** HoloLens egocentric RGB, depth, audio, gaze, hand/head poses, IMU, camera calibration, and dialogue transcripts.
- **Dataset family:** Independent HoloAssist collection; upstream source for EgoVoice, whose selected subset is smaller than the full collection.
- **Access evidence:** As of 2026-10-24: Open; the official site lists video, sensor, label, and split downloads. Downloads and media availability were not tested.
- **License observations:** The official site identifies the data license as CDLAv2 (Community Data License Agreement v2). The exact license text and separate code license were not checked.
- **Caveats:** The reason for the paper/site difference of 166 versus 169 hours is unknown; neither total should silently replace the other. EgoVoice uses a 124.8-hour upstream subset, not all HoloAssist footage. Native mistake detection uses history within the current coarse step; intervention-type prediction uses 1/3/5-second windows, and hand prediction uses 3 seconds of history. These tasks do not establish full-session memory or closed-loop assistance effectiveness. Recorded mistakes are real within controlled collaboration tasks.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [HoloAssist official project: tasks, data downloads, and 169-hour total](https://holoassist.github.io/)
- [HoloAssist ICCV 2023 paper: Table 2 and annotation definitions](https://arxiv.org/html/2309.17024)

---

<a id="ego-exo4d"></a>

## EGO-04 · Ego-Exo4D

**Core candidate** · **Year / version:** 2023 preprint; CVPR 2024; V2 released 2024-03-25

Synchronized first- and third-person recordings capture skilled activities such as cooking, repair, sports, and music. Key steps, action descriptions, expert commentary, proficiency, and pose annotations support multiview skill understanding.

- **Duration:** V2 take/full-session minimum, maximum, and mean are unknown. task_start_sec and task_end_sec mark task boundaries within a take; cropped keystep benchmark clips are a separate sample unit.
- **Collection size:** V2: 5,035 takes, 1,286.30 hours summed across all camera views, and 221.26 hours of egocentric footage. Deduplicated synchronized-session hours were not separately verified. Neither 1,286.30 / 5,035 nor an assumed one-to-one equal-length ego stream per take establishes a session mean.
- **Potential applications:** Key-step understanding; Cross-view correspondence; Skill assessment; Body and hand pose estimation.
- **Modalities / available information:** Aria egocentric and multiple GoPro third-person views, audio, gaze, trajectories, 3D point clouds, and body/hand poses.
- **Dataset family:** Independent Ego-Exo4D collection, not a subset of Ego4D; multiple synchronized views share a take.
- **Access evidence:** As of 2026-10-24: Gated; official instructions require accepting the data agreement and obtaining credentials. Full takes and keystep clips have separate downloads; downloading was not tested.
- **License observations:** A dedicated Ego-Exo4D data agreement governs use and redistribution. Ego4D code licenses do not establish the media license.
- **Caveats:** The V2 totals are retained with distinct all-view and ego units, following the 2024-03-25 and 2024-09-01 changelog entries. Keystep clips do not establish full-take lengths; screen long procedures using take task boundaries. Annotation coverage varies by take. Sports and music may require separate strata, and views of the same take must stay in one split. Expert quality feedback is not verified as uniform temporal error ground truth.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Ego-Exo4D official project](https://ego-exo4d-data.org/)
- [Ego-Exo4D V2 changelog: 2024-03-25 and 2024-09-01 releases](https://docs.ego-exo4d-data.org/changelog/)
- [Ego-Exo4D official access and data-agreement instructions](https://docs.ego-exo4d-data.org/getting-started/)

---

<a id="ego4d-goal-step"></a>

## EGO-05 · Ego4D Goal-Step

**Core candidate** · **Year / version:** NeurIPS 2023; ProVideLLM application in 2025

Goal annotations cover diverse Ego4D activities, while a smaller cooking-focused subset adds hierarchical steps and substeps. Temporal boundaries and goal descriptions support offline localization and online procedural recognition.

- **Duration:** Original paper Table 1: the full goal-label set has a reported mean video duration of approximately 23 minutes; the 851-video step/substep subset averages approximately 26 minutes. Minimum and maximum are unknown for both. The mean annotated segment duration of 32.5 seconds is not a whole-video mean.
- **Collection size:** Goal-label set: 7,353 videos, 2,807 video hours, and 319 goal classes. Nested step subset: 851 videos, 368 video hours, 47,721 step/substep segments, 86 goals, and 514 step classes. The 430 annotated-segment hours can overlap hierarchically and are not 430 independent video hours; subsets must not be added.
- **Potential applications:** Goal and step temporal localization; Online goal and step detection; Natural-language step localization.
- **Modalities / available information:** Egocentric video with hierarchical textual goals, steps, substeps, and temporal annotations.
- **Dataset family:** Annotations on existing Ego4D footage, not newly recorded video; overlaps with other Ego4D-derived datasets are possible.
- **Access evidence:** As of 2026-10-24: Underlying video is gated through Ego4D credentials; official instructions provide the goalstep CLI benchmark filter. The annotation repository is public, and the paper describes CLI annotation delivery. Downloading was not tested.
- **License observations:** Underlying video follows the Ego4D agreement. Annotation terms are inconsistent: the repository README states MIT; the paper datasheet says annotations need no license/restrictions in one place, while Section C.6 describes distribution under the standard Ego4D agreement. The applicable terms must be checked for each file or release package.
- **Caveats:** Use 368 video hours for the step subset and 430 cumulative annotated-segment hours, not 430 independent video hours. A downstream 15-30-minute sampling window is not a full-dataset range. Ego4D v2.1 regrouped previously split continuous footage involving 210 original videos; preserve group-to-video_uid mappings for splits. is_relevant marks relevance to a parent goal and is_continued marks continuation, neither an error label. ProVideLLM uses this dataset for online step detection and transfer; its next-step experiments on COIN and Assembly101 must not be attributed to Goal-Step.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Ego4D Goal-Step official repository, schema, and annotation license](https://github.com/facebookresearch/ego4d-goalstep)
- [ProVideLLM: Memory-efficient Streaming VideoLLMs for Real-time Procedural Video Understanding](https://arxiv.org/html/2504.13915)
- [Ego4D Goal-Step NeurIPS 2023 paper: Table 1 and datasheet](https://proceedings.neurips.cc/paper_files/paper/2023/file/7a65606fa1a6849450550325832036e5-Paper-Datasets_and_Benchmarks.pdf)
- [Ego4D v2.1 updates: Goal-Step and grouped videos](https://ego4d-data.org/docs/updates/)

---

<a id="hd-epic"></a>

## EGO-06 · HD-EPIC

**Core candidate** · **Year / version:** CVPR 2025

Unscripted cooking recordings span days and kitchens, capturing detailed object interactions and recipe preparation. Dense action, audio, gaze, object, and 3D annotations connect individual observations to recipes and spatial context.

- **Duration:** Full videos have a reported mean of 15.9 minutes and standard deviation of 14.5 minutes; minimum and maximum are unknown. Recording starts when a participant enters the kitchen and ends on leaving, so one video is not necessarily one complete recipe.
- **Collection size:** 156 videos totaling 41.3 hours in the paper; the official-site figure of 41 hours is rounded. Collection covers 9 kitchens and 69 recipes, with 59.4K actions, 50.9K audio events, 19.9K object tracks, and 26.6K VQA questions. Recipes average 4 hours 48 minutes of elapsed preparation-to-serving time across 2.1 videos; the longest spans 2 days 6 hours. These elapsed spans are not continuous recorded hours.
- **Potential applications:** Action and object understanding; Spatial grounding; Recipe-step alignment; Video question answering.
- **Modalities / available information:** Project Aria egocentric video, audio, gaze, 3D information, and scene digital twins; object tracks and hand masks.
- **Dataset family:** Independent HD-EPIC collection, distinct from EPIC-KITCHENS-100 and EPIC Fields; upstream footage for Minerva-Ego.
- **Access evidence:** As of 2026-10-24: Open; the official Bristol record lists data files totaling 2.3 TiB. Files were not downloaded or checked.
- **License observations:** The Bristol data record explicitly states CC BY 4.0. This does not establish licenses for all related datasets or code.
- **Caveats:** The audit refines the rounded 41-hour figure to 41.3 hours and adds the video mean. Recipe elapsed times and participant totals of 3.5-7.2 hours must not be presented as individual-video ranges. The density of 263 annotations per minute combines annotation types rather than counting 263 steps. High annotation density does not establish error ground truth or native next-action decision supervision.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [HD-EPIC official project and annotation statistics](https://hd-epic.github.io/)
- [University of Bristol HD-EPIC data record and license](https://data.bris.ac.uk/data/dataset/3cqb5b81wk2dc2379fx1mrxh47)
- [HD-EPIC paper, Sections 3 and B.2: collection and duration statistics](https://arxiv.org/html/2502.04144v2)

---

<a id="50salads"></a>

## EGO-07 · 50Salads

**Comparison** · **Year / version:** Data 2012; paper 2013

Participants prepare salads in a fixed setting while RGB-D video and object-mounted accelerometers record hand, tool, and ingredient interactions. Multilevel activity intervals include preparation, core, and post-action phases for temporal activity analysis.

- **Duration:** Full-sequence minimum, maximum, and exact mean remain unknown. The often-quoted approximately 5-10-minute range was not confirmed from the primary-source material obtained. The original abstract states over 4.5 hours for 50 sequences, implying only a mean greater than 5.4 minutes, not a typical duration.
- **Collection size:** 50 sequences from 25 participants preparing two salads each. The UbiComp 2013 abstract states over 4.5 hours of synchronized accelerometer and RGB-D data; the official dataset description more broadly says over 4 hours. These compatible lower bounds are not exact totals. Synchronized sensors do not add independent hours; cumulative annotation duration is unknown.
- **Potential applications:** Activity recognition; Action localization; Sequence and progress analysis; Sensor fusion.
- **Modalities / available information:** Third-person RGB-D video, object-mounted accelerometers, and multilevel temporal activity labels.
- **Dataset family:** Independent 50Salads collection with synchronized video and object-sensor streams.
- **Access evidence:** As of 2026-10-24: Open; the Dundee record provides a README and the original data-site entry point. Availability of files on the older site was not tested.
- **License observations:** The Dundee dataset record states CC BY-NC-SA 4.0; commercial use and unrestricted redistribution are not implied.
- **Caveats:** The canonical 2026-10-31 follow-up accepts the original abstract's >4.5-hour lower bound, correcting an earlier overly conservative audit that retained only >4 hours. The complete original paper was not obtained, so the 5-10-minute range is unconfirmed rather than proven absent. Secondary reports of 6.4-minute means or 5.3-hour totals were not adopted. A single task domain and limited scene variation constrain generalization; dedicated failure labels were not established.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Dundee 50 Salads official data record and license](https://discovery.dundee.ac.uk/en/datasets/50-salads/)
- [50 Salads official data-format archive: synchronized sensors and timestamps](https://discovery.dundee.ac.uk/ws/portalfiles/portal/10245400/50salads.pdf)
- [Stein and McKenna, UbiComp 2013: original abstract hosted by Dundee](https://discovery.dundee.ac.uk/en/publications/combining-embedded-accelerometers-with-computer-vision-for-recogn/)

---

<a id="breakfast"></a>

## EGO-08 · Breakfast Actions

**Comparison** · **Year / version:** CVPR 2014; official download notes documented in 2026

Multicamera recordings show participants preparing breakfast in different kitchens. Activity classes and coarse and fine action segments provide a controlled setting for recognition and temporal segmentation.

- **Duration:** CVPR 2014 full single-view videos have a derived mean of approximately 2.323 minutes (139.37 seconds), using approximately 77 hours and 1,989 videos summed across the paper's ten class counts. The 2016 extended manuscript's action-annotated set has 1,712 videos and 66.7 hours, implying approximately 2.338 minutes (140.26 seconds). Both support roughly 2.3 minutes, not a directly reported exact mean; minimum, maximum, and deduplicated-session mean remain unknown.
- **Collection size:** CVPR 2014: approximately 77 hours and 1,989 videos. The 2016 extended manuscript reports 1,712 action-annotated videos and 66.7 hours. Keep these bases separate. Collection includes 52 participants, 18 kitchens, 10 activities, 48 action units, and 3-5 cameras per location; totals include multiple views and the paper also mentions mirroring. Deduplicated session hours are unknown.
- **Potential applications:** Action recognition; Temporal action segmentation; Derived action anticipation.
- **Modalities / available information:** Multiview third-person RGB, coarse/fine temporal labels, and Fisher-vector features.
- **Dataset family:** Independent Breakfast collection; synchronized camera views must not be counted as separate executions.
- **Access evidence:** As of 2026-10-24: Open links to data and annotation mirrors are listed, but the official site says the raw-video mirror is incomplete and reports a Google Drive quota issue dated 2026-10-11. Complete media availability was not verified and downloads were not tested.
- **License observations:** An explicit data license was not verified on the official site. Mirror metadata and tool-code licenses do not replace original authorization.
- **Caveats:** The canonical follow-up adds derived means from matched paper versions; do not cross-divide or add their totals. The original 100k figure counts sampled codebook-training features, while 11,267 counts coarse action instances, including approximately 3,600 silence instances; neither counts full videos. The 2016 table's 26.0-second mean is for action segments. Media were not measured file by file. Low resolution, controlled scenes, multiview duplication, and incomplete mirrors limit use; dedicated failure labels were not established.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Breakfast official data page: collection scale and download availability](https://serre.lab.brown.edu/breakfast-actions-dataset.html)
- [The Language of Actions, CVPR 2014: Section 3 counts and Section 5.1 features](https://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Kuehne_The_Language_of_2014_CVPR_paper.pdf)
- [Cooking in the Kitchen, author extended manuscript dated 2016-03-17: Table 1 and Section 3.1](https://serre-lab.clps.brown.edu/wp-content/uploads/2016/11/2016_Kuehne_.pdf)

---

<a id="coin"></a>

## EGO-09 · COIN

**Comparison** · **Year / version:** CVPR 2019

YouTube instructional videos cover everyday procedures across 12 domains and 180 tasks. A domain-task-step hierarchy and manually labeled step intervals support broad instructional-video understanding.

- **Duration:** Full source-video durations range from 4.411667 to 1,236.250167 seconds (approximately 0.0735-20.6042 minutes), with a mean of 142.341911 seconds (approximately 2.372365 minutes), computed from duration fields in 11,827 official COIN.json records. Annotated steps range from 1 to 304 seconds and average 14.908616 seconds.
- **Collection size:** Official JSON: 11,827 video durations sum to 1,683,477.776057 seconds (approximately 467.632716 hours). The 46,354 step intervals sum to 691,074 seconds (approximately 191.965 hours), without merging overlaps. The website separately reports 476 hours and a 2.36-minute mean. These conflicting statistics remain distinct.
- **Potential applications:** Instructional step recognition; Temporal step localization; Step segmentation; Derived next-step and long-horizon step prediction.
- **Modalities / available information:** Web video, potentially including source audio, with task/step categories and temporal intervals.
- **Dataset family:** COIN instructional-video collection; source YouTube IDs should be used to check overlap with other web-video datasets.
- **Access evidence:** As of 2026-10-24: Hosted media copies require an institutional representative to sign an agreement and request access by email. Video URLs and annotation JSON are public for separate YouTube retrieval; registration/login is also listed. No request or media-download test was performed.
- **License observations:** The official annotation README restricts its codes and files to research while allowing sharing and modification. Hosted video copies require a separate license agreement; a uniform CC BY-NC license was not established.
- **Caveats:** The audit read and computed official metadata, without downloading media or running ffprobe. The reason for the website's 476 hours versus the JSON's approximately 467.633 hours is unknown; 476 x 60 / 11,827 is approximately 2.4148 minutes, also unlike the reported 2.36-minute mean. Edited tutorials may omit transitions and are not continuous full-task sessions. ProVideLLM supplies derived step-prediction protocols, not closed-loop decision evaluation; dedicated procedural-error labels were not verified.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [COIN official website: statistics and access conditions](https://coin-dataset.github.io/)
- [COIN official annotation README and license](https://raw.githubusercontent.com/coin-dataset/annotations/master/README.md)
- [ProVideLLM step-prediction tasks on COIN](https://arxiv.org/html/2504.13915v1)
- [COIN official JSON: per-video duration and annotated step intervals](https://raw.githubusercontent.com/coin-dataset/annotations/master/COIN.json)

---

<a id="crosstask"></a>

## EGO-10 · CrossTask

**Comparison** · **Year / version:** CVPR 2019

Web tutorials cover cooking, vehicle maintenance, crafts, and other procedures with ordered textual steps. Primary tasks have manually labeled temporal step boundaries, while related tasks provide additional videos without those boundaries.

- **Duration:** For primary source videos, the paper reports a mean of 4 minutes 57 seconds (4.95 minutes), with minimum and maximum unknown. The same paper's 212 hours / 2,750 videos implies approximately 4.625 minutes, which is inconsistent with that reported mean. The per-video range for related tasks is unknown.
- **Collection size:** Primary: 18 tasks, 2,750 videos, and 212 hours. Related: 65 tasks, 1,950 videos, and 161 hours. The arithmetic sum of 373 hours is not a verified deduplicated total, and 4,700 unique videos were not established. Only primary tasks have manual temporal boundaries.
- **Potential applications:** Cross-task weakly supervised step localization; Instructional step alignment.
- **Modalities / available information:** Web RGB video/audio, ordered step text, temporal annotations for primary tasks, and precomputed features.
- **Dataset family:** CrossTask primary and related web-video groups; cross-group source-ID overlap was not recalculated.
- **Access evidence:** As of 2026-10-24: Links only for source media; the official repository provides task descriptions, video URLs, annotations, and feature links. YouTube availability and downloading were not tested.
- **License observations:** BSD-3-Clause establishes the repository software license only. Separate media and annotation licenses were not verified.
- **Caveats:** Preserve the paper's inconsistent mean and count/total statistics without guessing a correction. Cross-group deduplication was not verified. The paper reports that an average of 31% of predefined steps are not shown; editing and valid procedural variants can explain missing steps, so they are not automatic omission-error labels. Next-step prediction and planning require separately defined derived protocols.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [CrossTask official repository and dataset documentation](https://github.com/DmZhukov/CrossTask)
- [CrossTask original paper, Section 5.2](https://arxiv.org/html/1903.08225)

---

<a id="ego4d"></a>

## EGO-11 · Ego4D

**Auxiliary** · **Year / version:** 2021 preprint; CVPR 2022; official-site scale documented in 2026

Large-scale egocentric recordings capture daily life and hand-object interactions across diverse locations. Separate annotation subsets support narration, state-change understanding, interaction analysis, and future-activity prediction.

- **Duration:** Full-collection minimum, maximum, and mean are unknown for both individual files and original continuous captures/sessions. Cropped lengths from downstream benchmarks do not establish a full-dataset range.
- **Collection size:** The official homepage reports 3,670 hours and 923 participants, with collection across 74 locations in 9 countries. These are parent-collection totals, not hours of a selected long-procedure subset; versions and derived annotations do not add new recording hours.
- **Potential applications:** Object state-change understanding; Hand-object interaction analysis; Future-activity prediction; Egocentric video understanding.
- **Modalities / available information:** Egocentric RGB and audio; additional sensors vary by collection source, and annotations vary by subset.
- **Dataset family:** Parent footage for Goal-Step, the Ego4D portions of EgoPlan, EgoPlan-Bench2, EgoSAT, and LongEgoRefer, among other derivatives.
- **Access evidence:** As of 2026-10-24: Gated; a signed data agreement and approved access credentials are required. Public descriptions do not imply registration-free downloads; media downloading was not tested.
- **License observations:** A dedicated Ego4D data agreement governs video access and use. Tool-repository licenses do not replace it.
- **Caveats:** The canonical audit retains the 3,670-hour total. The relationship between file segmentation and continuous sessions remains unverified; participant counts cannot establish a video mean. Full-procedure coverage and annotation density vary, and no uniform procedural-error ground truth was established. Do not count overlapping media from derived benchmarks as new footage.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Ego4D official homepage: collection scale and access process](https://ego4d-data.org/)

---

<a id="egoplan"></a>

## EGO-12 · EgoPlan / EgoPlan-IT / EgoPlan-Bench

**Comparison** · **Year / version:** 2023 preprint; IJCV publication 2026-02-12

Goal-conditioned questions ask which action should come next given an egocentric observation and action history. The first-generation benchmark combines EPIC-KITCHENS and Ego4D examples, while EgoPlan-IT supplies instruction-tuning questions from EPIC-KITCHENS.

- **Duration:** Minimum, maximum, and mean duration of each question's history video are unknown, and full source-session ranges were not verified. History up to the current action and the current observation are the relevant context units; full EPIC-KITCHENS or Ego4D recording lengths must not be substituted.
- **Collection size:** 4,939 evaluation multiple-choice questions across 419 scenarios. Goal counts conflict within the sources: 3,296 in the text versus 3,269 in arXiv v3 Table 2. EgoPlan-IT has 50K automatically constructed planning questions; 50K auxiliary action-recognition instructions reuse observations, and 164K external general instructions are separate. Deduplicated source-video hours and cumulative question-history hours are unknown.
- **Potential applications:** Goal-conditioned next-action selection; Video-based instruction tuning.
- **Modalities / available information:** Video/image observations, textual goals, action histories, and multiple-choice answers.
- **Dataset family:** First-generation annotations derived from EPIC-KITCHENS and Ego4D; EgoPlan-IT uses EPIC-KITCHENS only. No new recording hours are established.
- **Access evidence:** As of 2026-10-24: Open annotation entry points for Val/Test questions and IT data are listed in the official repository; the paper states that Test answer keys are withheld. Underlying EPIC-KITCHENS and Ego4D video must be obtained separately, with credentials required for Ego4D. Downloads were not tested.
- **License observations:** The paper states CC BY-NC 4.0 for EgoPlan-Val/Test/IT and BSD 3-Clause for code and models. Underlying media retain their respective EPIC-KITCHENS and Ego4D terms.
- **Caveats:** Keep the conflicting 3,296/3,269 goal counts explicit. QA and instruction counts are not independent videos and cannot establish duration. The 2026 journal publication does not imply new footage. Split by source video ID to prevent overlap across derivatives. This is offline next-action selection, not evidence of counterfactually optimal planning, closed-loop execution, or real procedural-error labels.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoPlan official repository](https://github.com/ChenYi99/EgoPlan)
- [EgoPlan paper v3: construction, statistics, and licensing](https://arxiv.org/html/2312.06722v3)
- [EgoPlan IJCV journal version](https://link.springer.com/article/10.1007/s11263-025-02676-0)

---

<a id="egoplan-bench2"></a>

## EGO-13 · EgoPlan-Bench2

**Comparison** · **Year / version:** 2024-12 preprint; 2025-04 revision; IJCV publication 2026-04-08

Multiple-choice questions evaluate goal-conditioned next-action reasoning across broader egocentric scenarios. Each example combines task-progress history, a current observation, a goal, and four candidate actions derived from Ego4D.

- **Duration:** Per-question task-progress/history videos range from a few seconds to approximately 5 minutes. The exact minimum and mean are unknown; this range does not describe complete upstream Ego4D sessions.
- **Collection size:** 1,321 questions drawn from 1,113 Ego4D videos, covering 4 broad domains and 24 scenarios. Deduplicated media hours and cumulative question-history duration are unknown. The 2026 journal version still reports 1,321 questions; inherited footage is not new recording time.
- **Potential applications:** Goal-conditioned next-action selection; Task-progress reasoning.
- **Modalities / available information:** Textual goals, current visual observations, history video/action context, and multiple-choice answers.
- **Dataset family:** Derived exclusively from Ego4D, unlike the first-generation benchmark's mixed upstream sources; possible overlap with its Ego4D portion and Goal-Step requires video_uid checks.
- **Access evidence:** As of 2026-10-24: Open question entry points are listed on the official project and repository. Underlying Ego4D media require acceptance of its data agreement. Links, media coverage, and answer packages were not tested.
- **License observations:** This benchmark's data license was not verified. The project template's CC BY-SA and the journal article's CC BY do not establish QA or media terms; Ego4D media remain under their parent agreement.
- **Caveats:** The audit confirms the approximate few-seconds-to-5-minute history range. The 690 questions with histories at most 30 seconds and 631 with longer histories are QA groups, not a distribution of independent videos. Do not describe 5 minutes as the maximum full-session length. Publication and expanded model analysis do not establish additional media. Offline answers do not demonstrate action execution, feedback-driven correction, or procedural-error ground truth.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoPlan-Bench2 official project](https://qiulu66.github.io/egoplanbench2/)
- [EgoPlan-Bench2 official repository](https://github.com/qiulu66/EgoPlan-Bench2)
- [EgoPlan-Bench2 IJCV journal version](https://link.springer.com/article/10.1007/s11263-026-02826-y)
- [EgoPlan-Bench2 paper, Sections III-C and V-A: sources and history duration](https://arxiv.org/html/2412.04447)

---

<a id="epic-fields"></a>

## EGO-14 · EPIC Fields

**Auxiliary** · **Year / version:** 2023

Camera trajectories and 3D reconstructions augment existing EPIC-KITCHENS cooking videos. The geometric information supports reconstruction and derived analyses of spatial context and object location.

- **Duration:** Minimum and maximum duration of the 671 covered source videos are unknown. Their derived mean is approximately 8.852 minutes using 99 hours / 671 videos; this is not a mean for registered-frame exposure or annotated clips.
- **Collection size:** 671 source videos covering approximately 99 hours and 45 kitchens, with recovered camera poses for 19M frames. These are geometric annotations on EPIC-KITCHENS media, not 99 additional independent video hours. Continuous registration coverage and independent-task duration need separate verification.
- **Potential applications:** 3D reconstruction; Derived spatial grounding; Camera-motion and scene-context analysis.
- **Modalities / available information:** RGB video, camera poses, COLMAP reconstructions, and 3D scene information.
- **Dataset family:** Geometric augmentation of EPIC-KITCHENS footage, with no additional independently recorded media.
- **Access evidence:** As of 2026-10-24: Open reconstruction-data instructions and code are listed in the official repository. RGB media must be obtained from EPIC-KITCHENS; downloading was not tested.
- **License observations:** The official README lists CC BY-NC 4.0. Upstream video retains EPIC-KITCHENS release conditions; the statement does not establish terms for every third-party dependency.
- **Caveats:** The canonical mean is derived from the matching covered-video count and hours. Duration extrema for all 700 EPIC-KITCHENS-100 files cannot be transferred to this 671-video subset. Recovered camera geometry is not an affordance annotation, closed-loop simulator, or procedural-error label. Keep shared parent videos together across splits and avoid counting them twice.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EPIC Fields official code, reconstruction data, and license](https://github.com/epic-kitchens/epic-fields-code)
- [EPIC Fields official Dataset and Benchmarks page](https://epic-kitchens.github.io/epic-fields/site)

---

<a id="epic-kitchens"></a>

## EGO-15 · EPIC-KITCHENS-100

**Core candidate** · **Year / version:** 2018; 100-hour version 2020/2021

Unscripted first-person recordings capture everyday kitchen activity and hand-object interactions. Temporal action intervals with verb-noun labels support action recognition, detection, and anticipation.

- **Duration:** Full video_id files range from 10.477133 to 3,708.04 seconds (approximately 0.174619-61.800667 minutes), with a mean of 514.429917 seconds (approximately 8.573832 minutes). These statistics were computed from the 700 duration values, in seconds, in official EPIC_100_video_info.csv metadata; they do not measure completion times of individual recipes or sessions.
- **Collection size:** 700 file durations sum to 360,100.941686 seconds (approximately 100.028039 hours), rounded to 100 hours in official descriptions. Collection spans 45 kitchens with approximately 89.9K actions. Annotated action-interval totals are separate; the 55-hour and 100-hour versions must not be added.
- **Potential applications:** Action recognition; Temporal action detection; Action anticipation.
- **Modalities / available information:** Egocentric RGB/audio and textual action annotations with verb-noun categories.
- **Dataset family:** EPIC-KITCHENS parent collection for EPIC Fields and part of first-generation EgoPlan; HD-EPIC is a separate collection.
- **Access evidence:** As of 2026-10-24: Open download entry points are provided by the team. Full-media downloading and availability were not verified.
- **License observations:** The first-generation EgoPlan paper identifies the EPIC-KITCHENS data it uses as CC BY-NC 4.0. Conditions of the selected release package still require confirmation.
- **Caveats:** The audit computed official CSV durations and checked their units but did not measure media with ffprobe. Recording boundaries need not coincide with recipe boundaries. Goal and step dependencies require additional mapping; unscripted activity is not verified error ground truth. VISOR and Fields add separate annotations to shared footage and must not add duplicate video hours.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EPIC team description of EPIC-KITCHENS-100 on the HD-EPIC site](https://hd-epic.github.io/)
- [EgoPlan paper: upstream EPIC-KITCHENS use and licensing](https://arxiv.org/html/2312.06722v3)
- [EPIC-KITCHENS-100 official annotation README: duration units](https://github.com/epic-kitchens/epic-kitchens-100-annotations)
- [EPIC_100_video_info.csv: official per-video duration metadata](https://raw.githubusercontent.com/epic-kitchens/epic-kitchens-100-annotations/master/EPIC_100_video_info.csv)

---

<a id="howto100m"></a>

## EGO-16 · HowTo100M

**Auxiliary** · **Year / version:** ICCV 2019

Internet instructional videos span cooking, crafts, personal care, gardening, fitness, and other narrated activities. Automatically obtained captions provide large-scale weak supervision for video-language learning.

- **Duration:** Minimum, maximum, and mean duration of full YouTube source videos are unknown. The duration distribution of caption-linked training clips was also not verified; 1.2M source videos and 136M captioned clips are different units.
- **Collection size:** Official description: approximately 15 years of video, 1.2M source videos, 136M captioned clips, and 23K activities. Whether the 15-year figure denotes deduplicated full-source duration or cumulative captioned-clip duration was not established, so it cannot support a source-video or clip mean.
- **Potential applications:** Video-text pretraining; Text-to-video retrieval; Weakly supervised instructional understanding.
- **Modalities / available information:** Web video, automatically obtained captions/narration, and precomputed features.
- **Dataset family:** Parent web-video collection for HT-Step and other derivatives; deduplicate overlap using YouTube IDs.
- **Access evidence:** As of 2026-10-24: Links only for source media; the official site lists data, README, and feature entry points, with video obtained from YouTube. Full-media availability and downloading were not tested.
- **License observations:** Dataset and media rights were not verified. Original video rights and platform conditions cannot be replaced by a pretraining-code license.
- **Caveats:** The audit confirms published scale but leaves the meaning of the total duration unresolved. Do not present 15 years as verified deduplicated full-session time, or 136M clips as complete tasks. Captions are weakly aligned, tutorials may be edited, and source links may expire. Dense manual step boundaries, dependency graphs, and failure labels are not available across the full collection.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [HowTo100M official project: scale and data access](https://www.di.ens.fr/willow/research/howto100m/)

---

<a id="ht-step"></a>

## EGO-17 · HT-Step

**Core candidate** · **Year / version:** NeurIPS 2023

A cooking-video subset of HowTo100M is aligned with procedural steps mined from wikiHow articles. Temporal intervals and a step taxonomy support grounding written instructions in video.

- **Duration:** Minimum and maximum duration of selected full source videos are unknown. Approximately 2,100 hours / approximately 20,000 videos implies a rough mean of 6.3 minutes, not an exact sample mean. The distribution of individual step-interval durations is unknown.
- **Collection size:** Approximately 20K HowTo100M source videos and 2.1K video hours, with 116K annotated step intervals and 4,958 step classes. Cumulative interval duration is unknown; 2.1K hours does not mean annotated foreground duration and cannot be added to the parent collection.
- **Potential applications:** Temporal grounding of article steps; Instruction-video alignment; Derived step-progress tracking.
- **Modalities / available information:** Video, narration, wikiHow procedural text, step classes, and temporal intervals.
- **Dataset family:** Annotations on a HowTo100M subset, with a taxonomy mined from wikiHow; no additional recorded footage.
- **Access evidence:** As of 2026-10-24: Open annotations, taxonomy, splits, and evaluation scripts are provided in the official repository. Source videos inherit HowTo100M/YouTube access constraints; media downloading was not tested.
- **License observations:** Annotations are explicitly CC BY-NC 4.0; evaluation code is MIT. Upstream video and wikiHow text retain their respective rights.
- **Caveats:** The canonical mean is a rough derivation from matching approximate source-video totals and does not extend to all HowTo100M videos. Annotation counts do not establish annotated duration. Article steps may differ from valid real executions; an absent article step is not automatically an omission error, and article order is not a verified unique dependency graph. Future-step and causal tasks need separate protocols.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [HT-Step official project: dataset scale and units](https://facebookresearch.github.io/htstep/)
- [HT-Step official annotations, splits, evaluation, and component licenses](https://github.com/facebookresearch/htstep)

---

<a id="youcook2"></a>

## EGO-18 · YouCook2

**Comparison** · **Year / version:** 2017/2018

Web cooking tutorials cover many recipes, mostly through third-person views and edited sequences. Human annotators mark procedure segments and write imperative step descriptions, with a second annotator reviewing the labels.

- **Duration:** Collected full videos have an approximate maximum of 10 minutes and a mean of 5.27 minutes; the minimum is unknown. Step segments range from 1 to 264 seconds and average 19.6 seconds; these are separate duration units.
- **Collection size:** 2,000 videos across 89 recipe classes, totaling 175.6 hours (approximately 176 hours when rounded in the abstract). Cumulative step-segment duration was not recalculated; source-video hours are not annotated-foreground hours.
- **Potential applications:** Temporal step localization; Procedural video description.
- **Modalities / available information:** Web video and English step descriptions with temporal boundaries.
- **Dataset family:** YouCook2 web instructional-video collection; original source IDs are relevant for overlap checks.
- **Access evidence:** As of 2026-10-24: Links only for source media; official materials provide data entry points, but downloadable-media coverage and downloading were not tested.
- **License observations:** The data license was not verified. An arXiv or download-script license does not establish dataset terms.
- **Caveats:** The audit confirms the 5.27-minute mean and approximate 10-minute maximum, with no evidence for a 3-minute lower bound. Untrimmed describes the collected file unit and does not guarantee continuous filming. Edited tutorials may omit state transitions; next-step, dependency, and error tasks require derived annotations and should not be treated as native failure supervision.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [YouCook2 paper: Towards Automatic Learning of Procedures from Web Instructional Videos, Statistics and Splits](https://arxiv.org/html/1703.09788)
