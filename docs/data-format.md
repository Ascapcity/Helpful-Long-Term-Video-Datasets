# Data format

`data/datasets.json` is the canonical catalog. `data/datasets.csv` is a flattened export for filtering and manual review. Stable IDs and the original checklist codes allow updates without losing the earlier audit trail.

| Field | Meaning |
| --- | --- |
| `id` | Stable lowercase resource identifier. |
| `code` | Original checklist code, such as `IND-01`. |
| `name` | English display name. |
| `category` | One of industrial, egocentric, robotics, medical, errors, frontier, streaming. |
| `year` | Reported release/paper year or version context, stored as text. |
| `role` | Editorial value: core-candidate, auxiliary, comparison, watchlist. |
| `summary` | Brief description of video content or benchmark construction. |
| `duration` | Full qualified duration statement. |
| `duration_short` | Navigation summary; consult the full field before using a statistic. |
| `total` | Collection size and its counting unit, where documented. |
| `tasks` | Suggested research applications, not a guarantee of native labels. |
| `modalities` | Modalities and available information described in the source review. |
| `access` | Dated access evidence and unresolved download restrictions. |
| `license` | Dated license observations; not legal permission granted by this catalog. |
| `family` | Parent or related dataset relationship, including synthetic origins. |
| `caveats` | Limits, conflicting statistics, and benchmark fit qualifications. |
| `sources` | Deduplicated objects containing an English `title` and an original `url`. |
| `source_checked_on` | ISO date for the broad source review. |
| `duration_checked_on` | ISO date for the duration audit. |

The CSV joins tasks with semicolons and source URLs with ` | `. Fields use descriptive text rather than misleading numeric coercions: an unknown range is not zero, and a mean is not a maximum. The JSON preserves the richer list structures.
