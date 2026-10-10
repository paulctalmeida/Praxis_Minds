# 02 – Services Catalog

Services are grouped into three families, matching the brand promise **Find → Build → Teach**, plus a fourth family of **AI-powered business services** that bring in cash early and open doors.

| Family | Services | Role in the business |
|---|---|---|
| **A. Find** | AI Quick-Start, AI Opportunity Audit | Entry offers: low risk for the client, and they lead into builds |
| **B. Build** | Workflow automation, custom AI apps & assistants, dashboards & integrations | Core revenue, biggest projects |
| **C. Teach** | Workshops, training programs, AI policy pack | Door-openers, trust builders, recurring demand |
| **D. Business services** | Websites, viability reports, pitch decks, business plans, marketing, research, SOPs, proposals/tenders | Fast cash flow; Claude does 70–80% of the drafting |
| **Recurring** | AI Partner retainer, maintenance & hosting, care plans, content retainers | Predictable monthly income |

Prices are summarized in [03 – Pricing](03-pricing.md). How to produce each deliverable with Claude is in [07 – Claude Playbook](07-claude-playbook.md).

---

## A. FIND

### A1. AI Quick-Start Session
- **Problem:** "We want to start with AI but don't know how."
- **What they get:** a 2-hour live session (remote or on-site) with the owner/managers. We review their main processes, show 3–5 live demos relevant to their business, and send a 1–2 page **"Top 5 AI quick wins"** summary afterwards.
- **How Claude helps:** prepare industry-specific demos beforehand; turn meeting notes into the summary in minutes.
- **Timeline:** 1 week, including prep and summary.
- **Upsell:** AI Opportunity Audit (credit the Quick-Start fee toward it).

### A2. AI Opportunity Audit ⭐ *flagship entry offer*
- **Problem:** "Where exactly will AI save us time or money, and how much?"
- **What they get:**
  1. Kickoff and short interviews with 3–6 key people (operations, finance, sales, admin).
  2. [AI readiness assessment](../templates/ai-readiness-assessment.md) survey for the team.
  3. Process map of 5–10 key workflows, with time spent and pain points.
  4. **AI Opportunity Report**: the top 5–10 opportunities ranked by impact vs. effort, estimated hours/€ saved, recommended tools, risks, and a 90-day roadmap.
  5. A 60-minute presentation of findings to leadership.
- **How Claude helps:** summarize interview transcripts, cluster pain points, estimate time savings, draft the report and slides, and build a quick prototype of the #1 opportunity to show in the final meeting (a powerful closer).
- **Timeline:** 2–3 weeks.
- **Upsell:** implementation project. **Credit 50–100% of the audit fee if they sign a build within 30 days.**

---

## B. BUILD

### B1. Workflow Automation
- **Problem:** repetitive manual tasks: data entry, copy-paste between systems, sorting emails, generating standard documents.
- **Typical projects:**
  - Invoices, orders, or delivery notes (PDF/email) → extracted data → ERP/accounting/spreadsheet
  - Incoming email triage → classify, summarize, draft a reply, route to the right person
  - CRM updates from calls and meetings → automatic notes and follow-up tasks
  - Standard documents (quotes, contracts, reports) generated from templates and data
  - Weekly reporting compiled automatically from multiple sources
- **What they get:** a working automation, documentation, a short training session, and 30 days of support.
- **How it's built:** n8n / Make / Zapier or Power Automate, connected to the Claude API for the "thinking" steps (reading, classifying, writing). Custom code with Claude Code when no-code isn't enough.
- **Timeline:** 1–4 weeks per workflow.
- **Upsell:** maintenance plan; the next workflow on the roadmap; AI Partner retainer.

### B2. Custom AI Apps & Assistants
- **Problem:** the company needs a tool that doesn't exist off the shelf.
- **Typical projects:**
  - **Company knowledge assistant:** chat with your manuals, policies, product catalog, and procedures (with source citations).
  - **Customer service assistant:** answers FAQs on the website or in email, and hands off to a human when needed.
  - **Quote/proposal generator:** fill a form, get a professional branded quote or proposal.
  - **Internal tools:** onboarding assistant, HR policy Q&A, sales call prep tool, tender analyzer.
  - **Document review tools:** compare contracts against a checklist and flag missing clauses (with human review).
- **What they get:** a web app (or Teams/Slack bot) with login, hosting setup, documentation, training, and 30 days of support.
- **How it's built:** Claude Code builds the app (e.g. Next.js or Python/Streamlit), the Claude API powers the AI, and it's hosted on Vercel, Render, Railway, or the client's cloud. See [08 – Tech Stack](08-tech-stack.md).
- **Timeline:** 3–8 weeks.
- **Upsell:** hosting and maintenance (monthly), new features, rollout to other departments, training.

### B3. Dashboards & Software Integrations
- **Problem:** "Our data is spread across systems; nobody sees the full picture." "Our tools don't talk to each other."
- **Typical projects:**
  - **Management dashboard:** sales, operations, and finance KPIs in one place, with an **AI-written weekly summary** ("Sales are down 8% in the North region, driven by…").
  - **Employee/team dashboards:** workload, task status, project progress, training completion.
  - **Integrations:** connect CRM ↔ ERP ↔ accounting ↔ spreadsheets ↔ email so data flows automatically.
  - **"Ask your data" assistant:** managers ask questions in plain language and get answers and charts.
- **How it's built:** Looker Studio / Power BI for clients already in those ecosystems; custom web dashboards (Next.js, Streamlit) built with Claude Code; APIs and n8n/Make for integrations.
- **Timeline:** 2–6 weeks.
- **Upsell:** monthly data/reporting support, new data sources, AI insights add-on.

> ⚠️ **HR and employee dashboards: compliance note.** Dashboards that *display* data (workload, project status, training completion) are standard. But AI systems that **evaluate, rank, or monitor employees, or influence hiring, promotion, task allocation, or dismissal**, are classed as **high-risk** under the EU AI Act and are tightly regulated by employment and data protection law. Avoid these in the early phase, or deliver them only with legal review. See [09 – Legal](09-legal-and-compliance.md#5-eu-ai-act-what-matters-for-praxis-minds).

---

## C. TEACH

### C1. AI Workshops (in-company)
- **Problem:** "Our team doesn't know how to use AI well, or is afraid of it."
- **Formats:** (full outlines in [workshop curriculum](../templates/workshop-curriculum.md))
  - **AI Fundamentals for Teams:** 90 minutes or a half-day
  - **AI for Your Role:** tracks for sales & marketing, admin & operations, finance, HR, management
  - **Build Your First AI Workflow:** full-day hands-on session
  - **AI for Leaders:** half-day strategy and governance session for executives
- **What they get:** a live workshop (on-site or remote), slides, a hands-on workbook, a prompt library tailored to their company, attendance certificates (useful as **AI-literacy evidence** for EU AI Act Article 4), and a follow-up Q&A session.
- **How Claude helps:** tailor examples and exercises to each client's industry and tools; generate workbooks, quizzes, and certificates.
- **Upsell:** Opportunity Audit (workshops surface lots of ideas); AI Champions program; builds.

### C2. AI Champions Program (6 weeks)
- A cohort of 5–15 employees meets weekly. Each person builds one real AI workflow for their own job, with office hours and a final demo day for management.
- **Why it sells:** creates internal AI leaders and produces 5–15 measurable improvements, which are great case-study material.

### C3. Public Workshops & Online Courses *(Phase 3+)*
- Open-enrollment workshops (per seat) and, later, a recorded online course. They build your brand and a mailing list, and generate income without client work.

### C4. AI Policy & Governance Pack
- **Problem:** "Employees use AI, but we have no rules."
- **What they get:** an AI acceptable-use policy, data classification rules ("what can go into AI tools"), an approved tools list, an AI literacy training record template, and a one-page employee guide.
- **How Claude helps:** drafts tailored to the company. *Recommend lawyer review for legal sign-off.*
- **Why it sells:** low price, quick to deliver, fits naturally after a workshop, and shows maturity.

---

## D. AI-POWERED BUSINESS SERVICES

These are services where Claude does most of the drafting and you add expertise, verification, design, and the client relationship. They're quick wins for cash flow and portfolio. **Don't lead your marketing with them; offer them to existing contacts and clients.**

### D1. Website Creation
- **Packages:** Starter (1–5 pages), Business (5–15 pages + blog/CMS + SEO basics), Plus (multilingual, booking/forms/integrations, AI chat assistant).
- **Process:** brief questionnaire → Claude drafts sitemap and copy → design/build with Claude Code (Astro/Next.js) or a builder (Webflow, Framer, WordPress) → client review (2 rounds) → launch → care plan.
- **Differentiator:** every site can include an **AI assistant** trained on the business's FAQs. That links to your core AI services.
- **Recurring:** care plan (hosting, updates, small edits, monthly report).

### D2. Viability & Feasibility Reports
- **Problem:** entrepreneurs or companies need to decide on, or raise money for, a new project: a new location, product, factory, franchise, or business.
- **What they get:** a professional report (template: [viability report](../templates/viability-report-template.md)) with market analysis, competition, operational plan, financial projections (3–5 years, P&L, cash flow, break-even, NPV/IRR/payback), scenarios and sensitivity, risks, and a recommendation. Delivered as a PDF/Word document, plus an Excel financial model and a summary presentation.
- **How Claude helps:** market research with web search (always verify sources), structure, writing, financial-model scaffolding in Excel, and charts.
- **Important:** you provide analysis and projections, **not investment advice or audited figures**. Include a disclaimer, and partner with an accountant when certified projections are required (e.g. for bank loans or public funding applications).
- **Upsell:** pitch deck, business plan, website for the new venture.

### D3. Pitch Decks & Business Presentations
- Investor pitch decks, sales decks, company presentations, board/strategy presentations, and conference talks.
- Claude drafts the storyline and the slides (PowerPoint/Google Slides); you refine the design and the message with the client.

### D4. Business Plans
- A full business plan for banks, investors, or public funding programs. Often bundled with D2 and D3 as a **"Funding Pack"** (viability report + business plan + pitch deck).

### D5. Marketing Content Services
- **One-off:** brand messaging, website copy, sales brochures, email sequences, product descriptions, case studies.
- **Monthly retainer:** LinkedIn/social calendar and posts, blog articles (SEO), a newsletter, and repurposing (1 article → 5 posts → 1 newsletter).
- **How Claude helps:** drafting in the client's brand voice (stored in a dedicated Claude Project per client), with you as editor and strategist.
- **Upsell:** set up the client's own AI content workflow and train their marketing person (that's a Build + Teach engagement).

### D6. Market & Competitor Research Reports
- Market overview, competitor benchmarking, customer persona research, pricing analysis, trend reports.
- Claude with web search gathers and synthesizes; you verify key facts and add insight.

### D7. Process Documentation & SOPs
- Turn "it's all in Maria's head" into clear, step-by-step procedures, checklists, and onboarding manuals.
- Record a walkthrough call → transcript → Claude drafts the SOP → expert review. Also the perfect input for a **knowledge assistant** (B2).

### D8. Proposal, Tender & Grant Writing Support
- Help companies respond to tenders (RFPs) and public funding calls: requirement checklists, compliance matrices, first drafts, editing.
- High value for companies that bid often. Can grow into a **tender analyzer app** (B2).

### D9. Translation & Localization
- Translating websites, product documentation, and marketing into other languages, with native-speaker review for important content.

---

## RECURRING SERVICES

| Service | What's included |
|---|---|
| **AI Partner retainer** | A fixed number of hours/month for improvements, new small automations, team support, monthly AI update and opportunities meeting |
| **App/automation maintenance & hosting** | Monitoring, fixes, API/model updates, small changes, hosting management |
| **Website care plan** | Hosting, security updates, backups, small edits, monthly report |
| **Content retainer** | Monthly marketing content (see D5) |
| **Dashboard/reporting support** | Data checks, new metrics, monthly AI insights report |

> **Goal:** turn every completed project into a recurring relationship. Recurring revenue is what makes the business stable.

---

## Service packaging ideas (bundles)

| Bundle | Contents | Who it's for |
|---|---|---|
| **AI Launchpad** | Opportunity Audit + Team Workshop + first automation | Companies starting with AI |
| **Funding Pack** | Viability report + business plan + pitch deck | Entrepreneurs, new projects, loan/grant applicants |
| **Digital Presence Pack** | Website + AI chat assistant + 3 months of content | Small businesses modernizing |
| **AI-Ready Team** | Leaders workshop + team workshops + AI policy pack + AI Champions program | Mid-size companies focused on adoption and compliance |
