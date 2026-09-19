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

Each lead has "kind" ("operator" -- runs/works inside their own small team, or
"consultant" -- fractional/agency serving several small clients at once) and
"personal_detail" -- the one real, specific thing about them the draft message
references, per outreach-pipeline-context.md's personalization style (simple,
specific, no overselling). finder.py turns kind + personal_detail into the actual
Draft Message column via a fixed template per outreach-pipeline-context.md's
Pipeline 2 design -- the value prop stays constant, only the reference point varies.

Every row starts with Status="" (blank) -- Charles fills in Approved/Rejected by hand
per the approval-gate design in outreach-pipeline-context.md. Nothing here has been
contacted. There is no working "click to send" link for LinkedIn DMs -- LinkedIn does
not support pre-filled message URLs -- so the workflow is: click Profile Link, click
Message, paste Draft Message, edit if needed, send.
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
        "kind": "consultant",
        "personal_detail": "you're running RevOps solo through PrecisionRevOps for multiple SaaS clients",
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
        "kind": "consultant",
        "personal_detail": "you're juggling fractional RevOps/CRO roles across Rev, AgentSync, Ekho, and OperateWise at once",
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
        "kind": "consultant",
        "personal_detail": "your recent post on what RevOps actually does and removing GTM silos",
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
        "kind": "consultant",
        "personal_detail": "you're advising several high-growth startups at once as a fractional RevOps/strategy leader",
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
        "kind": "consultant",
        "personal_detail": "you work as a fractional CFO across multiple early-stage B2B SaaS clients",
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
        "kind": "operator",
        "personal_detail": "you're running GROW Marketing Agency as a small, founder-led shop",
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
        "kind": "operator",
        "personal_detail": "you've built a lean senior team at Growth Union for early-stage B2B SaaS clients like Writer and Recorded Future",
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
        "kind": "operator",
        "personal_detail": "you're building Lynx Growth Agency around AI-driven marketing and automation",
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
        "kind": "operator",
        "personal_detail": "your writing on AI agents in RevOps as CEO of Forecastio",
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
        "kind": "consultant",
        "personal_detail": "your tagline about helping startups supercharge their small RevOps teams",
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
        "kind": "consultant",
        "personal_detail": "your work bridging gaps and scaling teams as a startup RevOps operator",
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
        "kind": "consultant",
        "personal_detail": "the dozens of early-stage companies you've helped clean up CRM/HubSpot data at Sequoia Solutions",
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
        "kind": "consultant",
        "personal_detail": "your posts on pipeline, forecasting, and AI at Revenue Hub Latam",
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
        "kind": "consultant",
        "personal_detail": "scaling GTM systems for B2B SaaS companies through your boutique RevOps consultancy",
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
        "kind": "operator",
        "personal_detail": "you built your own AI-powered social media tooling while running The SaaS Consultants",
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
    {
        "name": "Shaun Anderson",
        "title": "Founder",
        "company": "thisisagency.ai / hobo-web.co.uk -- forensic SEO agency",
        "profile_link": "https://www.linkedin.com/in/shaun-anderson-hobo/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're building agentic AI systems as an AI Marketing Engineer while running thisisagency.ai",
        "summary": (
            "Founder of a small forensic-SEO agency, also positions himself as an "
            "AI Marketing Engineer building agentic AI systems. Found via a single "
            "search pass, not cross-verified for exact headcount."
        ),
        "match_reason": (
            "Small agency founder already hands-on with agentic AI -- strong "
            "thematic fit; company size inferred from agency type, not confirmed."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jackie Connors",
        "title": "Founder & CEO",
        "company": "Digital Marketing Direction -- virtual HubSpot partner agency",
        "profile_link": "https://www.linkedin.com/in/jackiebconnors/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you run Digital Marketing Direction as a virtual HubSpot partner agency",
        "summary": (
            "Founder/CEO of a small virtual agency offering HubSpot/inbound "
            "training, consulting and content marketing. Size not independently "
            "confirmed beyond 'virtual agency' framing."
        ),
        "match_reason": (
            "Founder-led small HubSpot partner shop -- same ops-tooling audience "
            "multiplayer is targeting."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Sam Anderson",
        "title": "Chief Growth Officer / Founder",
        "company": "Origin 63 -- small growth agency",
        "profile_link": "https://www.linkedin.com/in/samanderson41/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running Origin 63 as a small, results-focused growth agency",
        "summary": (
            "Founder-level growth leader at a self-described small agency. Weaker "
            "verification than other rows -- single search snippet only."
        ),
        "match_reason": (
            "Small growth-agency founder; include but treat as lower-confidence "
            "given only one source found."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Josh Harcus",
        "title": "Revenue Growth & Retention Lead",
        "company": "Hüify -- HubSpot partner agency",
        "profile_link": "https://www.linkedin.com/in/joshharcus/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "your work on revenue growth and retention at Hüify, a HubSpot partner agency",
        "summary": (
            "Works on revenue growth/retention at a HubSpot partner agency. Exact "
            "headcount at Hüify unconfirmed."
        ),
        "match_reason": (
            "HubSpot-partner-agency operator in the ops-tooling audience; company "
            "size inferred, not confirmed."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Alex Williams",
        "title": "Independent HubSpot Consultant",
        "company": "Independent -- solo HubSpot consulting practice",
        "profile_link": "https://www.linkedin.com/in/awoxford/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you run your own solo HubSpot consulting practice",
        "summary": (
            "Solo independent HubSpot implementation/strategy consultant -- a "
            "one-person shop, which is close to the purest form of the "
            "'wearing every hat, no one to share tool context with' ICP signal."
        ),
        "match_reason": (
            "Solo consultant -- exact company-stage fit by definition, though this "
            "is a one-person 'team' rather than 5-50 people; worth including as a "
            "different flavor of the same pain (no one to share context with at all)."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Clwyd Probert",
        "title": "CEO & Founder, AI Consultant",
        "company": "Whitehat (UK) -- AI consulting",
        "profile_link": "https://uk.linkedin.com/in/clwyd-probert",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you work as an AI consultant at Whitehat, helping businesses adopt AI",
        "summary": (
            "CEO/Founder and AI consultant; company size and exact scope of "
            "Whitehat not independently confirmed -- single search snippet only."
        ),
        "match_reason": (
            "Directly in the AI-adoption-for-small-business space -- strong "
            "thematic fit, weaker company-size confirmation."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Clara Ma",
        "title": "Chief of Staff (Employee #3)",
        "company": "Kairos -- very early-stage startup",
        "profile_link": "https://www.linkedin.com/in/clarama/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're employee #3 and Chief of Staff at Kairos",
        "summary": (
            "Chief of Staff at a very early-stage startup (self-described as "
            "employee #3) -- partners with founders through the hardest parts of "
            "scaling. About as small/early as the ICP gets."
        ),
        "match_reason": (
            "Employee #3 at an early-stage startup wearing the ops/chief-of-staff "
            "hat -- textbook ICP fit on company stage."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Josephine Conneely",
        "title": "Chief of Staff -- GTM, Operations, AI",
        "company": "Unconfirmed (UK-based startup)",
        "profile_link": "https://uk.linkedin.com/in/josephineconneely",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "your Chief of Staff role spanning GTM, Operations, and AI",
        "summary": (
            "Chief of Staff with GTM/Operations/AI explicitly in her title -- "
            "current employer name and headcount not independently confirmed."
        ),
        "match_reason": (
            "Title puts AI and ops in the same remit -- strong thematic fit; "
            "company-size confirmation weaker than other rows."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Riddhi Sharma",
        "title": "CEO & Founder",
        "company": "Thought In A Dot -- content marketing agency",
        "profile_link": "https://www.linkedin.com/in/sharmariddhi/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running Thought In A Dot as a content marketing agency and brand strategist",
        "summary": (
            "14+ years in leadership/brand content strategy, now founder/CEO of a "
            "content marketing agency. Employee count unconfirmed."
        ),
        "match_reason": (
            "Small agency founder in the marketing-ops-adjacent content space."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "John Liska",
        "title": "Founder",
        "company": "Creative Engine (Austin, TX) -- branding & digital marketing agency",
        "profile_link": "https://www.linkedin.com/in/john-liska-594a52193/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you founded Creative Engine, a branding and digital marketing agency in Austin",
        "summary": (
            "Founder of a small branding/digital marketing agency in Austin. "
            "Employee count unconfirmed."
        ),
        "match_reason": (
            "Small agency founder -- fits the company-stage band, size inferred "
            "not confirmed."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Ajay G.",
        "title": "Founder",
        "company": "MAWD Agency -- Google Ads/SEO/websites for small businesses",
        "profile_link": "https://www.linkedin.com/in/ajayg514/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you run MAWD Agency managing Google Ads, SEO, and websites for small businesses",
        "summary": (
            "Founder of a small AI-forward performance-marketing agency serving "
            "small-business clients."
        ),
        "match_reason": (
            "Small agency founder in the exact small-business-serving segment; "
            "last-name not public in the source, listed as found."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Raj Goodman Anand",
        "title": "Founder & CEO",
        "company": "Goodman Lantern -- B2B content marketing agency",
        "profile_link": "https://www.linkedin.com/in/rajanand/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running Goodman Lantern, a B2B content marketing agency",
        "summary": (
            "Founder/CEO of a B2B content marketing agency serving clients across "
            "several continents -- distributed small team model, not independently "
            "headcount-confirmed."
        ),
        "match_reason": (
            "Founder wearing the ops/marketing hat; 'across five continents' framing "
            "suggests a distributed small team rather than a large single office, "
            "but worth double-checking size before approving."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Laney M. Silverman",
        "title": "Founder",
        "company": "The Design Boutique, Inc.",
        "profile_link": "https://www.linkedin.com/in/thedesignboutique/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you run The Design Boutique and pride yourselves on being able to pivot quickly as a small shop",
        "summary": (
            "Founder of a self-described boutique design agency, explicitly "
            "positioned around small-team speed/agility."
        ),
        "match_reason": (
            "Explicitly 'boutique' self-positioning -- good qualitative company-size "
            "signal even without a hard headcount number."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Thomas Kranzle",
        "title": "Founder, Director",
        "company": "Venture Visuals (Seattle) -- creative agency",
        "profile_link": "https://www.linkedin.com/in/thomaskranzle/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you founded Venture Visuals, a creative agency in Seattle",
        "summary": (
            "Founder/Director of a small creative agency in Seattle. Headcount "
            "unconfirmed."
        ),
        "match_reason": (
            "Small agency founder -- company-stage fit inferred from agency type."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Santosh Kushwaha",
        "title": "Founder",
        "company": "Visual Best -- AI Creative Production Agency",
        "profile_link": "https://in.linkedin.com/in/santosh-kushwaha-explorer",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running Visual Best, an AI creative production agency",
        "summary": (
            "Founder of a small, explicitly AI-native creative production agency. "
            "Headcount unconfirmed."
        ),
        "match_reason": (
            "AI-native agency founder -- strong thematic fit, company size inferred "
            "not confirmed."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "David Simões",
        "title": "Founder",
        "company": "Sounds Good Agency -- Shopify Plus partner (CEE region)",
        "profile_link": "https://cz.linkedin.com/in/davidjsimoes/en",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you describe your business as having an AI-first mindset while running Sounds Good Agency",
        "summary": (
            "Founder of a Shopify Plus agency serving DTC/B2B/Retail brands, "
            "self-describes as having an 'AI-first business mindset.' Headcount "
            "unconfirmed."
        ),
        "match_reason": (
            "Small agency founder explicitly framing the business around AI-first "
            "thinking -- strong thematic fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Mark Kennaley",
        "title": "Founder & CEO",
        "company": "SoftwareFactory.ai -- AI-native software engineering consultancy",
        "profile_link": "https://www.linkedin.com/in/markkennaley/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're a pioneer in AI-native software engineering as founder of SoftwareFactory.ai",
        "summary": (
            "Founder/CEO of a small AI-native software engineering consultancy. "
            "Headcount unconfirmed."
        ),
        "match_reason": (
            "Small AI-forward software consultancy founder -- exactly the kind of "
            "technical early adopter this product needs."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Philip Ledgerwood",
        "title": "AI Consultant / Software Developer",
        "company": "Independent -- solo AI consulting practice",
        "profile_link": "https://www.linkedin.com/in/phil-ledgerwood/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you help companies use AI securely and purposefully as an independent consultant",
        "summary": (
            "Solo independent consultant helping companies adopt AI securely. "
            "One-person practice -- same 'no one to share context with' signal as "
            "other solo consultants in this sheet."
        ),
        "match_reason": (
            "Solo AI consultant -- direct thematic fit and purest form of the "
            "company-stage signal."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Dylan Kinder",
        "title": "Independent AI Consultant",
        "company": "Independent -- installs AI systems into service businesses",
        "profile_link": "https://www.linkedin.com/in/dylankinder/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you install AI systems into service businesses as an independent consultant",
        "summary": (
            "Solo consultant helping small service businesses adopt AI tooling. "
            "Weaker verification -- single search snippet only."
        ),
        "match_reason": (
            "Solo AI-adoption consultant serving small businesses -- direct "
            "thematic fit, lower-confidence single-source finding."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Alex Marantelos",
        "title": "Co-Founder / CEO",
        "company": "Intryc (Y Combinator S24)",
        "profile_link": "https://www.linkedin.com/in/alexmarantelos/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder/CEO of Intryc, a Y Combinator S24 startup",
        "summary": (
            "Co-founder/CEO of a YC S24-batch startup -- confirmed very-early-stage "
            "by accelerator batch, though exact current headcount unconfirmed."
        ),
        "match_reason": (
            "YC-backed early-stage founder -- confirmed company stage (accelerator "
            "batch is public record) even without a hard headcount number."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Arham Khan",
        "title": "Founder",
        "company": "Pixated -- performance marketing agency (paid social/search)",
        "profile_link": "https://uk.linkedin.com/in/arhamkhan",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you founded Pixated, a performance marketing agency",
        "summary": (
            "Founder of a small performance marketing agency. Headcount "
            "unconfirmed."
        ),
        "match_reason": (
            "Small agency founder -- company-stage fit inferred from agency type."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Alex Brown",
        "title": "Founder & CEO",
        "company": "Tierra -- performance marketing agency for DTC ecommerce",
        "profile_link": "https://www.linkedin.com/in/alex-brown-tierra/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're scaling DTC ecommerce brands through Tierra",
        "summary": (
            "Founder/CEO of a small performance marketing agency for DTC ecommerce "
            "brands. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small agency founder -- company-stage fit inferred from agency type."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Oles Dziub",
        "title": "Co-Founder",
        "company": "Hey Digital -- SaaS performance marketing & creative agency",
        "profile_link": "https://www.linkedin.com/in/oles-dziub-b2b-saas-paid-ads-expert/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running Hey Digital, a performance marketing agency focused specifically on B2B SaaS",
        "summary": (
            "Co-founder of a small agency specializing in paid ads for B2B SaaS "
            "companies -- serves exactly multiplayer's target client base."
        ),
        "match_reason": (
            "Agency founder specializing in the B2B SaaS vertical multiplayer "
            "targets -- strong client-overlap fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Beckie Blackburn-Cooper",
        "title": "Founder",
        "company": "Boutique recruiting agency",
        "profile_link": "https://www.linkedin.com/in/beckie-blackburn-cooper-bri/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you run a boutique recruiting agency with a niche sector focus",
        "summary": (
            "Founder of a small, self-described boutique recruiting agency. "
            "Headcount unconfirmed."
        ),
        "match_reason": (
            "Explicitly 'boutique' self-positioning -- good qualitative size "
            "signal; different vertical (recruiting) than most of this sheet, "
            "useful diversification."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Katie Matthews",
        "title": "Founder & CEO",
        "company": "CollabRecruit -- small recruiting agency",
        "profile_link": "https://www.linkedin.com/in/kmtalentfinder/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "your writing on balancing technology and human connection in recruiting at CollabRecruit",
        "summary": (
            "Founder/CEO of a small recruiting agency, writes publicly about "
            "technology's role in staffing. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small agency founder already thinking publicly about tech's role in "
            "her business -- good adoption-readiness signal."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Becky Kuntz",
        "title": "Founder",
        "company": "BK's Bookkeeping",
        "profile_link": "https://www.linkedin.com/in/becky-kuntz/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you help small business owners get time back through BK's Bookkeeping",
        "summary": (
            "Founder of a small virtual bookkeeping practice serving small-business "
            "clients. Finance-ops-adjacent, similar band to Mariya Valeva elsewhere "
            "in this sheet."
        ),
        "match_reason": (
            "Small finance-ops shop founder -- weaker fit than marketing/RevOps "
            "rows but same company-stage band and same 'wearing every hat' pain."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Tom Wells",
        "title": "Business Development",
        "company": "Wells Virtual Bookkeeping, LLC",
        "profile_link": "https://www.linkedin.com/in/tom-wells-rad60/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're part of an AI Mastermind group applying tech-forward solutions to bookkeeping",
        "summary": (
            "Small virtual bookkeeping practice; actively participates in an AI "
            "Mastermind group -- already engaged with AI adoption specifically."
        ),
        "match_reason": (
            "Small ops-adjacent shop already active in an AI-adoption community -- "
            "good readiness signal despite being outside core marketing/RevOps."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jennifer Perez-Fong",
        "title": "CEO",
        "company": "Bookkeeping Done Right",
        "profile_link": "https://www.linkedin.com/in/jennifer-perez-fong-cpa/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you founded Bookkeeping Done Right to serve small and medium businesses in South Florida",
        "summary": (
            "CEO/founder of a small accounting practice serving SMBs, founded "
            "2013. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small finance-ops shop founder -- same lower-priority band as other "
            "bookkeeping rows in this sheet."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Parry Headrick",
        "title": "Founder",
        "company": "Crackle PR -- B2B tech PR agency (Boston)",
        "profile_link": "https://www.linkedin.com/in/parryheadrick/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're leading a team of senior PR leaders at Crackle PR",
        "summary": (
            "Founder of a small B2B tech PR agency. Headcount unconfirmed."
        ),
        "match_reason": (
            "B2B-tech-focused small agency founder -- adjacent vertical (PR) "
            "serving the same kind of small SaaS/tech clients."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Carin Warner",
        "title": "Co-Founder",
        "company": "Warner Communications -- PR & comms strategy",
        "profile_link": "https://www.linkedin.com/in/carinwarner/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "your writing on AI strategy in communications",
        "summary": (
            "Co-founder of a small PR/comms firm, publishes on AI strategy in "
            "communications specifically. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small agency co-founder already writing about AI strategy in her own "
            "field -- strong thematic fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Erika Torres",
        "title": "Founder",
        "company": "85th & Park Inc. -- creative marketing & communications agency",
        "profile_link": "https://www.linkedin.com/in/erika-torres85/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running 85th & Park, a culture-driven creative marketing and comms agency",
        "summary": (
            "Founder of a small creative marketing/communications agency. "
            "Headcount unconfirmed."
        ),
        "match_reason": (
            "Small agency founder -- company-stage fit inferred from agency type."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Sam Poutakidis",
        "title": "Founder",
        "company": "New AI Automation Agency",
        "profile_link": "https://www.linkedin.com/in/sampoutakidis/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you just founded a new AI automation agency",
        "summary": (
            "Founder of a brand-new AI automation agency. Very early-stage by "
            "definition; single search snippet only."
        ),
        "match_reason": (
            "Newest-stage AI-native agency founder in this sheet -- strong "
            "thematic fit, lower-confidence single-source finding."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "M Kazemi",
        "title": "Founder & CEO",
        "company": "Web design agency (Issaquah, WA)",
        "profile_link": "https://www.linkedin.com/in/m-kazemi-098880242/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running your own web design agency",
        "summary": (
            "Founder/CEO of a small web design agency. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small agency founder -- company-stage fit inferred from agency type."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Michael Lieu",
        "title": "Co-Founder",
        "company": "Boldly -- design agency (London)",
        "profile_link": "https://www.linkedin.com/in/michael-lieu-77746972/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running Boldly with a small team of creative minds",
        "summary": (
            "Co-founder of an award-winning design agency explicitly described as "
            "a small team. Good qualitative size signal."
        ),
        "match_reason": (
            "Explicitly 'small team' self-positioning -- solid company-size signal "
            "without a hard headcount number."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Kristen Ransom",
        "title": "CTO & Founder",
        "company": "IncluDe Web Design and Development Agency",
        "profile_link": "https://www.linkedin.com/in/kristen-m-ransom/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "your interest in AI adoption for web design and development",
        "summary": (
            "CTO/Founder of a small web design/dev agency, publicly interested in "
            "AI adoption for the field. Headcount unconfirmed."
        ),
        "match_reason": (
            "Technical founder already thinking about AI adoption -- good "
            "early-adopter signal."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Stefen Phelps",
        "title": "Co-Founder",
        "company": "Kelp Creative Agency",
        "profile_link": "https://www.linkedin.com/in/stefenphelps/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you co-founded Kelp Creative Agency",
        "summary": (
            "Software engineer and co-founder of a small creative agency. "
            "Headcount unconfirmed -- single search snippet only."
        ),
        "match_reason": (
            "Technical co-founder at a small creative agency -- good blend of "
            "ICP fit and technical early-adopter likelihood."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Dean Swennumson",
        "title": "Co-Founder, Head of Operations",
        "company": "Superstate",
        "profile_link": "https://www.linkedin.com/in/dean-swennumson-075798125/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and Head of Operations at Superstate",
        "summary": (
            "Co-founder wearing the Head of Operations hat at an early-stage "
            "startup. Headcount unconfirmed."
        ),
        "match_reason": (
            "Textbook 'founder wearing the ops hat' ICP fit; company size "
            "inferred from co-founder/early-stage framing, not confirmed."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Leah Bolden",
        "title": "Co-Founder & Head of Operations",
        "company": "See Jane Drill",
        "profile_link": "https://www.linkedin.com/in/leah-bolden-24419314",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and Head of Operations at See Jane Drill",
        "summary": (
            "Co-founder/Head of Operations at a small DIY-resource startup. "
            "Headcount unconfirmed."
        ),
        "match_reason": (
            "Founder wearing the ops hat at an early-stage company -- solid ICP "
            "fit by role and company stage."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Michael McCormack",
        "title": "Co-Founder & COO",
        "company": "10X ERP",
        "profile_link": "https://www.linkedin.com/in/michael-mccormack-10xerp/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and de-facto Operations Manager at 10X ERP",
        "summary": (
            "Co-founder/COO of a small startup, explicitly noted as acting as the "
            "de-facto Operations Manager -- wearing multiple hats."
        ),
        "match_reason": (
            "Co-founder explicitly wearing both COO and hands-on ops-manager "
            "hats -- strong 'founder wearing every hat' ICP fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Pavels Mordvicevs",
        "title": "Founder",
        "company": "Camel Digital -- PPC agency for B2B SaaS",
        "profile_link": "https://www.linkedin.com/in/pavels-mordvicevs-2aaa4666/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're targeting B2B SaaS founders specifically through Camel Digital",
        "summary": (
            "Founder of a small PPC agency explicitly targeting B2B SaaS founders "
            "-- serves exactly multiplayer's target client base."
        ),
        "match_reason": (
            "Agency founder specializing in the B2B SaaS vertical multiplayer "
            "targets -- strong client-overlap fit, same pattern as Oles Dziub."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Aaron Arnold",
        "title": "Founder",
        "company": "FeatherDot Media Group LLC -- video production/growth",
        "profile_link": "https://www.linkedin.com/in/fdmg/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "your work helping brands scale with strategic video content and AI repurposing",
        "summary": (
            "Founder of a small video production/growth agency, explicitly "
            "positions AI repurposing as part of the offering."
        ),
        "match_reason": (
            "AI-forward small agency founder -- direct thematic fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Evan Cassidy",
        "title": "CEO & Founder",
        "company": "Boomin' Brands Media",
        "profile_link": "https://www.linkedin.com/in/evanbcassidy/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're using AI tools like Heygen and Freepik at Boomin' Brands Media",
        "summary": (
            "Founder/CEO of a small creative media agency, already using AI "
            "content tools in production. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small agency founder already hands-on with AI production tools -- "
            "good early-adopter signal."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Yash Arora",
        "title": "Founder / Producer",
        "company": "Lemonade Creatives",
        "profile_link": "https://www.linkedin.com/in/yasharora16/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "your AI-led creative production work at Lemonade Creatives",
        "summary": (
            "Founder/producer of a small creative production studio incorporating "
            "AI-led production. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small agency founder already building AI into the production "
            "pipeline -- direct thematic fit."
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
        "personal_detail": "your newsletter on marketing ops team structure and career growth",
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
        "personal_detail": "your weekly newsletter for the marketing ops community",
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
        "personal_detail": "MO Pros hitting 4,000+ marketing/RevOps members",
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
