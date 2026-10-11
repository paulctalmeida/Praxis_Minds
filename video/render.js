/*
  Renders film.html to an MP4, frame by frame, so the video is smooth whatever the computer's speed.

  Needs Node 18+, ffmpeg on the PATH, and Playwright with Chromium:
    npm install playwright && npx playwright install chromium

  Usage:
    node render.js                       English, 60 fps  -> praxis-minds-film-en.mp4
    node render.js --lang pt             Portuguese       -> praxis-minds-film-pt.mp4
    node render.js --fps 30 --out a.mp4  other frame rate or file name
    node render.js --stills 5,20.5,90    PNG stills at those seconds (into ./stills)

  Fonts come from Google Fonts. On a machine without internet, put the Google Fonts CSS
  (saved as fonts.css) and its font files in one folder and set FONT_DIR to that folder.
*/
"use strict";
const { chromium } = require("playwright");
const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");
const { pathToFileURL } = require("url");

function arg(name, fallback) {
  const i = process.argv.indexOf("--" + name);
  return i > -1 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const lang = arg("lang", "en");
const fps = Number(arg("fps", 60));
const out = path.resolve(arg("out", `praxis-minds-film-${lang}.mp4`));
const stills = arg("stills", "");
const from = Number(arg("from", 0));

(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });

  const fontDir = process.env.FONT_DIR;
  if (fontDir) {
    await page.route(/fonts\.googleapis\.com/, (route) => route.fulfill({ path: path.join(fontDir, "fonts.css"), contentType: "text/css" }));
    await page.route(/fonts\.gstatic\.com/, (route) => route.fulfill({ path: path.join(fontDir, path.basename(new URL(route.request().url()).pathname)), contentType: "font/woff2" }));
  }

  page.on("pageerror", (err) => console.error("Page error:", err.message));
  const url = pathToFileURL(path.join(__dirname, "film.html")).href + `?render&lang=${lang}`;
  await page.goto(url);
  await page.waitForFunction(() => window.__ready === true, null, { timeout: 60000 });
  const duration = await page.evaluate(() => window.__duration);
  const cdp = await page.context().newCDPSession(page);
  async function frame(t) {
    await page.evaluate((x) => window.__seek(x), t);
    const { data } = await cdp.send("Page.captureScreenshot", { format: "png", optimizeForSpeed: true });
    return Buffer.from(data, "base64");
  }

  if (stills) {
    const dir = path.resolve("stills");
    fs.mkdirSync(dir, { recursive: true });
    for (const s of stills.split(",").map(Number)) {
      fs.writeFileSync(path.join(dir, `${lang}-${s.toFixed(2)}.png`), await frame(s));
    }
    console.log(`Stills saved in ${dir}`);
    await browser.close();
    return;
  }

  const ffmpeg = spawn("ffmpeg", [
    "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-i", "-",
    "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out
  ], { stdio: ["pipe", "inherit", "inherit"] });
  const total = Math.ceil((duration - from) * fps);
  const started = Date.now();
  for (let i = 0; i < total; i++) {
    const buf = await frame(from + i / fps);
    if (!ffmpeg.stdin.write(buf)) await new Promise((r) => ffmpeg.stdin.once("drain", r));
    if (i % (fps * 5) === 0) {
      const rate = (i + 1) / ((Date.now() - started) / 1000);
      process.stdout.write(`\rframe ${i + 1}/${total}, ${rate.toFixed(1)} frames/s   `);
    }
  }
  ffmpeg.stdin.end();
  await new Promise((r) => ffmpeg.on("close", r));
  await browser.close();
  console.log(`\nSaved ${out}`);
})().catch((err) => { console.error(err); process.exit(1); });
