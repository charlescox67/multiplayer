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
    {
        "name": "Katheryn Hunt",
        "title": "Founder & CEO",
        "company": "GROW Marketing Agency (St. Louis, MO)",
        "profile_link": "https://www.linkedin.com/in/katherynhunt/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Founder/CEO of a small digital marketing agency (web design, digital "
            "marketing, branding). Confirmed small: 1-10 employees per Crunchbase, "
            "~17 per ContactOut -- either way solidly inside the 5-50 band."
        ),
        "match_reason": (
            "Confirmed small-agency founder wearing the ops hat -- one of the "
            "cleanest company-size confirmations in this batch."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Adam Goyette",
        "title": "Founder",
        "company": "Growth Union (Chicago) -- boutique growth agency for early-stage B2B SaaS",
        "profile_link": "https://www.linkedin.com/in/adam-goyette/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Ex-Help Scout / G2 growth marketing exec, now runs a small agency "
            "assembling senior marketers for early-stage B2B SaaS clients (Writer, "
            "RevenueHero, Recorded Future named as clients). Exact employee count "
            "unconfirmed but the agency's model (small senior team, no bench) implies "
            "well under 50."
        ),
        "match_reason": (
            "Founder running a lean agency serving exactly the small-SaaS client base "
            "multiplayer targets; company size inferred from agency model, not directly "
            "confirmed -- worth a second look before approving."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "David Malevsky",
        "title": "Co-Founder",
        "company": "Lynx Growth Agency (Hallandale Beach, FL)",
        "profile_link": "https://www.linkedin.com/in/david-malevsky/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Co-founder of a boutique agency (patient acquisition for regenerative/"
            "integrative clinics) built around AI-driven marketing and automation. "
            "Employee count unconfirmed -- RocketReach shows only a handful of "
            "verified staff, consistent with a small shop."
        ),
        "match_reason": (
            "Self-describes as 'resolving business challenges using AI' -- co-founder "
            "at a small, AI-forward agency is a strong qualitative fit even though the "
            "exact headcount isn't independently confirmed."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Alex Zlotko",
        "title": "CEO",
        "company": "Forecastio (B2B sales forecasting for HubSpot)",
        "profile_link": "https://www.linkedin.com/in/alexzlotko/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "17 years in B2B sales/CS, now CEO of Forecastio, a small SaaS company "
            "building sales forecasting tools. Publishes regularly on AI agents in "
            "RevOps specifically."
        ),
        "match_reason": (
            "Small SaaS founder/CEO already writing publicly about AI agents in "
            "RevOps -- direct thematic overlap with multiplayer's pitch, though exact "
            "headcount at Forecastio is unconfirmed."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Kristofer Wille",
        "title": "RevOps Consultant & Advisor",
        "company": "Independent -- RevOpsVision (Berlin)",
        "profile_link": "https://www.linkedin.com/in/kriswille-revopsvision-revenue-operations-consultant-advisory/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "10+ years in SalesOps/RevOps in Berlin's startup scene. Self-positions "
            "explicitly as helping 'C-Level Leaders & Startups Supercharge Their "
            "Small RevOps Teams' -- his own tagline names the exact ICP."
        ),
        "match_reason": (
            "His public positioning IS the ICP description almost word-for-word "
            "(small RevOps teams at startups). Company size self-described, not "
            "independently verified."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Donna Sluijter",
        "title": "Startup Operator -- RevOps & Strategy",
        "company": "Independent / embedded RevOps for startups",
        "profile_link": "https://www.linkedin.com/in/donnasluijter/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Self-describes as a 'Startup Operator' bridging gaps and scaling teams "
            "in RevOps and strategy roles -- language that matches the ICP's "
            "'founder wearing every hat' profile."
        ),
        "match_reason": (
            "Title and self-description line up with the ICP almost exactly; "
            "specific current employer/headcount not independently confirmed."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "John McArdle",
        "title": "Founder",
        "company": "Sequoia Solutions -- RevOps/HubSpot consultancy for early-stage B2B tech",
        "profile_link": "https://www.linkedin.com/in/john-mcardle-m-s-71b58178/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Founded a small consultancy that has worked with dozens of early-stage "
            "companies cleaning up CRM/HubSpot data and building GTM systems -- "
            "not the 'Sequoia' VC firm, a separate small boutique of the same name."
        ),
        "match_reason": (
            "Founder-led small consultancy serving exactly the early-stage company "
            "band multiplayer targets."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Roberto Guerra",
        "title": "Founder",
        "company": "Revenue Hub Latam -- RevOps + HubSpot for B2B companies in LATAM",
        "profile_link": "https://www.linkedin.com/in/robguerra/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Runs a boutique RevOps/HubSpot consultancy for B2B companies across "
            "LATAM, publicly writing about pipeline, CRM, forecasting -- and AI."
        ),
        "match_reason": (
            "Boutique consultancy founder already writing about AI in the RevOps "
            "workflow -- direct thematic and company-stage fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Kristy Buige",
        "title": "Founder",
        "company": "Boutique RevOps consultancy -- B2B SaaS GTM systems",
        "profile_link": "https://www.linkedin.com/in/kristybuige/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Founded and leads a boutique RevOps consultancy enabling B2B SaaS "
            "companies to scale GTM systems, processes, and revenue performance."
        ),
        "match_reason": (
            "Founder of a small consultancy serving the same small-SaaS client "
            "base as several other rows in this sheet -- exact company name/size "
            "not independently confirmed beyond 'boutique.'"
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Johnathan Wang",
        "title": "Founder",
        "company": "The SaaS Consultants -- fractional CMO / marketing agency for SaaS",
        "profile_link": "https://www.linkedin.com/in/johnathan-wang/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Runs a small fractional-CMO agency for SaaS businesses and has "
            "personally built social-media-management software using Python/"
            "JavaScript and AI -- technical enough to be a strong early adopter."
        ),
        "match_reason": (
            "Small agency founder who is also hands-on technical/AI-building -- "
            "good combination of ICP fit and early-adopter likelihood."
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
    {
        "name": "Mike Rizzo",
        "title": "Founder & CEO",
        "company": "MarketingOps.com / MO Pros",
        "profile_link": "https://www.linkedin.com/in/mikedrizzo/",
        "contact_method": "LinkedIn only (no public email found)",
        "summary": (
            "Founded and runs MO Pros, the 4,000+ member marketing-ops community "
            "outreach-pipeline-context.md names directly as a target community. "
            "Certifies GTM Ops teams and runs the annual MOpza conference."
        ),
        "match_reason": (
            "Not a cold-outreach target -- he IS the gatekeeper of the exact "
            "community your context doc lists as a source. Worth a warmer, separate "
            "approach (community partnership / sponsorship) rather than a first-touch "
            "DM template."
        ),
        "status": "",
        "date_found": TODAY,
    },
]
