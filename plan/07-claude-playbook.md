# 07 – Claude Playbook

Claude is your **team**: researcher, writer, analyst, developer, designer, and trainer's assistant. This playbook explains which Claude tool to use for which job, how to set it up, and gives a copy-paste prompt library for every service.

> **You are the expert and the quality gate.** Claude produces drafts and builds fast; you bring the client relationship, the judgment, and the final review.

---

## 1. Which Claude tool for which job

| Tool | Use it for | Praxis Minds examples |
|---|---|---|
| **Claude app (claude.ai, desktop, mobile)** | Thinking, writing, analysis, research | Proposals, reports, content, call prep |
| **Projects** | Persistent context per client or per service (files + custom instructions) | "Client: Silva Logistics", "Praxis – Sales", "Praxis – Reports" |
| **Artifacts** | Interactive prototypes, mini-apps, diagrams, and mockups you can share by link | Prototype shown in the Audit presentation; clickable dashboard mockup |
| **Research / web search** | Gathering current information with sources | Market data for viability reports; competitor research; call prep |
| **File creation** | Generating Word, PowerPoint, Excel, and PDF files | Reports, decks, financial models, workshop workbooks |
| **Connectors** | Reading from Google Drive, Gmail, Calendar, and other tools | Pull meeting notes and documents into a proposal |
| **Skills** | Packaging a repeatable process (instructions + templates) Claude loads when needed | "Praxis proposal writer", "Praxis viability report" |
| **Claude Code** | Building software: websites, apps, dashboards, automations, scripts | The Praxis website; client apps; integrations; this repository |
| **Claude API** | AI inside the products you build for clients | Invoice extraction, email triage, knowledge assistants |

**Plan recommendation:** start on **Claude Pro**; move to **Max** when you're building with Claude Code daily; switch to **Team** when you have collaborators or need commercial data terms for client work. See [08 – Tech Stack](08-tech-stack.md).

---

## 2. Set up your Claude Projects

Create these Projects in week 1. Paste the custom instructions, and upload the listed files.

### Project: "Praxis – Sales"
**Upload:** [`02-services.md`](02-services.md), [`03-pricing.md`](03-pricing.md), [`proposal-template.md`](../templates/proposal-template.md), [`statement-of-work-template.md`](../templates/statement-of-work-template.md), your best past proposals.

**Custom instructions:**
```
You are the sales assistant for Praxis Minds, an AI consultancy that helps small and
medium businesses put AI into practice (Find → Build → Teach). Our niche is: [NICHE].

When I give you notes from a discovery call:
- Restate the client's problem in their own words and quantify its cost (hours, €, errors).
- Recommend the right Praxis Minds service from the services file. Never invent services.
- Price using the pricing file, always offering 3 options (Essential / Recommended / Complete).
- Write in plain, confident, jargon-free language. Be concise.
- Flag anything unclear that I should confirm with the client, as a list at the end.
- Flag any request that touches high-risk AI uses (hiring, employee evaluation, credit,
  health decisions) so I can check compliance.
```

### Project: "Praxis – Content"
**Upload:** [`01-vision-and-strategy.md`](01-vision-and-strategy.md), [`05-go-to-market.md`](05-go-to-market.md), 5–10 of your best posts (once you have them), a short style guide.

**Custom instructions:**
```
You write marketing content for Praxis Minds and its founder [NAME]. Audience: owners and
managers of [NICHE] companies with 10-250 employees.
Voice: practical, confident, friendly, no hype, no jargon, short sentences, concrete numbers
and examples. Never use these words: "revolutionize", "game-changer", "unlock",
"leverage", "delve".
Every post: one idea, a strong first line, a concrete example, and a soft call to action.
LinkedIn posts: 120-220 words, short paragraphs, max 3 hashtags, no emoji walls.
Never invent client results or statistics. Use [placeholders] where I must add real numbers.
```

### Project: "Praxis – Reports"
**Upload:** [`viability-report-template.md`](../templates/viability-report-template.md), a finished example report (once you have one).

**Custom instructions:**
```
You help Praxis Minds produce viability/feasibility reports, business plans, market research,
and pitch decks.
- Follow the report template structure.
- Clearly separate FACTS (with source and date), ASSUMPTIONS (labelled, with rationale),
  and ESTIMATES (with method).
- Use web search for market data; cite every source; prefer official statistics, industry
  associations, and reputable publications; flag anything older than 2 years.
- Financials: show formulas and assumptions; build conservative / base / optimistic scenarios.
- Never present projections as guarantees. Include the standard disclaimer.
- Write for a non-expert investor or bank: clear, structured, with charts where useful.
```

### Project per client: "Client – [Company]"
**Upload:** company profile, discovery notes, SOW, glossary of their terms, sample documents (anonymized), meeting transcripts.

**Custom instructions:**
```
This project is for [CLIENT], a [industry] company with [size]. Our engagement: [SOW summary].
Their goals and success metrics: [...]. Key people: [names/roles]. Their tools: [...].
Use their terminology (see glossary). Keep everything consistent with the SOW scope; flag
any out-of-scope request.
```

> ⚠️ For confidential client data, use a plan with commercial data terms (Team/Enterprise) or the API. See the [data-handling rules](06-delivery-process.md#data-handling-rules).

---

## 3. Golden rules for working with Claude

1. **Give context, not just commands.** Who is the client, what is the goal, who will read it, what does good look like.
2. **Provide examples and templates.** "Follow this structure" beats "write a report".
3. **Ask for a plan first** on big tasks ("Outline the report before writing it").
4. **Iterate.** Treat the first draft as a draft, and give specific feedback ("Section 3 is too generic. Use the numbers from the interview notes").
5. **Make Claude check itself:** "Review this for factual claims that need a source, and list them."
6. **Verify every fact, figure, and legal statement** before it reaches a client.
7. **Save winning prompts** back into this playbook or into a Skill. Your prompt library is a business asset.

---

## 4. Prompt library

Replace `[BRACKETS]` with your details. Paste notes and transcripts where indicated.

### 4.1 Rewrite my LinkedIn profile
```
Rewrite my LinkedIn headline, About section, and Featured section ideas. I'm the founder of
Praxis Minds (AI consultancy: Find → Build → Teach). Niche: [NICHE]. My background: [CV
summary]. Goal: owners of [NICHE] companies should understand in 5 seconds what I do and
book a free 20-minute AI check. Give me 3 headline options and 1 About section (max 1,500
characters) with a clear call to action.
```

### 4.2 Prepare for a discovery call
```
I have a discovery call with [NAME], [ROLE] at [COMPANY] ([website]). Research the company
using web search and give me:
1. A 5-line company summary (what they do, size, markets, recent news).
2. The 5 most likely AI opportunities for a company like this, with estimated time savings.
3. 8 smart questions to ask, specific to their business.
4. Which Praxis Minds demo I should show and why.
Mark anything you're unsure about.
```

### 4.3 Turn call notes into a proposal
```
Here are my notes from a discovery call with [COMPANY]:
[PASTE NOTES OR TRANSCRIPT]
Draft a proposal using our proposal template. Include: their problem in their words, the
cost of the problem, the recommended solution, 3 options with prices from our rate card,
timeline, what we need from them, and next steps. Then list any questions I must confirm
before sending.
```

### 4.4 AI Opportunity Audit: analyze interviews
```
Below are transcripts from interviews with [N] employees of [COMPANY] ([industry]) and the
results of their AI readiness survey.
[PASTE]
1. List every task/process mentioned, with: who does it, frequency, time per occurrence,
   pain points, and tools used.
2. Identify AI/automation opportunities. For each: description, estimated hours saved per
   month (show the calculation), complexity (low/medium/high), risks, data needed, and
   recommended tools.
3. Rank them in an impact vs. effort table, and recommend the top 5.
4. Note any quick wins doable in under 1 week.
Use only the information provided; label assumptions clearly.
```

### 4.5 AI Opportunity Audit: write the report and slides
```
Using the analysis above, write the AI Opportunity Report for [COMPANY]:
1. Executive summary (half a page, numbers first)
2. Current situation: key processes and pain points
3. Top 5 opportunities: for each, problem → solution → benefit (hours/€) → effort → risks
4. 90-day roadmap (phases, with what happens in each)
5. Recommended next step and investment (3 options)
6. Appendix: full opportunity list, methodology, assumptions
Then create a 10-slide presentation version for the leadership meeting.
```

### 4.6 Solution design for an automation
```
Design an automation for [COMPANY] for this process: [DESCRIBE AS-IS PROCESS + SAMPLE INPUTS].
Their tools: [ERP/CRM/email/etc.]. Constraints: [budget, no-code preferred, data location].
Give me: the to-be process (step list + simple diagram), the tool choice with reasons
(n8n/Make/Zapier/Power Automate/custom code), where the Claude API is used and with what
prompt, where a human reviews, error handling, security considerations, an estimated monthly
running cost, and a build plan in 1-week sprints.
```

### 4.7 Start a client build in Claude Code
Create a `CLAUDE.md` in the client project repository first:
```
# Project: [Client] – [App name]
Goal: [one sentence + success metric]
Users: [who, how many, technical level]
Stack: [e.g. Next.js + TypeScript + Supabase + Claude API], hosted on [Vercel/Render/client cloud]
Data: [sources]; personal data: [yes/no] → [handling rules]
Conventions: TypeScript strict, tests for core logic, env vars for secrets (never commit keys),
README with setup + run + deploy steps.
Out of scope: [list]
```
Then, in Claude Code:
```
Read CLAUDE.md. Propose an implementation plan in small milestones that can each be demoed.
Start with milestone 1 only, then stop and show me how to run it.
```

### 4.8 Build a dashboard
```
Build a [web dashboard with Next.js / Streamlit app] for [COMPANY] showing these KPIs:
[list] from this data: [CSV/DB/API description + sample]. Include filters for [date, region,
product], clear charts, and a "Weekly AI summary" panel that calls the Claude API to explain
the main changes vs. last week in 5 bullet points for a non-technical manager. Use mock data
first so I can demo it, and keep the data layer separate so I can connect real sources later.
```

### 4.9 Tailor a workshop to a client
```
Tailor our "AI Fundamentals for Teams" workshop (outline attached) for [COMPANY], a
[industry] company. Attendees: [roles, number, AI experience]. Their tools: [M365/Google/...].
Their concerns from the pre-survey: [...].
Create: (1) the agenda with timings, (2) 6 hands-on exercises using realistic tasks from
their jobs, (3) a 1-page prompt cheat-sheet for their roles, (4) 3 discussion questions about
safe use and their data rules, (5) a 5-question quiz for the AI-literacy record.
```

### 4.10 Website: copy, then build
```
Step 1 (Claude app): Write website copy for [BUSINESS]: [description, audience, services,
location, tone, competitors' sites]. Give the sitemap, then the full copy for each page with
SEO title and meta description. Include a clear call to action on each page.

Step 2 (Claude Code): Build a fast, responsive website with [Astro/Next.js] using this copy
(in /content), brand colors [..], font [..]. Include a contact form, booking link, privacy
policy page, cookie-free analytics, and good SEO basics. Make it easy for a non-developer to
edit the text later.
```

### 4.11 Viability report
```
Prepare a viability study for: [PROJECT: e.g. "a 40-room boutique hotel in [city]"].
Client inputs: [investment budget, location, timeline, financing, founder experience].
Follow our viability report template. Process:
1. First, give me the outline and a list of the data you need from me vs. what you'll research.
2. Research market size, demand trends, competitors (with prices), and regulations using web
   search; cite all sources with dates.
3. Build the financial model as an Excel file: CAPEX, OPEX, revenue drivers, 5-year P&L,
   cash flow, break-even, NPV/IRR/payback, and 3 scenarios + a sensitivity table on the
   2 most important assumptions.
4. Write the report with an executive summary and a clear recommendation.
Label all assumptions. Include the disclaimer.
```

### 4.12 Pitch deck
```
Create a 12-slide investor pitch deck for [COMPANY/PROJECT] from this material: [PASTE].
Structure: problem, solution, market, product, business model, traction, competition, go-to-
market, team, financials, ask & use of funds, contact. One key message per slide (as the slide
title), max 30 words of body text per slide, and speaker notes for each slide. Suggest a visual
for each slide. Output as PowerPoint.
```

### 4.13 Monthly content calendar
```
Create next month's LinkedIn calendar: 12 posts for [NICHE] decision-makers, rotating
demo / tip / case study / opinion / behind-the-scenes / news explained. For each: hook
(first line), full draft, suggested visual, and best day to post. This month's themes:
[e.g., invoice automation, AI literacy rules, our new workshop dates]. Real results I can
mention: [list, or "none yet"].
```

### 4.14 Personalized outreach message
```
Write a short LinkedIn message (max 300 characters for a connection note, plus a 600-character
follow-up) to [NAME], [ROLE] at [COMPANY]. What I know: [recent post/news/mutual contact].
Goal: a 20-minute chat about AI opportunities in their [process]. Tone: personal, helpful,
zero sales pressure. No flattery clichés. Give me 2 versions.
```

### 4.15 Case study
```
Write a case study from this project data: client [name or "a mid-size distributor"],
problem [..], solution [..], timeline [..], before/after metrics [..], client quote [..].
Format: title with the main result, 3-line summary, Challenge, Solution, Results (bullets with
numbers), Quote, "What's next". Also give me a LinkedIn post version and a 1-slide version.
```

### 4.16 SOP from a recording
```
Here's the transcript of [EMPLOYEE] explaining how they [PROCESS]:
[PASTE]
Write a standard operating procedure: purpose, scope, roles, tools, step-by-step instructions
(numbered, one action per step), decision points, common mistakes, and a checklist. Mark any
step that's unclear with [CONFIRM].
```

### 4.17 Tender / RFP analysis
```
Analyze this tender document [ATTACH]. Give me: (1) a summary, (2) all mandatory requirements
in a compliance matrix (requirement | section | our response | evidence needed), (3) evaluation
criteria and weights, (4) deadlines and submission format, (5) risks and questions to submit
to the contracting authority, (6) a go/no-go recommendation with reasons.
```

### 4.18 AI policy pack
```
Draft an AI acceptable-use policy for [COMPANY] ([industry], [size], tools: [..], located in
[country/EU]). Include: purpose, approved tools, data classification (what can and cannot be
entered into AI tools), human review requirements, transparency with customers, intellectual
property, AI literacy training requirement and records, incident reporting, and roles. Plus a
1-page plain-language employee summary. Note where legal review is recommended.
```

### 4.19 Weekly client update
```
Turn these notes into a weekly update email for [CLIENT PROJECT OWNER]: [notes]. Sections:
Done this week · Next week · Decisions/inputs needed from you (with dates) · Risks. Max 200
words, friendly and clear.
```

---

## 5. Turning prompts into Skills

When a prompt becomes a process you run every week (proposals, audit reports, viability reports), package it as a **Claude Skill**: a folder with instructions plus your templates. Claude then follows the same high-quality process every time, and you can share it with future team members. Good first Skills to create:

1. `praxis-proposal`: discovery notes → 3-option proposal in your format
2. `praxis-audit-report`: interviews → opportunity analysis → report + slides
3. `praxis-viability-report`: brief → research → Excel model → report
4. `praxis-workshop-tailor`: base workshop → client-specific materials
