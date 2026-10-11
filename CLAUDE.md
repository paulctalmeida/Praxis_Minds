# CLAUDE.md: Praxis Minds

This repository is the operating manual for **Praxis Minds**, an AI consultancy (tagline: "AI, put into practice"). It holds strategy, plans, templates, and client records. It is not a software project.

## The business in brief
- **Promise:** Find → Build → Teach. We find AI opportunities, build working solutions, and train teams.
- **Services:** AI Opportunity Audits, workflow automation, custom AI apps/assistants, dashboards & integrations, AI workshops and training, plus AI-powered business services (websites, viability reports, pitch decks, business plans, marketing content). See `plan/02-services.md`.
- **Clients:** small and medium businesses (10–250 employees) in the chosen niche.
- **Currency:** EUR. Prices: `plan/03-pricing.md`.

## Current focus
<!-- Update as the business evolves -->
- **Phase:** 0–1 (Foundation & launch). See `START-HERE.md`
- **Primary niche:** _TBD (choose with the scorecard in plan/01)_
- **Backup niche:** _TBD_
- **Founding clients signed:** 0

## Repository layout
- `START-HERE.md`: first-30-days checklist (update checkboxes as tasks are completed)
- `plan/`: strategy documents 01–11
- `templates/`: proposal, SOW, discovery script, readiness assessment, viability report, workshops, outreach, kickoff, case study
- `clients/<client-name>/`: one folder per client, copied from `clients/_template/`
- `website/`: the company website (static HTML/CSS/JS, no build step). Design tokens are at the top of `website/assets/styles.css`; keep prices on the site in sync with `plan/03-pricing.md`. The site is bilingual: English in `website/index.html`, European Portuguese (pt-PT, AO90 spelling) in `website/pt/index.html`. Any content change goes into both. See `website/README.md`.
- `video/`: the 94-second animated film (`film.html`, EN and PT), its renderer, its soundtrack (made in code by `video/audio/soundtrack.py`, so it is free to use) and the MP4s. It follows the website design in https://claude.ai/artifact/9Lms1UPDn7ZYY25LgYHe4y (teal, coral, line-drawn logo) and reuses that site's example week and calculator numbers, so update it when those change. See `video/README.md`.

## How to work in this repo
- When creating client documents, **start from the matching file in `templates/`** and save the result in `clients/<client-name>/`.
- Use prices from `plan/03-pricing.md` and always offer 3 options (Essential / Recommended / Complete).
- Writing style: plain, confident, jargon-free, concise. No hype words ("revolutionize", "game-changer", "unlock", "leverage", "delve").
- Never invent client results, statistics, testimonials, or sources. Use `[placeholders]` for numbers the founder must supply.
- For reports: separate facts (with source + date), assumptions (labelled), and estimates (with method).
- Flag any project touching high-risk AI uses (employment decisions, employee evaluation/monitoring, credit scoring, biometrics). See `plan/09-legal-and-compliance.md`.
- **Never store** personal data, credentials, API keys, or confidential client documents in this repo (see `clients/README.md`).
- When plans change (niche, prices, phase), update the relevant `plan/` file and the "Current focus" section above.
