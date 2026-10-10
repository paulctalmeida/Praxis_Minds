# Praxis Minds website

A static website: plain HTML, CSS and JavaScript. There's no build step, no framework, and nothing to install, so it can be hosted almost anywhere for free and edited in any text editor (or by asking Claude).

```
website/
├── index.html          the homepage (all sections)
├── privacy.html        privacy policy (draft: fill in before launch)
├── 404.html            "page not found"
├── robots.txt          for search engines
├── sitemap.xml         for search engines
└── assets/
    ├── styles.css      all design: colours, fonts, layout (tokens at the top)
    ├── main.js         the example week, the calculator, the contact form
    ├── favicon.svg     browser tab icon
    └── og-image.png    preview image for LinkedIn/WhatsApp/email shares
```

## Preview it on your computer
Open `index.html` in a browser. Everything works locally except sending the contact form (see below).

## Before you launch: checklist

- [ ] **Domain and email.** The site uses `praxisminds.com` and `hello@praxisminds.com`. If yours differ, search and replace them in `index.html`, `privacy.html`, `robots.txt` and `sitemap.xml`.
- [ ] **Contact form.** Create a free form endpoint (e.g. [Formspree](https://formspree.io)), then paste its URL into `data-endpoint=""` on the `<form id="contact-form">` in `index.html`. Until then, visitors get their message ready to copy into an email, and the form never pretends a message was sent.
- [ ] **LinkedIn.** Replace `https://www.linkedin.com/` in the footer with your company page.
- [ ] **Booking link** *(optional).* If you use Cal.com or Calendly, point the "Book a 20-min call" buttons (`href="#contact"`) to your booking page.
- [ ] **Privacy page.** Fill in every highlighted `[placeholder]` in `privacy.html`, remove its `noindex` line, and have it checked by a lawyer.
- [ ] **Prices.** Check the prices in the *Method*, *What we build*, *Workshops*, *Also from the same desk* and *Prices* sections against [`plan/03-pricing.md`](../plan/03-pricing.md).
- [ ] **Analytics** *(optional).* If you add analytics, prefer a cookie-free tool (e.g. Plausible) so you don't need a cookie banner, and mention it in `privacy.html`.

## Common edits

| What | Where |
|---|---|
| Founding places taken | `data-taken="0"` on `<ol class="slots">` in `index.html` (0–5); the boxes and the counter update automatically |
| Example week | The `.day` blocks in `index.html`. `--s` = start hour, `--d` = hours now, `--a` = hours after (a person checking), `--i` = animation order. Each freed yellow block starts at `--s + --a` and lasts `--d − --a`. The totals are calculated automatically. |
| Calculator tasks | The `<select id="calc-task">` options in `index.html` and the matching `presets` in `assets/main.js`. Assumptions (46 weeks, 70%, 40-hour week) are at the top of the calculator code. |
| Colours | The tokens at the top of `assets/styles.css`: light theme first, dark theme below |
| Fonts | Archivo (headlines), Public Sans (text), Martian Mono (figures and labels), Nanum Pen Script (handwritten notes), all from Google Fonts |

## Publish it (free options)

| Host | How |
|---|---|
| **Netlify** | Go to app.netlify.com/drop and drag the `website` folder in. Then connect your domain under *Domain settings*. |
| **Cloudflare Pages** | Create a project, upload the `website` folder (or connect this GitHub repo with build output directory `website`). |
| **GitHub Pages** | Repo settings → Pages → deploy from a branch. Note that GitHub Pages serves from the repo root or `/docs`, so you'd move or copy the folder. |
| **Vercel** | Import this repo and set the root directory to `website`. No build command. |

After connecting the domain, turn on HTTPS (all four do this automatically) and test the contact form once.

## Design notes
The look comes from the paperwork the site's clients deal with every day: ballpoint-blue ink, highlighter yellow, planner grids, coupon cut lines and handwritten notes. The hero shows an example admin week where repetitive work (hatched) shrinks to a short check (blue) and the freed time turns yellow. Both light and dark themes are supported, and all animation switches off for visitors who prefer reduced motion.
