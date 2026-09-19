
COMPETITOR INTELLIGENCE AGENT - CONTEXT FOR CLAUDE CODE (SEPARATE PROJECT)
=============================================================================
This is a SEPARATE, standalone project -- not a build task. Purpose is pure 
research/monitoring: find competitors in the "multiplayer AI collaboration" 
space beyond what's already been identified, and continuously dig into their 
reviews, strengths, weaknesses, and feature sets.

BACKGROUND -- COMPETITORS ALREADY IDENTIFIED (starting list, not exhaustive)
- Dust (dust.tt) -- main enterprise-focused competitor, $40M Series B raised, 
  3,000+ orgs, 300k+ agents deployed, ~$29/seat/month, weak entry-level support, 
  steep learning curve for non-developers
- Relay.app -- closer to the small-team wedge, 4.9/5 on G2 (71 reviews), 5.0 on 
  Capterra, free tier + $38/mo Professional, praised for ease of setup/support
- Carly -- email-native AI agent, lets non-technical teammates use it via email 
  threads instead of a separate app interface
- Fastio -- predictable pricing ($29/mo Starter for 5 seats), positions as 
  persistent storage layer for agent+human collaboration on files

TASK FOR THE AGENT
---------------------
1. FIND MORE COMPETITORS beyond the four above. Search broadly:
   - Google search for "multiplayer AI," "AI agent collaboration platform," 
     "shared AI workspace," "team AI agent tool," etc.
   - Reddit deep-dives: search r/AI_Agents, r/SaaS, r/startups, r/marketing, 
     r/sales for people mentioning tools they use for team-shared AI agent work, 
     complaints about existing tools, or "what do you use for X" threads
   - Look at "alternatives to Dust" / "alternatives to Relay" articles and lists, 
     which tend to surface adjacent competitors
   - Check YC's own portfolio/RFS-adjacent companies since multiplayer AI was a 
     recent YC Request for Startups category
   
2. FOR EACH COMPETITOR FOUND, gather:
   - Company name, funding status if known, approximate size/traction (users, 
     orgs, reviews count)
   - Pricing model and actual price points
   - Review site data: G2, Capterra, Trustpilot ratings and review counts
   - If they have a mobile app: check Apple App Store and Google Play Store 
     listings specifically for their FEATURE LIST as described in the store 
     listing, plus star rating and review count there
   - Read through actual review text (not just star ratings) to extract:
     - Recurring PRAISE themes (what users consistently like)
     - Recurring COMPLAINT themes (what users consistently dislike/wish was 
       different)
   - Note their positioning: who do they explicitly target (enterprise vs. 
     small team vs. specific vertical like sales/marketing/engineering)?

3. OUTPUT FORMAT
   - Compile into a running comparison table/sheet: one row per competitor, 
     columns for the fields above
   - Flag any competitor that appears to already be targeting the specific 
     wedge Charles is going for (small teams, non-engineering verticals like 
     sales/marketing ops) as HIGH PRIORITY to review in depth
   - This is meant to run periodically/be re-checked over time as an ongoing 
     competitive monitoring function, not just a one-time report

PURPOSE / HOW THIS FEEDS BACK
- This is intel-gathering only, not a build task
- Findings should sharpen the differentiation angle for the main multiplayer AI 
  product (see separate product context file) -- specifically watching for 
  whether the "true multiplayer" (agents interacting with each other, not just 
  humans sharing one agent) and "non-engineering vertical" angles stay open, 
  or whether new entrants are closing those gaps too

STATUS: Not yet run. This context is a starting point for a Claude Code session 
to execute as a research task.
