# Outreach, Pipeline 1 (The Finder)

Standalone from the product build (see `outreach-pipeline-context.md`). Finds
people who match the ICP, writes them to `leads.xlsx` for Charles to review,
and stops there. No automated sending happens in this repo.

There is no product yet. The draft messages this generates are research asks,
not a pitch: how does this person's team actually use AI day to day, and is
there any shared visibility across teammates, or does it stay solo. That's
input to deciding what to build, not a trial invite.

## Run it

```bash
pip install -r requirements.txt
python3 finder.py
```

Regenerates `leads.xlsx` from `leads_seed.py`. Both tabs are written sorted by
Confidence, high to low.

## What's in the sheet

- **Leads tab**, people who plausibly are the ICP themselves (5-50 person
  team, ops-adjacent title or a founder wearing that hat). This is the
  approval queue.
- **Connectors tab**, marketing-ops community voices (newsletter authors,
  etc.) who reach the ICP audience but aren't a direct lead themselves. Kept
  separate so they don't get approved for cold outreach by mistake.
- **Confidence column**, derived from the caveats already written into each
  row's Profile Summary and Match Reason (an explicit "confirmed" headcount
  or accelerator batch reads high; "unconfirmed," "self-described," or
  "single search snippet" reads low; everything else is medium). It's a
  readout of what's already on the record per row, not a separate score.

Every row starts with `Status` blank. Per the approval gate in
`outreach-pipeline-context.md`, Charles is the one who marks rows `Approved`
before anything moves to a first-touch message. Nothing here does that
automatically.

## Current batch

150 leads + 3 connectors, found via manual web search across several
sessions (see the docstring in `leads_seed.py` for exactly how each was
verified). The ICP signal `outreach-pipeline-context.md` originally asked for
("2-3+ people on a team independently using ChatGPT/Claude with no shared
visibility") essentially never surfaces through plain web search;
LinkedIn/Reddit posts with that specific pain point aren't indexed well
enough to find that way. What plain search *does* surface reliably: real
people whose public title, company, or accelerator batch fits the ICP
profile, and increasingly, YC/Techstars-backed co-founders whose company
stage is public record rather than self-described.

## Why there's no scraper

`outreach-pipeline-context.md` explicitly flags automated LinkedIn scraping
(even small-volume, non-API) as a ToS/ban risk, and automated mass texting as
TCPA exposure. So `finder.py` has no scraping or login logic, it only formats
whatever rows you feed it into the approval sheet. Two ways to get more rows
in:

1. **Manual research** (what produced this batch): append verified rows to
   `leads_seed.py` by hand.
2. **A real sourcing tool Charles runs himself**, e.g. a LinkedIn Sales
   Navigator or Apollo.io export saved as CSV, loaded into the same row shape
   and passed to `write_sheet()` in `finder.py`. That's the realistic path to
   real volume; this session doesn't have access to either.

## Not built here (by design)

Pipeline 2 (first-message drafting + send) is intentionally not started. Per
`outreach-pipeline-context.md`, the send step has to be a separate tool
Charles runs locally under his own LinkedIn login, not something this
session can build or run.
