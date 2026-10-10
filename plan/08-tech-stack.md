# 08 – Tech Stack

Keep the stack **small, standard, and reusable**. Every client project should reuse the same building blocks, so each build is faster than the last.

## Stack overview

| Category | Recommended | Alternatives | Notes |
|---|---|---|---|
| AI assistant (your daily work) | **Claude** (Pro → Max → Team) | — | Writing, research, analysis, files, prototypes |
| AI coding | **Claude Code** | — | Websites, apps, dashboards, integrations |
| AI inside client products | **Claude API** | Claude via AWS Bedrock, Google Vertex AI, or Microsoft Foundry | Use the client's cloud when they require it |
| Workflow automation | **n8n** | Make, Zapier, Power Automate (Microsoft clients) | n8n can be self-hosted, which helps with data control |
| App framework | **Next.js (TypeScript)** | Python + FastAPI / Streamlit | Streamlit is great for quick internal tools and dashboards |
| Database + login | **Supabase** (Postgres, auth, storage, pgvector) | Firebase, client's own database | EU region available |
| Hosting | **Vercel** / Netlify / Render / Railway | Client's Azure/AWS/GCP | Free tiers for demos |
| Dashboards | **Looker Studio** (free), **Power BI** | Metabase (open-source), custom Next.js/Streamlit | Match what the client already uses |
| Websites | **Astro or Next.js + Claude Code** | Webflow, Framer, WordPress | Use builders when the client must edit pages themselves |
| Workspace | Google Workspace or Microsoft 365 | — | Professional email on your domain |
| CRM | **HubSpot Free** | Pipedrive, Notion, spreadsheet | Start simple |
| Booking | Cal.com / Calendly | Google Calendar booking pages | Link on website + email signature |
| Design | Canva, Figma | — | Social graphics, slides, mockups |
| Video | Loom (or any screen recorder) | — | Demo videos, async client updates |
| Security | Password manager (Bitwarden/1Password), MFA everywhere | — | Non-negotiable from day 1 |
| Accounting & invoicing | Local accounting software your accountant supports | — | Must meet your country's invoicing rules |

---

## Claude plans (for you and your team)

Consumer and team prices change over time, so **check the current prices at [claude.com/pricing](https://claude.com/pricing).** Indicative prices (USD) reported in 2026:

| Plan | Indicative price | When to use it |
|---|---|---|
| **Pro** | ~$20/month (~$17/month billed annually) | Month 1: writing, research, Projects, light Claude Code |
| **Max** | ~$100 or ~$200/month (5× or 20× Pro usage) | When you build with Claude Code every day |
| **Team** | Per seat/month (Standard and Premium seats) | When you add collaborators or want commercial data terms for client work |
| **Enterprise** | Custom | Later, if you grow to a larger team |

---

## Claude API models & pricing

API usage is billed **per token** (roughly ¾ of a word). Rates in USD per million tokens (MTok), as of October 2026; check the current [pricing page](https://claude.com/pricing) before quoting clients.

| Model | Input $/MTok | Output $/MTok | Best for |
|---|---|---|---|
| **Claude Opus 5.5** | $4.00 | $20.00 | **The default.** Complex reasoning, agents, coding, high-quality writing, document analysis |
| **Claude Sonnet 5.5** | $2.00 | $10.00 | Everyday, high-volume work where speed matters: assistants, triage, drafting |
| **Claude Haiku 5.5** | $0.10 | $0.50 | Very high-volume, simple tasks: classification, routing, simple extraction |
| **Claude Fable 5.1** | $10.00 | $50.00 | The hardest, highest-stakes reasoning tasks |

**Rule of thumb:** prototype with **Opus 5.5**, measure quality on real samples, and only move a high-volume step to Sonnet or Haiku if the test results stay good.

**Ways to cut running costs:**
- **Prompt caching:** reuse long, fixed instructions or documents across requests at a fraction of the input price.
- **Batch API:** about **50% cheaper** for work that doesn't need an instant answer (overnight document processing, weekly reports).
- **Short outputs:** ask for structured, concise output (e.g. JSON fields, not essays).
- **Spend limits:** set monthly limits per API key/workspace in the Claude Console, with **one workspace or key per client**.

### Claude API cost examples

These are rough estimates for illustration. Real usage varies; reasoning (thinking) tokens are billed as output, so **measure during the pilot** and set a buffer.

| Use case | Volume/month | Tokens/month | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|---|
| Knowledge assistant: ~5,000 input + 500 output tokens per question | 2,000 questions | 10M in / 1M out | ~$60 | ~$30 | ~$1.50 |
| Invoice extraction: ~3,000 input + 400 output tokens per invoice | 1,000 invoices | 3M in / 0.4M out | ~$20 | ~$10 | ~$0.50 |
| Weekly AI dashboard summary: ~20,000 input + 1,000 output tokens | 4 summaries | 80k in / 4k out | ~$0.40 | ~$0.20 | ~$0.01 |

**Business takeaway:** AI running costs are usually **tiny compared with the value** (hours saved). Charge for the outcome and for maintenance, and pass API costs through at cost or include them up to a cap.

---

## Reusable building blocks (your component library)

Build these once, then reuse and adapt them for every client. They're your speed advantage and your margin.

| Block | Description | Used in |
|---|---|---|
| **Document extractor** | PDF/email → structured fields (JSON/spreadsheet) with confidence flags | Invoices, orders, forms, contracts |
| **Email triage** | Classify → summarize → draft reply → route | Customer service, sales inbox |
| **Knowledge assistant** | Chat over company documents with source citations, access control | Policies, manuals, product catalogs |
| **Report generator** | Data + template → written report (Word/PDF) | Weekly reports, client reports, audits |
| **AI summary widget** | Explains dashboard changes in plain language | Dashboards |
| **Quote/proposal builder** | Form → branded document | Sales teams |
| **Website starter** | Astro/Next.js template with SEO, forms, booking, AI chat | Website service |
| **Workshop kit** | Slides, workbook, exercises, quiz, certificate | All workshops |

**Knowledge assistants, simple approach first:** for small document sets (up to a few hundred pages), place the documents directly in the prompt (Claude's 1M-token context) and use prompt caching to keep costs down. Move to a search/vector database (e.g. Supabase pgvector) only when the document collection is large or changes constantly.

---

## Tool budget

| Item | Phase 1 (months 1–3) | Phase 3+ (growth) |
|---|---|---|
| Claude subscription | ~€20 (Pro) | ~€100–€200 (Max) or Team seats |
| Claude API (demos/dev; client usage billed to clients) | €20–€50 | €50–€100 |
| Workspace email (Google/Microsoft) | €7–€15 | €15–€30 (2 users) |
| Domain(s) | ~€2–€5 (≈ €20–€60/year) | same |
| Hosting (demos, own website) | €0 (free tiers) | €20–€50 |
| Automation tool (n8n cloud/Make) | €0–€25 | €25–€60 |
| Canva Pro | ~€12 | ~€12 |
| CRM | €0 | €0–€50 |
| Booking, video, password manager | €0–€20 | €20–€40 |
| **Total** | **~€60–€200/month** | **~€250–€550/month** |

---

## Security baseline (from day 1)

- [ ] Multi-factor authentication (MFA) on every account (email, Claude, GitHub, hosting, banking)
- [ ] Password manager; never share passwords by email or chat
- [ ] Separate API keys **per client**, with spend limits; rotate if exposed
- [ ] Secrets in environment variables / secret stores, never in code or documents
- [ ] Encrypted laptop, automatic updates, backups
- [ ] Client production systems in the **client's own accounts** wherever possible
- [ ] Keep this repository **private**
