# Praxis Minds: the film

A 94-second animated film built on the website design in [this artifact](https://claude.ai/artifact/9Lms1UPDn7ZYY25LgYHe4y): warm paper white, deep teal and coral, Plus Jakarta Sans with one Instrument Serif italic per headline, rounded cards, icon tiles, pill toggles and the line-drawn logo. It ends with the logo drawing itself. There is an English and a European Portuguese version, with the copy taken from the artifact's two language versions.

The `website/` folder in this repo still holds the earlier blue-and-yellow design. The film follows the artifact, not that folder.

```
video/
├── film.html                   the film itself: open it in a browser to watch or present it
├── render.js                   turns film.html into an MP4, frame by frame
├── praxis-minds-film-en.mp4    1920×1080, 60 fps, English
├── praxis-minds-film-pt.mp4    1920×1080, 60 fps, Portuguese (pt-PT)
├── poster-en.jpg               cover image for LinkedIn or a video player
└── poster-pt.jpg
```

The film has no sound. Add music when you post it (LinkedIn, YouTube and most editors have a royalty-free library), or play it silently on a screen at events. All the information is on screen, so it works with the sound off.

## What it shows

| Time | Scene | What happens |
|---|---|---|
| 0:00 | The week | A clock races from Monday to Friday while invoices, emails and spreadsheets pile up. "Every single *week.*" |
| 0:06 | The example week | The paperwork collapses into the website's example week card: 13 h 30 min of repetitive work. A cursor flips *Now* to *With Praxis*, the teal bars shrink and the coral time back (10 h 45 min) shows. The camera zooms through the teal switch. |
| 0:18 | Find → Build → Teach | The three steps on the dark teal band. |
| 0:23 | 01 Find | The week's tasks are scanned, ranked by hours and euros, circled, and turned into "Your 90-day plan". |
| 0:30 | Tools we build: document reader | An invoice is scanned, its fields fly into the ERP ledger, six more follow, and one is flagged for a person. |
| 0:38 | Tools we build: inbox triage | Emails arrive, get tagged and summarised, a reply is drafted, and a person approves it. |
| 0:45 | Tools we build: dashboard | A circle opens from the Send button. Five systems connect and the dashboard builds itself: KPIs count up, charts draw, the Monday summary writes itself. |
| 0:57 | Tools we build: knowledge assistant | A staff question gets a plain answer with a link to the exact paragraph in the handbook. |
| 1:02 | 03 Teach | The services tabs slide to *Workshops* and the workshop cards come in, with the EU AI Act note. |
| 1:07 | Your numbers | The website's calculator fills in (307 hours, €7,670 a year, 215 hours back), then five everyday tasks add up to 1,204 hours a year, 843 of them handed back. |
| 1:18 | House rules | The five promises and "Let's talk it through." on the dark band. |
| 1:22 | Contact | "Tell us the task *everyone dreads.*" The form fills in and is sent. The panel shrinks into the website's rounded contact card and falls away. |
| 1:26 | Logo | The logo draws itself as one line, then PRAXIS MINDS and "AI, put into *practice.*" with the coral scribble, as in the website's hero. |

## Where the numbers come from

Nothing in the film is a client result.
- **The week and the ranking** use the website's example admin week (labelled "Illustration only" and "Example" on screen), at €25 an hour and 46 working weeks.
- **The calculator** uses the website calculator's default numbers and its assumptions (46 working weeks, about 70% taken over by AI, a person checks). The five-task total uses the calculator's presets for each task.
- **The dashboard** is labelled "Sample data". Supplier and customer names are made up.

If you change the example week or the calculator on the website, change the film too (both languages).

## Watch or present it from the browser

Open `film.html` in Chrome, Edge or Safari. It scales to any screen. It needs an internet connection for the fonts.
- **Space** or a click: pause and play. **← →**: jump 3 seconds. The bar at the bottom appears when you move the mouse.
- `film.html?lang=pt` shows the Portuguese version, `?loop` plays on repeat (for a screen at an event), `?t=45` starts at 45 seconds.

## Change something

All the text is in the `STR` table at the top of the script in `film.html`, English first and Portuguese below. A `|` breaks a headline into lines and `*words*` are set in the italic serif. Headlines shrink on their own if a translation is longer. Colours and fonts are the website's tokens at the top of the file. Timings are the numbers (in seconds) inside each scene's `update` function.

## Make the MP4 again

Needs [Node.js](https://nodejs.org) 18 or later and [ffmpeg](https://ffmpeg.org).

```
cd video
npm install playwright
npx playwright install chromium
node render.js               # English  -> praxis-minds-film-en.mp4
node render.js --lang pt     # Portuguese -> praxis-minds-film-pt.mp4
node render.js --stills 15   # a single frame as PNG, in ./stills (for a poster)
```

Each version takes several minutes. The renderer steps through the film frame by frame, so the result is smooth on any computer.

## Where to use it
- LinkedIn: the company page, the *Featured* section of your profile, and as a post (see `plan/05-go-to-market.md`).
- The start of a Lunch & Learn talk or a discovery call.
- A screen at events, on `?loop`.
- On the website, as an optional video in the hero. Keep the MP4 out of the page's first load (use a poster image and load the video on click), so the site stays fast.
