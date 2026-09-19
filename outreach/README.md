# Outreach — Pipeline 1 (The Finder)

Standalone from the product build (see `outreach-pipeline-context.md`). Finds and
qualifies ICP leads for multiplayer, writes them to `leads.xlsx` for Charles to
review, and stops there — no automated sending happens in this repo.

## Run it

```bash
pip install -r requirements.txt
python3 finder.py
```

Regenerates `leads.xlsx` from `leads_seed.py`.

## What's in the sheet

- **Leads tab** — people who plausibly are the ICP themselves (5–50 person team,
  ops-adjacent title or a founder wearing that hat). This is the approval queue.
- **Connectors tab** — marketing-ops community voices (newsletter authors, etc.)
  who reach the ICP audience but aren't a direct lead themselves. Kept separate so
  they don't get approved for cold outreach by mistake.

Every row starts with `Status` blank. Per the approval gate in
`outreach-pipeline-context.md`, Charles is the one who marks rows `Approved` before
anything moves to a first-touch message — nothing here does that automatically.

## Current batch (first run)

5 leads + 2 connectors, found via manual web search this session (see the docstring
in `leads_seed.py` for exactly how each was verified). This is a small, honest batch,
not a full pipeline run — the ICP signal `outreach-pipeline-context.md` asks for
("2-3+ people on a team independently using ChatGPT/Claude with no shared visibility")
essentially never surfaces through plain web search; LinkedIn/Reddit posts with that
specific pain point aren't indexed well enough to find that way. What plain search
*does* surface reliably: real people whose public title/company fits the ICP profile
(mostly small-shop and fractional RevOps/MarketingOps operators), which is what's here.

## Why there's no scraper

`outreach-pipeline-context.md` explicitly flags automated LinkedIn scraping (even
small-volume, non-API) as a ToS/ban risk, and automated mass texting as TCPA exposure.
So `finder.py` has no scraping or login logic — it only formats whatever rows you feed
it into the approval sheet. Two ways to get more rows in:

1. **Manual research** (what produced this batch): append verified rows to
   `leads_seed.py` by hand.
2. **A real sourcing tool Charles runs himself**, e.g. a LinkedIn Sales Navigator or
   Apollo.io export saved as CSV, loaded into the same row shape and passed to
   `write_sheet()` in `finder.py`. That's the realistic path to real volume — this
   session doesn't have access to either.

## Not built here (by design)

Pipeline 2 (first-message drafting + send) is intentionally not started. Per
`outreach-pipeline-context.md`, the send step has to be a separate tool Charles runs
locally under his own LinkedIn login — not something this session can build or run.
