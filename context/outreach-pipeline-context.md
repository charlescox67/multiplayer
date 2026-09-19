
OUTREACH AUTOMATION PIPELINE - CONTEXT FOR CLAUDE CODE (SEPARATE PROJECT)
============================================================================
This is a SEPARATE, standalone project from the multiplayer AI SaaS product build. 
Run this as its own Claude Code session/agent, independent of product development. 
Purpose: find and qualify ICP leads for the multiplayer AI startup, with a human 
approval gate before any outreach happens, then send small, personalized, 
manually-approved first messages, with a defined handoff for what happens if 
someone replies.

IMPORTANT CONSTRAINTS / REALITY CHECK
----------------------------------------
- Mass automated LinkedIn outreach violates LinkedIn's terms of service and risks 
  account bans. Even SMALL volume automated sending through unofficial methods 
  (not LinkedIn's official API) can still get flagged -- it's about behavior 
  pattern (send speed, consistent timing, browser automation signatures), not 
  just raw volume. Randomized delays between sends and genuinely small batch 
  sizes reduce but do not eliminate this risk.
- Automated/mass unsolicited texting has real legal exposure (TCPA in the US) -- 
  avoid building auto-texting to strangers.
- Claude (in chat/voice form) cannot log into or send messages from Charles's 
  personal LinkedIn directly. The send step must be built as a separate tool 
  Charles runs locally (e.g. a script using LinkedIn's official API where 
  available, or a browser automation tool that logs in as him) -- Claude Code 
  can help build/run this once Charles is at his own machine.
- Batches stay small and manually curated -- Charles reviews the sheet and picks 
  the best names himself before anything sends. Keep that human curation step 
  as core to the design.

TWO-PIPELINE STRUCTURE
-------------------------
PIPELINE 1 -- THE FINDER (fully automatable)
- Runs on a schedule (e.g. every few hours or daily)
- Searches target sources for ICP matches:
  - LinkedIn posts/profiles matching titles like "marketing operations manager," 
    "revenue operations," "sales ops," "growth lead," especially those posting 
    about ChatGPT/AI tool usage or pain points
  - Reddit threads in r/MarketingAutomation, r/AI_Agents, r/marketing, r/sales
  - Communities: RevGenius, MO Pros (MarketingOps) if browsable/scrapeable
- ICP signals to match against: company size 5-50 people, ops-adjacent title or 
  founder wearing that hat, small agency/SaaS/consulting shop, signals of 2-3+ 
  people using AI tools individually with no shared visibility
- For each match, pull into the sheet:
  - Name, Title, Company, Profile/Post Link
  - Best contact method found (LinkedIn profile URL, public email if 
    discoverable, or note "LinkedIn only" if no other contact found)
  - What they're about / short profile summary (background, focus area, recent 
    activity) -- enough detail to both qualify them AND later personalize a 
    message
  - Match Reason (the specific pain point or signal that made them a fit)
  - Status column (blank by default, Charles fills in Approved/Rejected)
  - Date Found
- Build approach: Python script using web search/scraping + openpyxl for Excel, 
  or Google Sheets API if a live-updating shared sheet is preferred

APPROVAL GATE (manual, by Charles)
- Charles reviews the sheet, picks the best-fit names himself
- Marks "Status" column as Approved for only the small batch he wants to reach 
  out to at a time
- Only rows marked Approved get picked up by Pipeline 2

PIPELINE 2 -- FIRST-MESSAGE DRAFTER + SEMI-AUTOMATED SEND
- Watches the sheet for rows marked "Approved"
- For each approved row, analyzes the profile info already gathered (experience, 
  role, background, recent activity/posts) and drafts ONE first-touch message 
  personalized to that person
  - Personalization style: SIMPLE and TO THE POINT. Reference one real, specific 
    detail about their background/role/situation so it doesn't read as generic, 
    but don't oversell, don't over-compliment, don't try too hard to please them. 
    Short and direct beats warm and elaborate.
  - Keep the core value proposition consistent (the pain point / what Charles is 
    building) but let the specific reference point vary naturally per person
- Writes the draft into a "Draft Message" column in the sheet for Charles to 
  review/edit
- Sending: once Charles approves, the send happens through Charles's own local 
  tool/script (built separately, using his LinkedIn login) -- small batches, 
  randomized delays, not a bulk blast

CONVERSATION HANDOFF LOGIC (IMPORTANT)
- AI/automation's job ends after the FIRST message is sent.
- Default: Charles personally handles any reply and the rest of that 
  conversation himself.
- EXCEPTION: If Charles explicitly opts in for a given conversation, AI can 
  continue the back-and-forth conversation with that person after they reply, 
  then produce a summarized writeup of the conversation/data for Charles 
  afterward rather than him having to read the full thread.
- Design the tool so this is a per-conversation toggle/choice, not an 
  all-or-nothing default -- Charles decides case by case whether to take over 
  personally or let it continue automated.

TECH NOTES
- Google Sheets API is probably the better shared database vs. local Excel file, 
  since multiple Claude Code sessions (finder + drafter, possibly running on 
  different schedules) need to read/write the same data reliably
- Keep the two pipelines as separate scripts/agents that both just read/write 
  the same sheet -- decouples them so they can run independently
- This whole project should run in the background/on schedule while Charles is 
  doing other work (Roblox game dev, product build, etc.) on the same machine

STATUS: Not yet built. This context is a starting point for a Claude Code session 
to turn into an actual build plan and then real code.
