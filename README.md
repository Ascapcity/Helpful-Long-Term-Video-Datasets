# Helpful Long-Term Video Datasets Are You Need For VLM/MLLM Reasoning

A source-linked collection for **long-term video understanding, procedural reasoning, environment-state tracking, next-step decisions, error detection, and proactive assistance** with vision-language models (VLMs) and multimodal large language models (MLLMs).

**94 records · 7 categories · English descriptions · Qualified duration statistics · JSON / CSV exports**

> **Scope matters:** these are not all long videos, and they are not 94 independent video corpora. The collection also includes short procedural sequences, derived benchmarks, diagnostic clips, general long-video QA, and watchlist resources. Length and cross-step reasoning difficulty are separate dimensions.

**Source review:** October 24, 2026. **Duration audit:** October 31, 2026. Access and licensing notes retain their own review date; data availability may change. The audit used primary documents and selected metadata, not full-media measurements of every sample. Five emerging entries received an additional [publication spot check](docs/publication-checks.md) on October 31.

📚 ## Browse by category

| Category | Records | Main focus |
| --- | ---: | --- |
| [Industrial Assembly and Maintenance](catalog/industrial.md) | 11 | Assembly, disassembly, maintenance, tool use, and human-robot collaboration. |
| [Egocentric and Instructional Procedures](catalog/egocentric.md) | 18 | Cooking, daily activities, skill learning, instructional videos, and first-person task progress. |
| [Robotics and Embodied Interaction](catalog/robotics.md) | 15 | Real and simulated robot episodes, demonstrations, manipulation, planning, and recovery. |
| [Medical and Laboratory Workflows](catalog/medical.md) | 11 | Surgical procedures, operating rooms, laboratory protocols, and specialist execution quality. |
| [Errors, Anomalies, and Safety](catalog/errors.md) | 18 | Procedural mistakes, unintentional actions, quality assessment, traffic incidents, and surveillance comparisons. |
| [Emerging Benchmarks and Watchlist](catalog/frontier.md) | 8 | Recent egocentric reasoning, assistance, grounding, and synthetic diagnostics; access and task scope vary. |
| [Long Video, Streaming, and Proactive Assistance](catalog/streaming.md) | 13 | Long-context memory, online understanding, causal reasoning, and timely assistance. |

💡 ## How to use this resource

1. Choose a category above, or scan the complete dataset index below.
2. Open a dataset's detailed entry for its content, qualified duration, collection size, potential applications, modalities, upstream family, access notes, caveats, and primary links.
3. Read the [methodology and duration rules](docs/methodology.md) before comparing lengths or treating a record as benchmark-ready.
4. Download the [JSON catalog](data/datasets.json) or [CSV table](data/datasets.csv) for your own filtering. See the [field definitions](docs/data-format.md).

### Choose by the reasoning problem

| Research question | Useful places to start | What to check |
| --- | --- | --- |
| Which step is happening, and what state has changed? | [Industrial](catalog/industrial.md), [egocentric](catalog/egocentric.md), [medical](catalog/medical.md) | Full execution coverage, step boundaries, object states, and prerequisites. |
| What should the actor do next? | [Robotics](catalog/robotics.md), [egocentric](catalog/egocentric.md) | Future-action targets, valid alternatives, goals, and whether a policy is actually evaluated. |
| Did an execution fail, and how can it recover? | [Errors and safety](catalog/errors.md), [industrial](catalog/industrial.md) | Error onset, causes, recovery labels, normal controls, and real versus synthetic failures. |
| What earlier evidence matters now? | [Long video and streaming](catalog/streaming.md) | Continuous recording versus memory span, query timing, and source-video overlap. |
| When should an assistant intervene? | [Streaming and assistance](catalog/streaming.md), [emerging benchmarks](catalog/frontier.md) | Causal access to past frames, intervention timing, and access to released annotations. |

### Reading the labels

**Core candidate** means promising for the target research questions; **Auxiliary** supports a component; **Comparison** provides a related baseline; **Watchlist** requires unresolved evidence or access checks. These are editorial relevance assessments, not certifications of long duration, complete labels, or download readiness. Suggested applications may require additional annotation.

A **mean** is not a range; **SD** is not a min/max bound; accumulated multi-view hours are not independent execution hours. A short evaluation window is not the length of its parent recording. Unknown values and conflicting statistics are preserved in detailed entries.

👋 ## Complete dataset index

Click a dataset name for its full description and primary links. The duration column is a navigation aid; the detailed entry defines the version, unit, and evidence limitations.

### Industrial Assembly and Maintenance

Assembly, disassembly, maintenance, tool use, and human-robot collaboration.

| Dataset | Duration summary | Suggested focus |
| --- | --- | --- |
| [Assembly101](catalog/industrial.md#assembly101) | Mean 7.1 min (SD 3.4 min); min-max unverified | Action recognition and temporal segmentation; Action anticipation |
| [IndustReal](catalog/industrial.md#industreal) | Derived mean ~4.14 min (5.8 h / 84 videos); min-max unverified | Action recognition; Assembly-state detection |
| [ENIGMA-51](catalog/industrial.md#enigma51) | Derived mean ~25.9 min (rounded 22 h / 51 videos); min-max unverified | Untrimmed hand-object interaction detection; Short-term object interaction anticipation |
| [IMPACT](catalog/industrial.md#impact-industrial) | Derived mean ~4.3 min (~8 independent h / 112 trials); min-max unverified | Step and assembly-state recognition; Anomaly classification and recovery-phase detection |
| [IndEgo](catalog/industrial.md#indego) | Overall mean 205 s; actions <1 min; complete tasks up to 68 min; unified range unreported | Mistake detection; Task understanding and reasoning QA |
| [ATTACH](catalog/industrial.md#attach) | Mean complete assembly 8.2 min; min-max unverified | Per-hand action recognition; Temporal action detection |
| [HA-ViD](catalog/industrial.md#havid) | Mean single-board assembly 1 min 37 s; min-max unverified | Hierarchical action recognition and segmentation; Object detection and tracking |
| [HA4M](catalog/industrial.md#ha4m) | Range ~33.23-242.07 s (frames / 30 fps); reported mean 98.40 s | Action recognition; Temporal action segmentation |
| [IKEA ASM](catalog/industrial.md#ikea-asm) | Mean video ~1.89 min; min-max unverified; mean atomic action ~6 s | Action recognition and segmentation; Human pose estimation |
| [IPAD](catalog/industrial.md#ipad) | Video mean/range unverified; equipment cycles 5-30 s (not video lengths) | Industrial process anomaly detection; Equipment cycle modeling |
| [MECCANO](catalog/industrial.md#meccano) | Range 9.23-35.45 min; conflicting means: text 21.14 min, table 20.79 min | Action recognition; Action anticipation |

### Egocentric and Instructional Procedures

Cooking, daily activities, skill learning, instructional videos, and first-person task progress.

| Dataset | Duration summary | Suggested focus |
| --- | --- | --- |
| [CaptainCook4D](catalog/egocentric.md#captaincook4d) | Recordings: derived mean ~14.766 min; min/max unknown | Procedural error recognition; Step localization |
| [EPIC-Tent](catalog/egocentric.md#epic-tent) | 2019: recording mean 13.6 min; task segments 4.3-24.1 min; 2020 video stats unknown | Action recognition and detection; Step tracking |
| [HoloAssist](catalog/egocentric.md#holoassist) | Sessions: derived mean ~4.484 min (2023 paper); min/max unknown | Mistake detection; Intervention-type prediction |
| [Ego-Exo4D](catalog/egocentric.md#ego-exo4d) | V2 full takes/sessions: min/max/mean unknown; keystep clips are separate | Key-step understanding; Cross-view correspondence |
| [Ego4D Goal-Step](catalog/egocentric.md#ego4d-goal-step) | Video means: goal set ~23 min; step subset ~26 min; min/max unknown | Goal and step temporal localization; Online goal and step detection |
| [HD-EPIC](catalog/egocentric.md#hd-epic) | Full videos: mean 15.9 min, SD 14.5 min; min/max unknown | Action and object understanding; Spatial grounding |
| [50Salads](catalog/egocentric.md#50salads) | Full sequences: mean >5.4 min (derived lower bound); exact mean/min/max unknown | Activity recognition; Action localization |
| [Breakfast Actions](catalog/egocentric.md#breakfast) | Video means, derived: 2014 ~2.323 min; 2016 annotated set ~2.338 min; min/max unknown | Action recognition; Temporal action segmentation |
| [COIN](catalog/egocentric.md#coin) | Source videos: min-max 4.411667-1,236.250167 s; mean 142.341911 s | Instructional step recognition; Temporal step localization |
| [CrossTask](catalog/egocentric.md#crosstask) | Primary: reported mean 4m57s; totals imply ~4.625 min; min/max unknown | Cross-task weakly supervised step localization; Instructional step alignment |
| [Ego4D](catalog/egocentric.md#ego4d) | Full files and continuous sessions: min/max/mean unknown | Object state-change understanding; Hand-object interaction analysis |
| [EgoPlan / EgoPlan-IT / EgoPlan-Bench](catalog/egocentric.md#egoplan) | Per-question history and source-session durations unknown | Goal-conditioned next-action selection; Video-based instruction tuning |
| [EgoPlan-Bench2](catalog/egocentric.md#egoplan-bench2) | Question histories: a few seconds to ~5 min; exact minimum and mean unknown | Goal-conditioned next-action selection; Task-progress reasoning |
| [EPIC Fields](catalog/egocentric.md#epic-fields) | Covered source videos: derived mean ~8.852 min; min/max unknown | 3D reconstruction; Derived spatial grounding |
| [EPIC-KITCHENS-100](catalog/egocentric.md#epic-kitchens) | Full files: min-max 10.477133-3,708.04 s; mean 514.429917 s | Action recognition; Temporal action detection |
| [HowTo100M](catalog/egocentric.md#howto100m) | Source-video and captioned-clip duration distributions unknown | Video-text pretraining; Text-to-video retrieval |
| [HT-Step](catalog/egocentric.md#ht-step) | Source videos: rough derived mean ~6.3 min; min/max unknown | Temporal grounding of article steps; Instruction-video alignment |
| [YouCook2](catalog/egocentric.md#youcook2) | Full videos: mean 5.27 min, maximum ~10 min; minimum unknown | Temporal step localization; Procedural video description |

### Robotics and Embodied Interaction

Real and simulated robot episodes, demonstrations, manipulation, planning, and recovery.

| Dataset | Duration summary | Suggested focus |
| --- | --- | --- |
| [BEHAVIOR-1K / 2025 Challenge Demonstrations](catalog/robotics.md#behavior-1k) | Mean ~396.98 s (6.62 min), derived; episode min-max unknown | Task progress estimation with added step labels; Robot state tracking |
| [RH20T-P / RH20T](catalog/robotics.md#rh20t-p) | Primitive clip and parent episode durations unknown | Temporal primitive recognition; Next-primitive prediction within episodes |
| [RoboFail / REFLECT](catalog/robotics.md#robofail-reflect) | Execution duration unknown; one failure timestamp establishes >=5 min 24 s of history | Failure localization; Failure explanation |
| [TEACh](catalog/robotics.md#teach) | Full gameplay/TfD and local EDH durations unknown | Dialogue-conditioned action prediction; Task state tracking |
| [ALFRED](catalog/robotics.md#alfred) | Full rollout and action/subtask clip durations unknown | Language-conditioned action prediction; Subgoal and step recognition from trajectory alignment |
| [BridgeData V2](catalog/robotics.md#bridgedata-v2) | Trajectory min-max, mean, and typical duration unknown | Language-conditioned action prediction; Trajectory-level task recognition |
| [CALVIN](catalog/robotics.md#calvin) | Training windows: 1-2 s; continuous play-session and task-chain durations unknown | Language-conditioned robot control; Sequential instruction execution |
| [DROID](catalog/robotics.md#droid) | Mean ~16.58 s per trajectory, derived from approximate totals; min-max unknown | Language-conditioned action prediction; General manipulation learning |
| [EgoTV](catalog/robotics.md#egotv) | Trial/video min-max, mean, and typical duration unknown | Egocentric task verification; Compositional generalization |
| [LIBERO / LIBERO-Long](catalog/robotics.md#libero) | Episode durations unknown, including LIBERO-Long | Lifelong robot learning; Language-conditioned manipulation |
| [Open X-Embodiment / RT-X](catalog/robotics.md#open-x-embodiment) | No unified sample duration; per-source min-max and means unknown | Cross-embodiment action learning; Robot policy transfer |
| [RoboCasa / RoboCasa365](catalog/robotics.md#robocasa365) | Human demos: most 10-60 s, some >3 min; derived mean ~40.06 s; min-max unknown | Multistep kitchen manipulation; Task progress estimation in annotated subsets |
| [RoboSet](catalog/robotics.md#roboset) | Trial and complete activity-sequence durations unknown | Robot action prediction; Task-level manipulation recognition |
| [RoboVQA](catalog/robotics.md#robovqa) | Mean: full episode 102 s; medium-horizon segment 14 s; both min-max unknown | Visual question answering about task progress; Intermediate-step recognition |
| [Mobile ALOHA](catalog/robotics.md#mobile-aloha) | Complete mobile-manipulation episode durations unknown | Mobile bimanual imitation learning, subject to data availability; Robot action prediction |

### Medical and Laboratory Workflows

Surgical procedures, operating rooms, laboratory protocols, and specialist execution quality.

| Dataset | Duration summary | Suggested focus |
| --- | --- | --- |
| [LabSuperVision (LSV)](catalog/medical.md#labsupervision) | Full protocols unknown; parsed slices: XM 57-600 s (mean 433.86 s); DJI 0.8-1747 s (mean 176.70 s) | Operation-to-protocol alignment; Protocol issue analysis from metadata |
| [MultiBypass140](catalog/medical.md#multibypass140) | Range 37-178 min; center means 110/72 min; also 111 +/- 33 / 73 +/- 20 min (mean +/- SD) | Surgical phase and step recognition; Intraoperative adverse-event detection and severity assessment |
| [FineBio](catalog/medical.md#finebio) | Mean trial 3.9 min; min-max unknown; mean step 14.3 s; mean atomic operation ~0.9 s | Hierarchical step segmentation; Atomic operation detection |
| [Cholec80](catalog/medical.md#cholec80) | Mean ~38 min (SD 16 min); min-max unknown | Surgical phase recognition; Instrument presence detection |
| [CholecT50](catalog/medical.md#cholect50) | Derived mean annotation coverage ~33.62 min at 1 fps; video min-max unknown | Instrument-verb-target action-triplet recognition; Local surgical interaction analysis |
| [ExpVid](catalog/medical.md#expvid) | Mean: Level 3 ~8 min, Level 2 ~48 s, Level 1 ~8 s; final ranges unknown | Laboratory operation and material understanding; Step ordering and sequence generation |
| [GraSP](catalog/medical.md#grasp) | Range 0.69-3.86 h (rounded endpoints); mean 2.49 h (SD 0.77 h) | Hierarchical surgical phase and step recognition; Instrument instance segmentation |
| [MM-OR](catalog/medical.md#mm-or) | Full procedures typically ~90 min; clips 1-10 min (22), task subset 1-5 min (20) | Operating-room phase and relation-state recognition; Next-action anticipation |
| [PitVis-2023](catalog/medical.md#pitvis) | Mean train/validation 80.0 min; hidden test 66.5 min; both min-max unknown | Surgical step recognition; Instrument recognition |
| [SAR-RARP50](catalog/medical.md#sar-rarp50) | All 50: mean/range unknown; RARP-45 only: ~2-12 min, mean ~5 min | Fine-grained suturing action recognition; Surgical instrument semantic segmentation |
| [Trauma THOMPSON](catalog/medical.md#trauma-thompson) | Reported means 64.96 s regular / 42.48 s JIT; conflicting total; min-max unknown | Emergency-procedure action recognition; Action anticipation |

### Errors, Anomalies, and Safety

Procedural mistakes, unintentional actions, quality assessment, traffic incidents, and surveillance comparisons.

| Dataset | Duration summary | Suggested focus |
| --- | --- | --- |
| [Ego-MC-Bench](catalog/errors.md#qualcomm-mistake-corrections) | Inferred mean ~15 min per recording session; min/max unknown; not measured per video. | Streaming mistake detection; Timely intervention |
| [EgoPER](catalog/errors.md#egoper) | Inferred paper mean ~4.35 min; task means 1.6-9.3 min, not a video range; release duration unknown. | Procedural step segmentation; Procedural error detection |
| [Anomalous Toy Assembly (ATA)](catalog/errors.md#ata) | Inferred mean ~77.5 s per view video; min/max unknown; four views share one execution. | Action segmentation; Unseen sequence anomaly detection |
| [AQA-7](catalog/errors.md#aqa7) | Typical actions <5 s; trampoline ~20 s; not a measured video range; overall mean unknown. | Action quality assessment; Cross-action quality learning |
| [Assembly101-O](catalog/errors.md#assembly101-o) | Derived evaluation-sequence duration unknown; parent Assembly101 statistics do not apply. | Online open-set mistake detection; One-class mistake detection |
| [DADA-2000](catalog/errors.md#dada-2000) | Inferred mean ~10.98 s; Table I implies ~10.83 s; frame-count discrepancy; min/max unknown. | Accident attention prediction; Hazard warning research |
| [DoTA](catalog/errors.md#dota) | Inferred mean ~15.65 s at the released 10 fps; min/max unknown. | Traffic anomaly temporal localization; Traffic anomaly spatial localization |
| [Ego-CoMist](catalog/errors.md#qualcomm-counterfactual-mistakes) | Annotation-row intervals: 10-1,054.969 s; mean 34.2708 s; not independent videos. | Counterfactual instruction-action mismatch training; Corrective feedback generation |
| [EgoErrorVQA](catalog/errors.md#egoerrorvqa) | Selected VQA clip durations unknown; parent full-video durations do not apply. | Procedural error visual question answering; Error-type identification |
| [EgoOops](catalog/errors.md#egooops) | Video mean 8.2 min; task means 1.9-26.1 min, not a video range; step mean 40.7 s. | Text-conditioned mistake recognition; Mistake explanation |
| [EgoProceL](catalog/errors.md#egoprocel) | Reported video mean 769.2 s (~12.82 min); min/max unknown. | Procedure learning; Step ordering |
| [EPIC-Tent / Epic-tent-O](catalog/errors.md#epic-tent-o) | Epic-tent-O duration unknown; parent >7 h total must not be assigned to the derivative. | Online procedural mistake detection; Step recognition |
| [FineDiving](catalog/errors.md#finediving) | Individual-dive duration unknown; 96 sampled model frames do not establish video length. | Action quality assessment; Fine-grained dive phase recognition |
| [MATT-Bench](catalog/errors.md#matt-bench) | Ego4D-M temporal experiment mean ~8 s only; other subsets and overall duration unknown. | Semantic mistake attribution; Ego4D-M temporal mistake attribution |
| [OOPS!](catalog/errors.md#oops) | Mean 9.4 s; median 7.6 s; 3-30 s selection bounds, not measured extrema. | Unintentional action recognition; Intentional-to-unintentional transition localization |
| [ProceL](catalog/errors.md#procel) | Conflicting means: reported 251.5 s vs inferred ~236.5 s; min/max unknown. | Procedure learning; Key-step localization |
| [UCF-Crime](catalog/errors.md#ucf-crime) | Inferred mean ~4.04 min; min/max unknown; surveillance rather than procedural episodes. | Weakly supervised anomaly detection; Temporal anomaly localization |
| [XD-Violence](catalog/errors.md#xd-violence) | Inferred mean ~2.74 min; min/max unknown; untrimmed does not guarantee long videos. | Audiovisual violence detection; Weakly supervised temporal anomaly localization |

### Emerging Benchmarks and Watchlist

Recent egocentric reasoning, assistance, grounding, and synthetic diagnostics; access and task scope vary.

| Dataset | Duration summary | Suggested focus |
| --- | --- | --- |
| [EgoSafetyBench](catalog/frontier.md#egosafetybench) | Main synthetic clips: fixed 5 s (design min=max); chunks 0.5 s | Hazard detection; False-alarm control |
| [EgoSAT](catalog/frontier.md#egosat) | Constructed sessions: roughly 230-300 s; reported mean 296.8 s | Streaming current-action narration; Interaction visibility-switch detection |
| [EgoTL](catalog/frontier.md#egotl) | Task episodes: reported 2-4 min; separate walkthroughs ~2 min; exact extrema unmeasured | Memory-conditioned planning; Environment-conditioned action reasoning |
| [LongEgoRefer](catalog/frontier.md#longegorefer) | Source selection >=20 min; reported mean ~45.248 min; exact min/max unverified | Long-video referring-expression comprehension; Temporal object localization |
| [Minerva-Ego](catalog/frontier.md#minerva-ego) | Video contexts: reported range 10 s-75 min; reported mean 20 min | Multistep video question answering; Temporal and spatial evidence reasoning |
| [EgoGapBench](catalog/frontier.md#egogapbench) | Not applicable: static images, not video | Egocentric action selection; Perspective-sensitive action reasoning |
| [EgoVoice](catalog/frontier.md#egovoice) | Session means, derived: train ~4.405 min; held-out ~4.553 min; min/max unknown | Proactive speech timing; Silence-versus-intervention prediction |
| [ObjChangeVR](catalog/frontier.md#objchangevr) | Typical trajectories: short ~60 s, long ~180 s; not min/max | Object-presence state question answering; Cross-view temporal object memory |

### Long Video, Streaming, and Proactive Assistance

Long-context memory, online understanding, causal reasoning, and timely assistance.

| Dataset | Duration summary | Suggested focus |
| --- | --- | --- |
| [Qualcomm Interactive Cooking](catalog/streaming.md#qic) | Full-video and advanced_planning duration distributions unknown | Cooking progress estimation; Next-step guidance |
| [EgoServe / Vinci2](catalog/streaming.md#egoserve) | Derived means: HoloAssist 4.59 min, CaptainCook4D 12.69 min; EgoLife unknown; min-max unknown | Intervention timing; Proactive guidance generation |
| [CausalVQA](catalog/streaming.md#causalvqa) | QA clips: mean 24.8 s, maximum 288.9 s; minimum unknown | Causal video question answering; Counterfactual outcome reasoning |
| [EgoLife / EgoLifeQA](catalog/streaming.md#egolife) | ~50 h of history/person over 7 days; individual file min-max and mean unknown | Long-term episodic memory; Object and event retrieval |
| [EgoMemReason v1.1](catalog/streaming.md#egomemreason) | Video/prefix durations unknown; 25.9 h mean memory backtracking is not video length | Cross-day state accumulation; Event ordering |
| [HourVideo](catalog/streaming.md#hourvideo) | Video range: 20-120 min; reported mean ~45.7 min | Long-video question answering; Historical evidence retrieval |
| [LongVideoBench](catalog/streaming.md#longvideobench) | Design groups span 8 s-60 min; mean 473 s (~7.88 min); exact observed min-max unreported | Referring video question answering; Long-context evidence retrieval |
| [OVBench / VideoChat-Online](catalog/streaming.md#ovbench) | Video and evaluation-prefix duration distributions unknown | Online step prediction and verification; Procedure recall |
| [OVO-Bench](catalog/streaming.md#ovo-bench) | Video/clip durations unknown; 263.42 s is mean query timestamp, not video length | Historical event tracing; Real-time visual perception |
| [STORM-Bench](catalog/streaming.md#storm-bench) | Compact-episode and upstream full-recording durations unknown | Online state tracking from video prefixes; Abstention under insufficient evidence |
| [StreamingBench](catalog/streaming.md#streamingbench) | Full duration unknown; main context is 60 s before each query; All Context varies | Real-time video understanding; Audiovisual question answering |
| [Video-MME v1](catalog/streaming.md#video-mme) | v1 range: 11 s-1 h; derived mean ~16.93 min | Multi-domain video question answering; Short-, medium-, and long-context comparison |
| [EgoStream (Forte, Lando, and Furnari)](catalog/streaming.md#egostream) | Video/subclip/prefix durations unknown; immediate to >8 h describes recall delay | Streaming episodic memory evaluation; Answer-validity tracking |

## Contribute and maintain

Corrections with primary-source evidence are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the editing workflow, [data-format.md](docs/data-format.md) for the schema, and [CHANGELOG.md](CHANGELOG.md) for release notes.

The JSON is the editable source of truth. Regenerate the readable catalog and CSV with:

```bash
python scripts/build_catalog.py
python scripts/validate_catalog.py
```

## Attribution and data rights

Please cite the original dataset papers and follow each provider's current terms. This repository contains catalog descriptions and source links; it does not redistribute videos, private industrial data, or full papers. Code licenses and dataset licenses can differ. Inclusion here grants no rights to the underlying media.

Maintained by [Ascapcity](https://github.com/Ascapcity). The original source review and duration audit are dated separately to make future corrections traceable.
