# Robotics and Embodied Interaction

[Back to the collection](../README.md) · [Duration methodology](../docs/methodology.md) · [JSON data](../data/datasets.json)

Real and simulated robot episodes, demonstrations, manipulation, planning, and recovery.

**15 records.** Suggested applications are editorial research directions; consult annotations and caveats before assuming native task support.

## Contents

- [ROB-01 · BEHAVIOR-1K / 2025 Challenge Demonstrations](#behavior-1k)
- [ROB-02 · RH20T-P / RH20T](#rh20t-p)
- [ROB-03 · RoboFail / REFLECT](#robofail-reflect)
- [ROB-04 · TEACh](#teach)
- [ROB-05 · ALFRED](#alfred)
- [ROB-06 · BridgeData V2](#bridgedata-v2)
- [ROB-07 · CALVIN](#calvin)
- [ROB-08 · DROID](#droid)
- [ROB-09 · EgoTV](#egotv)
- [ROB-10 · LIBERO / LIBERO-Long](#libero)
- [ROB-11 · Open X-Embodiment / RT-X](#open-x-embodiment)
- [ROB-12 · RoboCasa / RoboCasa365](#robocasa365)
- [ROB-13 · RoboSet](#roboset)
- [ROB-14 · RoboVQA](#robovqa)
- [ROB-15 · Mobile ALOHA](#mobile-aloha)

---

<a id="behavior-1k"></a>

## ROB-01 · BEHAVIOR-1K / 2025 Challenge Demonstrations

**Core candidate** · **Year / version:** 2022 onward; demonstrations released in 2025

Simulated household demonstrations cover multistep cleaning, organizing, and cooking with object state changes. The 2025 Challenge release contains 10,000 episodes across 50 tasks, with synchronized video streams and robot actions and states for studying task progress and action prediction.

- **Duration:** Complete 2025 Challenge episodes: minimum and maximum unknown; mean approximately 396.98 seconds (6.62 minutes), derived as 119,094,660 frames / 30 fps / 10,000 episodes.
- **Collection size:** Approximately 1,102.73 hours, derived as 119,094,660 / 30 / 3,600; each episode timeline counted once.
- **Potential applications:** Task progress estimation with added step labels; Robot state tracking; Action prediction from demonstrations; Visual reasoning about multistep household tasks.
- **Modalities / available information:** LeRobot-format actions, observation.state, synchronized multiview video including RGB and depth/segmentation-related streams, episode metadata, and Parquet tables; complete semantic object predicates require simulator definitions or additional export.
- **Dataset family:** BEHAVIOR / OmniGibson
- **Access evidence:** As of 2026-10-24: Open release documented by the official Hugging Face dataset card, including MP4 path templates, Parquet tables, and metadata. Dataset downloads and playback were not tested.
- **License observations:** The 2025-challenge-demos dataset card specifies MIT for this release. Simulator, scene, and third-party asset terms require separate checks; MIT does not establish a license for the entire BEHAVIOR/OmniGibson family.
- **Caveats:** The minute-scale mean and multistep tasks do not establish that every episode is long. The 90,000 video files are multiple views/modalities of the same episodes, not 90,000 independent episodes; do not multiply total hours by nine. The dataset card and meta/info.json report 10,000 episodes, 119,094,660 temporal frames, 90,000 videos, 30 fps, and 50 tasks. The 1,000-task universe is larger than this demonstration release. Episode success rates and full semantic state coverage remain unverified; successful simulated demonstrations do not establish real failure or recovery labels.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [BEHAVIOR official project](https://behavior.stanford.edu/)
- [BEHAVIOR-1K official repository](https://github.com/StanfordVL/BEHAVIOR-1K)
- [BEHAVIOR 2025 Challenge dataset card and temporal metadata](https://huggingface.co/datasets/behavior-1k/2025-challenge-demos)

---

<a id="rh20t-p"></a>

## ROB-02 · RH20T-P / RH20T

**Core candidate** · **Year / version:** 2024; parent RH20T released in 2023

RH20T-P segments real robot manipulation episodes into labeled primitives with temporal boundaries and object-related information. Linking these annotations to parent RH20T trajectories supports step recognition and next-primitive prediction across contact-rich manipulation tasks.

- **Duration:** RH20T-P primitive clips: minimum, maximum, mean, and typical duration unknown. Complete parent RH20T episodes: minimum, maximum, and mean unknown.
- **Collection size:** RH20T-P clip hours unknown; parent RH20T total hours were not verified in the duration audit.
- **Potential applications:** Temporal primitive recognition; Next-primitive prediction within episodes; Sensor-conditioned manipulation analysis; Step tracking after alignment to parent trajectories.
- **Modalities / available information:** Parent RH20T includes multiview RGB/RGB-D, robot actions and proprioception, force-related signals, and tactile data or human demonstrations in some configurations; RH20T-P adds primitive labels, frame boundaries, object slots, and spatial information.
- **Dataset family:** RH20T
- **Access evidence:** As of 2026-10-24: Open links documented for parent RH20T at multiple resolutions and RH20T-P annotations on Google Drive; parent episode ID alignment was not tested. Dataset downloads and playback were not tested.
- **License observations:** Parent scenes 0001-0005 specify CC BY-SA 4.0. For scenes 0006-0010, the text says CC BY-NC 4.0 but links to CC BY-NC-SA 4.0 and requires noncommercial use; publisher clarification is needed. A separate RH20T-P annotation license is unverified. The paper footnote describing the parent as MIT does not override the official partition terms.
- **Caveats:** The short-clip characterization refers to primitive granularity, not a verified duration threshold. Recover elapsed time using parent episode IDs, start/end frames, and the corresponding frame rate; primitive counts are not complete-task counts. The project reports about 33,000 clips across 44 tasks, while the paper reports about 38,000 clips across 67 tasks; these versions have not been aligned to a release manifest. Neither count provides duration. Long episodes and failure-cause or recovery labels remain unverified.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [RH20T official project and partition licenses](https://rh20t.github.io/)
- [RH20T-P official project: primitive annotation boundaries](https://sites.google.com/view/rh20t-primitive/main)
- [RH20T-P paper](https://arxiv.org/abs/2403.19622)
- [RH20T-P annotation access instructions](https://github.com/Zx55/cga-challenge/tree/main/data/rh20tp)

---

<a id="robofail-reflect"></a>

## ROB-03 · RoboFail / REFLECT

**Core candidate** · **Year / version:** 2023

RoboFail evaluates failure localization, explanation, and corrective planning in multistep kitchen tasks. The original REFLECT study separates 100 injected AI2-THOR failure scenarios from 30 controlled real UR5e scenarios, allowing analysis of errors whose causes precede the final failure.

- **Duration:** Complete failed executions: minimum, maximum, mean, and typical duration unknown. An official example marks a failure at 05:24, establishing at least 5 minutes 24 seconds of observed history for that example, not its video endpoint or the dataset maximum.
- **Collection size:** Total real-robot and simulated failure-video hours are both unknown.
- **Potential applications:** Failure localization; Failure explanation; Corrective plan evaluation; Historical root-cause analysis.
- **Modalities / available information:** Simulated RGB-D, robot state, and ground-truth metadata; real UR5e teleoperation with RGB-D observations. Simulated ground-truth fields must not be assumed available for real recordings.
- **Dataset family:** REFLECT / RoboFail
- **Access evidence:** As of 2026-10-24: Links only: the project data endpoint returned HTTP 403 during the original check; the official repository separately links a real-world dataset on Google Drive and a notebook for generating simulated failures. Full video, label, recovery-trajectory, and simulated-release coverage remain unverified. Dataset downloads and playback were not tested.
- **License observations:** The REFLECT software repository is MIT. Independent licenses for the original real and simulated RoboFail data packages were not verified; neither software MIT nor a later AHA license establishes redistribution rights for these data.
- **Caveats:** Minute-scale multistep failures are demonstrated, but not every record is known to be long. Keep real UR5e cases, AI2-THOR simulations, keyframe summaries, and complete execution histories separate. Official failure timestamps include 05:24 for serving a microwaved potato and other examples at 02:22 and 03:47; these are lower bounds on observed history, not complete video durations. The 30 real scenarios span 11 tasks and are controlled teleoperated failures; the 100 simulated scenarios span 10 tasks with injected failures. Corrective success rates and generated explanations do not establish released recovery videos or human ground-truth labels.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [REFLECT paper: failure explanation and correction](https://arxiv.org/abs/2306.15724)
- [REFLECT official project: real-world results and failure timestamps](https://robot-reflect.github.io/)
- [REFLECT official repository and real-data links](https://github.com/columbia-ai-robotics/reflect)
- [REFLECT MIT software license](https://github.com/columbia-ai-robotics/reflect/blob/main/LICENSE)

---

<a id="teach"></a>

## ROB-04 · TEACh

**Core candidate** · **Year / version:** 2021 onward; updated in 2022

TEACh records Commander-Follower dialogue and actions while people complete household tasks in AI2-THOR. Task configurations and execution histories support instruction following, dialogue-conditioned action prediction, and reasoning about previously completed subgoals.

- **Duration:** Complete gameplay or Trajectory from Dialogue (TfD) episodes: minimum, maximum, mean, and typical duration unknown. Local Execution from Dialogue History (EDH) instances: minimum, maximum, and mean also unknown.
- **Collection size:** Total video hours unknown.
- **Potential applications:** Dialogue-conditioned action prediction; Task state tracking; Instruction following; Analysis of corrections and clarification in dialogue.
- **Modalities / available information:** Simulated egocentric images, dialogue and action events, task configurations, and state-change information; human participation in dialogue does not make the imagery real-world footage.
- **Dataset family:** AI2-THOR / TEACh
- **Access evidence:** As of 2026-10-24: Open: the official teach_download tool provides all_games, experiment_games, and evaluation-instance packages. Image/action logs can be used to generate offline replay videos. Dataset downloads and playback were not tested.
- **License observations:** Code and model weights: MIT. Images: Apache 2.0 under IMAGESLICENSE. Other data: CDLA-Sharing 1.0 under DATALICENSE.
- **Caveats:** Action counts, human interaction time, and rendered replay duration measure different quantities; do not convert action counts directly to seconds. EDH instances are local histories, not independent complete-task videos. The official repository separates gameplay, EDH, and TfD files and supports saving timestep observations and generating videos with --create_video; game and instance files were revised on 2022-12-28. No per-video duration distribution was verified. Dialogue can expose answers, and simulated corrections do not establish real-robot failure or recovery ground truth.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [TEACh official repository: data, licenses, and episode replay](https://github.com/alexa/teach)

---

<a id="alfred"></a>

## ROB-05 · ALFRED

**Comparison** · **Year / version:** 2020

ALFRED pairs natural-language household instructions with expert action sequences and egocentric observations in AI2-THOR. Tasks combine navigation, object handling, and irreversible state changes such as heating or cleaning, supporting instruction following and subgoal reasoning.

- **Duration:** Complete task rollouts or demonstration videos: minimum, maximum, mean, and typical duration unknown. Duration statistics for action and subtask clips are also unknown.
- **Collection size:** Total video hours unknown.
- **Potential applications:** Language-conditioned action prediction; Subgoal and step recognition from trajectory alignment; Object state reasoning; Instruction-following evaluation.
- **Modalities / available information:** Simulated RGB images and video.mp4, traj_data.json, high- and low-level actions/plans, language, PDDL states, and ResNet features in Full Dataset 2.1.0; Lite and Modeling packages do not include the same modalities.
- **Dataset family:** AI2-THOR / ALFRED
- **Access evidence:** As of 2026-10-24: Open links: the official data README describes the approximately 109 GB Full Dataset 2.1.0 with trajectory JSON, raw images, PDDL states, videos, and features; Lite and Modeling alternatives are also listed. Dataset downloads and playback were not tested.
- **License observations:** The repository README specifies MIT. Independent authorization for raw images, assets, and data packages was not verified; underlying AI2-THOR asset terms require separate consideration.
- **Caveats:** Long-horizon here denotes composed actions and irreversible state changes, not verified long continuous real-world recordings. Rendering frame rates and action counts do not establish real execution time; no usable duration range or mean was reported on the checked project page. Navigation can dominate the footage, task templates are limited, and expert plans do not provide real error-recovery histories.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [ALFRED official project](https://askforalfred.com/)
- [ALFRED official repository and data access](https://github.com/askforalfred/alfred)
- [ALFRED Full Dataset 2.1.0: videos, formats, and action alignment](https://github.com/askforalfred/alfred/blob/master/data/README.md)

---

<a id="bridgedata-v2"></a>

## ROB-06 · BridgeData V2

**Auxiliary** · **Year / version:** 2023

BridgeData V2 contains real robot trajectories for tabletop manipulation, kitchen and sink interactions, and object organization. Language-labeled trajectories and robot actions support language-conditioned manipulation and action prediction across varied scenes.

- **Duration:** Individual trajectories: minimum, maximum, mean, and typical duration unknown.
- **Collection size:** Total hours unknown; trajectory counts do not establish recording hours.
- **Potential applications:** Language-conditioned action prediction; Trajectory-level task recognition; Visual manipulation representation learning.
- **Modalities / available information:** Multiview RGB available as JPEG frames, robot observations and actions, and language; camera and depth availability vary.
- **Dataset family:** BridgeData
- **Access evidence:** As of 2026-10-24: Open: the official page provides JPEG data links, training code, and a trajectory viewer. Dataset downloads and playback were not tested.
- **License observations:** The official project specifies CC BY 4.0 for all data. Code licenses must be checked in the relevant repositories.
- **Caveats:** The official project reports 60,096 trajectories spanning teleoperation and scripted collection, with trajectory-level language labels. Mostly basic manipulation and some more complex tasks do not establish that all trajectories are short or long; reliable duration statistics remain unknown. Keep collection modes and synchronized camera views separate, and account for 2x-speed evaluation demonstrations. Concatenating independent episodes changes state continuity and does not establish naturally continuous long-horizon activity or failure histories.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [BridgeData V2 official project: dataset composition and evaluation videos](https://rail-berkeley.github.io/bridgedata/)
- [BridgeData V2 paper](https://arxiv.org/abs/2308.12952)

---

<a id="calvin"></a>

## ROB-07 · CALVIN

**Core candidate** · **Year / version:** 2022

CALVIN records simulated robot play with drawers, sliding doors, switches, lights, and objects across four environment layouts. Scene states, actions, and partially language-labeled intervals support language-conditioned control and evaluation of sequential task chains.

- **Duration:** Relabeled goal-conditioned training windows span 1-2 seconds, as reported in the paper; their mean is unknown. Minimum, maximum, and mean durations of original continuous play sessions, language-annotated clips, and evaluation task chains are each unknown.
- **Collection size:** 24 hours of original play data, approximately 6 hours per environment across 4 environments. Overlapping training windows do not add recording hours.
- **Potential applications:** Language-conditioned robot control; Sequential instruction execution; Robot and scene state tracking; Action prediction from play.
- **Modalities / available information:** Simulated RGB, robot and scene states, actions, episode frame data, and language-labeled intervals; exact modality coverage depends on the data version.
- **Dataset family:** CALVIN
- **Access evidence:** As of 2026-10-24: Open: the official dataset README links D, ABC, ABCD, and debug packages with checksums; frame observations can be converted into offline videos. Dataset downloads and playback were not tested.
- **License observations:** Repository MIT applies explicitly to software. A separate data license was not verified, so redistribution rights for all recordings are unconfirmed.
- **Caveats:** Continuous play sequences and second-scale training windows are different units; compositional task-chain evaluation does not make each training sample a long video. Paper section III-B.1 reports 24 hours and 1-2-second relabeled windows, while the dataset README reports about 6 hours per environment. Play is not necessarily a successful procedure, and language labels cover only some intervals. Pin a corrected release and its checksums because language annotations and scene_info have been revised. Failure and recovery evaluation requires additional trajectories or labels.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [CALVIN official repository](https://github.com/mees/calvin)
- [CALVIN official dataset README: layout, downloads, and hours](https://github.com/mees/calvin/blob/main/dataset/README.md)
- [CALVIN MIT software license](https://github.com/mees/calvin/blob/main/LICENSE)
- [CALVIN paper: play data and relabeled training windows](https://arxiv.org/html/2112.03227)

---

<a id="droid"></a>

## ROB-08 · DROID

**Auxiliary** · **Year / version:** 2024

DROID collects real Franka robot demonstrations in homes, offices, and other varied environments. Multiview observations, language, and robot actions support general manipulation learning, with collector-provided outcomes offering a limited basis for success analysis.

- **Duration:** Complete demonstration trajectories: minimum and maximum unknown; mean approximately 16.58 seconds, derived as 350 hours * 3,600 / 76,000 trajectories using approximate source totals.
- **Collection size:** 350 hours of interaction data, as reported by the official project.
- **Potential applications:** Language-conditioned action prediction; General manipulation learning; Trajectory outcome analysis; Robot state tracking.
- **Modalities / available information:** Real multiview RGB, raw camera recordings and robot trajectories; RLDS packages include images, language, actions, and proprioception. Raw stereo/depth coverage differs from compressed RLDS coverage.
- **Dataset family:** DROID
- **Access evidence:** As of 2026-10-24: Open: official documentation provides Google Cloud paths and examples for raw and RLDS data; correspondence of failed trajectories across the two versions remains unverified. Dataset downloads and playback were not tested.
- **License observations:** The paper specifies CC BY 4.0 for data. Code licenses require separate repository checks.
- **Caveats:** The short-trajectory characterization is based on an aggregate mean of roughly seventeen seconds, not a claim that every trajectory is short. The official abstract reports 76,000 trajectories and 350 hours together; synchronized views must not be counted as extra time. Fine-grained step labels and semantic object states require additional work. Outcome labels do not establish failure causes or recovery supervision, and demonstrated actions are not necessarily optimal next decisions.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [DROID official project: trajectory and interaction-hour totals](https://droid-dataset.github.io/)
- [DROID official data formats and access documentation](https://droid-dataset.github.io/droid/the-droid-dataset.html)
- [DROID paper](https://arxiv.org/abs/2403.12945)

---

<a id="egotv"></a>

## ROB-09 · EgoTV

**Comparison** · **Year / version:** 2023

EgoTV evaluates whether simulated egocentric household videos satisfy natural-language task descriptions. ALFRED-derived trials combine video, trajectories, and symbolic states to study task verification and generalization to new step combinations and environments.

- **Duration:** Individual trials or video.mp4 files: minimum, maximum, mean, and typical duration unknown.
- **Collection size:** Total video hours unknown.
- **Potential applications:** Egocentric task verification; Compositional generalization; Task-order and state-change reasoning.
- **Modalities / available information:** Simulated egocentric video, natural-language tasks, trajectory JSON, and PDDL states; the primary task is offline verification.
- **Dataset family:** AI2-THOR / ALFRED-derived generation
- **Access evidence:** As of 2026-10-24: Open code and sample entry points: the repository documents video directories, an example notebook, and generation instructions; availability of the complete pregenerated release was not fully verified. Dataset downloads and playback were not tested.
- **License observations:** The official repository LICENSE specifies CC BY-NC 4.0. Inherited components, underlying assets, and any additional data-package terms require separate checks.
- **Caveats:** Multistep task verification does not establish long video duration. Keep generated trials separate from model-sampled clips, and do not convert ALFRED action counts into video seconds. The repository places video.mp4 and traj_data.json in each trial and documents ALFRED-based generation, but usable duration statistics were not verified. A failed task-description match does not necessarily represent a physical execution failure; task verification also does not establish optimal next-action supervision.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [EgoTV official repository: trial structure and generation](https://github.com/facebookresearch/EgoTV)
- [EgoTV CC BY-NC 4.0 license](https://github.com/facebookresearch/EgoTV/blob/main/LICENSE)
- [EgoTV ICCV 2023 paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Hazra_EgoTV_Egocentric_Task_Verification_from_Natural_Language_Task_Descriptions_ICCV_2023_paper.pdf)

---

<a id="libero"></a>

## ROB-10 · LIBERO / LIBERO-Long

**Comparison** · **Year / version:** 2023

LIBERO provides simulated manipulation suites for lifelong learning across spatial, object, goal, and task-composition variations. Demonstrations, language, and executable task definitions support transfer learning and action prediction, including the LIBERO-Long suite.

- **Duration:** Individual demonstrations or episodes, including LIBERO-Long: minimum, maximum, mean, and typical duration unknown.
- **Collection size:** Total video or simulated demonstration hours unknown.
- **Potential applications:** Lifelong robot learning; Language-conditioned manipulation; Task transfer evaluation; Action prediction from demonstrations.
- **Modalities / available information:** Simulated RGB, robot actions and states, task language, BDDL task definitions, and demonstration trajectory packages.
- **Dataset family:** LIBERO
- **Access evidence:** As of 2026-10-24: Open: official scripts support suite downloads and an official README-linked Hugging Face mirror; offline observations or fixed-version renders can be used. Dataset downloads and playback were not tested.
- **License observations:** The official README license table specifies MIT for code and CC BY 4.0 for datasets.
- **Caveats:** The LIBERO-Long name does not establish video duration. Simulation action horizons, control frequencies, and exported video frame rates require separate alignment; do not infer seconds from step counts or describe the whole suite as long video. The checked official README did not report usable episode duration ranges or means. Repackaging and removal of stationary frames can alter timing, so pin the source and preprocessing. Demonstrations provide feasible actions rather than uniquely optimal decisions; failure evaluation requires additional rollouts.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [LIBERO official repository: suites, data, and licenses](https://github.com/Lifelong-Robot-Learning/LIBERO)
- [LIBERO dataset mirror linked by the official README](https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets)

---

<a id="open-x-embodiment"></a>

## ROB-11 · Open X-Embodiment / RT-X

**Auxiliary** · **Year / version:** 2023

Open X-Embodiment aggregates existing robot datasets across institutions, embodiments, and manipulation settings. Its RLDS episode and step interface supports cross-dataset action learning while retaining source-specific observation fields and collection protocols.

- **Duration:** A single collection-wide sample duration is not applicable. Source-specific minimum, maximum, and mean durations were not audited individually and remain unknown.
- **Collection size:** A deduplicated collection-wide total in hours is unknown; source datasets, mirrors, and derived versions must not simply be added together.
- **Potential applications:** Cross-embodiment action learning; Robot policy transfer; Source-specific manipulation analysis.
- **Modalities / available information:** RLDS episodes and steps with source-dependent RGB, actions, language, and proprioceptive states; fields and sampling rates are not uniform across datasets.
- **Dataset family:** Cross-dataset robotics collection, including BridgeData
- **Access evidence:** As of 2026-10-24: Open entry points: the official repository documents RLDS access, source dataset listings, and usage guides. Availability and access conditions vary by source. Dataset downloads and playback were not tested.
- **License observations:** The repository specifies Apache 2.0 for software and CC BY 4.0 for other included materials. These terms do not override external source-data licenses; attribution and derivative redistribution conditions must be checked per source.
- **Caveats:** The official dataset overview describes a collection of 60 existing datasets spanning multiple robot embodiments, not a single video corpus with a common collection protocol. Audit episode definitions, sampling/control frequencies, duration, and continuity per source; never substitute a single range or mean for the whole collection. Source versions, field semantics, duplicate samples, and recording-domain leakage require attention. No unified failure-cause or recovery annotation system is established.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Open X-Embodiment official project: source dataset overview](https://robotics-transformer-x.github.io/)
- [Open X-Embodiment official repository](https://github.com/google-deepmind/open_x_embodiment)

---

<a id="robocasa365"></a>

## ROB-12 · RoboCasa / RoboCasa365

**Core candidate** · **Year / version:** 2024; RoboCasa365 released in 2026

RoboCasa provides simulated kitchen tasks involving cooking, cleaning, storage, appliances, and containers. RoboCasa365 combines human demonstrations and synthetic trajectories for studying robot control, task composition, and simulator-grounded state reasoning.

- **Duration:** RoboCasa365 human demonstrations: most last 10-60 seconds, with a long tail exceeding 3 minutes; this is a typical distribution, not the minimum-maximum range, which remains unknown. Human-demonstration mean approximately 40.06 seconds, derived as (404 + 208) hours * 3,600 / 55,000 episodes. Synthetic-demonstration and earlier RoboCasa duration ranges and means are unknown.
- **Collection size:** RoboCasa365 reports 404 hours of human pretraining, 208 hours of human target-task data, and 1,615 hours of synthetic pretraining; their sum is 2,227 hours.
- **Potential applications:** Multistep kitchen manipulation; Task progress estimation in annotated subsets; Simulator-grounded state reasoning; Action prediction and closed-loop policy evaluation.
- **Modalities / available information:** Simulated observations or rendered RGB, robot actions, simulator states, and task definitions; some data may be state trajectories requiring rendering rather than packaged MP4 video.
- **Dataset family:** RoboCasa
- **Access evidence:** As of 2026-10-24: Open: official code and documentation provide simulator, asset, and dataset entry points; offline video may use supplied images or fixed-version rendering. Package formats were not verified through downloads. Dataset downloads and playback were not tested.
- **License observations:** The official repository specifies MIT for code and CC BY 4.0 for assets and datasets; separately licensed included assets retain their own terms.
- **Caveats:** The typical 10-60-second description applies only to the 55,000 human demonstrations, not hard bounds or the synthetic and earlier RoboCasa releases. Paper section 3.4.3 reports the three hour totals, the human episode count, and a tail beyond 3 minutes. Evaluation horizon limits are not training-video lengths. Keep 2024 and 2026 statistics separate, and do not equate simulator control scores with video-understanding scores. Successful simulated demonstrations do not supply real failure or recovery ground truth.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [RoboCasa official project and 2026 release updates](https://robocasa.ai/)
- [RoboCasa official repository and licenses](https://github.com/robocasa/robocasa)
- [RoboCasa365 paper](https://arxiv.org/abs/2603.04356)
- [RoboCasa365 paper: section 3.4.3 dataset statistics](https://arxiv.org/html/2603.04356)

---

<a id="roboset"></a>

## ROB-13 · RoboSet

**Auxiliary** · **Year / version:** 2023

RoboSet organizes real everyday manipulation data into semantic activities containing several tasks. Teleoperation and kinesthetic playback trajectories provide synchronized camera observations and robot signals for action learning and task-level analysis.

- **Duration:** Individual trajectories or trials: minimum, maximum, mean, and typical duration unknown. Durations of complete multitask activity sequences are also unknown.
- **Collection size:** Total recording hours unknown.
- **Potential applications:** Robot action prediction; Task-level manipulation recognition; Analysis of teleoperation and kinesthetic playback.
- **Modalities / available information:** Multicamera images and robot observations/actions stored in trial-level HDF5 groups including data, derived, and config; derived fields require subset-specific inspection.
- **Dataset family:** RoboSet / RoboPen
- **Access evidence:** As of 2026-10-24: Open links: the official site provides teleoperation, kinesthetic, and autonomous data entry points with HDF5 reading examples. Dataset downloads and playback were not tested.
- **License observations:** The project page links MIT for "This work," but its applicability to specific data packages was not independently confirmed. Redistribution permission for all images and trajectories remains unverified.
- **Caveats:** Four synchronized cameras observe the same trial and do not lengthen its timeline. Activities containing 4-6 tasks do not establish that each trajectory records a whole activity. The official composition is 28,500 trajectories: 9,500 teleoperated and 19,000 kinesthetic playback trajectories, with four views per frame; these counts are not duration statistics. Do not construct purported continuous activities by joining independent trials. Names of derived fields do not establish state/success ground truth, and playback collection does not establish failures.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [RoboSet official project: dataset composition](https://robopen.github.io/roboset/)
- [RoboSet teleoperation data documentation](https://robopen.github.io/roboset/teleoperation.html)

---

<a id="robovqa"></a>

## ROB-14 · RoboVQA

**Comparison** · **Year / version:** 2023 / 2024

RoboVQA pairs real office-task videos with language questions about progress, intermediate steps, and high-level planning. Its robot, human, and human-with-gripper embodiments support visual task reasoning across different ways of carrying out similar goals.

- **Duration:** Original long-horizon episodes have a reported mean of 102 seconds; segmented medium-horizon episodes have a reported mean of 14 seconds. Minimum and maximum durations are unknown for both units, and the dataset-wide range of VQA input-window lengths is unknown.
- **Collection size:** 238 hours of video reported by the paper/project; reused complete episodes, segments, and VQA pairs must not be added together.
- **Potential applications:** Visual question answering about task progress; Intermediate-step recognition; High-level planning questions; Cross-embodiment task reasoning.
- **Modalities / available information:** Real RGB video, task instructions, and multiround language questions and answers across embodiments; public continuous robot-control actions and complete environment-state vectors were not verified.
- **Dataset family:** RoboVQA
- **Access evidence:** As of 2026-10-24: Open entry points: official Cloud Storage links and the official repository are public, with a Hugging Face mirror linked from the project. Coverage of original full videos and QA packages remains unverified. Dataset downloads and playback were not tested.
- **License observations:** The official repository specifies Apache 2.0 for software and CC BY 4.0 for other materials. Mirrors do not alter original terms; package-specific attribution and additional conditions must be retained.
- **Caveats:** Long-horizon denotes multistep tasks here: the mean complete episode is under two minutes, and medium-horizon segments average fourteen seconds. Paper section II reports 238 hours, 5,246 long-horizon episodes, 92,948 medium-horizon episodes, and the respective 102-second and 14-second means; Figure 1 describes retrospective segmentation. The 238-hour total does not reconcile directly with 5,246 * 102 seconds, so preserve the reported means instead of deriving a replacement. View-counting and reuse conventions remain unresolved. Published QA and intervention-rate experiments do not establish an interactive simulator, full control data, optimal counterfactual actions, or failure-cause labels.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [RoboVQA official project](https://robovqa.github.io/)
- [RoboVQA official repository and licenses](https://github.com/google-deepmind/robovqa)
- [RoboVQA paper](https://arxiv.org/abs/2311.00899)
- [RoboVQA paper: section II data and Figure 1](https://arxiv.org/html/2311.00899)

---

<a id="mobile-aloha"></a>

## ROB-15 · Mobile ALOHA

**Watchlist** · **Year / version:** 2024

Mobile ALOHA demonstrates real mobile bimanual manipulation involving cooking, cabinet interactions, storage, and other everyday tasks. Its training code exposes robot observations and actions useful for imitation learning, while complete public real-data coverage remains unverified.

- **Duration:** Complete mobile-manipulation demonstrations or episodes: minimum, maximum, mean, and typical duration unknown.
- **Collection size:** Total hours in the public data release are unknown. The paper uses 50 demonstrations per task as a training setting, not a recording-hour total.
- **Potential applications:** Mobile bimanual imitation learning, subject to data availability; Robot action prediction; Multistep manipulation analysis, subject to full-episode access.
- **Modalities / available information:** Real multicamera images, dual-arm joint observations, and actions; official HDF5 visualization code reads observations/qpos, qvel, images, and action. Public coverage of mobile-base actions is unverified.
- **Dataset family:** ALOHA
- **Access evidence:** As of 2026-10-24: Links only: the project and code are public, and HDF5 reading/writing and visualization entry points were checked. A complete public manifest of real Mobile ALOHA data was not verified; simulated demonstration links do not establish availability of the real mobile dataset. Dataset downloads and playback were not tested.
- **License observations:** Code and data permissions must be separated. An explicit license and complete release package for real Mobile ALOHA demonstrations were not verified; code licensing does not establish video redistribution rights.
- **Caveats:** Multistep mobile manipulation does not establish that every recording is long in elapsed time. The official abstract describes 50 demonstrations per task and examples including cooking, opening cabinets, and elevator use, but no usable episode duration distribution. Keep static ALOHA, Mobile ALOHA data, and edited project demonstrations separate. Project videos demonstrate behavior without establishing machine-readable labels or redistributable training data. Reported success rates do not establish released failure and recovery trajectories.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Mobile ALOHA official project](https://mobile-aloha.github.io/)
- [ACT++ official training repository](https://github.com/MarkFzp/act-plus-plus)
- [Mobile ALOHA HDF5 episode visualization source](https://github.com/MarkFzp/act-plus-plus/blob/main/visualize_episodes.py)
