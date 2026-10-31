# Industrial Assembly and Maintenance

[Back to the collection](../README.md) · [Duration methodology](../docs/methodology.md) · [JSON data](../data/datasets.json)

Assembly, disassembly, maintenance, tool use, and human-robot collaboration.

**11 records.** Suggested applications are editorial research directions; consult annotations and caveats before assuming native task support.

## Contents

- [IND-01 · Assembly101](#assembly101)
- [IND-02 · IndustReal](#industreal)
- [IND-03 · ENIGMA-51](#enigma51)
- [IND-04 · IMPACT](#impact-industrial)
- [IND-05 · IndEgo](#indego)
- [IND-06 · ATTACH](#attach)
- [IND-07 · HA-ViD](#havid)
- [IND-08 · HA4M](#ha4m)
- [IND-09 · IKEA ASM](#ikea-asm)
- [IND-10 · IPAD](#ipad)
- [IND-11 · MECCANO](#meccano)

---

<a id="assembly101"></a>

## IND-01 · Assembly101

**Core candidate** · **Year / version:** 2022

People disassemble and reassemble 101 types of toy vehicles without fixed step-by-step instructions. Synchronized egocentric and external views capture natural changes in action order, assembly mistakes, and rework.

- **Duration:** Mean sequence duration: 7.1 minutes, with a standard deviation of 3.4 minutes; minimum and maximum durations are unverified. Mean fine-grained action duration: 1.7 seconds; mean coarse-grained action duration: 16.5 seconds.
- **Collection size:** 362 independent sequences; 4,321 camera-view videos totaling 513 hours across views.
- **Potential applications:** Action recognition and temporal segmentation; Action anticipation; Mistake and observed correction detection; Cross-view process-state tracking (derived).
- **Modalities / available information:** Synchronized video from 8 fixed RGB cameras and 4 head-mounted grayscale cameras; camera calibration and 3D hand poses.
- **Dataset family:** Assembly101
- **Access evidence:** Links only, as checked on 2026-10-24: the official site announced migration to Hugging Face in May 2026; the download repository still contained older Google Drive tools. Account requirements and complete video downloads were not verified.
- **License observations:** Data and annotations: CC BY-NC 4.0, stated on the official site and annotation README. Open access does not authorize commercial redistribution.
- **Caveats:** The 7.1-minute mean and 3.4-minute standard deviation are not a minimum-to-maximum range. Count synchronized views once per independent execution and split by execution to avoid leakage. Mistake annotations cover 328 assembly sequences, not all 4,321 view videos. Some mistakes explicitly have no correction; observed rework does not establish an optimal repair policy. Recovery-pair coverage was not verified. README examples contain possible timestamp anomalies, but the full CSV files were not audited and cannot be assumed to share those anomalies. The tasks use toys.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Assembly101 official page](https://assembly-101.github.io/)
- [Assembly101 original paper, Section 3 and Figure 4](https://assembly-101.github.io/assets/Assembly101.pdf)
- [Assembly101 annotation README](https://raw.githubusercontent.com/assembly-101/assembly101-annotations/main/README.md)
- [Assembly101 mistake annotations and correction exceptions](https://github.com/assembly-101/assembly101-mistake-detection)
- [Assembly101 mistake detection README, raw text](https://raw.githubusercontent.com/assembly-101/assembly101-mistake-detection/main/README.md)
- [Assembly101 Hugging Face host linked by the official page](https://huggingface.co/datasets/cvml-nus/assembly101)

---

<a id="industreal"></a>

## IND-02 · IndustReal

**Core candidate** · **Year / version:** 2023 release / 2024 WACV

Participants assemble, maintain, and replace parts of a 3D-printed construction toy car in a controlled industrial-style setting. Egocentric recordings capture correct steps, omitted steps, and incorrect assembly with part-state and completion annotations.

- **Duration:** Minimum and maximum video durations are unverified. The mean is approximately 4.14 minutes, calculated from the reported 5.8 hours divided by 84 videos.
- **Collection size:** 84 videos totaling 5.8 hours; 27 participants. The project page rounds the duration to approximately 6 hours.
- **Potential applications:** Action recognition; Assembly-state detection; Correct and incorrect step completion recognition; Omission detection and process memory (derived).
- **Modalities / available information:** HoloLens 2 egocentric RGB, grayscale stereo, depth, hand and head poses, and gaze; 3D part geometry.
- **Dataset family:** IndustReal
- **Access evidence:** Links only, as checked on 2026-10-24: the official repository links a 4TU data record and records release on 2023-11-01. The 4TU page request timed out; downloads were not tested.
- **License observations:** The code repository has an Apache-2.0 license and its README broadly describes IndustReal as Apache-2.0. The 4TU data license was not verified, so that statement does not establish the final license for video and 3D assets.
- **Caveats:** The mean is derived from a dataset total and does not show that every video meets a long-duration threshold. The 38 incorrect completions are events, not 38 error classes; 35 videos contain omissions or incorrect completions, and 48 execution orders are reported. Natural and deliberately induced errors coexist, with their proportions unverified. Several execution errors appear only in validation/test, so preserve the original split. The dataset covers one toy product family and does not provide a validated optimal correction policy.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [IndustReal official repository](https://github.com/TimSchoonbeek/IndustReal)
- [IndustReal original paper, Table 1](https://arxiv.org/html/2310.17323)
- [IndustReal author project page](https://timschoonbeek.github.io/industreal.html)
- [IndustReal 4TU data record; page request timed out](https://data.4tu.nl/datasets/b008dd74-020d-4ea4-a8ba-7bb60769d224)

---

<a id="enigma51"></a>

## IND-03 · ENIGMA-51

**Core candidate** · **Year / version:** 2023 preprint / 2024 WACV

Participants repair circuit boards in a simulated industrial laboratory while following audio and augmented-reality guidance. Egocentric videos show interactions with oscilloscopes, power supplies, electric screwdrivers, and other repair tools across two procedures.

- **Duration:** Minimum and maximum video durations are unverified. The derived mean is approximately 25.9 minutes, using the official rounded total of 22 hours divided by 51 videos.
- **Collection size:** 51 egocentric videos totaling 22 hours; 19 participants and 2 repair procedures.
- **Potential applications:** Untrimmed hand-object interaction detection; Short-term object interaction anticipation; Natural-language understanding of repair interactions.
- **Modalities / available information:** HoloLens 2 RGB video, textual procedures, and environment/object 3D models; estimated hand keypoints and SAM-generated segmentation.
- **Dataset family:** ENIGMA-51
- **Access evidence:** Links only, as checked on 2026-10-24: the official page lists separate video, annotation, and textual-procedure download entries. File retrieval was not tested.
- **License observations:** The data license was not verified; paper or code licensing must not be substituted for a data license.
- **Caveats:** The derived mean relies on a rounded total and still needs per-video metadata verification; recording interruptions were not checked. Estimated hand keypoints and SAM masks are not manual ground truth. Repairing a faulty board does not establish supervision for operator mistakes or recovery. Procedure steps and acceptable part states require additional alignment, and the next object is not an optimal next repair action. Coverage is limited to two guided procedures and a single egocentric view.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [ENIGMA-51 official page and dataset statistics](https://fpv-iplab.github.io/ENIGMA-51/)
- [ENIGMA-51 official repository](https://github.com/fpv-iplab/ENIGMA-51)

---

<a id="impact-industrial"></a>

## IND-04 · IMPACT

**Core candidate** · **Year / version:** 2026

Participants assemble and disassemble a commercial angle grinder using professional tools in a controlled setting. Five synchronized views record multiple valid execution orders, assembly states, anomalies, and recovery actions.

- **Duration:** Minimum and maximum trial durations are unverified. The derived mean is approximately 4.3 minutes, using approximately 8 hours of independent execution time divided by 112 trials.
- **Collection size:** 112 trials by 13 participants; approximately 8 independent hours and 39.5 accumulated hours across 5 views.
- **Potential applications:** Step and assembly-state recognition; Anomaly classification and recovery-phase detection; Short-term action anticipation; Long-term action sequence prediction.
- **Modalities / available information:** 1 egocentric and 4 external RGB views; the release manifest lists depth for the 4 external views, egocentric audio and gaze, and features.
- **Dataset family:** IMPACT
- **Access evidence:** Links only, as checked on 2026-10-24: the official repository provides version 1.1 Google Drive and Hugging Face links, samples, and checksum manifests. Downloads and checksum validation were not run.
- **License observations:** Data assets and author documentation: CC BY-NC-SA 4.0, verified in LICENSE-DATA. Code, scripts, and configuration: Apache-2.0. Third-party or separately licensed files retain their own terms.
- **Caveats:** The five-view accumulated total cannot be divided by 112 to obtain trial duration; the approximately 8 independent hours are rounded. The data cover one product family in a controlled setting. The proportion of spontaneous versus deliberately induced anomalies was not verified. The manifest does not establish egocentric depth availability. Prediction of observed future actions is not an optimal decision policy. Version 1.1 reflects a July 2026 revision. As of 2026-10-24, the manuscript was marked under review and the listed November 2026 conference was still in the future, so conference publication was not confirmed.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [IMPACT manuscript v1, Table 1 and Section 3](https://arxiv.org/html/2604.10409)
- [IMPACT official repository](https://github.com/Kratos-Wen/IMPACT)
- [IMPACT separate data license](https://github.com/Kratos-Wen/IMPACT/blob/main/LICENSE-DATA)

---

<a id="indego"></a>

## IND-05 · IndEgo

**Core candidate** · **Year / version:** 2025

Workers perform industrial assembly, disassembly, inspection, repair, woodworking, and logistics tasks, including two-person collaboration. The collection mixes complete task recordings with tool demonstrations and short actions, using egocentric and external views where available.

- **Duration:** Mixed units: individual actions last a few seconds to less than 1 minute, while complete tasks reach up to 68 minutes. The reported overall mean is 205 seconds (3.42 minutes); a unified minimum-to-maximum range is not reported.
- **Collection size:** 3,460 egocentric recordings totaling 197.1 hours and 1,092 external-view recordings totaling 96.8 hours; these are not additive independent task hours.
- **Potential applications:** Mistake detection; Task understanding and reasoning QA; Current-step and collaborative process memory (derived).
- **Modalities / available information:** Egocentric and external video, narrated audio, gaze, motion, hand poses, and semi-dense point clouds; external views are not available for every subset.
- **Dataset family:** IndEgo
- **Access evidence:** Open file listing, as checked on 2026-10-24: the institutional Hugging Face repository exposes a data card and file entries. Downloads were not tested. Completion of the announced directory reorganization was not verified, and a viewer type-conversion error did not establish that raw files were unavailable.
- **License observations:** The institutional data card states CC BY 4.0; additional package-specific terms were not checked.
- **Caveats:** The 68-minute figure is a maximum for complete tasks, not the duration of all videos. Some QA and collaboration benchmarks use 1-minute slices. Short actions, tool demonstrations, complete tasks, and overlapping views must be distinguished; fix the version and manifest before evaluating long sequences. Error timestamp coverage, recovery pairing, and the balance of spontaneous versus induced errors were not verified. QA does not itself establish an online next-step decision task.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [IndEgo original paper](https://arxiv.org/abs/2511.19684)
- [Fraunhofer IPK IndEgo data card](https://huggingface.co/datasets/FraunhoferIPK/IndEgo)
- [IndEgo NeurIPS paper](https://papers.nips.cc/paper_files/paper/2025/file/8e5dc5969a6174fcaaececd890c7f59b-Paper-Datasets_and_Benchmarks_Track.pdf)
- [IndEgo paper, Table 1 and Appendices A and J](https://arxiv.org/html/2511.19684)

---

<a id="attach"></a>

## IND-06 · ATTACH

**Auxiliary** · **Year / version:** 2023

Participants assemble furniture and workpieces in a setup designed around a collaborative robot viewpoint. Three camera views capture simultaneous two-handed activity with separate action labels for each hand.

- **Duration:** Mean complete assembly execution duration: 8.2 minutes; minimum and maximum durations are unverified.
- **Collection size:** 126 executions recorded from 3 views yield 378 videos; 17.2 independent hours and 51.6 accumulated view-hours, with 42 participants.
- **Potential applications:** Per-hand action recognition; Temporal action detection; Parallel two-hand interaction analysis.
- **Modalities / available information:** Multi-view RGB, depth, infrared, and Azure Kinect-estimated 3D skeletons.
- **Dataset family:** ATTACH
- **Access evidence:** Links only, as checked on 2026-10-24: the original paper links the TU Ilmenau dataset page. Working downloads and application requirements were not verified.
- **License observations:** The data license was not verified; paper or code licensing must not be substituted for a data license.
- **Caveats:** The reported maximum of 299 seconds describes an action segment, not a complete video. Synchronized views must not be counted as separate executions or split across training and evaluation. Dense hand-action labels do not establish part quality, task dependencies, optimal collaboration, or error/recovery supervision; these would require additional annotation.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [ATTACH original paper](https://arxiv.org/abs/2304.08210)
- [ATTACH institutional dataset page](https://www.tu-ilmenau.de/neurob/data-sets-code/attach-dataset)
- [ATTACH paper, Section 3](https://arxiv.org/html/2304.08210)

---

<a id="havid"></a>

## IND-07 · HA-ViD

**Auxiliary** · **Year / version:** 2023

Participants assemble individual boards from a three-board Generic Assembly Box using industrial parts and tools. Multi-view recordings capture two-handed work, natural pauses, mistakes, and changes in execution order during learning.

- **Duration:** Mean video duration for a single-board assembly task: 1 minute 37 seconds; minimum and maximum durations are unverified.
- **Collection size:** 3,222 task video streams; the paper reports 86.9 accumulated hours across views and modalities.
- **Potential applications:** Hierarchical action recognition and segmentation; Object detection and tracking; Assembly progress and efficiency analysis; Two-hand coordination analysis.
- **Modalities / available information:** Multi-view and multimodal imagery with object and tool information; the exact published stream combinations require a version-specific manifest check.
- **Dataset family:** HA-ViD; DuHa reuses HA-ViD source videos, but the per-video mapping was not verified.
- **Access evidence:** Links only, as checked on 2026-10-24: the paper provides an official project link. Complete dataset downloads were not verified.
- **License observations:** The data license was not verified; paper or code licensing must not be substituted for a data license.
- **Caveats:** Each video unit is one board assembly, not the complete box assembly. Accumulated views/modalities and the 3,222 stream count do not establish that many independent full tasks. Do not join clips into complete procedures without continuity evidence. Error labels are reported, but error-type coverage and recovery pairing were not verified. Deduplicate DuHa against this source family.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [HA-ViD original paper and dataset scale](https://arxiv.org/html/2307.05721)
- [HA-ViD project page linked by the paper](https://iai-hrc.github.io/ha-vid)

---

<a id="ha4m"></a>

## IND-08 · HA4M

**Auxiliary** · **Year / version:** 2022

Participants assemble a complete planetary gearbox in a controlled laboratory. A single Azure Kinect captures three assembly stages with synchronized visual and geometric modalities for action recognition and segmentation.

- **Duration:** The original paper reports 997-7,262 frames per video; at 30 fps, this corresponds to approximately 33.23-242.07 seconds. The paper reports a mean of 98.40 seconds, retained as stated.
- **Collection size:** 217 videos in the original paper version, with 41 participants and 12 action classes; expanded releases require separate statistics.
- **Potential applications:** Action recognition; Temporal action segmentation; Assembly progress tracking (derived).
- **Modalities / available information:** One Azure Kinect: RGB, depth, infrared, aligned RGB-D, point clouds, and skeletons; this is a single-view multimodal capture.
- **Dataset family:** HA4M; the separate HARMA human-robot collaboration collection is not a version of HA4M.
- **Access evidence:** Links only, as checked on 2026-10-24: the institutional GitLab repository identifies Science Data Bank DOI 10.57760/sciencedb.01872 for the fixed paper version and links a growing release. Downloads were not tested.
- **License observations:** The data license was not verified; paper or code licensing must not be substituted for a data license.
- **Caveats:** Duration endpoints are converted from frame counts and frame rate. The table mean of 98.40 seconds is preserved without independently correcting it. Updated releases must be measured separately. Multiple modalities do not imply multiple camera views. Part-quality, procedural-error, recovery, and dependency-graph annotations were not verified; part-state and next-step tasks would require construction.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [HA4M institutional repository](https://baltig.cnr.it/ISP/ha4m)
- [Authors description of HA4M and HARMA](https://ceur-ws.org/Vol-3762/505.pdf)
- [HA4M original paper, Table 6 at tables/7; 30 fps stated in the text](https://www.nature.com/articles/s41597-022-01843-z/tables/7)

---

<a id="ikea-asm"></a>

## IND-09 · IKEA ASM

**Auxiliary** · **Year / version:** 2020 release / 2021 paper

People assemble four types of furniture across five environments. Synchronized camera views capture part handling and assembly actions with pose, part-segmentation, and tracking annotations.

- **Duration:** Mean video duration: approximately 1.89 minutes; minimum and maximum durations are unverified. Mean atomic action duration: approximately 6 seconds.
- **Collection size:** 371 assembly samples with 3 RGB views per sample; approximately 35.27 accumulated video hours and 48 participants.
- **Potential applications:** Action recognition and segmentation; Human pose estimation; Furniture-part segmentation and tracking; Assembly progress estimation (derived).
- **Modalities / available information:** 3 RGB streams and 1 depth stream per sample; camera extrinsics, human poses, and part segmentation/tracking.
- **Dataset family:** IKEA ASM; IKEA Ego 3D and the web-video IAW collection are separately collected datasets and must not be merged into its scale.
- **Access evidence:** Links only, as checked on 2026-10-24: the official page provides Google Drive links for compressed videos. Downloads were not tested.
- **License observations:** Data and benchmark: CC BY-NC 4.0. Code: MIT. Commercial licensing requires contacting the authors.
- **Caveats:** The total accumulates multiple views. Figure 2 shows a distribution, not verified exact minimum and maximum durations. Full finished-product coverage was not verified for every sample. Only approximately 1% of keyframes have manual pose/part annotations; the rest are pseudo ground truth. Split by source assembly to avoid view leakage. Native error, recovery, and quality supervision were not established.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [IKEA ASM official page](https://ikeaasm.github.io/)
- [IKEA ASM original paper, dataset statistics and Figure 2](https://arxiv.org/html/2007.00394v2)

---

<a id="ipad"></a>

## IND-10 · IPAD

**Comparison** · **Year / version:** 2024

Real and synthetic videos depict periodic production processes for 16 types of industrial equipment. The collection supports analysis of process cycles and temporal anomalies in machine operation.

- **Duration:** Per-video minimum, maximum, and mean durations are unverified. Equipment operating cycles last 5-30 seconds; these are cycle lengths, not video durations.
- **Collection size:** More than 6 hours of real and synthetic video covering 16 equipment types.
- **Potential applications:** Industrial process anomaly detection; Equipment cycle modeling.
- **Modalities / available information:** Real and synthetic industrial process video.
- **Dataset family:** IPAD
- **Access evidence:** Links only, as checked on 2026-10-24: the original paper provides a project link. Download availability was not verified.
- **License observations:** The data license was not verified; paper or code licensing must not be substituted for a data license.
- **Caveats:** A cycle length is not a video duration, and repeated cycles do not by themselves constitute long-horizon multistep reasoning. Machine processes differ from human goal-directed assembly or maintenance. Fine-grained pixel, frame, and interval annotation coverage was not verified. Whether anomalies in real recordings were spontaneous or induced was not established. Operator step, intent, next-action decision, and recovery supervision are not provided by the verified description.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [IPAD original paper, acquisition and process cycles](https://arxiv.org/html/2404.15033)
- [IPAD project page](https://ljf1113.github.io/IPAD_VAD)

---

<a id="meccano"></a>

## IND-11 · MECCANO

**Auxiliary** · **Year / version:** 2021 / multimodal extension 2022

Participants follow instructions to assemble a metal toy motorcycle with small parts and hand tools. Egocentric video records screw, nut, and wrench interactions alongside depth and gaze for fine-grained action and active-object analysis.

- **Duration:** Complete video duration range: 9.23-35.45 minutes. The paper text reports a mean of 21.14 minutes, while its comparison table reports 20.79 minutes; both are retained as decimal-minute values.
- **Collection size:** 20 complete assembly videos from 20 participants; 8,857 annotated action segments are not 8,857 independent procedures.
- **Potential applications:** Action recognition; Action anticipation; Next active-object prediction; Gaze and hand-object interaction analysis.
- **Modalities / available information:** Synchronized egocentric RGB, depth, and gaze; hand/active-object and next-active-object boxes.
- **Dataset family:** MECCANO and its multimodal extension share the same dataset family; the extension is not an independent additional collection.
- **Access evidence:** Links only, as checked on 2026-10-24: the author site provides separate RGB video, depth, gaze, and annotation links. Downloads were not tested.
- **License observations:** The data license was not verified; paper or code licensing must not be substituted for a data license.
- **Caveats:** The text and comparison-table means disagree and must not be merged into one precise mean. Values use the original decimal minutes, not minutes-and-seconds notation. The data cover one toy task and a small participant group. Native part-state, error, and recovery supervision was not established. Predicting the next interaction object does not identify an optimal assembly step. Align original and multimodal versions before combining them.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [MECCANO official multimodal page](https://iplab.dmi.unict.it/legacy/MECCANO/)
- [MECCANO official repository](https://github.com/fpv-iplab/MECCANO)
- [MECCANO Multimodal paper, acquisition section and comparison table](https://arxiv.org/html/2209.08691)
