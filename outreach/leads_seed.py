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
    {
        "name": "Paul Dietrich",
        "title": "Co-Founder & CPO",
        "company": "Spherecast (Y Combinator S24)",
        "profile_link": "https://www.linkedin.com/in/pauldietrich98/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and CPO of Spherecast, a YC S24 company",
        "summary": (
            "Co-founder/CPO of a YC S24-batch startup -- accelerator batch is "
            "public record, confirming very-early company stage."
        ),
        "match_reason": (
            "YC-backed early-stage founder -- confirmed company stage; technical "
            "co-founder role suggests strong early-adopter fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Avi Konduru",
        "title": "Co-Founder",
        "company": "Shor (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/avi-konduru-54b3a6bb/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Shor, a YC S25 company",
        "summary": (
            "Co-founder of a YC S25-batch startup -- confirmed very-early stage "
            "by accelerator batch."
        ),
        "match_reason": (
            "YC-backed early-stage founder -- confirmed company stage, textbook "
            "ICP by definition."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Dhruv Roongta",
        "title": "Co-Founder",
        "company": "slashy.com (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/dhruv-roongta-421a7b214/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of slashy.com, a YC S25 company",
        "summary": (
            "Co-founder of a YC S25-batch startup -- confirmed very-early stage "
            "by accelerator batch."
        ),
        "match_reason": (
            "YC-backed early-stage founder -- confirmed company stage."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Michael Kim",
        "title": "Co-Founder",
        "company": "AgentMail (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/michaelhyunkim/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of AgentMail, a YC S25 company",
        "summary": (
            "Co-founder of a YC S25-batch startup building AI-agent-related "
            "infrastructure -- confirmed very-early stage and directly AI-native."
        ),
        "match_reason": (
            "YC-backed early-stage founder in the AI-agent space itself -- "
            "strong thematic AND company-stage fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Ishaan Sehgal",
        "title": "Co-Founder",
        "company": "Omnara (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/ishaan-sehgal/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Omnara, a YC S25 company",
        "summary": (
            "Co-founder of a YC S25-batch startup -- confirmed very-early stage "
            "by accelerator batch."
        ),
        "match_reason": (
            "YC-backed early-stage founder -- confirmed company stage."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Raj Lad",
        "title": "Co-Founder",
        "company": "Infinite (Y Combinator W25)",
        "profile_link": "https://www.linkedin.com/in/rajlad/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Infinite, a YC W25 company, previously at Sardine",
        "summary": (
            "Co-founder of a YC W25-batch startup -- confirmed very-early stage "
            "by accelerator batch."
        ),
        "match_reason": (
            "YC-backed early-stage founder -- confirmed company stage."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Kushal Mohta",
        "title": "Co-Founder",
        "company": "Optifye.ai (Y Combinator W25)",
        "profile_link": "https://www.linkedin.com/in/kushal-mohta-6926931b4/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Optifye.ai, a YC W25 company",
        "summary": (
            "Co-founder of a YC W25-batch AI startup -- confirmed very-early "
            "stage and directly AI-native."
        ),
        "match_reason": (
            "YC-backed early-stage AI founder -- strong thematic AND "
            "company-stage fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Nand Vinchhi",
        "title": "Co-Founder",
        "company": "Axal (Y Combinator W25)",
        "profile_link": "https://www.linkedin.com/in/nandvinchhi/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Axal, a YC W25 company",
        "summary": (
            "Co-founder of a YC W25-batch startup -- confirmed very-early stage "
            "by accelerator batch."
        ),
        "match_reason": (
            "YC-backed early-stage founder -- confirmed company stage."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "William Barthell",
        "title": "Co-Founder",
        "company": "Janet AI (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/william-barthell/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Janet AI, a YC S25 company",
        "summary": (
            "Co-founder of a YC S25-batch AI startup -- confirmed very-early "
            "stage and directly AI-native."
        ),
        "match_reason": (
            "YC-backed early-stage AI founder -- strong thematic AND "
            "company-stage fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Aditya Iyengar",
        "title": "Co-Founder",
        "company": "Candor (Y Combinator W25)",
        "profile_link": "https://www.linkedin.com/in/aditya-v-iyengar/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Candor, a YC W25 company focused on insider-risk",
        "summary": (
            "Co-founder of a YC W25-batch startup -- confirmed very-early stage "
            "by accelerator batch."
        ),
        "match_reason": (
            "YC-backed early-stage founder -- confirmed company stage."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Adam Wooten",
        "title": "Founder",
        "company": "Taia -- translation workflow platform / AI consultant",
        "profile_link": "https://www.linkedin.com/in/adamwooten/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you built Taia, a workflow system addressing friction in translation processes",
        "summary": (
            "Translation-tech/AI consultant and founder of a small workflow "
            "platform. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small AI-native tooling founder -- direct thematic fit, different "
            "vertical (localization) for diversification."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Ebru Yildirim",
        "title": "Founder & CEO",
        "company": "Ollang -- localization",
        "profile_link": "https://www.linkedin.com/in/ebru-yildirim-ollang/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "your take that AI translating doesn't mean localization is solved",
        "summary": (
            "Founder/CEO of a small localization company with two decades of "
            "enterprise localization experience, publicly skeptical of "
            "AI-solves-everything narratives -- a thoughtful, engaged voice."
        ),
        "match_reason": (
            "Small agency founder actively engaging with AI's real limits in her "
            "field -- a more skeptical but still relevant prospect."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Adriana Biarnes Garcia",
        "title": "Founder",
        "company": "Libre Design Studio -- design studio for founders/startups",
        "profile_link": "https://www.linkedin.com/in/adriana-biarnes-garcia/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you run Libre Design Studio specifically for founders and startups",
        "summary": (
            "Founder of a small design studio explicitly positioned to serve "
            "founders/startups. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small studio founder serving the exact startup client base "
            "multiplayer targets."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Atiqur Rahaman",
        "title": "Founder",
        "company": "Design Monks",
        "profile_link": "https://www.linkedin.com/in/atiq31416/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you founded Design Monks",
        "summary": (
            "Founder of a small design agency. Headcount unconfirmed -- single "
            "search snippet only."
        ),
        "match_reason": (
            "Small agency founder -- company-stage fit inferred from agency type, "
            "lower-confidence single-source finding."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Crystal J. Morgan",
        "title": "Fractional Customer Success Consultant",
        "company": "Independent -- serves SaaS founders and CS teams",
        "profile_link": "https://www.linkedin.com/in/crystaljmorgan/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you help SaaS founders and CS teams with customer success operations as a fractional consultant",
        "summary": (
            "Fractional Customer Success consultant serving multiple small SaaS "
            "clients at once -- same fractional-across-many-teams pattern as "
            "other consultant rows in this sheet."
        ),
        "match_reason": (
            "Fractional CS consultant across small SaaS clients -- ops-adjacent "
            "vertical (customer success) not yet represented in this sheet."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Thomas Christensen",
        "title": "Founder",
        "company": "Revora Consultants -- Customer Success consulting for B2B SaaS",
        "profile_link": "https://www.linkedin.com/in/thomas-christensen-0814a39/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you help B2B SaaS companies turn Customer Success into measurable revenue at Revora Consultants",
        "summary": (
            "Founder of a small CS consultancy for B2B SaaS companies. "
            "Headcount unconfirmed."
        ),
        "match_reason": (
            "Small CS consultancy founder serving the exact small-SaaS client "
            "base multiplayer targets."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Peter Varga",
        "title": "Founder",
        "company": "Lafluence & Trendin -- AI-native OS for influencer agencies",
        "profile_link": "https://www.linkedin.com/in/petervarga1/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're building Trendin, an AI-native operating system for influencer agencies",
        "summary": (
            "Ex-Google, founder of two small companies including an explicitly "
            "AI-native product for influencer agencies. Headcount unconfirmed."
        ),
        "match_reason": (
            "AI-native small-company founder -- direct thematic fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jamiu Akanbi",
        "title": "Founder",
        "company": "Hidden Gems -- creator-led growth for B2B AI & SaaS companies",
        "profile_link": "https://www.linkedin.com/in/jamiu-akanbi/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running Hidden Gems, focused on creator-led growth specifically for B2B AI & SaaS companies",
        "summary": (
            "Founder of a small agency specializing in B2B AI/SaaS client growth "
            "-- serves exactly multiplayer's target client base."
        ),
        "match_reason": (
            "Agency founder specializing in the B2B AI/SaaS vertical multiplayer "
            "targets -- strong client-overlap fit."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Krishna Kammili",
        "title": "Founder",
        "company": "LegalConnect -- AI-assisted legal documents for SMEs",
        "profile_link": "https://www.linkedin.com/in/krishnakammili/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you built LegalConnect to deliver AI-drafted, solicitor-reviewed legal documents for SMEs",
        "summary": (
            "Founder of a small legal-tech company already combining AI drafting "
            "with human review. Headcount unconfirmed."
        ),
        "match_reason": (
            "AI-native small-company founder in an underrepresented vertical "
            "(legal tech) -- direct thematic fit, good diversification."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jay Pietig",
        "title": "Founding Partner",
        "company": "Startup Legal Group, LLC (Kansas City)",
        "profile_link": "https://www.linkedin.com/in/jay-pietig-startuplegalgroup/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you run Startup Legal Group, serving startup clients directly",
        "summary": (
            "Founding partner of a small legal practice explicitly serving "
            "startup clients. Headcount unconfirmed."
        ),
        "match_reason": (
            "Small legal practice founder serving the exact startup client base "
            "multiplayer targets -- underrepresented vertical for diversification."
        ),
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Chris Pisarski",
        "title": "Co-Founder",
        "company": "Crustdata (Y Combinator F24)",
        "profile_link": "https://www.linkedin.com/in/chris-pisarski/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Crustdata, a YC F24 company",
        "summary": "Co-founder of a YC F24-batch startup -- confirmed very-early stage by accelerator batch.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Manmohit Grewal",
        "title": "Co-Founder",
        "company": "Crustdata (Y Combinator F24)",
        "profile_link": "https://www.linkedin.com/in/manmohitgrewal/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Crustdata, a YC F24 company",
        "summary": "Co-founder of a YC F24-batch startup -- confirmed very-early stage by accelerator batch.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Shawn Shivdat",
        "title": "Co-Founder & CEO",
        "company": "Penciled (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/shawn-shivdat/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and CEO of Penciled, a YC W24 company",
        "summary": "Co-founder/CEO of a YC W24-batch startup -- confirmed very-early stage by accelerator batch.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Sarah Hamer",
        "title": "Co-Founder / COO",
        "company": "RetailReady (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/sarah-hamer/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and COO of RetailReady, a YC W24 company",
        "summary": "Co-founder/COO of a YC W24-batch startup -- confirmed very-early stage, and she's the one directly wearing the ops hat.",
        "match_reason": "YC-backed early-stage COO -- exact 'founder wearing the ops hat' ICP fit with confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Chris Aeberli",
        "title": "Co-Founder",
        "company": "Sonia (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/chris-aeberli/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Sonia, a YC W24 company",
        "summary": "Co-founder of a YC W24-batch startup -- confirmed very-early stage by accelerator batch.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "William Wang",
        "title": "Co-Founder",
        "company": "Centralize (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/williamwang77/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Centralize, a YC W24 company",
        "summary": "Co-founder of a YC W24-batch startup -- confirmed very-early stage by accelerator batch.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Andy Li",
        "title": "Co-Founder & CEO",
        "company": "Respan (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/hanheli/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and CEO of Respan, a YC W24 company",
        "summary": "Co-founder/CEO of a YC W24-batch startup -- confirmed very-early stage by accelerator batch.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Givi Beridze",
        "title": "Co-Founder & CEO",
        "company": "KLIPY (Techstars-backed)",
        "profile_link": "https://www.linkedin.com/in/giviberidze/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and CEO of KLIPY, a Techstars-backed company",
        "summary": "Co-founder/CEO of a Techstars-backed early-stage startup -- confirmed very-early stage by accelerator affiliation.",
        "match_reason": "Accelerator-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Karla Valdivieso",
        "title": "Co-Founder & CEO",
        "company": "Shappi (Techstars-backed)",
        "profile_link": "https://www.linkedin.com/in/kvaldivieso/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and CEO of Shappi, a Techstars-backed company",
        "summary": "Co-founder/CEO of a Techstars-backed early-stage startup -- confirmed very-early stage by accelerator affiliation.",
        "match_reason": "Accelerator-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Harry Dixon",
        "title": "CEO & Co-Founder",
        "company": "Building mate -- AI growth teammate for small businesses",
        "profile_link": "https://www.linkedin.com/in/harryjdixon1/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're building 'mate,' an AI growth teammate for small businesses",
        "summary": "Co-founder/CEO of an early-stage startup building an AI teammate product for small businesses -- directly AI-native and thematically adjacent.",
        "match_reason": "Early-stage AI-native founder building a directly adjacent product category -- strong thematic fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Mihai Iancu",
        "title": "Founder & CEO",
        "company": "MspCoreX -- AI-first platform for Managed Service Providers",
        "profile_link": "https://www.linkedin.com/in/mihai-iancu-2605681a/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're building MspCoreX to replace fragmented MSP tool stacks with one intelligent core",
        "summary": "Founder/CEO of a small AI-first platform for MSPs -- directly AI-native, unifying-tools angle close to multiplayer's own pitch.",
        "match_reason": "AI-native small-company founder building a product with a very similar 'unify fragmented tools' thesis.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Michelle McCulloch",
        "title": "Founder",
        "company": "Real Marketing Muscle -- helps small/mid-sized agencies grow",
        "profile_link": "https://www.linkedin.com/in/michelle-mcculloch-616b953/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "your mission of helping small and mid-sized agencies grow through Real Marketing Muscle",
        "summary": "Founder of a small consultancy explicitly focused on helping other small agencies grow -- both an ICP member and a possible channel into other small agencies.",
        "match_reason": "Small consultancy founder whose own client base is other small agencies -- potential dual lead/channel value.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Nahme Chokeir",
        "title": "Founder & CEO",
        "company": "Research Connections, Inc. -- market research consulting",
        "profile_link": "https://www.linkedin.com/in/nchokeir/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're running Research Connections, a market research consulting and field management company",
        "summary": "Founder/CEO of a small market research consultancy. Headcount unconfirmed.",
        "match_reason": "Small agency founder in an underrepresented vertical (market research) for diversification.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jake Wujastyk",
        "title": "Founder",
        "company": "JakeWu Market Research",
        "profile_link": "https://www.linkedin.com/in/jakewujastyk/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you run JakeWu Market Research, a small solo-founder shop",
        "summary": "Solo/very-small market research founder. Headcount unconfirmed -- single search snippet only.",
        "match_reason": "Solo-founder small shop -- purest form of the company-stage signal, lower-confidence single source.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Moritz Schmidt",
        "title": "Co-Founder",
        "company": "GEMESYS -- deeptech startup, confirmed under 10 people",
        "profile_link": "https://www.linkedin.com/in/schmidtmo/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of GEMESYS, a deeptech company with under 10 people",
        "summary": "Co-founder of a deeptech startup explicitly described as under 10 people -- rare, directly confirmed headcount.",
        "match_reason": "One of the few rows with an explicitly confirmed sub-10-person headcount -- very high-confidence ICP fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jenna Gaidusek",
        "title": "Founder & CEO",
        "company": "AI for Interior Designers -- educational platform",
        "profile_link": "https://www.linkedin.com/in/jenna-gaidusek-33175a26/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you founded an education platform teaching interior designers to use AI",
        "summary": "Founder/CEO of a small AI-education platform for a specific creative vertical (interior design). Headcount unconfirmed.",
        "match_reason": "AI-adoption-focused small-company founder in a new vertical (interior design) -- direct thematic fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Nina Grondin",
        "title": "Partner & Co-Founder",
        "company": "Curioso -- design/architecture studio collective",
        "profile_link": "https://www.linkedin.com/in/nina-grondin/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you co-founded Curioso, an assemblage of designers, architects, and business-minded creatives",
        "summary": "Co-founder of a small multidisciplinary design/architecture studio. Headcount unconfirmed.",
        "match_reason": "Small studio co-founder in an underrepresented vertical (architecture/design) for diversification.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Snehadeep Das",
        "title": "Founder & Chief Designer",
        "company": "Studio ORCHIVIZ -- AI-driven architectural visualization",
        "profile_link": "https://www.linkedin.com/in/snehadeep-das-81203b16b/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you use AI-driven design tools as founder of Studio ORCHIVIZ",
        "summary": "Founder/Chief Designer of a small AI-driven architectural visualization studio. Headcount unconfirmed.",
        "match_reason": "AI-native small studio founder -- direct thematic fit, underrepresented vertical.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Austin Richard",
        "title": "Co-Founder",
        "company": "digital3 AI -- AI accessibility for entrepreneurs and small businesses",
        "profile_link": "https://www.linkedin.com/in/digital3ai/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're making AI accessible and practical for entrepreneurs and small business owners at digital3 AI",
        "summary": "Co-founder of a small company focused on AI accessibility for small businesses -- directly aligned mission.",
        "match_reason": "AI-native small-company co-founder whose own mission overlaps directly with multiplayer's target audience.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Akeem Williams",
        "title": "Co-Founder",
        "company": "Thread (Y Combinator W23)",
        "profile_link": "https://www.linkedin.com/in/akeem-k-williams/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Thread, a YC W23 company",
        "summary": "Co-founder of a YC W23-batch startup. CAVEAT: this batch is ~3 years old as of now -- company may have grown well past the 5-50 band since the accelerator batch, worth re-checking current headcount before approving.",
        "match_reason": "YC-backed founder, but older batch than the other YC rows in this sheet -- lower confidence on current company size specifically.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Ty Sharp",
        "title": "Co-Founder & CEO",
        "company": "inBuild (Y Combinator W23)",
        "profile_link": "https://www.linkedin.com/in/ty-sharp/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and CEO of inBuild, a YC W23 company",
        "summary": "Co-founder/CEO of a YC W23-batch startup. CAVEAT: batch is ~3 years old, current headcount may exceed the 5-50 band -- re-verify before approving.",
        "match_reason": "YC-backed founder, older batch -- lower confidence on current size.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Vlad Matsiiako",
        "title": "Co-Founder",
        "company": "Infisical (Y Combinator W23)",
        "profile_link": "https://www.linkedin.com/in/vmatsiiako/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Infisical, a YC W23 company",
        "summary": "Co-founder of a YC W23-batch developer-tools startup. CAVEAT: batch is ~3 years old, current headcount may exceed the 5-50 band.",
        "match_reason": "YC-backed founder in dev tooling, older batch -- lower confidence on current size, still worth a look given the technical audience fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Neel Balar",
        "title": "Co-Founder",
        "company": "Clueso -- AI video creation (Y Combinator W23)",
        "profile_link": "https://www.linkedin.com/in/neelbalar7/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Clueso, an AI video creation company from YC W23",
        "summary": "Co-founder of a YC W23-batch AI startup. CAVEAT: batch is ~3 years old, current headcount may exceed the 5-50 band.",
        "match_reason": "AI-native founder, older YC batch -- lower confidence on current size but strong thematic fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Yael Chen Zion",
        "title": "Founder",
        "company": "Ashley Digital -- brand voice/content agency",
        "profile_link": "https://www.linkedin.com/in/yaelchenzion/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you built an AI agent trained on multiple brand voices and content formats at Ashley Digital",
        "summary": "Founder of a small content/brand-voice agency, already building custom AI agents into the workflow -- directly AI-native.",
        "match_reason": "Small agency founder already building bespoke AI agents -- strong thematic fit and technical sophistication.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Ai Jane L.",
        "title": "Founder",
        "company": "Common AI -- AI/no-code accessibility for small businesses",
        "profile_link": "https://www.linkedin.com/in/aijane-common-ai/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're democratizing access to AI and no-code tools for individuals and small businesses through Common AI",
        "summary": "Founder of a small company focused on AI accessibility for small businesses -- directly aligned mission with multiplayer's audience.",
        "match_reason": "AI-native founder whose own mission is helping small businesses use AI -- direct thematic fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Vanhishikha Bhargava",
        "title": "Founder",
        "company": "Contensify -- SEO/content for B2B SaaS",
        "profile_link": "https://ae.linkedin.com/in/vanhishikhab",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you've partnered with 100+ B2B SaaS companies on SEO and content through Contensify",
        "summary": "Founder of a small content/SEO agency specializing in B2B SaaS clients across martech, AI, HRtech, CRM and devtools.",
        "match_reason": "Agency founder specializing in the exact B2B SaaS vertical multiplayer targets -- strong client-overlap fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Sourav Ganguly",
        "title": "Founder",
        "company": "Branded Minds -- brand strategy for early-stage startups",
        "profile_link": "https://www.linkedin.com/in/sourav-ganguly-3697904/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you focus on brand strategy specifically for early-stage startups at Branded Minds",
        "summary": "Founder of a small brand strategy agency serving early-stage startups. Headcount unconfirmed.",
        "match_reason": "Small agency founder serving the exact early-stage startup client base multiplayer targets.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Ulli Appelbaum",
        "title": "Founder & CSO",
        "company": "First The Trousers -- brand strategy and positioning consultancy",
        "profile_link": "https://www.linkedin.com/in/ulliappelbaum/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you run First The Trousers as a brand strategy and positioning consultancy",
        "summary": "Founder/CSO of a small brand strategy consultancy. Headcount unconfirmed.",
        "match_reason": "Solo/small consultancy founder -- fits the consultant pattern in this sheet.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Lance Mald",
        "title": "Founder",
        "company": "BrandChef.ai",
        "profile_link": "https://www.linkedin.com/in/lancemald/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're building BrandChef.ai",
        "summary": "Founder of a small, explicitly AI-named branding tool/agency. Headcount unconfirmed -- single search snippet only.",
        "match_reason": "AI-native small-company founder -- direct thematic fit, lower-confidence single-source finding.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Branden Lower",
        "title": "Founder",
        "company": "Build -- branding agency",
        "profile_link": "https://www.linkedin.com/in/branden-lower-634b1b139/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you founded Build, a branding agency built around practical design",
        "summary": "Founder of a small branding agency. Headcount unconfirmed.",
        "match_reason": "Small agency founder -- company-stage fit inferred from agency type.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Morrie Schonfeld",
        "title": "Co-Founder",
        "company": "Pingo (Y Combinator S25) -- team of 3",
        "profile_link": "https://www.linkedin.com/in/morrie-schonfeld-1628002b1/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Pingo, a YC S25 company with a team of just 3 people",
        "summary": "Co-founder of a YC S25-batch startup, confirmed team size of 3 -- as small and confirmed as this sheet gets.",
        "match_reason": "Confirmed 3-person team -- extremely high-confidence ICP fit on company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Gurveer Singh",
        "title": "Co-Founder & CEO",
        "company": "Certus AI (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/gurveer-singh29/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and CEO of Certus AI, a YC S25 company",
        "summary": "Co-founder/CEO of a YC S25-batch AI startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage AI founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Alex Avnit",
        "title": "Co-Founder",
        "company": "Paloma -- AI-native CRM (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/alex-avnit-222b3611a/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Paloma, an AI-native CRM from YC S25",
        "summary": "Co-founder of a YC S25-batch AI-native CRM startup -- confirmed very-early stage, ex-Deel/Revolut background.",
        "match_reason": "YC-backed early-stage AI founder -- confirmed company stage and directly AI-native product.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Khalid A.",
        "title": "Founder",
        "company": "Munify (Y Combinator S25) -- 20 people, $20M ARR",
        "profile_link": "https://www.linkedin.com/in/khalidashmawy/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you've grown Munify to $20M ARR with a team of just 20 people",
        "summary": "Founder of a YC S25-batch startup with an explicitly confirmed 20-person team -- rare, directly confirmed headcount right in the ICP's sweet spot.",
        "match_reason": "Explicitly confirmed 20-person team -- one of the highest-confidence company-size matches in this sheet.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Arjun Talati",
        "title": "Co-Founder",
        "company": "Knowlify (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/arjun-talati/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Knowlify, a YC S25 company",
        "summary": "Co-founder of a YC S25-batch startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Nazli Danis",
        "title": "Co-Founder",
        "company": "Paloma -- AI-native CRM (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/nazlidanis/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Paloma, an AI-native CRM from YC S25",
        "summary": "Co-founder of a YC S25-batch AI-native CRM startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage AI founder -- confirmed company stage; second co-founder at Paloma alongside Alex Avnit, both worth reaching independently.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Neha Suresh",
        "title": "Co-Founder",
        "company": "Procindex (Y Combinator S25)",
        "profile_link": "https://www.linkedin.com/in/nehasuresh1904/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Procindex, a YC S25 company",
        "summary": "Co-founder of a YC S25-batch startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "John Yeo",
        "title": "Co-Founder",
        "company": "Autumn (Y Combinator S25)",
        "profile_link": "https://uk.linkedin.com/in/johnyeocx",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Autumn, a YC S25 company",
        "summary": "Co-founder of a YC S25-batch startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Susan Sarit",
        "title": "Founder",
        "company": "Empower and Cultivate -- People Ops & Systems consulting",
        "profile_link": "https://www.linkedin.com/in/susan-sarit/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you help founders build self-sufficient teams as a People Ops & Systems consultant",
        "summary": "Founder of a small People Ops consultancy explicitly supporting small business owners and founders.",
        "match_reason": "Consultant serving the exact small-founder audience multiplayer targets, in an underrepresented vertical (people ops).",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Heidi R. Haskins",
        "title": "Founder",
        "company": "Elevated Prana People Ops Consulting",
        "profile_link": "https://www.linkedin.com/in/heidiparks/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you focus on People Ops/HR solutions specifically for startups and tech companies",
        "summary": "Founder of a small People Ops consultancy focused on startups and tech companies specifically.",
        "match_reason": "Consultant explicitly serving the startup/tech audience multiplayer targets.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Michelle Dicks",
        "title": "Owner",
        "company": "Quantum People Ops",
        "profile_link": "https://www.linkedin.com/in/michelle-dicks-3872a791/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you provide scalable HR systems for growing teams through Quantum People Ops",
        "summary": "Owner of a small People Ops consultancy providing scalable HR systems for growing teams.",
        "match_reason": "Consultant in the people-ops vertical serving growing small teams.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Danielle Laurent",
        "title": "Founder",
        "company": "Founder's HR Lab",
        "profile_link": "https://www.linkedin.com/in/danielle-laurent/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you're passionate about building systems for small businesses and helping agency owners specifically",
        "summary": "Founder of a small HR consultancy explicitly focused on building systems for small businesses and agency owners.",
        "match_reason": "Consultant serving small agency owners specifically -- direct overlap with the agency-founder rows elsewhere in this sheet.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jill Hutchins",
        "title": "Managing Consultant / Founder",
        "company": "Your HR Partners -- boutique HR services",
        "profile_link": "https://www.linkedin.com/in/jillhutchins/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you run Your HR Partners as a boutique human resources services company",
        "summary": "Founder of a small, explicitly boutique HR consulting firm. Headcount unconfirmed.",
        "match_reason": "Explicitly 'boutique' self-positioning -- good qualitative size signal.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Taylor Scher",
        "title": "Founder",
        "company": "Taylor Scher Consulting, LLC -- B2B SaaS SEO/content",
        "profile_link": "https://www.linkedin.com/in/taylorjosephscher/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you just onboarded your first full-time employee (an editorial manager) at Taylor Scher Consulting",
        "summary": "Founder of a B2B SaaS content/SEO consultancy who just hired employee #1 -- explicitly confirmed as a 2-person shop right now.",
        "match_reason": "Explicitly confirmed 2-person company (just crossed from solo to first hire) -- very high-confidence smallest-possible ICP fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Apoorv Sharma",
        "title": "Founder",
        "company": "Found On AI -- AI search for B2B SaaS (Bengaluru)",
        "profile_link": "https://www.linkedin.com/in/apoorvshrm/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're helping B2B SaaS companies with AI search visibility at Found On AI",
        "summary": "Founder of a small AI-search consultancy for B2B SaaS companies. Headcount unconfirmed.",
        "match_reason": "AI-native small consultancy founder serving multiplayer's exact target client base.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Anis Msakni",
        "title": "Search & AI Visibility Consultant",
        "company": "Independent -- for B2B/SaaS companies",
        "profile_link": "https://es.linkedin.com/in/anis-msakni-7b17991a9",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you help B2B/SaaS companies grow visibility and revenue through SEO and AEO",
        "summary": "Solo independent Search & AI Visibility consultant for B2B/SaaS companies.",
        "match_reason": "Solo consultant serving multiplayer's exact target client base -- purest form of the company-stage signal.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Matt Craig",
        "title": "Co-Founder",
        "company": "Sheepdog Projects -- BI Consulting and Data Strategy",
        "profile_link": "https://www.linkedin.com/in/mathieucraig/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you co-founded Sheepdog Projects to offer BI consulting and data strategy services",
        "summary": "Co-founder of a small BI/data-strategy consultancy. Headcount unconfirmed.",
        "match_reason": "Small consultancy founder in an underrepresented vertical (BI/analytics) for diversification.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Peter O'Donoghue",
        "title": "Founder",
        "company": "Nynch -- growth platform for consultants and fractionals",
        "profile_link": "https://www.linkedin.com/in/peterodonoghue/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're building Nynch, a growth platform specifically for consultants and fractional professionals",
        "summary": "Founder of a small SaaS company building tools for the exact fractional-consultant audience heavily represented elsewhere in this sheet.",
        "match_reason": "Small SaaS founder whose own customer base overlaps with many other rows in this sheet -- interesting potential channel as well as direct lead.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Michael Twiddy",
        "title": "Founder",
        "company": "Fame -- The B2B Podcast Agency",
        "profile_link": "https://uk.linkedin.com/in/michael-twiddy-1a1391196",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you discuss AI integration in podcast production at Fame",
        "summary": "Founder of a small B2B podcast production agency, already discussing AI integration in the workflow.",
        "match_reason": "Small agency founder already engaging with AI in production -- good adoption-readiness signal.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jason Bradwell",
        "title": "Founder",
        "company": "B2B Better -- podcast agency",
        "profile_link": "https://www.linkedin.com/in/jason-bradwell-40b45751/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you discuss how AI is being integrated into podcast production workflows at B2B Better",
        "summary": "Founder of a small B2B podcast agency, publicly discussing AI in production. Headcount unconfirmed.",
        "match_reason": "Small agency founder already engaging with AI in production -- good adoption-readiness signal.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Dominic Noble",
        "title": "Founder",
        "company": "Frogotiv -- animation/video studio",
        "profile_link": "https://www.linkedin.com/in/dominicnoble/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you and your co-founder originally handled strategy, storyboarding, illustration, animation, revisions, and client communication together at Frogotiv",
        "summary": "Founder of a small animation/video studio, explicitly confirmed to have started with just two founders doing every function themselves -- textbook wearing-every-hat ICP signal.",
        "match_reason": "Confirmed tiny founding team doing every function personally -- very high-confidence ICP fit on company stage and pain point.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Oyinkro K",
        "title": "Founder",
        "company": "K.OS VISUALS -- creative GTM partner for AI/SaaS companies",
        "profile_link": "https://www.linkedin.com/in/oyinkro-creativevideographer/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're positioning K.OS VISUALS as a creative GTM partner for fast-growing AI/SaaS companies",
        "summary": "Founder of a small creative agency positioned specifically for AI/SaaS company clients.",
        "match_reason": "Small agency founder serving multiplayer's exact target client base.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Costin Modoianu",
        "title": "Strategic Video Partner",
        "company": "Independent -- video for SaaS & Tech",
        "profile_link": "https://www.linkedin.com/in/costin-modoianu/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you turn complex SaaS products into clear, high-impact video as a strategic video partner",
        "summary": "Solo/small video production consultant specializing in SaaS and tech clients.",
        "match_reason": "Solo consultant serving multiplayer's exact target client base.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Marek Bartík",
        "title": "Founder",
        "company": "pipetail.io -- AWS & Kubernetes DevOps consulting",
        "profile_link": "https://www.linkedin.com/in/marekbartik/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you help companies adopt DevOps culture through on-site workshops and consulting at pipetail.io",
        "summary": "Solo/small DevOps consultancy founder. Technical audience, likely an early adopter of new tooling.",
        "match_reason": "Solo technical consultant -- purest form of the company-stage signal, strong early-adopter likelihood.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Michal Maxian",
        "title": "Founder",
        "company": "AI & Cloud Architecture consulting -- built a RAG platform for 15k+ users",
        "profile_link": "https://www.linkedin.com/in/mmaxian/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you built a RAG platform for 15k+ users and now consult on DevOps culture and AI adoption",
        "summary": "AI & Cloud Architect and founder of a small consultancy, hands-on building AI infrastructure himself.",
        "match_reason": "Deeply technical AI-native founder -- strong thematic fit and early-adopter likelihood.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Samuel Anderson-Levy",
        "title": "Founder",
        "company": "Fractional CMO Agency (New York)",
        "profile_link": "https://www.linkedin.com/in/samuel-anderson-levy-33508528a/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you run a fractional CMO agency in New York",
        "summary": "Founder of a small fractional-CMO agency. Headcount unconfirmed.",
        "match_reason": "Fractional marketing consultant -- direct fit with the marketing-ops ICP.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Joshua Kimber",
        "title": "Founder & Owner",
        "company": "sōsh -- fractional CMO / digital marketing agency",
        "profile_link": "https://www.linkedin.com/in/joshkimber/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're driving data-driven growth for clients as founder of sōsh",
        "summary": "Founder/owner of a small fractional-CMO/digital-marketing agency. Headcount unconfirmed.",
        "match_reason": "Small agency founder in the core marketing-ops ICP.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Sara Pastor Ruprichova",
        "title": "Fractional CMO",
        "company": "White Cloud Communications (Prague)",
        "profile_link": "https://www.linkedin.com/in/pastorsara/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you help founders and SMEs turn marketing spend into measurable growth through White Cloud Communications",
        "summary": "Founder of a small strategic marketing consultancy serving growing businesses across Europe and beyond.",
        "match_reason": "Fractional marketing consultant serving small businesses -- direct ICP fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Kristen Palmer",
        "title": "Co-Founder / CEO",
        "company": "Boutique digital marketing consulting firm (B2B professional services)",
        "profile_link": "https://www.linkedin.com/in/kristenpalmer1/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you co-founded a boutique full-service digital marketing consulting firm for B2B professional services",
        "summary": "Co-founder/CEO of a small, self-described boutique marketing consultancy. Ex-Accenture.",
        "match_reason": "Explicitly 'boutique' self-positioning -- good qualitative company-size signal.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Dawn Jacobs",
        "title": "Fractional CMO",
        "company": "Independent -- partners with early-stage founders/CEOs",
        "profile_link": "https://www.linkedin.com/in/dawnmjacobs/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you partner with early-stage founders and CEOs to build brands that scale",
        "summary": "Fractional CMO explicitly partnering with early-stage founders. Headcount unconfirmed.",
        "match_reason": "Fractional marketing consultant serving early-stage founders -- direct ICP fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Jonny Butler",
        "title": "Fractional CMO",
        "company": "Independent -- strategy & execution for early-stage B2B SaaS",
        "profile_link": "https://www.linkedin.com/in/jonnybutler/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you've been 3x Head of Marketing at B2B SaaS startups before going fractional",
        "summary": "Fractional CMO with direct in-house B2B SaaS marketing leadership experience, now serving early-stage SaaS clients.",
        "match_reason": "Fractional marketing consultant with direct B2B SaaS operator background -- strong ICP and empathy fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Hugo Pereira",
        "title": "Fractional CGO/CMO",
        "company": "Independent -- B2B SaaS & deep tech",
        "profile_link": "https://www.linkedin.com/in/hugosbpereira/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you wrote \"Teams in Hell\" and are a 1x exited founder now doing fractional growth work",
        "summary": "Fractional CGO/CMO for B2B SaaS and deep tech, author and previously exited founder himself.",
        "match_reason": "Fractional consultant with founder-side empathy (previously exited a company himself) -- strong ICP fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Annabell V.",
        "title": "Co-Founder & CTO",
        "company": "CoCrafter (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/annabell-v-86a73b227/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and CTO of CoCrafter, a YC W24 company",
        "summary": "Co-founder/CTO of a YC W24-batch startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage technical co-founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Nicole Atack",
        "title": "Co-Founder",
        "company": "Yarn (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/nicole-atack-98194b2b8/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Yarn, a YC W24 company",
        "summary": "Co-founder of a YC W24-batch startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "David Lalor",
        "title": "CEO & Co-Founder",
        "company": "Swift (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/davidlalor5/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're CEO and co-founder of Swift, a YC W24 company",
        "summary": "Co-founder/CEO of a YC W24-batch startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Md Abdul Halim Rafi",
        "title": "Co-Founder & CTO",
        "company": "Octolane AI (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/md-abdul-halim-rafi/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder and CTO of Octolane AI, a YC W24 company",
        "summary": "Co-founder/CTO of a YC W24-batch AI startup -- confirmed very-early stage and directly AI-native.",
        "match_reason": "YC-backed early-stage AI founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Joseph Palakapilly",
        "title": "Co-Founder",
        "company": "Meticulate (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/jpalakapilly/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you're co-founder of Meticulate, a YC W24 company",
        "summary": "Co-founder of a YC W24-batch startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Alex Choi",
        "title": "Co-Founder",
        "company": "Basalt Tech (Y Combinator W24)",
        "profile_link": "https://www.linkedin.com/in/alex-choi/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "operator",
        "personal_detail": "you co-founded Basalt Tech with Maximillian Bhatti, a YC W24 company",
        "summary": "Co-founder of a YC W24-batch startup -- confirmed very-early stage.",
        "match_reason": "YC-backed early-stage founder -- confirmed company stage.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Marcus McGehee",
        "title": "Founder",
        "company": "The AI Consulting Lab",
        "profile_link": "https://www.linkedin.com/in/marcusmcgehee/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "your observation that companies buy AI licenses, announce it, and six months later only 10% of the team is actually using the tools",
        "summary": "Founder of a small AI-adoption consultancy whose core finding -- that AI adoption fails on culture/training, not technology -- is nearly identical to multiplayer's own thesis about scattered, unused AI tool access.",
        "match_reason": "Near-perfect thematic match: his own research names the exact 'AI tools bought but not actually adopted/shared' problem multiplayer is built to solve.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Miranda Jones",
        "title": "Founder / Lead Consultant",
        "company": "AI Consulting Network",
        "profile_link": "https://www.linkedin.com/in/miranda-jones-16a256115/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you're empowering small businesses with AI tools and services through AI Consulting Network",
        "summary": "Founder of a small AI-adoption consultancy for small businesses. Headcount unconfirmed.",
        "match_reason": "AI-adoption consultant serving multiplayer's exact target client base -- direct thematic fit.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "David MacKillop",
        "title": "Founder",
        "company": "MacKillop Solutions -- AI agent and automation consulting",
        "profile_link": "https://www.linkedin.com/in/david-mackillop/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you build intelligent workflows and AI agents using tools like n8n, Make.com, and Airtable",
        "summary": "Founder of a small AI automation consultancy, hands-on building agent workflows for clients.",
        "match_reason": "Technical AI-agent-building consultant -- strong thematic fit and early-adopter likelihood.",
        "status": "",
        "date_found": TODAY,
    },
    {
        "name": "Matthew Kuchera",
        "title": "Co-Founder & CEO",
        "company": "Mission AI Consulting",
        "profile_link": "https://www.linkedin.com/in/matthewkuchera/",
        "contact_method": "LinkedIn only (no public email found)",
        "kind": "consultant",
        "personal_detail": "you specialize in AI platform adoption and implementation at Mission AI Consulting",
        "summary": "Co-founder/CEO of a small AI consultancy specifically focused on platform adoption and implementation -- exactly the failure mode multiplayer addresses.",
        "match_reason": "AI-adoption specialist consultant -- near-direct thematic match with multiplayer's core value proposition.",
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
