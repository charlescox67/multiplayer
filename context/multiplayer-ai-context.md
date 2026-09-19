
MULTIPLAYER AI STARTUP - CONTEXT AND BUILD PLAN FOR CLAUDE CODE
==================================================================

CONTEXT SUMMARY (paste this as the opening prompt in Claude Code)
-------------------------------------------------------------------
I'm building a multiplayer AI collaboration SaaS. Core idea: individual AI agents 
(belonging to different coworkers on a team) currently work in isolated, personal 
chats with no shared visibility. I want to build a shared workspace where each 
person's AI agent posts its activity, outputs, and status into one shared thread 
that the whole team can see, comment on, redirect, or hand off to each other -- 
agents and humans as co-equal participants in one channel, not siloed individual 
sessions.

Biggest competitor is Dust (dust.tt) -- they raised $40M Series B, have 3,000+ 
orgs and 300k+ deployed agents, but they are built for enterprise: expensive 
(~$29/seat/month, ~580 EUR/month for a 20-person team), steep learning curve for 
non-developers, weak entry-level support, and every case study they cite is a 
large enterprise (Clay, Profound, Persona, Doctolib). That's their structural 
weakness -- they can't easily go downmarket without cannibalizing enterprise deals.

Closer competitors who ARE built for smaller teams: Relay.app (4.9/5 on G2 across 
71 reviews, 5.0 on Capterra, free tier + $38/mo Professional tier, praised for 
ease of setup and fast support) and Carly (email-native AI agent, lets non-technical 
people use it without learning a new interface). These prove the "simple and cheap 
for small teams" angle isn't fully open anymore, so my differentiation needs to be:
1) TRUE multiplayer -- agents seeing and reacting to each other's work directly, 
   not just one-person-one-agent with sharing bolted on
2) Vertical focus on non-engineering teams -- sales ops, marketing ops, RevOps -- 
   nobody is marketing specifically to that crowd yet

ICP: Companies of 5-50 people, past solo-founder stage, no dedicated IT/ops 
department yet. Best-fit roles: marketing ops, sales ops, revenue ops, or a 
founder wearing that hat. Best-fit company types: small agencies, small SaaS 
companies, consulting shops -- client-work-driven, already comfortable paying 
for productivity tools. Trigger signal: 2-3+ people on a team independently 
using ChatGPT/Claude for real recurring work (research, drafts, follow-ups, 
reporting) with zero shared visibility between them. Explicitly NOT targeting 
large enterprises (e.g. Nvidia-scale companies) at this stage -- that's a 
year-two move once there's real traction and case studies.

PRICING MODEL: Flat per-seat subscription (target ~$10-15/seat/month, undercutting 
Dust's ~$29/seat) covering the core product/workspace experience with included 
usage limits. SEPARATE near-cost API pass-through fee for programmatic/automated 
agent usage (calls made by code directly, not through the UI) -- mirroring how 
Anthropic prices API access separately from a Claude subscription. Priced close 
to cost rather than marked up like Dust does, this becomes a selling point for 
teams doing heavier automation. Single plan at launch, no tiering complexity yet.

MARKET SIZING (directional estimates, not a dedicated published report):
- TAM: Global AI agents market ~$11-12B in 2026, projected to ~$50-93B by 2030 
  (44-46% CAGR). Multi-agent/collaboration systems flagged as the fastest-growing 
  sub-segment.
- SAM: Collaboration/orchestration layer specifically (not single-purpose bots), 
  estimated at roughly 5-10% of the total AI agent market -- roughly $1-1.5B today, 
  potentially $4-8B by 2030.
- SOM: Realistic early capture target as a small player -- a few hundred small 
  teams at ~$15/seat with ~10-person average team size = low millions in ARR, 
  a reasonable early milestone, not a moonshot.

BUILD COST ESTIMATE: Roughly $50-150/month in real cash costs to run a working 
beta (Postgres hosting ~$5-25/mo, app hosting ~$7-25/mo, domain/email ~$2-3/mo, 
API usage for ~10 light beta teams ~$100-300/mo). Real cost is founder time, not 
capital -- this does NOT require raised funding just to build and beta-test it.

TIMELINE ESTIMATE: ~6-10 weeks of actual build effort solo with heavy Claude Code 
use; realistically ~10-14 weeks of calendar time given also running 916 Pressure 
Washers and Pinnacle concurrently.


BUILD PLAN / PHASES (rough, not final -- meant to spark a real plan in Claude Code)
-------------------------------------------------------------------------------------
PHASE 1 (~wks 1-2): Core infrastructure
- Postgres backend for structured state (users, teams, workspaces, agent activity log)
- Auth + basic team/workspace creation
- Skeleton of the shared workspace UI shell (chat-like interface)

PHASE 2 (~wks 2-5): THE CORE DIFFERENTIATOR
- Shared agent activity feed: agents post updates/outputs into a shared thread
- Event bus / real-time push so updates appear live for the whole team
- Ability for a teammate (or another agent) to comment, redirect, or take over 
  a task directly in the shared thread
- This is the hardest and most important part -- avoid just building "shared 
  chat log," build actual interactive collaboration between agents and humans

PHASE 3 (~wks 5-7): First integrations + notifications
- Slack integration (most requested / where ops teams already live)
- Generic webhook so any agent (Claude-based, custom script, whatever) can post in
- Basic notification system (something happened, come look)

PHASE 4 (~wks 7-8+): Beta polish
- Onboarding flow simple enough to need zero technical hand-holding (this is the 
  wedge vs. Dust -- must be dramatically easier to set up)
- Stability pass
- Ready to hand to first 5-10 beta teams

GO-TO-MARKET / BETA PLAN
- Give free access to first 5-10 beta teams for 30-60 days in exchange for 
  weekly feedback calls
- Convert early teams to "founding customer" pricing -- locked-in lower rate 
  for life as thank-you for early feedback + becomes case study material
- Find beta teams manually via: LinkedIn search using titles like "marketing 
  operations manager" / "revenue operations" / "growth lead" combined with 
  recent posts mentioning ChatGPT/AI tools; RevGenius and MO Pros (MarketingOps) 
  communities; r/MarketingAutomation and r/AI_Agents on Reddit; small agency 
  directories (e.g. Clutch.co)
- Outreach message angle: lead with the PAIN (scattered, untracked AI work, 
  lost context when someone's out), not with "agent" or "multiplayer AI" jargon
- Sample outreach text: "Curious if anyone else on a small team has this problem 
  -- everyone's using ChatGPT or Claude for real work, research, drafts, follow-ups, 
  but it all lives in separate chats with zero shared visibility. If someone's out 
  sick or leaves, that context just disappears. Building something to fix that, 
  looking for a few small teams to test it early, free, in exchange for feedback."

NEXT STEPS TO FIGURE OUT WITH CLAUDE CODE
- Concrete tech stack decision (likely Node.js given existing pipeline experience 
  from the website generator project)
- Data model for "agent activity" that's generic enough to work across different 
  agent types (Claude-based, custom scripts, etc.)
- MVP scope cut -- what's the smallest version of Phase 2 that still proves the 
  core "true multiplayer" differentiation
