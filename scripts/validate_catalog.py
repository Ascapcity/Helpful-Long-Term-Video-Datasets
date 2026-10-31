"""Check record coverage, public language, source structure, and local links."""
import csv
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"industrial": 11, "egocentric": 18, "robotics": 15, "medical": 11, "errors": 18, "frontier": 8, "streaming": 13}
REQUIRED = {"id", "code", "name", "category", "year", "role", "summary", "duration", "duration_short", "total", "tasks", "modalities", "access", "license", "family", "caveats", "sources", "source_checked_on", "duration_checked_on"}

def main():
    data = json.loads((ROOT / "data/datasets.json").read_text(encoding="utf-8-sig"))
    errors = []
    def check(ok, message):
        if not ok:
            errors.append(message)
    check(len(data) == 94, "Expected 94 initial records; update the scope explicitly when expanding.")
    check(len({r["id"] for r in data}) == len(data), "Duplicate dataset IDs")
    check(len({r["code"] for r in data}) == len(data), "Duplicate checklist codes")
    check(dict(Counter(r["category"] for r in data)) == EXPECTED, "Unexpected category counts")
    source_count = 0
    for row in data:
        key = row["id"]
        check(set(row) == REQUIRED, f"{key}: field mismatch")
        check(row["role"] in {"core-candidate", "auxiliary", "comparison", "watchlist"}, f"{key}: invalid role")
        for field in REQUIRED:
            check(bool(row.get(field)), f"{key}: empty {field}")
        check(isinstance(row["tasks"], list), f"{key}: tasks must be a list")
        check(len(row["duration_short"]) <= 140, f"{key}: overly long duration summary")
        urls = [s["url"] for s in row["sources"]]
        check(len(set(urls)) == len(urls), f"{key}: duplicate source URL")
        for src in row["sources"]:
            parsed = urlparse(src["url"])
            check(parsed.scheme in {"https", "http"} and bool(parsed.netloc), f"{key}: invalid source URL")
            check(bool(src["title"]), f"{key}: missing source label")
        source_count += len(urls)
        for field in ("source_checked_on", "duration_checked_on"):
            check(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", row[field])), f"{key}: invalid date")
        page = (ROOT / "catalog" / f"{row['category']}.md").read_text(encoding="utf-8")
        check(page.count(f'<a id="{key}"></a>') == 1, f"{key}: missing or repeated anchor")
    with (ROOT / "data/datasets.csv").open(encoding="utf-8", newline="") as f:
        csv_rows = list(csv.DictReader(f))
    check([r["id"] for r in csv_rows] == [r["id"] for r in data], "CSV coverage/order mismatch")
    public = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "CHANGELOG.md", *sorted((ROOT / "docs").glob("*.md")), *sorted((ROOT / "catalog").glob("*.md")), ROOT / "data/datasets.json", ROOT / "data/datasets.csv"]
    local_links = 0
    for path in public:
        text = path.read_text(encoding="utf-8-sig")
        check(not re.search(r"[\u3400-\u9fff]", text), f"{path.name}: non-English CJK text")
        check("\ue200" not in text and "\ue202" not in text, f"{path.name}: internal citation token")
        check(not re.search(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|[CD]:[\\/])", text), f"{path.name}: possible secret or local path")
        if path.suffix != ".md":
            continue
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith(("https://", "http://", "mailto:")):
                continue
            filepart, _, anchor = target.partition("#")
            dest = (path.parent / unquote(filepart)).resolve() if filepart else path
            check(dest.exists(), f"{path.name}: missing local target {target}")
            if anchor and dest.exists():
                contents = dest.read_text(encoding="utf-8-sig")
                check(f'<a id="{anchor}"></a>' in contents, f"{path.name}: missing anchor {target}")
            local_links += 1
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(data)} records, 7 categories, {source_count} source references, {local_links} local links; English-only content and CSV alignment verified.")
    print("This validator checks structure and local navigation; it does not certify external-link uptime or dataset-download availability.")

if __name__ == "__main__":
    main()
