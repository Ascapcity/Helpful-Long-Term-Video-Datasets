# Contributing

Contributions that improve source quality, correct a duration, clarify a release, or add an appropriate resource are welcome.

## Update a record

Edit `data/datasets.json`, then run:

```bash
python scripts/build_catalog.py
python scripts/validate_catalog.py
```

The README, category pages, and CSV are generated from the JSON. Commit generated changes together with the data change. Python 3.10 or newer is sufficient; no third-party package is required.

## Evidence checklist

- Prefer original papers, official dataset pages, author repositories, and released metadata.
- Include the precise version and a source URL for numerical claims.
- State whether a duration describes a full video, execution, clip, action, annotation interval, or memory span.
- Preserve distinctions between means, standard deviations, ranges, upper bounds, and inferred statistics.
- Document parent-dataset relationships and potential overlap.
- Describe access and license evidence separately. A working project page is not proof that data were downloaded.
- Mark unknowns and conflicting source statistics explicitly.
- Explain how the resource supports state tracking, procedural understanding, decisions, failures, assistance, or a useful comparison.
- Write all published content in English. Do not upload private samples, tokens, or restricted media.

Use an issue to propose a correction when the evidence is incomplete. Include the record ID, affected statement, proposed replacement, and a primary-source link. Changes to dataset counts or categories also require updating the validation expectations and this collection's scope description.
