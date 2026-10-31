# Medical and Laboratory Workflows

[Back to the collection](../README.md) · [Duration methodology](../docs/methodology.md) · [JSON data](../data/datasets.json)

Surgical procedures, operating rooms, laboratory protocols, and specialist execution quality.

**11 records.** Suggested applications are editorial research directions; consult annotations and caveats before assuming native task support.

## Contents

- [MED-01 · LabSuperVision (LSV)](#labsupervision)
- [MED-02 · MultiBypass140](#multibypass140)
- [MED-03 · FineBio](#finebio)
- [MED-04 · Cholec80](#cholec80)
- [MED-05 · CholecT50](#cholect50)
- [MED-06 · ExpVid](#expvid)
- [MED-07 · GraSP](#grasp)
- [MED-08 · MM-OR](#mm-or)
- [MED-09 · PitVis-2023](#pitvis)
- [MED-10 · SAR-RARP50](#sar-rarp50)
- [MED-11 · Trauma THOMPSON](#trauma-thompson)

---

<a id="labsupervision"></a>

## MED-01 · LabSuperVision (LSV)

**Core candidate** · **Year / version:** unknown

Egocentric and external recordings show wet-laboratory procedures such as pipetting, cell culture, PCR, and RNA extraction. Some demonstrations deliberately introduce protocol deviations, with textual protocols and issue metadata describing the operations.

- **Duration:** For complete independent experiments or protocols, the minimum, maximum, and mean are unknown. Parseable CSV records/slices only: XM has 57 of 92 rows spanning 57-600 seconds (0.95-10 minutes), with a mean of 433.86 seconds (7.23 minutes); DJI has 70 of 161 rows spanning 0.8-1,747 seconds (0.0133-29.1167 minutes), with a mean of 176.70 seconds (2.945 minutes). These means were calculated in the duration audit from non-missing Length values.
- **Collection size:** Independent experiment hours are unknown. Known Length values sum to 24,730 seconds for XM and 12,368.8 seconds for DJI; these sums cannot be added as deduplicated experiment time.
- **Potential applications:** Operation-to-protocol alignment; Protocol issue analysis from metadata; Next-step prediction from protocols (derived; continuity must be checked).
- **Modalities / available information:** XM smart-glasses egocentric video; DJI external video and images; textual protocols and scene/tool metadata.
- **Dataset family:** LabSuperVision / LSV
- **Access evidence:** Open file listing, as checked on 2026-10-24: the Hugging Face tree contains MP4 files, protocols, and CSVs. Small metadata files were read, but videos were not downloaded or probed and complete large-file availability was not tested.
- **License observations:** The data card states CC BY-NC 4.0; noncommercial restrictions apply.
- **Caveats:** XM has 35 additional blank Length rows; DJI has 75 blank rows and 16 NA values. Missing values were not treated as zero, and the complete media collection was not probed. The card reports 90 XM metadata entries and 105 video files, whereas the CSV contains 92 nonempty Slice_ID rows. DJI has 161 metadata entries, including images; the card describes 127 videos, 34 images, and 251 mixed files. Views, consecutive slices, and file counts are not independent experiments. Issue is populated in 17 XM and 18 DJI rows, while Time_stamp is populated in 0 XM and 17 DJI rows; these counts are neither distinct error-event counts nor frame-level truth. Blank Issue fields are not verified negatives. Deliberately staged deviations do not measure natural error rates, and full-protocol continuity and outcome coverage remain unproven.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [LabSuperVision official data card](https://huggingface.co/datasets/YinkaiW/LSV)
- [XM egocentric metadata CSV, raw content inspected](https://huggingface.co/datasets/YinkaiW/LSV/blob/main/XMglass/xm.csv)
- [DJI external-view metadata CSV, raw content inspected](https://huggingface.co/datasets/YinkaiW/LSV/blob/main/DJI/dji.csv)

---

<a id="multibypass140"></a>

## MED-02 · MultiBypass140

**Core candidate** · **Year / version:** 2023; IAE annotation extension 2025

Clinical laparoscopic videos show Roux-en-Y gastric bypass operations from centers in Strasbourg and Bern. Hierarchical phase and step labels describe the surgical workflow, and a later annotation extension adds intraoperative adverse events and severity.

- **Duration:** Individual surgery range: 37-178 minutes, using global extrema across the three splits in Appendix Table 7. StrasBypass70 spans 41-178 minutes and BernBypass70 spans 37-145 minutes. The main text reports respective means of 110 and 72 minutes; the discussion instead reports 111 +/- 33 and 73 +/- 20 minutes (mean +/- standard deviation), retained as a reporting difference.
- **Collection size:** 140 surgeries, 70 per center. The reported 1 fps frame counts, 464,794 + 305,907 = 770,701, imply approximately 214.08 hours of temporal coverage; this is a derived total.
- **Potential applications:** Surgical phase and step recognition; Intraoperative adverse-event detection and severity assessment; Cross-center workflow generalization; Future-step and event prediction from past context (derived).
- **Modalities / available information:** Endoscopic RGB, temporal phase/step labels, and intraoperative adverse-event labels with severity.
- **Dataset family:** MultiBypass140 combines StrasBypass70 and BernBypass70. The 2025 intraoperative adverse-event extension annotates the same surgeries rather than adding 140 new cases.
- **Access evidence:** Open download links, as checked on 2026-10-24: the official repository lists six data archives and annotation/visualization instructions. Actual downloads and per-file completeness were not tested.
- **License observations:** The official README restricts code, models, and datasets to noncommercial scientific research under CC BY-NC-SA 4.0. Third-party code retains its own license.
- **Caveats:** Standard deviations are not duration endpoints; the reported range comes from explicit split-level extrema. The differing center means are retained rather than silently reconciled. Sampling at 1 fps preserves the source surgery time scale. Labels cover 12 phases, 46 steps, and 5 adverse-event categories; severity is 1-5, with 0 indicating no adverse event. Adverse events do not automatically indicate operator misconduct, an omitted step, or complete protocol-compliance supervision. Positive-case counts and event-boundary coverage were not audited, and not every case can be assumed to contain an anomaly.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [MultiBypass140 official data and adverse-event extension](https://github.com/CAMMA-public/MultiBypass140)
- [Challenges in Multi-centric Generalization: Phase and Step Recognition in Roux-en-Y Gastric Bypass Surgery, Sections 2-3 and Appendix C Table 7](https://arxiv.org/html/2312.11250v1)

---

<a id="finebio"></a>

## MED-03 · FineBio

**Core candidate** · **Year / version:** 2025 (journal version)

Participants carry out mock biological experiments spanning seven protocols in a laboratory setup. Synchronized head-mounted and external cameras capture protocol steps, atomic operations, and interactions with manipulated and affected objects.

- **Duration:** Mean independent trial/protocol execution duration: 3.9 minutes; per-trial minimum and maximum durations are unknown. Mean step duration: 14.3 seconds; mean atomic operation duration: approximately 0.9 seconds (0.91 seconds in the text), representing lower-level units.
- **Collection size:** 226 valid trials by 32 participants, with approximately 14.5 independent hours. Six synchronized views total 87 recording hours (14.5 x 6), not 87 independent hours.
- **Potential applications:** Hierarchical step segmentation; Atomic operation detection; Object and manipulated/affected-object detection; Future-step prediction from protocol history (derived).
- **Modalities / available information:** RGB from 1 head-mounted and 5 external cameras; step, atomic-operation, object, and interaction annotations.
- **Dataset family:** FineBio
- **Access evidence:** By request, as checked on 2026-10-24: sign the FineBio License Agreement and submit the form; approved applicants receive links and credentials by email for noncommercial research/development. No application or download test was performed.
- **License observations:** Data use is governed by a dedicated license agreement; code is MIT. The official README records an agreement update on 2026-09-10, so the applicable updated agreement must be used.
- **Caveats:** Duration-distribution plot axes were not treated as observed minimum and maximum values. Synchronized views are not independent trials. Mock experiments substitute distilled water for reagents and omit or shorten waiting periods such as centrifugation and PCR machine processes; their durations do not represent complete real wet-lab wall-clock time. Mock acquisition does not imply error annotations: native protocol-deviation, experimental-failure, and per-step compliance truth were not established. Minute-scale trials and derived prediction splits do not establish an optimal decision task.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [FineBio official repository and access agreement](https://github.com/aistairc/FineBio)
- [FineBio: A Fine-Grained Video Dataset of Biological Experiments with Hierarchical Annotation, Figure 2 and Sections 3.2.1-3.2.3](https://link.springer.com/article/10.1007/s11263-025-02523-2)

---

<a id="cholec80"></a>

## MED-04 · Cholec80

**Auxiliary** · **Year / version:** 2016

Clinical endoscopic videos record complete laparoscopic gallbladder removal surgeries performed by 13 surgeons. Annotations track surgical phases and instrument presence through the operations.

- **Duration:** Mean complete-surgery video duration: approximately 38 minutes, with a standard deviation of 16 minutes, directly reported in Section 3.1 of a subsequent CAMMA-team paper. Per-video minimum and maximum durations remain unknown; 38 +/- 16 minutes is a mean and standard deviation, not a 22-54 minute range.
- **Collection size:** 80 surgery videos. Exact total hours of original video remain unknown; the rounded 38-minute mean does not establish an official precise total.
- **Potential applications:** Surgical phase recognition; Instrument presence detection; Future-phase prediction (derived); Whole-surgery history evaluation (derived).
- **Modalities / available information:** Endoscopic RGB at 25 fps; phase labels at 25 fps and instrument-presence labels at 1 fps.
- **Dataset family:** Cholec80 / CholecT50: 45 of the 50 CholecT50 source videos come from Cholec80; split and deduplicate by original surgery.
- **Access evidence:** Open download link, as checked on 2026-10-24: the CAMMA directory provides a direct cholec80.zip link. Actual download and archive contents were not tested.
- **License observations:** Dataset authorization terms were not verified; public download availability does not establish commercial-use or redistribution rights.
- **Caveats:** The duration mean and standard deviation come from a 2023 accepted follow-up paper by the CAMMA team, confirmed through its official publication directory, not directly from the EndoNet original paper or dataset summary page. No verified per-video extrema or more precise mean are substituted. Phase durations, sampled frame counts, and original video lengths are different statistics. Seven phase classes describe complete recordings, not recordings of just one phase; phase labels are not fine-grained steps or action triplets. Native anomaly or step-compliance labels were not established. Avoid source overlap with CholecT50 across evaluation splits.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [CAMMA official dataset directory and Cholec80 entry](https://camma.unistra.fr/datasets/)
- [EndoNet: A Deep Architecture for Recognition Tasks on Laparoscopic Videos, Section IV-A, Table I, and Figure 4](https://arxiv.org/pdf/1602.03012)
- [CAMMA official publication directory](https://camma.unistra.fr/publications/)
- [Dissecting Self-Supervised Learning Methods for Surgical Computer Vision, CAMMA team, 2023 accepted manuscript, Section 3.1, page 5](https://arxiv.org/pdf/2207.00449)

---

<a id="cholect50"></a>

## MED-05 · CholecT50

**Auxiliary** · **Year / version:** 2022; public release 2023

Laparoscopic gallbladder surgery videos depict instrument, action, and anatomical-target interactions. Frames sampled at 1 fps carry action-triplet labels, with instrument-tip boxes available for a five-video subset.

- **Duration:** Per-surgery minimum and maximum durations are unknown, and the paper does not directly report an overall mean video duration. Dividing 100,863 frames sampled at 1 fps by 50 source videos implies approximately 33.62 minutes of annotated temporal coverage per video; this is a coverage estimate, not a measured video-container duration.
- **Collection size:** 50 source surgeries; 100,863 frames at 1 fps imply approximately 28.02 hours of annotated temporal coverage. The 161,005 triplet label instances are not videos or seconds.
- **Potential applications:** Instrument-verb-target action-triplet recognition; Local surgical interaction analysis; Instrument-tip detection on the annotated subset; Next-action prediction (derived; continuity must be verified).
- **Modalities / available information:** Endoscopic RGB and instrument-verb-target triplets at 1 fps; instrument-tip boxes for 5 videos.
- **Dataset family:** CholecT50 draws 45 source videos from Cholec80 and 5 from Cholec120; it is not 50 new surgeries independent of Cholec80.
- **Access evidence:** By request, as checked on 2026-10-24: full dataset access requires the official request form. Direct links for some challenge validation data do not establish unrestricted full-dataset access. No application or download test was performed.
- **License observations:** Data: CC BY-NC-SA 4.0, including noncommercial and share-alike requirements for redistribution or derivatives.
- **Caveats:** Sampled frames, original high-frame-rate videos, and triplet instances are different units. Triplet counts and additional detection annotations must not be counted as independent procedures. Full-video release coverage and temporal continuity need verification before derived prediction tasks. Action triplets do not automatically identify goal-directed clinical steps; rare triplets do not establish procedural errors. Native anomaly, protocol-compliance, and optimal planning labels were not established. Deduplicate and split by original source surgery.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [CholecT50 official repository](https://github.com/CAMMA-public/cholect50)
- [CAMMA dataset releases and source relationships](https://camma.unistra.fr/datasets/)
- [CholecT50 full-data request and partial validation download instructions](https://github.com/CAMMA-public/cholect50/blob/master/docs/README-Downloads.md)
- [Rendezvous original paper, Section 3 and Table 3 data splits](https://arxiv.org/pdf/2109.03223)

---

<a id="expvid"></a>

## MED-06 · ExpVid

**Auxiliary** · **Year / version:** 2025

Published JoVE Research videos demonstrate laboratory experiments across 13 disciplines, with narration and editorial cuts. Three annotation levels cover atomic actions, intermediate stages, and full published procedures through questions about operations, order, prediction, and conclusions.

- **Duration:** Source-video filtering used 378-728 seconds (6.30-12.13 minutes), a 25th-75th percentile selection window rather than measured extrema of the final release. Level-3 full experiment videos average approximately 8 minutes, with final minimum and maximum durations unknown. Level-1 action clips average approximately 8 seconds and Level-2 stage segments approximately 48 seconds; actual extrema at both levels are unknown.
- **Collection size:** 390 source experiment videos. Multiplying 390 by the approximate 8-minute Level-3 mean gives roughly 52 hours, a rough estimate rather than an exact total; Level-1/2 slices cannot be added to Level-3 source time.
- **Potential applications:** Laboratory operation and material understanding; Step ordering and sequence generation; Next-step question answering; Constructed procedure-completeness verification; Scientific conclusion question answering.
- **Modalities / available information:** Video, QA JSONL, and ASR captions, including video paths, questions, options, and answers.
- **Dataset family:** ExpVid is derived from JoVE Research video articles; its three levels reuse the same source experiments.
- **Access evidence:** Open file listing, as checked on 2026-10-24: the official Hugging Face tree contains Level-3 MP4 assets and Level-2 JSONL annotations, including step prediction and video verification. Only file metadata was checked; media downloads and availability of all 390 videos were not tested.
- **License observations:** The data card states CC BY-NC 4.0. Rights to third-party JoVE source videos require separate verification and cannot be inferred from annotation licensing.
- **Caveats:** The source filtering window precedes editing and is not the final video range. Some conclusion pages, charts, and analysis footage were removed; full procedure does not guarantee continuous capture of all waiting time. The 20-60 second Level-2 text segmentation constraint is not a measured video range. Completeness questions are constructed by deleting a nonfinal step from a list, not by establishing that the recorded operator omitted it. QA prediction is not equivalent to continuous online prediction, natural error detection, or optimal decisions.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [ExpVid official data card](https://huggingface.co/datasets/OpenGVLab/ExpVid)
- [ExpVid original paper, Section 3.1 filtering and preprocessing; prediction and completeness tasks](https://arxiv.org/html/2510.11606v1)
- [ExpVid Level-3 MP4 asset directory](https://huggingface.co/datasets/OpenGVLab/ExpVid/tree/main/videos/level_3)

---

<a id="grasp"></a>

## MED-07 · GraSP

**Core candidate** · **Year / version:** 2024

Long endoscopic recordings show robot-assisted radical prostatectomy with hierarchical surgical activity annotations. Phase and step labels describe the workflow, while instrument segmentation and atomic-action labels describe local spatial interactions.

- **Duration:** Individual video range: 0.69-3.86 hours, equivalent to 41.4-231.6 minutes, converted from already-rounded hour values in Table 3. Mean: 2.49 hours (149.4 minutes); standard deviation: 0.77 hours (46.2 minutes).
- **Collection size:** 13 surgery videos totaling 32.37 hours; 116,521 sampled frames at 1 fps. Original recordings are at 30 fps.
- **Potential applications:** Hierarchical surgical phase and step recognition; Instrument instance segmentation; Atomic surgical action recognition; Future-step and long-history modeling (derived).
- **Modalities / available information:** Endoscopic RGB with phase, step, instrument-segmentation, and atomic-action annotations; 30 fps and 1 fps frame releases.
- **Dataset family:** GraSP extends PSI-AVA: 8 videos are reused and re-reviewed from PSI-AVA, and 5 are newly added.
- **Access evidence:** Open download links, as checked on 2026-10-24: the official README links a Google Drive directory with videos.tar.gz, full 30 fps training/evaluation frames and annotations, a lightweight 1 fps version, and raw frames. Downloads and full file completeness were not tested.
- **License observations:** The paper release statement mentions MIT and the repository license is MIT. The specific authorization for original surgical videos in the data directory was not independently verified; code licensing alone does not establish unrestricted redistribution of all assets.
- **Caveats:** The range uses explicit per-case extrema, not mean plus/minus standard deviation. Rounded hour values do not provide second-accurate endpoints. Different frame-sampling versions and reused PSI-AVA cases are not new surgeries. The official repository corrected phase/step annotations in December 2024; fix the annotation version for evaluation. The dataset has few cases from one procedure, and fine-grained temporal coverage needs checking. Native adverse-event or per-step compliance labels were not established, and derived future-step prediction is not an optimal surgical decision policy.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Pixel-Wise Recognition for Holistic Surgical Scene Understanding, Table 3 and Section 3.3](https://arxiv.org/html/2401.11174v2)
- [GraSP official videos, frame releases, and annotation-version information](https://github.com/BCV-Uniandes/GraSP)

---

<a id="mm-or"></a>

## MED-08 · MM-OR

**Core candidate** · **Year / version:** 2025

Multimodal operating-room recordings capture robotic total and partial knee replacement procedures performed on patient phantoms. Full procedures and additional short demonstrations support team-interaction analysis, next-action anticipation, and detection of sterility breaches.

- **Duration:** The 17 complete procedures typically last approximately 90 minutes each; their minimum and maximum durations are unknown. Appendix Section 8 reports 22 short clips of 1-10 minutes each, whereas the violation-detection task description reports 20 short clips of 1-5 minutes; both scopes are retained.
- **Collection size:** 17 long procedures at approximately 90 minutes imply about 25.5 hours, not an exact total. Across the full dataset, 92,983 synchronized timepoints at 1 Hz imply approximately 25.83 hours of temporal coverage, including short clips; camera streams are not multiplied into independent duration.
- **Potential applications:** Operating-room phase and relation-state recognition; Next-action anticipation; Sterility-breach detection; Panoptic segmentation and scene-graph analysis.
- **Modalities / available information:** Multi-view RGB-D, robot data, audio and other sensor information, panoptic segmentation, and scene graphs; per-file synchronization and public modality coverage were not fully checked.
- **Dataset family:** MM-OR
- **Access evidence:** By request, as checked on 2026-10-24: the official README requires an application form and agreement to data-use terms before providing a download script for multiple ZIP archives. No form was submitted and no download was tested.
- **License observations:** The data-use agreement and specific raw-data license were not verified; model or code licenses must not be extended to the multimodal recordings.
- **Caveats:** The appendix reports 22 clips of 1-10 minutes, while the violation task reports 20 clips of 1-5 minutes; this unresolved task/statistics scope difference must not be silently overwritten. Count each synchronized timepoint once across cameras and modalities. Phantom procedures are not real-patient clinical cases. Dedicated correct/incorrect short demonstrations and full procedures do not necessarily share an anomaly distribution; sterility-breach labels do not estimate clinical infection or naturally occurring adverse-event rates. Next-action labels do not certify patient-specific optimal decisions.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [MM-OR paper, overview, violation-detection task, and Appendix Section 8 dataset statistics](https://arxiv.org/html/2503.02579v1)
- [MM-OR official repository and access instructions](https://github.com/egeozsoy/MM-OR)

---

<a id="pitvis"></a>

## MED-09 · PitVis-2023

**Core candidate** · **Year / version:** 2023 (challenge); DOI issued 2024; metadata publicationYear 2026

Endoscopic transsphenoidal pituitary surgery recordings cover nasal access, the sphenoid sinus, dural opening, tumor removal, hemostasis, and repair. Step and instrument annotations accompany long procedures, including recorded periods when the endoscope is outside the patient.

- **Duration:** For the 25 training/validation videos, mean in-patient time is 72.8 minutes and mean out-of-patient time is 7.2 minutes, totaling 80.0 minutes per video. For the 8 hidden-test videos, the corresponding means are 60.9 and 5.6 minutes, totaling 66.5 minutes. Full-video minimum and maximum durations are unknown for both groups.
- **Collection size:** 25 released training/validation videos and 8 hidden-test videos. Rounded means imply approximately 33.33 and 8.87 hours respectively, approximately 42.20 hours combined; the 33 videos are not all publicly released.
- **Potential applications:** Surgical step recognition; Instrument recognition; Next-step prediction from temporal transitions (derived); Long-history surgical workflow modeling (derived).
- **Modalities / available information:** Endoscopic RGB, step and instrument labels, mapping CSVs, and video-encoding metadata.
- **Dataset family:** PitVis-2023 / EndoVis; the UCL release describes the 25 training/validation videos, with 8 challenge test videos kept hidden.
- **Access evidence:** Links only, as checked on 2026-10-24: the ended challenge redirects downloads to a UCL DOI whose metadata describes 25 MP4 videos and corresponding CSVs. The old challenge required a Synapse account and registration form; the 8 hidden-test videos are explicitly withheld. UCL file-access permissions and downloads were not verified.
- **License observations:** The UCL DOI registration metadata states CC BY-NC-SA 4.0 for the published record. This does not establish access rights to withheld test data.
- **Caveats:** Add mean in-patient and out-of-patient times to describe whole-video mean duration; excluding out-of-patient frames from evaluation does not mean they were never recorded. Component medians must not be added as a whole-video median. The canonical paper values 72.8 + 7.2 minutes refine the original rounded 73 + 7 minute figures. The step ontology lists 14 numbered steps, but 2 rare steps were removed, leaving 12 evaluated classes; keep these counts distinct. Hemostasis, occlusion, and out-of-patient footage are not adverse-event or compliance labels. The DOI was issued on 2024-08-20 and updated on 2026-09-29, with publicationYear 2026; the metadata refresh year is not the original collection year. Fix release and annotation versions.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [PitVis official repository](https://github.com/dreets/pitvis)
- [PitVis official dataset description, read through the public Synapse API](https://www.synapse.org/Synapse:syn51232283/wiki/621585)
- [PitVis official participation requirements and later release link](https://www.synapse.org/Synapse:syn51232283/wiki/621587)
- [UCL PitVis-2023 data release record](https://doi.org/10.5522/04/26531686)
- [PitVis DOI registration metadata: scale, dates, and license](https://api.datacite.org/dois/10.5522/04/26531686)
- [PitVis-2023 Challenge paper, Section 4.2.1 Videos](https://arxiv.org/html/2409.01184v1)

---

<a id="sar-rarp50"></a>

## MED-10 · SAR-RARP50

**Auxiliary** · **Year / version:** 2022

Clinical endoscopic clips show dorsal venous complex suturing during robot-assisted radical prostatectomy, performed by eight surgeons of different experience levels. Fine-grained two-handed action and instrument-segmentation annotations describe this local surgical phase rather than the entire operation.

- **Duration:** For all 50 SAR-RARP50 samples, per-sample minimum, maximum, and mean durations are unknown. Figure 1 is explicitly labeled RARP-45 and describes an approximate 2-12 minute task range with a mean of approximately 5 minutes; these statistics remain restricted to RARP-45 and are not extrapolated to all 50.
- **Collection size:** Dorsal venous complex suturing-phase clips from 50 RARP surgeries, split into 40 training and 10 test cases. Total hours for all 50 are unknown and cannot be calculated as 50 x 5 minutes.
- **Potential applications:** Fine-grained suturing action recognition; Surgical instrument semantic segmentation; Local next-action prediction (derived).
- **Modalities / available information:** Endoscopic RGB; continuous action annotations at 60 Hz and framewise labels at 10 Hz; instrument semantic segmentation at 1 Hz. Video acquisition is 60 fps.
- **Dataset family:** SAR-RARP50 / EndoVis 2022; source surgeries contribute DVC suturing-phase clips, and the paper separately labels its duration plot RARP-45.
- **Access evidence:** Links only, as checked on 2026-10-24: the old Synapse process required registration, acceptance of rules, and approval. Registration closed on 2022-09-02, and the participation page now links a complete UCL mirror. Mirror file-access permissions and downloads were not tested, so neither the old route nor unrestricted current access is assumed.
- **License observations:** The old Synapse terms restricted independent public redistribution. The current UCL mirror license was not verified; original challenge terms and later release terms need separate confirmation.
- **Caveats:** These are not complete prostatectomy recordings. Do not silently relabel the RARP-45 figure as RARP50 or infer that appearing in the 50-case challenge paper makes it a 50-case statistic. Acquisition frame rate and annotation sampling rates do not establish clip length. Labels cover 7 fine-grained action classes plus Other and 9 segmentation classes; imprecise action boundaries are annotation uncertainty, not clinical anomaly labels. Native procedural-error supervision was not established, and this single phase provides limited evidence for whole-operation planning or long-term goal dependencies.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [SAR-RARP50 official evaluation repository](https://github.com/surgical-vision/SAR_RARP50-evaluation)
- [EndoVis SAR-RARP50 data entry linked by the repository](https://www.synapse.org/#!Synapse:syn27618412/wiki/)
- [SAR-RARP50 official dataset scope and annotation description](https://www.synapse.org/Synapse:syn27618412/wiki/616886)
- [SAR-RARP50 official participation page: registration closure and UCL mirror](https://www.synapse.org/Synapse:syn27618412/wiki/616883)
- [SAR-RARP50 challenge paper, Section 4.1 and Figure 1 RARP-45 statistics](https://arxiv.org/html/2401.00496v1)
- [SAR-RARP50 UCL complete-data mirror; file permissions unverified](https://rdr.ucl.ac.uk/projects/SAR-RARP50_Segmentation_of_surgical_instrumentation_and_Action_Recognition_on_Robot-Assisted_Radical_Prostatectomy_Challenge/191091)

---

<a id="trauma-thompson"></a>

## MED-11 · Trauma THOMPSON

**Auxiliary** · **Year / version:** 2025

Egocentric recordings show simulated emergency procedures: cricothyrotomy, chest-tube insertion, tourniquet application, intraosseous infusion, and needle decompression. Regular equipment and just-in-time improvised-tool conditions support action, hand, tool, and medical question-answering tasks.

- **Duration:** Per-video or independent-procedure minimum and maximum durations are unknown. The paper's Video duration paragraph reports overall means of 64.96 seconds for regular recordings and 42.48 seconds for JIT recordings, but also reports a conflicting total of 11,528 minutes. The means are retained as reported, not treated as reliable full-procedure durations with the unit conflict resolved.
- **Collection size:** 220 source videos: 177 regular and 43 JIT. The paper reports 11,528 minutes, with that unit retained despite the unresolved conflict; trustworthy total hours are unknown. The 3,717 derived action clips are not 3,717 independent procedures.
- **Potential applications:** Emergency-procedure action recognition; Action anticipation; Hand tracking; Medical tool detection; Medical visual question answering.
- **Modalities / available information:** Egocentric RGB, temporal action labels, hand boxes, tool boxes, and medical QA; hand tracking covers a 30-video subset.
- **Dataset family:** Trauma THOMPSON
- **Access evidence:** Gated, as checked on 2026-10-24: the official README requires a usage-consent form that redirects to download links after submission; the paper also points to Harvard Dataverse. No form was submitted and no download was tested.
- **License observations:** The README footer states CC BY 4.0, while its VQA example JSON states CC BY-NC-SA 4.0. This licensing conflict requires package/platform-specific or author confirmation; a single permissive license cannot be claimed for the entire dataset.
- **Caveats:** Do not silently replace the reported minutes with seconds, convert the reported second-based means to minutes as a unit correction, or divide 11,528 by 60 to claim a verified hour total. Per-procedure-category means are not per-sample duration extrema. Distinguish simulated source procedures from derived action clips. These are simulated demonstrations, not natural emergency-patient recordings, and the conflicting total does not establish long-horizon coverage. JIT changes tool resources and does not itself indicate a violation. Native procedural-error intervals and optimal emergency decision labels were not established. The README and VQA example also disagree on licensing.

**Primary links** · Source review: 2026-10-24 · Duration audit: 2026-10-31

- [Trauma THOMPSON official repository](https://github.com/purdue-isat/TT)
- [An Egocentric Life-Saving Interventional Procedure Dataset of Actions, Medical Questions, Maneuvers and Tools, Data Overview and Video duration](https://www.nature.com/articles/s41597-025-06365-y)
