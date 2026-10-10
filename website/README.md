# Praxis Minds website

A static website: plain HTML, CSS and JavaScript. There's no build step, no framework, and nothing to install, so it can be hosted almost anywhere for free and edited in any text editor (or by asking Claude).

```
website/
├── index.html          the homepage in English (all sections)
├── pt/index.html       the homepage in Portuguese (Portugal), served at /pt/
├── privacy.html        privacy policy, English (draft: fill in before launch)
├── privacidade.html    privacy policy, Portuguese (draft: fill in before launch)
├── 404.html            "page not found", in both languages
├── robots.txt          for search engines
├── sitemap.xml         for search engines, with language alternates
└── assets/
    ├── styles.css      all design: colours, fonts, layout (tokens at the top)
    ├── main.js         menu, animations, service tabs, the example week, the calculator, the contact form (both languages)
    ├── favicon.svg     browser tab icon
    ├── og-image.png    share image, English
    └── og-image-pt.png share image, Portuguese
```

## Two languages
- The English site is at `/` and the Portuguese site at `/pt/`. A switch in the header (EN | PT) links each page to its translation, and the pages tell search engines about each other (`hreflang`).
- Both languages share the same `styles.css` and `main.js`. Page text lives in each HTML file. The few messages the script writes itself (calculator sentence, form errors, "Copied") are in the `STRINGS` table at the top of `assets/main.js`, and number formats follow the language (`€7,670` / `7670 €`, `5.4` / `5,4`).
- The Portuguese is European Portuguese (pt-PT) with the current spelling (AO90). To target Brazil as well, the vocabulary needs adapting (equipa → equipe, ecrã → tela, ficheiro → arquivo, and so on).
- **When you change one language, change the other.** Prices, the example week and the FAQ appear in both files.

## Preview it on your computer
Open `index.html` in a browser. Everything works locally except sending the contact form (see below).

## Before you launch: checklist

- [ ] **Domain and email.** The site uses `praxisminds.com`, with `hello@praxisminds.com` on the English pages and `ola@praxisminds.com` on the Portuguese pages (set both mailboxes up, or forward `ola@` to `hello@`). If yours differ, search and replace them across the whole `website` folder (both languages, `robots.txt` and `sitemap.xml`).
- [ ] **Contact form.** Create a free form endpoint (e.g. [Formspree](https://formspree.io)), then paste its URL into `data-endpoint=""` on the `<form id="contact-form">` in **both** `index.html` and `pt/index.html`. Each message includes a `language` field so you know which version it came from. Until then, visitors get their message ready to copy into an email, and the form never pretends a message was sent.
- [ ] **LinkedIn.** Replace `https://www.linkedin.com/` in both footers with your company page.
- [ ] **Booking link** *(optional).* If you use Cal.com or Calendly, point the "Book a 20-min call" buttons (`href="#contact"`) to your booking page.
- [ ] **Privacy pages.** Fill in every highlighted `[placeholder]` in `privacy.html` and `privacidade.html`, remove their `noindex` lines, and have them checked by a lawyer.
- [ ] **Prices.** Check the prices in the *How a project runs*, *Services* (all three tabs) and *Pricing* sections against [`plan/03-pricing.md`](../plan/03-pricing.md).
- [ ] **Analytics** *(optional).* If you add analytics, prefer a cookie-free tool (e.g. Plausible) so you don't need a cookie banner, and mention it in `privacy.html`.

## Common edits

| What | Where |
|---|---|
| Founding places taken | `data-taken="0"` on `<ol class="slots">` in `index.html` (0–5); the boxes and the counter update automatically |
| Example week (hero card) | The `.wk-row` lines in `index.html`. `--now` = hours a week today, `--after` = hours a person still spends checking, `--i` = animation order. Bars are scaled so 4 hours fills the width (`--max` on `.wk-rows` in `styles.css`). The totals and the "time back" figure are calculated automatically. |
| Services | One section with three tabs: *Tools we build* (`#build`), *Workshops* (`#workshops`) and *Business documents* (`#more`). Each tab is a `.tab-panel` holding `.card` items. Links to `#build`, `#workshops` or `#more` open that tab. Without JavaScript, all three show one after the other. |
| Calculator tasks | The `<select id="calc-task">` options in `index.html` and the matching `presets` in `assets/main.js`. Assumptions (46 weeks, 70%, 40-hour week) are at the top of the calculator code. |
| Colours | The tokens at the top of `assets/styles.css`: light theme first, dark theme below. Brand: deep teal `#0D5C55`, coral `#EF6C4D`, dark panels `#0B2724`, page `#F7F6F2`. |
| Fonts | Plus Jakarta Sans (everything) and Instrument Serif italic (one accent word per headline, inside `<em>`), both from Google Fonts |
| Icons | Inline SVG symbols at the top of each HTML page, used as `<svg class="ic"><use href="#i-name"/></svg>`. Both language files carry the same set. |
| Logo | A "P" in two parts: a teal stem (practice) and a coral bowl (minds). It is inline SVG in each page header and footer, and in `assets/favicon.svg`. |
| Share images | `assets/og-image.png` and `og-image-pt.png`, 1200 × 630. |

## Publish it (free options)

| Host | How |
|---|---|
| **Netlify** | Go to app.netlify.com/drop and drag the `website` folder in. Then connect your domain under *Domain settings*. |
| **Cloudflare Pages** | Create a project, upload the `website` folder (or connect this GitHub repo with build output directory `website`). |
| **GitHub Pages** | Repo settings → Pages → deploy from a branch. Note that GitHub Pages serves from the repo root or `/docs`, so you'd move or copy the folder. |
| **Vercel** | Import this repo and set the root directory to `website`. No build command. |

After connecting the domain, turn on HTTPS (all four do this automatically) and test the contact form once.

## Design notes
Calm and professional, with a little warmth: warm paper white, deep teal for trust, coral for the moments that matter (time back, the founding offer), and generous space between sections. Each headline has one word in an italic serif, so the page reads as one voice.

The page runs in the order a visitor decides: what we do (hero), how a project runs (Find → Build → Teach), what we offer (Services, in tabs), what it's worth to you (calculator), what you can hold us to (house rules), what it costs (pricing and founding places), questions, and contact.

The hero card shows an example admin week: each task's bar (teal) shrinks to the time a person still spends checking, and the rest turns coral as time back. It plays once when the card first appears, and visitors can switch between *Now* and *With Praxis*.

Motion is subtle: the hero fades in, sections rise into place as you scroll, the background glows drift slowly, and numbers count up. Light and dark themes are both supported. All animation switches off for visitors who prefer reduced motion, and nothing stays hidden if JavaScript doesn't load.
