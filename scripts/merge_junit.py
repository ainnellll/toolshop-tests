import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def main(src: str, out: str) -> int:
    files = sorted(Path(src).rglob("junit.xml"))
    if not files:
        print(f"Не найдено ни одного junit.xml в {src}")
        return 1

    merged = ET.Element("testsuites", name="pytest tests (merged)")
    totals = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0}
    for f in files:
        root = ET.parse(f).getroot()
        suites = [root] if root.tag == "testsuite" else root.findall("testsuite")
        for suite in suites:
            merged.append(suite)
            for key in totals:
                totals[key] += int(suite.get(key, 0))
    for key, value in totals.items():
        merged.set(key, str(value))

    out_path = Path(out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(merged).write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Склеено {len(files)} файлов -> {out_path}: {totals}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))