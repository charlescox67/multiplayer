#!/usr/bin/env python3
"""
Pipeline 1 -- The Finder (see outreach-pipeline-context.md).

Builds outreach/leads.xlsx: one tab of ICP-matching leads for the human approval
gate, one tab of community "connectors" who aren't direct leads. Charles reviews
the Leads tab and sets Status to Approved/Rejected by hand -- nothing here sends
anything or scrapes anything live.

This first run is seeded from outreach/leads_seed.py: rows found via manual web
research this session (see that file's docstring for the verification approach and
its limits). There is intentionally no automated LinkedIn/Reddit scraper wired in --
outreach-pipeline-context.md flags that unofficial LinkedIn automation risks account
bans and that only official APIs or Charles's own logged-in tooling should ever touch
LinkedIn directly. To extend sourcing, either:
  - append more manually-verified rows to leads_seed.py, or
  - point SOURCE_FN at a real data source (e.g. a Sales Navigator / Apollo export
    loaded from CSV) that returns dicts shaped like the ones in leads_seed.py.

Usage:
    pip install -r outreach/requirements.txt
    python3 outreach/finder.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, str(Path(__file__).parent))
from leads_seed import CONNECTORS, LEADS  # noqa: E402

COLUMNS = [
    ("name", "Name", 22),
    ("title", "Title", 34),
    ("company", "Company", 38),
    ("profile_link", "Profile / Post Link", 46),
    ("contact_method", "Best Contact Method", 26),
    ("summary", "Profile Summary", 55),
    ("match_reason", "Match Reason", 50),
    ("status", "Status", 14),
    ("date_found", "Date Found", 14),
]

HEADER_FILL = PatternFill(start_color="1F2937", end_color="1F2937", fill_type="solid")
HEADER_FONT = Font(color="FFFFFF", bold=True)
WRAP = Alignment(wrap_text=True, vertical="top")
LINK_FONT = Font(color="1155CC", underline="single")


def dedupe(rows: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for row in rows:
        key = row["profile_link"].strip().lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def write_sheet(wb: Workbook, title: str, rows: list[dict]) -> None:
    ws = wb.create_sheet(title)
    for col_idx, (_, header, width) in enumerate(COLUMNS, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        ws.column_dimensions[get_column_letter(col_idx)].width = width
    ws.freeze_panes = "A2"

    for row_idx, row in enumerate(dedupe(rows), start=2):
        for col_idx, (key, _, _) in enumerate(COLUMNS, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=row.get(key, ""))
            cell.alignment = WRAP
            if key == "profile_link" and row.get(key):
                cell.hyperlink = row[key]
                cell.font = LINK_FONT

    if rows:
        status_col = next(i for i, (k, _, _) in enumerate(COLUMNS, start=1) if k == "status")
        dv = DataValidation(type="list", formula1='"Approved,Rejected"', allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{get_column_letter(status_col)}2:{get_column_letter(status_col)}{len(rows) + 1}")


def build(output_path: Path) -> None:
    wb = Workbook()
    wb.remove(wb.active)
    write_sheet(wb, "Leads", LEADS)
    write_sheet(wb, "Connectors", CONNECTORS)
    wb.save(output_path)
    print(f"Wrote {len(dedupe(LEADS))} lead(s) and {len(dedupe(CONNECTORS))} connector(s) to {output_path}")


if __name__ == "__main__":
    build(Path(__file__).parent / "leads.xlsx")
