# Publication spot checks: emerging resources

Five entries received an additional primary-source check on **October 31, 2026**. This was a targeted publication check, not a new audit of all 94 records. Their source-review dates reflect the additional check.

| Resource | Evidence confirmed | Boundary retained |
| --- | --- | --- |
| EgoVoice | The official page schedules code, models, and data for November 2026. | This remains a future release plan at the October 31 cutoff; a paper is not a downloadable dataset. |
| EgoGapBench | Public benchmark JSONL files are present; the main file contains 440 image bundles and 1,000 questions. | Image acquisition was not tested. It is a static-image action-selection benchmark, not a long-video dataset. |
| EgoSafetyBench | The gated dataset manifest lists 1,200 MP4s; the revised paper reports a separate 20-clip real-video sanity check. | Listed files do not prove successful gated downloads. Keep the main synthetic benchmark separate from the small real-video check. |
| EgoTL | The public manifest lists 19 episode-annotation JSON files and 256 MP4 clips. | These are file counts, not 256 independent episodes or proof that all 400 paper-reported episodes were released. |
| LongEgoRefer | A public annotation JSON and dated file history are present; source videos are obtained separately through Ego4D. | Annotation availability does not establish video access, complete annotation integrity, or measured media durations. |

## Primary sources

### EgoVoice

- [Original paper and submission history](https://arxiv.org/abs/2610.12248)
- [Official project and release plan](https://egocentricvoice.github.io/)

### EgoGapBench

- [Original paper](https://arxiv.org/abs/2607.00547)
- [Official repository and acquisition tools](https://github.com/jhCOR/EgoGapBench)
- [Benchmark upload commit](https://github.com/jhCOR/EgoGapBench/commit/6d2d95b67a9834eecf022194f429f78647ae87e4)

### EgoSafetyBench

- [Dataset record](../catalog/frontier.md#egosafetybench) includes the revised paper, official code, and dataset links. Code and dataset licenses are recorded separately.

### EgoTL

- [Original paper](https://arxiv.org/abs/2604.09535)
- [Official project](https://ego-tl.github.io/)
- [Dataset card](https://huggingface.co/datasets/luuuulinnnn/EgoTL-DATA)
- [Public dataset manifest](https://huggingface.co/api/datasets/luuuulinnnn/EgoTL-DATA)
- [Upload history](https://huggingface.co/api/datasets/luuuulinnnn/EgoTL-DATA/commits/main)

### LongEgoRefer

- [Original paper](https://arxiv.org/abs/2607.02096)
- [Official repository](https://github.com/shunya-kato/LongEgoRefer)
- [Annotation documentation](https://github.com/shunya-kato/LongEgoRefer/blob/main/dataset/README.md)
- [Annotation upload commit](https://github.com/shunya-kato/LongEgoRefer/commit/09f49e6499c0ddc1a192d5611f7b3a904e4d0ec5)

## Evidence limits

A commit timestamp establishes repository history, not necessarily the first date of public availability. A current manifest establishes listed artifacts, not successful decoding or complete media coverage. The spot check inspected small annotation files and public metadata; it did not accept gated terms or download large media corpora.

[Back to the collection](../README.md) · [Methodology](methodology.md)
