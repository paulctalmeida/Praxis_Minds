# 06 – Delivery Process

A standard process makes every project predictable for the client and repeatable for you. It is the same for every Build project; Find, Teach, and business services use a shortened version (see the bottom of this page).

```
 1. Sign      2. Kickoff     3. Discover    4. Design     5. Build       6. Test        7. Launch     8. Handover    9. Support &
 & onboard →  meeting    →   & collect  →   & approve →   in sprints →   with users →   (go-live)  →  & training  →  case study
 (day 0)      (week 1)       data            (sign-off)    (weekly demos)  (UAT)                                    (30 days → retainer)
```

---

## Stage 1: Sign & onboard (day 0)
- [ ] Proposal accepted → send the **SOW** ([template](../templates/statement-of-work-template.md)) + services agreement (+ DPA if personal data is involved)
- [ ] Deposit invoice sent and paid
- [ ] Create the client folder from [`clients/_template/`](../clients/_template/)
- [ ] Create a dedicated **Claude Project** for the client (context: company profile, goals, SOW, glossary)
- [ ] Send a welcome email: what happens next, who you need, kickoff date

## Stage 2: Kickoff meeting (week 1, 60 minutes)
Use the [kickoff checklist](../templates/project-kickoff-checklist.md).
- Confirm goals and **success metrics** (e.g. "reduce invoice processing from 12 hours to 2 hours a week")
- Measure the **baseline** now. You'll need it for the case study.
- Name the client's **project owner** (one person who decides and answers questions)
- Agree access needs (systems, sample data, accounts), the communication channel, and the weekly update day
- Confirm what's **out of scope**

## Stage 3: Discover & collect (week 1–2)
- Shadow or record the current process (screen recording + narration is ideal)
- Collect **real samples** (e.g. 30–50 invoices, emails, reports), anonymized where possible
- Document the "as-is" process and edge cases. Claude turns recordings and transcripts into process maps quickly.

## Stage 4: Design & approve
- Short **solution design** (1–3 pages): "to-be" process, tools, data flow, where humans check AI output, security approach
- A clickable mockup or quick prototype (Claude Artifacts are great for this)
- **Client sign-off** before the main build. This protects you from scope creep.

## Stage 5: Build in sprints (1-week cycles)
- Build with Claude Code / no-code tools following the [tech stack](08-tech-stack.md)
- **Weekly update** (email or a 15-minute call): done, next, blockers, decisions needed
- **Weekly demo** of working progress, even if rough
- Change requests → written, estimated, approved before work starts

## Stage 6: Test with users (UAT)
- Test with **real data** and the people who will use it
- Measure accuracy (e.g. "extraction correct on 47/50 invoices") and fix the gaps
- Define how errors are handled: what happens when the AI is unsure? (Flag for human review.)
- Security check: access control, secrets stored safely, logging, no data exposed

## Stage 7: Launch
- Go-live plan: date, who's affected, rollback plan
- Run in **parallel** with the old process for 1–2 weeks when the stakes are high
- Monitor closely during the first week

## Stage 8: Handover & training
- **Documentation:** how it works, how to use it, what to do when something breaks, who to call
- **Training session(s)** for users (recorded)
- Hand over credentials and ownership per the contract (client owns their accounts and data)
- Final invoice

## Stage 9: Support & case study
- **30 days of included support** (bug fixes, small adjustments)
- At day 30: **results review meeting** comparing before and after metrics
  - Ask for the **testimonial** and **case-study permission**
  - Present the **maintenance plan / AI Partner retainer**
  - Ask: "Who else do you know who has this problem?"
- Write the case study ([template](../templates/case-study-template.md))

---

## Shortened processes

### Find (Quick-Start / Audit)
Sign → pre-call questionnaire / [readiness assessment](../templates/ai-readiness-assessment.md) → interviews/workshop → Claude-assisted analysis → report + presentation → proposal for the next step.

### Teach (workshops)
Book → pre-workshop survey (roles, tools, AI experience, concerns) → tailor examples to their company → deliver → send materials, certificates, and a feedback form → 2-week follow-up Q&A → offer the next step (Audit / Champions program).

### Business services (websites, reports, decks)
Brief/questionnaire → Claude-assisted first draft → **your expert review and fact-check** → client review (round 1) → revisions → client review (round 2) → final delivery → upsell (care plan, deck, content).

---

## Quality rules (non-negotiable)

1. **Human review of every AI-generated deliverable** before the client sees it. You are responsible for the output, not Claude.
2. **Fact-check numbers, names, laws, and sources** in reports. Never deliver an unverified statistic.
3. **Test on real data** before saying something works.
4. **Humans in the loop** for decisions that affect money, legal matters, health, or people's jobs.
5. **Document everything** so the client isn't dependent on your memory.
6. **Under-promise, over-deliver** on timelines.

## Data-handling rules

1. Use **commercial terms** for client data: the Claude API, or Claude Team/Enterprise plans, whose terms don't use your data for model training by default (always verify current terms). Don't paste confidential client data into personal/consumer accounts.
2. Ask for **anonymized or sample data** whenever real personal data isn't necessary.
3. Store client files in the client's own systems or in an access-controlled company drive. **Do not commit confidential client data to Git repositories** unless the repo is private and the contract allows it.
4. Use **the client's own accounts** (API keys, hosting, automation tools) for production systems where possible, so they own their data and costs.
5. Keep secrets (API keys, passwords) in a password manager or secret store, never in documents or code.
6. Sign a **DPA** when you process personal data on the client's behalf (see [09 – Legal](09-legal-and-compliance.md)).
7. Delete or return client data at the end of the engagement, as the contract specifies.
