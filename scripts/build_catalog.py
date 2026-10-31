"""Generate the public Markdown catalog and CSV from the English JSON records."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Helpful Long-Term Video Datasets Are You Need For VLM/MLLM Reasoning"
CATEGORIES = [
    ("industrial", "Industrial Assembly and Maintenance", "Assembly, disassembly, maintenance, tool use, and human-robot collaboration."),
    ("egocentric", "Egocentric and Instructional Procedures", "Cooking, daily activities, skill learning, instructional videos, and first-person task progress."),
    ("robotics", "Robotics and Embodied Interaction", "Real and simulated robot episodes, demonstrations, manipulation, planning, and recovery."),
    ("medical", "Medical and Laboratory Workflows", "Surgical procedures, operating rooms, laboratory protocols, and specialist execution quality."),
    ("errors", "Errors, Anomalies, and Safety", "Procedural mistakes, unintentional actions, quality assessment, traffic incidents, and surveillance comparisons."),
    ("frontier", "Emerging Benchmarks and Watchlist", "Recent egocentric reasoning, assistance, grounding, and synthetic diagnostics; access and task scope vary."),
    ("streaming", "Long Video, Streaming, and Proactive Assistance", "Long-context memory, online understanding, causal reasoning, and timely assistance."),
]
ROLE = {"core-candidate": "Core candidate", "auxiliary": "Auxiliary", "comparison": "Comparison", "watchlist": "Watchlist"}

def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")

def link_name(text):
    return text.replace("[", "\\[").replace("]", "\\]")

def write(path, text):
    path.write_text(text.rstrip() + "\n", encoding="utf-8")

def main():
    data = json.loads((ROOT / "data/datasets.json").read_text(encoding="utf-8-sig"))
    count = Counter(r["category"] for r in data)
    readme = [
        f"# {TITLE}",
        "",
        "A source-linked collection for **long-term video understanding, procedural reasoning, environment-state tracking, next-step decisions, error detection, and proactive assistance** with vision-language models (VLMs) and multimodal large language models (MLLMs).",
        "",
        f"**{len(data)} records · 7 categories · English descriptions · Qualified duration statistics · JSON / CSV exports**",
        "",
        "> **Scope matters:** these are not all long videos, and they are not 94 independent video corpora. The collection also includes short procedural sequences, derived benchmarks, diagnostic clips, general long-video QA, and watchlist resources. Length and cross-step reasoning difficulty are separate dimensions.",
        "",
        "**Source review:** October 24, 2026. **Duration audit:** October 31, 2026. Access and licensing notes retain their own review date; data availability may change. The audit used primary documents and selected metadata, not full-media measurements of every sample. Five emerging entries received an additional [publication spot check](docs/publication-checks.md) on October 31.",
        "",
        "## Browse by category",
        "",
        "| Category | Records | Main focus |",
        "| --- | ---: | --- |",
    ]
    for slug, title, description in CATEGORIES:
        readme.append(f"| [{title}](catalog/{slug}.md) | {count[slug]} | {description} |")
    readme += [
        "",
        "## How to use this resource",
        "",
        "1. Choose a category above, or scan the complete dataset index below.",
        "2. Open a dataset's detailed entry for its content, qualified duration, collection size, potential applications, modalities, upstream family, access notes, caveats, and primary links.",
        "3. Read the [methodology and duration rules](docs/methodology.md) before comparing lengths or treating a record as benchmark-ready.",
        "4. Download the [JSON catalog](data/datasets.json) or [CSV table](data/datasets.csv) for your own filtering. See the [field definitions](docs/data-format.md).",
        "",
        "### Choose by the reasoning problem",
        "",
        "| Research question | Useful places to start | What to check |",
        "| --- | --- | --- |",
        "| Which step is happening, and what state has changed? | [Industrial](catalog/industrial.md), [egocentric](catalog/egocentric.md), [medical](catalog/medical.md) | Full execution coverage, step boundaries, object states, and prerequisites. |",
        "| What should the actor do next? | [Robotics](catalog/robotics.md), [egocentric](catalog/egocentric.md) | Future-action targets, valid alternatives, goals, and whether a policy is actually evaluated. |",
        "| Did an execution fail, and how can it recover? | [Errors and safety](catalog/errors.md), [industrial](catalog/industrial.md) | Error onset, causes, recovery labels, normal controls, and real versus synthetic failures. |",
        "| What earlier evidence matters now? | [Long video and streaming](catalog/streaming.md) | Continuous recording versus memory span, query timing, and source-video overlap. |",
        "| When should an assistant intervene? | [Streaming and assistance](catalog/streaming.md), [emerging benchmarks](catalog/frontier.md) | Causal access to past frames, intervention timing, and access to released annotations. |",
        "",
        "### Reading the labels",
        "",
        "**Core candidate** means promising for the target research questions; **Auxiliary** supports a component; **Comparison** provides a related baseline; **Watchlist** requires unresolved evidence or access checks. These are editorial relevance assessments, not certifications of long duration, complete labels, or download readiness. Suggested applications may require additional annotation.",
        "",
        "A **mean** is not a range; **SD** is not a min/max bound; accumulated multi-view hours are not independent execution hours. A short evaluation window is not the length of its parent recording. Unknown values and conflicting statistics are preserved in detailed entries.",
        "",
        "## Complete dataset index",
        "",
        "Click a dataset name for its full description and primary links. The duration column is a navigation aid; the detailed entry defines the version, unit, and evidence limitations.",
    ]
    for slug, title, description in CATEGORIES:
        rows = [r for r in data if r["category"] == slug]
        readme += ["", f"### {title}", "", description, "", "| Dataset | Duration summary | Suggested focus |", "| --- | --- | --- |"]
        page = [f"# {title}", "", f"[Back to the collection](../README.md) · [Duration methodology](../docs/methodology.md) · [JSON data](../data/datasets.json)", "", description, "", f"**{len(rows)} records.** Suggested applications are editorial research directions; consult annotations and caveats before assuming native task support.", "", "## Contents", ""]
        for r in rows:
            focus = "; ".join(r["tasks"][:2])
            readme.append(f"| [{cell(link_name(r['name']))}](catalog/{slug}.md#{r['id']}) | {cell(r['duration_short'])} | {cell(focus)} |")
            page.append(f"- [{r['code']} · {link_name(r['name'])}](#{r['id']})")
        for r in rows:
            page += ["", "---", "", f'<a id="{r["id"]}"></a>', "", f"## {r['code']} · {r['name']}", "", f"**{ROLE[r['role']]}** · **Year / version:** {r['year']}", "", r["summary"], "", f"- **Duration:** {r['duration']}", f"- **Collection size:** {r['total']}", f"- **Potential applications:** {'; '.join(r['tasks'])}.", f"- **Modalities / available information:** {r['modalities']}", f"- **Dataset family:** {r['family']}", f"- **Access evidence:** {r['access']}", f"- **License observations:** {r['license']}", f"- **Caveats:** {r['caveats']}", "", f"**Primary links** · Source review: {r['source_checked_on']} · Duration audit: {r['duration_checked_on']}", ""]
            for src in r["sources"]:
                page.append(f"- [{link_name(src['title'])}]({src['url']})")
        write(ROOT / f"catalog/{slug}.md", "\n".join(page))
    readme += [
        "",
        "## Contribute and maintain",
        "",
        "Corrections with primary-source evidence are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the editing workflow, [data-format.md](docs/data-format.md) for the schema, and [CHANGELOG.md](CHANGELOG.md) for release notes.",
        "",
        "The JSON is the editable source of truth. Regenerate the readable catalog and CSV with:",
        "",
        "```bash",
        "python scripts/build_catalog.py",
        "python scripts/validate_catalog.py",
        "```",
        "",
        "## Attribution and data rights",
        "",
        "Please cite the original dataset papers and follow each provider's current terms. This repository contains catalog descriptions and source links; it does not redistribute videos, private industrial data, or full papers. Code licenses and dataset licenses can differ. Inclusion here grants no rights to the underlying media.",
        "",
        "Maintained by [Ascapcity](https://github.com/Ascapcity). The original source review and duration audit are dated separately to make future corrections traceable.",
    ]
    write(ROOT / "README.md", "\n".join(readme))
    fields = list(data[0].keys())
    with (ROOT / "data/datasets.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in data:
            flat = dict(row)
            flat["tasks"] = "; ".join(row["tasks"])
            flat["sources"] = " | ".join(s["url"] for s in row["sources"])
            writer.writerow(flat)
    print(f"Generated README, {len(CATEGORIES)} category pages, and CSV for {len(data)} records.")

if __name__ == "__main__":
    main()

