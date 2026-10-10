# 09 – Legal & Compliance

> **This is general guidance, not legal or tax advice.** Rules differ by country. Book one session with a local **accountant** and one with a **business lawyer** in month 1. It's money well spent.

## 1. Company setup

| Step | What to do | Who helps |
|---|---|---|
| Legal structure | **Sole trader/freelancer** (simplest, cheapest, but personal liability) vs. **limited company** (protects personal assets, more admin, often better once profits grow). Many consultants start as sole traders and convert later; with build projects carrying liability risk, a limited company can make sense earlier. | Accountant |
| Registration | Register the business and activity codes (consulting, IT services, training) with your country's business/tax authority. | Accountant |
| Tax & VAT | Register for VAT if required; understand VAT rules for B2B services to other EU countries (reverse charge) and non-EU clients. | Accountant |
| Social security | Register as self-employed or as a company director, as your country requires. | Accountant |
| Bank account | Separate business account from day 1. | Bank |
| Name protection | Check that "Praxis Minds" is free in the business registry and trademark databases (national office and EUIPO for the EU). Consider registering the trademark once revenue starts. | Lawyer / IP office |
| Invoicing | Use certified/compliant invoicing software if your country requires it. | Accountant |
| Training certification *(optional)* | Some countries let accredited training providers' courses count toward mandatory employee-training hours or funding. Check whether certification is worth it for your workshops. | Training authority |

---

## 2. Contracts you need

Get these drafted or reviewed by a lawyer once, then reuse them.

| Document | Purpose | Key clauses |
|---|---|---|
| **Master Services Agreement (MSA)** / Terms of Service | The general rules for all work with a client | Payment terms, IP, confidentiality, **limitation of liability** (e.g. capped at fees paid), warranties, AI disclaimer, termination, governing law |
| **Statement of Work (SOW)** | The specific project ([template](../templates/statement-of-work-template.md)) | Scope, deliverables, out of scope, timeline, price, acceptance criteria, change requests, client responsibilities |
| **NDA** | Confidentiality before discovery or audits | Mutual, 2–5 years |
| **Data Processing Agreement (DPA)** | Required under GDPR when you process personal data **on the client's behalf** | Purpose, data types, security measures, **sub-processors** (e.g. Anthropic, hosting providers), deletion, breach notification |
| **Workshop terms** | Bookings, cancellations, recordings | Cancellation policy, materials licence (internal use only) |
| **Subcontractor agreement** | When you use freelancers | Confidentiality, IP assignment to you/client, data protection, quality |
| **Referral partner agreement** | Referral fees | Fee %, when it's paid, duration |
| **Website legal pages** | Privacy policy, cookie policy, terms | Required for your own site and the client sites you build |

### Intellectual property (IP): the standard approach
- **The client owns the final deliverables** (their custom code, documents, content) **once paid in full.**
- **Praxis Minds keeps ownership of its pre-existing tools, templates, and reusable components**, and grants the client a perpetual licence to use them inside the deliverable. This protects your component library, your main speed advantage.
- Note that AI-generated content may have limited copyright protection in some countries. Avoid promising exclusivity beyond what the law supports, and keep human creative contribution in key deliverables.

### AI-specific contract clauses
- **AI disclosure:** "Praxis Minds uses AI tools, including Claude by Anthropic, to assist in producing deliverables. All deliverables are reviewed by our team."
- **Accuracy disclaimer:** AI systems can make errors; the client is responsible for reviewing outputs used for important decisions; human-review steps are part of the design.
- **Third-party services:** the client accepts the terms of the AI/hosting providers used in their solution; API usage costs are billed as agreed.
- **Reports & projections:** viability reports and business plans are analyses based on stated assumptions, **not financial or investment advice, and not guarantees.**

---

## 3. Insurance

| Insurance | Why |
|---|---|
| **Professional indemnity / errors & omissions** | Covers claims that your advice or software caused a client loss. **The most important one.** |
| **Cyber liability** | Data breaches, ransomware, client data incidents |
| **General/public liability** | On-site workshops and visits to client premises |

Get quotes before your first build goes live. Some clients will ask for proof of insurance.

---

## 4. GDPR & data protection (EU)

If you or your clients are in the EU, or you handle EU residents' data, GDPR applies.

**For Praxis Minds itself:**
- [ ] Privacy policy on the website (what you collect, why, how long, rights)
- [ ] Cookie consent if you use non-essential cookies/analytics
- [ ] Keep a simple **record of processing activities** (CRM contacts, newsletter, client data)
- [ ] Newsletter: opt-in consent; easy unsubscribe
- [ ] Cold outreach: B2B rules vary by country. Keep it relevant, personal, and include an opt-out.

**For client projects:**
- [ ] Identify whether the project involves **personal data** (employees, customers). If yes, sign a **DPA**.
- [ ] **Data minimization:** use only the data needed; anonymize samples.
- [ ] Check **where data is processed** (e.g. EU hosting options, the AI provider's data terms and processing locations) and list sub-processors in the DPA.
- [ ] Use AI providers' **commercial terms** (API/Team/Enterprise) that don't use client data for training by default. Verify the current terms.
- [ ] For high-risk processing (e.g. large-scale employee data, monitoring), the client may need a **Data Protection Impact Assessment (DPIA)**. Flag it and involve their DPO/lawyer.
- [ ] **Employee monitoring** is heavily restricted in most EU countries (and may require works council or employee consultation). Be careful with "employee dashboards."

---

## 5. EU AI Act: what matters for Praxis Minds

The EU AI Act entered into force on 1 August 2024 and applies in stages. Parts of it were amended in 2026 by the "Digital Omnibus on AI." **Check the current consolidated text and dates before advising clients;** this area is changing.

### a) AI literacy (Article 4): a sales opportunity
- Since **2 February 2025**, providers and deployers of AI systems (which includes **any company whose staff use AI tools at work**) must take measures to support AI literacy among staff.
- The 2026 Digital Omnibus **recalibrated** this obligation: companies must still take measures to promote AI literacy, but the wording around guaranteeing a "sufficient level" for each individual was softened. **AI literacy remains an obligation.**
- **What this means for you:** your **workshops, AI policy pack, and training records** directly help clients meet this obligation. Use this in your marketing, accurately and without fear-mongering ("Train your team and document it" rather than "You'll be fined!").

### b) Transparency (Article 50)
- People must be informed when they're interacting with an AI system (e.g. a website chatbot), and certain AI-generated content must be disclosed/marked. **Build this into every assistant you deliver** (e.g. "I'm an AI assistant. A human can help you at…").

### c) High-risk AI: avoid early, or handle with care
AI used in these areas is **high-risk**, with heavy obligations (risk management, data governance, documentation, human oversight, registration):
- **Employment & workers' management:** recruitment/CV screening, promotion or termination decisions, task allocation based on behaviour or traits, **monitoring and evaluating employee performance**
- Access to essential services (e.g. **credit scoring**, insurance pricing for individuals)
- Education (exam scoring, admissions), critical infrastructure, law enforcement, migration, justice

Under the 2026 amendments, some high-risk obligations were postponed (reportedly to December 2027 for standalone systems such as employment uses). **Verify the current dates.**

**Praxis Minds policy:** in years 1–2, **don't build systems that make or materially influence decisions about people** in these areas. Productivity tools, document processing, knowledge assistants, reporting dashboards, and content generation are generally minimal/limited-risk uses.

### d) Prohibited practices (never build)
Including: emotion recognition in the workplace or education (except for medical/safety reasons), social scoring, manipulative techniques that cause harm, untargeted scraping of facial images, and certain biometric categorization.

---

## 6. Responsible AI checklist (use on every project)

- [ ] Clear purpose; no prohibited or high-risk use (or legal review done)
- [ ] Personal data identified → DPA, minimization, lawful basis confirmed by the client
- [ ] Human review for important outputs; users can escalate to a human
- [ ] Users are told when they're interacting with AI
- [ ] Accuracy tested on real samples; known limitations documented
- [ ] Security: access control, secrets management, logging, client-owned accounts
- [ ] Client team trained (and AI-literacy training recorded)
- [ ] Documentation handed over
