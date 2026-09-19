"""
Seed data for the outreach Finder pipeline (Pipeline 1 in outreach-pipeline-context.md).

Every row here was found via manual web research (WebSearch tool, no LinkedIn/Reddit
scraping, no automated login) and cross-checked for a real, currently-active public
profile before being added. Nothing in this file is invented -- if a detail (company,
size, contact method) could not be verified, it's marked "Unconfirmed" rather than
guessed.

Two buckets, matching the ICP defined in multiplayer-ai-context.md (companies of
5-50 people, past solo-founder stage, ops-adjacent title or a founder wearing that hat):

LEADS       -- people who plausibly ARE the ICP themselves (run or work inside a
               small team) and are candidates for the actual first-touch outreach.
CONNECTORS  -- marketing-ops community voices (newsletter authors, etc.) who reach
               the ICP audience at scale but are not themselves a 5-50 person buyer.
               Useful for community/content plays, not cold outreach -- kept in a
               separate tab so they don't get mixed into the approval queue by mistake.

Every row starts with Status="" (blank) -- Charles fills in Approved/Rejected by hand
per the approval-gate design in outreach-pipeline-context.md. Nothing here has been
contacted.
"""

from datetime import date

TODAY = date.today().isoformat()

LEADS = [
    {
        "name": "Elizabeth Danowski",
        "title": "Founder — Revenue Operations & Strategy Leader",
        "company": "PrecisionRevOps LLC",
        "profile_link": "https://www.linkedin.com/in/elizabeth-danowski-8b264513/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Runs her own small RevOps consulting practice (PrecisionRevOps LLC) "
            "focused on people/process/technology, CRM migration, and data quality "
            "for SaaS clients. As a solo/small-shop operator she IS the ICP: wearing "
            "every ops hat with no team to share tool context with."
        ),
        "match_reason": (
            "Founder of a small (solo/very small) RevOps consulting shop -- exact "
            "ICP fit on company stage and role. Likely juggling multiple client "
            "workstreams solo, a strong proxy for the 'no shared visibility' pain."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jeremy Lamande",
        "title": "Fractional Head of Revenue Operations",
        "company": "Lamande LLC (fractional RevOps for early/mid-stage SaaS); concurrent fractional roles at Rev, AgentSync, Ekho, OperateWise",
        "profile_link": "https://www.linkedin.com/in/jeremy-lamande/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "20 years building RevOps functions from scratch; now runs Lamande LLC, "
            "a fractional RevOps/CRO practice serving several early-to-mid-stage SaaS "
            "startups at once. LinkedIn 'Top Sales Operations Voice.'"
        ),
        "match_reason": (
            "Runs a small consulting practice AND sits inside multiple small SaaS "
            "teams concurrently (classic 5-50 person startup engagements) -- doubles "
            "as both a direct lead and a channel into several ICP companies at once."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Haris Odobasic",
        "title": "Co-Founder & Revenue Strategy Partner",
        "company": "Revenue Wizards",
        "profile_link": "https://www.linkedin.com/posts/harisodobasic_what-does-revops-do-revenue-operations-activity-7263475951290740736-3JwA",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Co-founder of Revenue Wizards, a small revenue-strategy consulting firm. "
            "Posts regularly on LinkedIn about what RevOps does and removing GTM silos."
        ),
        "match_reason": (
            "Co-founder wearing the ops hat at a small consulting shop; his own "
            "public content (silos, alignment) lines up directly with the "
            "'scattered, untracked work' pitch angle."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Deepa Patel",
        "title": "Fractional Revenue & Strategy Leader",
        "company": "Independent — C-Suite advisor across SaaS/AI/startup clients",
        "profile_link": "https://www.linkedin.com/in/deepa--patel/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "15+ years across RevOps, Marketing Ops, Enablement, Strategy and Finance; "
            "now works independently as a fractional/advisory leader to multiple "
            "high-growth startups at once."
        ),
        "match_reason": (
            "Independent operator serving several small/startup clients in parallel "
            "-- same 'context lost across separate chats' problem multiplied across "
            "accounts rather than teammates."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Mariya Valeva",
        "title": "Fractional CFO",
        "company": "Independent — B2B SaaS clients (~$2M+ ARR)",
        "profile_link": "https://www.linkedin.com/in/mariyavaleva-yourscalingpartner/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Fractional CFO working with early-stage B2B SaaS companies around the "
            "$2M+ ARR mark -- i.e. the 5-50 person stage. Finance/ops-adjacent rather "
            "than pure marketing/sales ops."
        ),
        "match_reason": (
            "Ops-adjacent (finance) leader embedded in multiple small SaaS teams; "
            "weaker fit than the RevOps/MOps rows above but same team-size band and "
            "same fractional-across-many-small-teams dynamic -- worth a lower-priority pass."
        ),
        "status": "",
        "date_found": TODAY,
    },
]

CONNECTORS = [
    {
        "name": "Darrell Alfonso",
        "title": "Author, \"The Marketing Operations Leader\" newsletter",
        "company": "Substack (independent) — background includes marketing ops leadership at Amazon",
        "profile_link": "https://darrellalfonso.substack.com/",
        "contact_method": "Substack / LinkedIn",
        "summary": (
            "Widely-read voice in the marketing-ops community; writes about team "
            "structure, career growth, and AI adoption in MOps. Not himself a 5-50 "
            "person company operator today (large-company background)."
        ),
        "match_reason": (
            "Not a direct ICP lead -- flagged separately as a possible content/community "
            "distribution channel into the exact audience (marketing ops leads at small "
            "teams) rather than a cold-outreach target."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jen Bergren",
        "title": "Author, weekly marketing ops newsletter",
        "company": "Substack (independent)",
        "profile_link": "https://jenbergren.substack.com/",
        "contact_method": "Substack / LinkedIn",
        "summary": (
            "Runs a long-running weekly newsletter for the marketing ops community; "
            "frequently features guest practitioners and AI-adoption discussion."
        ),
        "match_reason": (
            "Same as Darrell Alfonso above -- a distribution/connector play into the "
            "ICP audience, not a direct 5-50 person company lead."
        ),
        "status": "",
        "date_found": TODAY,
    },
]
