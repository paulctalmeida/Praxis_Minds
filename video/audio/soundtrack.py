#!/usr/bin/env python3
"""
Praxis Minds film: the soundtrack.

The music and the sound effects are synthesised here from nothing: no samples, no loops, so there
is no licence to buy or credit. The result is the same on every run.

  python3 soundtrack.py            -> soundtrack.m4a (music and effects, used by render.js)
                                      and soundtrack.wav (the same, uncompressed)
  python3 soundtrack.py --stems    -> also music.wav and sfx.wav, for mixing with a voice

Needs Python 3, numpy and scipy (pip install numpy scipy), and ffmpeg on the PATH to write the
.m4a. The mix is set to -16 LUFS, the usual level for online video.

The times below follow film.html. If a scene moves there, move it here too.
"""
import argparse
import os
import subprocess
from functools import lru_cache

import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
LENGTH = 93.5
HERE = os.path.dirname(os.path.abspath(__file__))
N = int((LENGTH + 4) * SR)

# ---------------------------------------------------------------- timeline (film.html)
PHRASES = [0.25 + k * 0.86 for k in range(5)]          # hook lines
EVERY_WEEK = 4.6                                        # "Every single week."
LANDINGS = [.35, .8, 1.2, 1.55, 1.9, 2.2, 2.5, 2.78, 3.05, 3.3, 3.55, 3.8]   # paperwork lands
BARS_FORM = [6.85 + i * 0.12 for i in range(6)]        # cards become the week's bars
CLICKS = [10.5, 43.58, 84.5]                            # cursor clicks
ZOOM = (16.4, 18.2)                                     # zoom through the teal switch
PUSHES = [22.95, 30.2, 37.7, 56.7, 62.2, 67.3, 77.9]   # page transitions
SCRIBBLES = [(5.0, .7), (12.7, .8), (28.1, .7), (36.55, .6)]   # coral pen lines in the film
POSTED = [33.3] + [34.32 + k * .4 for k in range(5)]   # ledger rows posted
FLAGGED = 36.32                                         # the row a person checks
MAILS = [38.55 + k * .3 for k in range(6)]              # emails arriving
CIRCLE = 44.7                                           # the dashboard opens from Send
CHAT = (58.55, 59.3, 60.95)                             # question sent, answer, source
FORM_OK = 84.65                                         # contact form sent
PANEL_FALL = 85.25                                      # contact panel shrinks and falls
LOGO_PARTS = [(86.0, .1), (86.1, .24), (86.34, 1.53), (87.87, .53)]   # the logo line, piece by piece
LOGO_DONE = 88.4
LETTERS = [89.0 + i * .035 for i in range(12) if i != 6]   # P R A X I S _ M I N D S
TAGLINE = 89.7
TAG_SCRIBBLE = (90.35, 1.1)
TRAIL = (91.7, 1.4)                                     # coral light along the logo
# where the pen tip is on screen while the logo draws: (x, y) in pixels every 0.05 s from 86.05,
# read from film.html in the browser. The sound follows it: x sets the pan, height sets the pitch.
TIP = [(1012, 539), (1043, 508), (1077, 428), (1077, 384), (1042, 362), (1001, 377), (935, 432), (901, 461),
       (867, 489), (832, 516), (790, 512), (764, 477), (759, 433), (770, 391), (796, 355), (832, 330), (873, 313),
       (916, 304), (960, 302), (1004, 307), (1047, 317), (1088, 335), (1123, 362), (1149, 397), (1160, 440),
       (1159, 484), (1148, 527), (1120, 561), (1080, 577), (1053, 590), (1065, 632), (1031, 612), (998, 583),
       (962, 570), (918, 574), (876, 560), (846, 528), (834, 460), (835, 416), (854, 376), (895, 367), (933, 390),
       (965, 421), (996, 453), (1030, 481), (1070, 501), (1120, 514), (1169, 507)]
TIP_T = 86.05 + .05 * np.arange(len(TIP))

# ---------------------------------------------------------------- musical grid
GROOVE = 10.5                     # the band comes in on the "With Praxis" click
LOGO = 86.0                       # 33 bars later the logo starts to draw
BAR = (LOGO - GROOVE) / 33        # about 105 beats a minute
BEAT = BAR / 4


def at(bar, beat=0.0):
    return GROOVE + bar * BAR + beat * BEAT


rng = np.random.default_rng(2026)


def mtof(m):
    return 440.0 * 2.0 ** ((m - 69) / 12.0)


def tarr(sec):
    return np.arange(int(sec * SR)) / SR


def norm(y):
    return y / (np.max(np.abs(y)) + 1e-12)


def sos(kind, f, order=2):
    return signal.butter(order, f, btype=kind, fs=SR, output="sos")


def filt(y, kind, f, order=2):
    return signal.sosfilt(sos(kind, f, order), y)


def noise(sec, seed):
    return np.random.default_rng(seed).standard_normal(int(sec * SR))


class Bus:
    def __init__(self):
        self.x = np.zeros((2, N))

    def add(self, t, y, gain=1.0, pan=0.0):
        if y.ndim == 1:
            if np.isscalar(pan):
                a = (pan + 1) * np.pi / 4
                y = np.vstack([y * np.cos(a), y * np.sin(a)]) * np.sqrt(2)
            else:
                a = (np.asarray(pan) + 1) * np.pi / 4
                y = np.vstack([y * np.cos(a), y * np.sin(a)]) * np.sqrt(2)
        i = int(round(t * SR))
        if i < 0:
            y, i = y[:, -i:], 0
        j = min(N, i + y.shape[1])
        if j > i:
            self.x[:, i:j] += gain * y[:, : j - i]


def pan_sweep(n, p0, p1):
    return np.linspace(p0, p1, n)


# ---------------------------------------------------------------- instruments
@lru_cache(maxsize=None)
def pluck(m, ring=1.0, bright=1.0):
    """A nylon-string pluck: harmonics that fade faster the higher they are."""
    f, t = mtof(m), tarr(ring)
    y = np.zeros_like(t)
    for k in range(1, 18):
        fk = f * k * (1 + .00025 * k * k)
        if fk > 15000:
            break
        a = abs(np.sin(np.pi * k * .22)) / k
        tau = .85 * bright / (1 + .38 * (k - 1) ** 1.25)
        y += a * np.sin(2 * np.pi * fk * t + .7 * k) * np.exp(-t / tau)
    pick = filt(noise(.006, m), "highpass", 3000) * np.exp(-np.arange(int(.006 * SR)) / (.0015 * SR)) * .08
    y[: len(pick)] += pick
    y *= np.minimum(1, t / .0015)
    fade = int(.04 * SR)
    y[-fade:] *= np.linspace(1, 0, fade)
    return norm(y)


@lru_cache(maxsize=None)
def marimba(m, ring=1.0):
    f, t = mtof(m), tarr(ring)
    y = (np.sin(2 * np.pi * f * t) * np.exp(-t / .42)
         + .3 * np.sin(2 * np.pi * 3.93 * f * t) * np.exp(-t / .07)
         + .06 * np.sin(2 * np.pi * 9.2 * f * t) * np.exp(-t / .025))
    y *= np.minimum(1, t / .0012)
    return norm(y)


@lru_cache(maxsize=None)
def bell(m, ring=2.2):
    """A soft celesta-like bell."""
    f, t = mtof(m), tarr(ring)
    y = np.zeros_like(t)
    for r, a, tau in ((1, 1, 1.1), (2, .3, .5), (3.01, .14, .28), (4.07, .09, .16), (5.43, .05, .09)):
        y += a * np.sin(2 * np.pi * f * r * t + r) * np.exp(-t / tau)
    y *= np.minimum(1, t / .002)
    return norm(y)


@lru_cache(maxsize=None)
def bass(m, dur):
    f, t = mtof(m), tarr(dur + .12)
    y = np.sin(2 * np.pi * f * t) + .38 * np.sin(4 * np.pi * f * t + .3) + .14 * np.sin(6 * np.pi * f * t + .6)
    env = np.minimum(1, t / .006) * (.62 + .38 * np.exp(-t / .16))
    rel = t > dur
    env[rel] *= np.maximum(0, 1 - (t[rel] - dur) / .1)
    y = np.tanh(1.5 * y * env) / np.tanh(1.5)
    return filt(y, "lowpass", 1100)


def pad(notes, dur, att=.9, rel=1.6, cutoff=2000, seed=0):
    """A warm, slowly breathing chord, slightly detuned left and right."""
    t = tarr(dur + rel)
    out = np.zeros((2, len(t)))
    r = np.random.default_rng(seed)
    notes = [m for m in notes if m >= 48]          # the bass covers the low end
    for m in notes:
        f = mtof(m)
        for ch, cents in ((0, -6), (1, 6)):
            fd = f * 2 ** (cents / 1200)
            for k in range(1, 9):
                if fd * k > 9000:
                    break
                out[ch] += (1 / k ** 1.7) * np.sin(2 * np.pi * fd * k * t + r.uniform(0, 6.28))
    env = np.where(t < att, .5 - .5 * np.cos(np.pi * np.minimum(t, att) / att), 1.0)
    tail = t > dur
    env[tail] *= np.exp(-(t[tail] - dur) / (rel / 4))
    lfo = 1 + .06 * np.sin(2 * np.pi * .23 * t + seed)
    out *= env * lfo
    out = signal.sosfilt(sos("lowpass", cutoff), out, axis=1)
    return out / (len(notes) ** .5 * 2.2)


@lru_cache(maxsize=None)
def kick():
    t = tarr(.45)
    f = 47 + 72 * np.exp(-t / .034)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / .2)
    y[: int(.004 * SR)] += filt(noise(.004, 11), "highpass", 2500) * .12
    return norm(y)


@lru_cache(maxsize=None)
def clap():
    t = tarr(.35)
    nz = filt(noise(.35, 12), "bandpass", [900, 3600])
    env = np.zeros_like(t)
    for b in (0, .009, .018):
        env += np.where(t >= b, np.exp(-(t - b) / .006), 0)
    env = .5 * env + .55 * np.exp(-t / .085)
    return norm(nz * env)


@lru_cache(maxsize=None)
def shaker():
    t = tarr(.1)
    y = filt(noise(.1, 13), "highpass", 5200) * np.minimum(1, t / .006) * np.exp(-t / .035)
    return norm(y)


@lru_cache(maxsize=None)
def hat():
    t = tarr(.08)
    return norm(filt(noise(.08, 14), "highpass", 8000) * np.exp(-t / .022))


@lru_cache(maxsize=None)
def cymbal_swell(sec=1.6):
    t = tarr(sec)
    y = filt(noise(sec, 15), "highpass", 4500)
    return norm(y * np.minimum(1, t / .01) * np.exp(-t / .55))


@lru_cache(maxsize=None)
def tick(hi=True):
    t = tarr(.05)
    f = 3300 if hi else 2200
    y = np.sin(2 * np.pi * f * t) * np.exp(-t / .004) + .5 * filt(noise(.05, 16 + hi), "highpass", 4000) * np.exp(-t / .0012)
    return norm(y * np.minimum(1, t / .0006))


@lru_cache(maxsize=None)
def paper(seed):
    t = tarr(.2)
    nz = noise(.2, 100 + seed)
    y = filt(nz, "lowpass", 2600) * np.minimum(1, t / .002) * np.exp(-t / .045)
    y += .5 * filt(nz, "bandpass", [350, 1200]) * np.exp(-t / .03)
    y += .35 * np.sin(2 * np.pi * 115 * t) * np.exp(-t / .035)
    return norm(y)


@lru_cache(maxsize=None)
def ui_click():
    y = np.zeros(int(.12 * SR))
    for start, f in ((0, 2500), (.065, 1800)):
        t = tarr(.03)
        c = np.sin(2 * np.pi * f * t) * np.exp(-t / .0035) + .4 * filt(noise(.03, int(f)), "highpass", 3000) * np.exp(-t / .0012)
        i = int(start * SR)
        y[i:i + len(c)] += c * (1 if start == 0 else .7)
    return norm(y)


@lru_cache(maxsize=None)
def pop(f0=650, f1=980):
    t = tarr(.09)
    f = f0 + (f1 - f0) * (1 - np.exp(-t / .012))
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.minimum(1, t / .002) * np.exp(-t / .028)
    return norm(y)


def whoosh(dur, f0, f1, peak=.6, width=.75, seed=0):
    """Air moving: noise whose band slides from f0 to f1, loudest at `peak` (0..1)."""
    n = int(dur * SR)
    x = noise(dur, 200 + seed)
    f, tt, Z = signal.stft(x, SR, nperseg=1024)
    prog = np.clip(tt / dur, 0, 1)
    fc = f0 * (f1 / f0) ** prog
    lf = np.log2(np.maximum(f, 20))[:, None]
    mask = np.exp(-.5 * ((lf - np.log2(fc)[None, :]) / width) ** 2)
    env = np.where(prog < peak, (prog / peak) ** 2, ((1 - prog) / (1 - peak + 1e-9)) ** 1.6)
    _, y = signal.istft(Z * mask * env[None, :], SR, nperseg=1024)
    return norm(y[:n])


def riser(dur, m0, m1, seed=0):
    t = tarr(dur)
    f = mtof(m0) * (mtof(m1) / mtof(m0)) ** (t / dur)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) + .3 * np.sin(4 * np.pi * np.cumsum(f) / SR)
    y = .55 * whoosh(dur, 400, 6000, peak=.97, width=.9, seed=seed) + .2 * tone * (t / dur) ** 2
    return norm(y)


@lru_cache(maxsize=None)
def boom():
    t = tarr(1.0)
    f = 38 + 30 * np.exp(-t / .12)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / .38)
    y += .25 * filt(noise(1.0, 21), "lowpass", 300) * np.exp(-t / .25)
    return norm(y)


def tip_at(t):
    """Pen tip on screen at film time t, as (pan -1..1, height 0..1)."""
    x = np.interp(t, TIP_T, [p[0] for p in TIP])
    y = np.interp(t, TIP_T, [p[1] for p in TIP])
    return (x - 960) / 230 * .7, (632 - y) / 330


def pen_stroke(t0, t1, seed=0):
    """The logo line: a soft airy stroke whose pitch rises and falls with the pen and whose
    loudness follows its speed. Returns a mono signal and its pan, sample by sample."""
    dur = t1 - t0
    n = int(dur * SR)
    x = noise(dur, 500 + seed)
    f, tt, Z = signal.stft(x, SR, nperseg=1024)
    pan, h = tip_at(t0 + tt)
    fc = 900 * 2 ** (2.2 * h)                      # about 900 Hz at the bottom of the mark, 4.1 kHz at the top
    spd = np.hypot(np.gradient(np.interp(t0 + tt, TIP_T, [p[0] for p in TIP])),
                   np.gradient(np.interp(t0 + tt, TIP_T, [p[1] for p in TIP])))
    spd = .55 + .45 * spd / (spd.max() + 1e-9)
    lf = np.log2(np.maximum(f, 20))[:, None]
    mask = np.exp(-.5 * ((lf - np.log2(fc)[None, :]) / .55) ** 2) + .25 * np.exp(-.5 * ((lf - np.log2(2.1 * fc)[None, :]) / .4) ** 2)
    prog = tt / dur
    env = np.clip(prog / .04, 0, 1) * np.clip((1 - prog) / .05, 0, 1) * spd
    _, y = signal.istft(Z * mask * env[None, :], SR, nperseg=1024)
    y = y[:n]
    grain = filt(noise(dur, 600 + seed), "lowpass", 70)
    y *= 1 + .35 * grain / (np.std(grain) + 1e-9)
    pan_s, _ = tip_at(t0 + np.arange(n) / SR)
    return norm(y), np.clip(pan_s, -.9, .9)


def pencil(dur, seed=0, parts=None):
    """Graphite on paper: a soft grainy hiss that follows the pen, pausing where it lifts."""
    t = tarr(dur)
    nz = noise(dur, 300 + seed)
    tex = filt(nz, "bandpass", [1800, 6500]) + .35 * filt(nz, "bandpass", [450, 1400])
    grain = filt(noise(dur, 400 + seed), "lowpass", 45)
    grain = 1 + .75 * grain / (np.std(grain) + 1e-9) * .5
    env = np.zeros_like(t)
    for s, d in parts or [(0, dur)]:
        w = np.clip((t - s) / .015, 0, 1) * np.clip((s + d - t) / .02, 0, 1)
        env = np.maximum(env, w)
    env = signal.sosfilt(sos("lowpass", 60), env)
    return norm(tex * np.abs(grain) * env)


# ---------------------------------------------------------------- harmony
CH = {
    "D":    dict(pad=[50, 57, 64, 66], strum=[57, 62, 66, 69], bass=38),
    "A/C#": dict(pad=[49, 57, 64, 69], strum=[57, 61, 64, 69], bass=37),
    "Bm":   dict(pad=[47, 54, 62, 66], strum=[59, 62, 66, 71], bass=35),
    "G":    dict(pad=[43, 55, 59, 66], strum=[55, 59, 62, 67], bass=31),
    "D/F#": dict(pad=[42, 57, 62, 66], strum=[57, 62, 66, 69], bass=42),
    "Em7":  dict(pad=[40, 55, 59, 62], strum=[55, 59, 62, 64], bass=40),
    "A":    dict(pad=[45, 57, 61, 64], strum=[57, 61, 64, 69], bass=45),
    "Asus": dict(pad=[45, 57, 62, 64], strum=[57, 62, 64, 69], bass=45),
    "Bm11": dict(pad=[47, 54, 62, 64, 66], strum=[59, 62, 64, 66], bass=35),
    "Dmaj9": dict(pad=[38, 50, 57, 61, 64, 66], strum=[50, 57, 61, 64, 66, 69], bass=38),
}
PROG_A = ["D", "A/C#", "Bm", "G"]
PROG_B = ["G", "D/F#", "Em7", "A"]

# melodies: (beat within a 4-bar phrase, note, length in beats)
MEL_A = [(0, 78, .5), (.75, 81, .5), (1.5, 81, .5), (2.5, 78, .5), (3, 76, .75),
         (4, 76, .5), (4.75, 74, .5), (5.5, 76, .5), (6.5, 69, 1),
         (8, 74, .5), (8.75, 78, .5), (9.5, 81, .5), (10.5, 83, .5), (11, 81, .75),
         (12, 74, .5), (12.75, 76, .5), (13.5, 74, .5), (14, 71, 1.5)]
MEL_B = [(0, 86, .75), (1, 83, .5), (1.5, 81, .5), (2.5, 83, .5), (3, 81, .5),
         (4, 78, .75), (5, 81, .5), (5.5, 78, .5), (6.5, 76, 1),
         (8, 79, .75), (9, 76, .5), (9.5, 79, .5), (10.5, 83, .5), (11, 81, .5),
         (12, 81, .75), (13, 76, .5), (13.5, 73, .5), (14, 69, 1.5)]

STRUM = [(0, "d", 1), (1, "d", .7), (1.5, "u", .45), (2.5, "u", .6), (3, "d", .8), (3.5, "u", .45)]


def chord_at(n):
    if 16 <= n < 24:
        return PROG_B[n % 4]
    if n == 31:
        return "G"
    if n == 32:
        return "Asus"
    return PROG_A[n % 4]


# ---------------------------------------------------------------- the score
def compose():
    music, sfx, verb, sverb = Bus(), Bus(), Bus(), Bus()   # verb, sverb: what the music and the effects send to the reverb

    def strum(t, name, vel=1, direction="d", gain=.3, ring=1.0):
        notes = CH[name]["strum"]
        if direction == "u":
            notes = notes[::-1][:3]
        for i, m in enumerate(notes):
            y = pluck(m, ring)
            g = gain * vel * (1 - .06 * i)
            music.add(t + i * .013, y, g, -.25 + .1 * i)
            verb.add(t + i * .013, y, g * .22, -.25 + .1 * i)

    def mel(t0, phrase, inst, gain, pan, octave=0):
        for beat, m, length in phrase:
            y = inst(m + octave)
            music.add(t0 + beat * BEAT, y, gain, pan)
            verb.add(t0 + beat * BEAT, y, gain * .45, pan)

    # ---- intro: the busy week (0 to 10.5)
    for k in range(40):                       # a clock that will not stop
        t = at(-5, k * .5)
        if .12 < t < EVERY_WEEK:
            music.add(t, tick(k % 2 == 0), .1 + .06 * (t / EVERY_WEEK), .35 if k % 2 else -.35)
    for i, t in enumerate(PHRASES):           # a muted chord on each line of text
        for j, m in enumerate([59, 62, 66]):
            music.add(t + j * .01, pluck(m, .35, .25), .4, -.1)
        verb.add(t, pluck(66, .35, .25), .1)
    for i, t in enumerate(LANDINGS):          # paperwork landing on the pile
        sfx.add(t - .08, paper(i), .3 + .04 * (i % 3), -.4 + .7 * ((i * 37) % 11) / 10)
    music.add(EVERY_WEEK, bass(35, 1.6), .34)
    music.add(EVERY_WEEK, pad(CH["Bm"]["pad"], at(-1) - EVERY_WEEK, att=1.2, seed=1), .45)
    music.add(at(-1), pad(CH["A"]["pad"], at(0) - at(-1), att=.8, rel=.6, seed=2), .45)
    sfx.add(5.85, whoosh(1.1, 3500, 500, peak=.4, seed=1), .12, -.2)
    for i, t in enumerate(BARS_FORM):         # the week's bars, one note each
        y = marimba([66, 69, 71, 74, 78, 81][i])
        music.add(t, y, .2, .2)
        verb.add(t, y, .1, .2)
    for k, m in enumerate([69, 73, 76, 81]):   # a hopeful arpeggio before the click
        y = marimba(m)
        music.add(at(-1, k), y, .13, .3)
        verb.add(at(-1, k), y, .08, .3)
    sfx.add(at(0) - 1.25, riser(1.25, 62, 74, seed=1), .1)

    # ---- the band comes in on the click (bars 0 to 32)
    for n in range(33):
        t = at(n)
        name = chord_at(n)
        light = n < 4
        breakdown = n >= 31
        music.add(t, pad(CH[name]["pad"], BAR + .05, att=.35 if n else .02, rel=.7, seed=10 + n), .32 if not breakdown else .42)
        verb.add(t, pad(CH[name]["pad"], BAR, att=.4, rel=.7, seed=50 + n), .12)
        # plucked chords
        if light:
            for b in (0, 2):
                strum(t + b * BEAT, name, 1 if b == 0 else .75, "d", .27)
        elif breakdown:
            strum(t, name, .8, "d", .26, ring=2.0)
            strum(t + 2.5 * BEAT, name, .45, "u", .26)
        else:
            for b, d, v in STRUM:
                strum(t + b * BEAT, name, v, d, .27 if n < 16 or n >= 24 else .3)
        # bass
        root = CH[name]["bass"]
        if light:
            music.add(t, bass(root, BEAT * 1.8), .32)
            music.add(t + 2 * BEAT, bass(root, BEAT * 1.8), .27)
        elif not breakdown:
            for b, m, length, g in ((0, root, .9, .35), (1.5, root, .4, .24), (2.5, root, .4, .27), (3.5, root + 7, .35, .21)):
                music.add(t + b * BEAT, bass(m, BEAT * length), g)
        else:
            music.add(t, bass(root, BAR * .9), .25)
        # drums
        if not breakdown:
            for b in (0, 2) if light else (0, 2, 2.75) if n % 2 else (0, 2):
                music.add(t + b * BEAT, kick(), .5 if light else .6)
            if not light:
                for b in (1, 3):
                    music.add(t + b * BEAT, clap(), .36, .05)
                    verb.add(t + b * BEAT, clap(), .12)
                for s in range(16):
                    v = (.5, .22, .85, .3)[s % 4]
                    music.add(t + s * BEAT / 4, shaker(), .13 * v, .45)
            if n >= 16:
                for b in (.5, 1.5, 2.5, 3.5):
                    music.add(t + b * BEAT, hat(), .09, -.35)
        else:
            for s in range(8):
                music.add(t + s * BEAT / 2, shaker(), .07 * (1 if s % 2 else .5), .45)
        # sixteenth-note arpeggios in the B section
        if 16 <= n < 24:
            notes = CH[name]["strum"]
            for s in range(16):
                m = notes[(s * 3) % len(notes)] + 12
                y = pluck(m, .4, .6)
                music.add(t + s * BEAT / 4, y, .055 * (1 if s % 2 == 0 else .6), .4 if s % 2 else -.4)
                verb.add(t + s * BEAT / 4, y, .03)
    music.add(at(0), cymbal_swell(), .09, .1)       # the bloom on the click
    music.add(at(0), bell(86), .14, .25)
    verb.add(at(0), bell(86), .1)

    # melodies (four-bar phrases)
    mel(at(4), MEL_A, bell, .2, .2)
    mel(at(8), MEL_A, marimba, .2, .25)
    mel(at(16), MEL_B, bell, .2, .2)
    mel(at(20), MEL_B, marimba, .2, .25)
    mel(at(20), MEL_B, bell, .08, -.2, octave=-12)
    mel(at(24), MEL_A, marimba, .18, .25)
    mel(at(28), MEL_B[:9], bell, .18, .2)

    # a small lift into the dashboard
    for s in range(8):
        music.add(at(14, 2) + s * BEAT / 4, clap(), .1 + .03 * s, .05)
    sfx.add(at(15) - 1.15, riser(1.15, 66, 78, seed=2), .08)
    music.add(at(15), cymbal_swell(), .08, -.1)

    # ---- the logo (86.0 to the end)
    sfx.add(at(31) + 2 * BAR - 1.4, riser(1.4, 62, 81, seed=3), .08)
    music.add(LOGO, boom(), .22)
    music.add(LOGO, pad(CH["Bm11"]["pad"], 88.5 - LOGO, att=.4, rel=.8, cutoff=1700, seed=90), .4)
    music.add(88.5, pad(CH["G"]["pad"], .5, att=.15, rel=.5, seed=91), .35)
    music.add(89.0, pad(CH["A"]["pad"], .7, att=.15, rel=.4, seed=92), .35)
    music.add(TAGLINE, pad(CH["Dmaj9"]["pad"], LENGTH - TAGLINE, att=.25, rel=2.5, cutoff=2400, seed=93), .45)
    verb.add(TAGLINE, pad(CH["Dmaj9"]["pad"], 2.5, att=.25, rel=2.5, seed=94), .18)
    strum(TAGLINE, "Dmaj9", 1, "d", .32, ring=2.6)
    music.add(TAGLINE, bass(38, 3.0), .32)
    music.add(TAGLINE, kick(), .3)
    for m, g in ((81, .15), (86, .17), (90, .08)):
        music.add(TAGLINE + .02, bell(m, 3.0), g, .2)
        verb.add(TAGLINE + .02, bell(m, 3.0), g * .6)

    # the logo line: an airy stroke that follows the pen, a fine graphite grain, and a rising run
    # of chimes, each panned to where the pen is on screen
    start, end = LOGO_PARTS[0][0], LOGO_DONE
    stroke, pan_s = pen_stroke(start, end + .05, seed=1)
    sfx.add(start, stroke, .5, pan_s)
    sverb.add(start, stroke, .16, pan_s)
    grain = pencil(end - start + .05, seed=1)
    sfx.add(start, grain, .1, pan_s[: len(grain)])
    scale = [69, 71, 74, 76, 78, 81, 83, 86, 88, 90, 93, 95]
    steps = 22
    for k in range(steps):
        tk = start + .03 + k / (steps - 1) * (end - start - .08)
        m = scale[int(k / steps * len(scale))]
        g = .085 * (.7 + .3 * np.sin(k * 1.7) ** 2)
        p = float(tip_at(tk)[0])
        sfx.add(tk, bell(m, 1.2), g, p)
        sverb.add(tk, bell(m, 1.2), g * .9, p)
    sfx.add(LOGO_DONE, bell(98, 2.0), .1, .1)           # the line closes
    sverb.add(LOGO_DONE, bell(98, 2.0), .08)
    sfx.add(LOGO_DONE + .02, pop(700, 1050), .1)
    sfx.add(88.55, whoosh(.9, 2200, 700, peak=.35, seed=8), .07, -.3)   # the mark moves aside
    for i, t in enumerate(LETTERS):                      # the name rises, letter by letter
        y = marimba([74, 76, 78, 81, 83, 86, 88, 90, 93, 95, 98][i])
        sfx.add(t, y, .07 + .004 * i, -.3 + .06 * i)
        sverb.add(t, y, .05)
    s0, d0 = TAG_SCRIBBLE                                 # the coral scribble under "practice."
    sfx.add(s0, pencil(d0, seed=2), .12, pan_sweep(int(d0 * SR), -.2, .45))
    t0, d1 = TRAIL                                        # the coral light runs along the line
    for k in range(16):
        g = k / 15
        i = min(3, int(g * 4))                            # each piece of the line gets a quarter of it
        pen = LOGO_PARTS[i][0] + (g * 4 - i) * LOGO_PARTS[i][1]
        m = [86, 88, 90, 93, 95, 98, 100, 102][k % 8] - (12 if k > 9 else 0)
        p = float(tip_at(pen)[0])
        sfx.add(t0 + g * d1, bell(m, 1.4), .05, p)
        sverb.add(t0 + g * d1, bell(m, 1.4), .06, p)

    # ---- effects through the film
    for t in CLICKS:
        sfx.add(t - .045, ui_click(), .2, .25)
    zs, ze = ZOOM
    sfx.add(zs, whoosh(ze - zs + .1, 250, 5000, peak=.93, width=.9, seed=3), .2)
    sfx.add(zs, riser(ze - zs, 62, 86, seed=4), .07)
    music.add(ze, boom(), .2)
    for i, t in enumerate(PUSHES):
        sfx.add(t, whoosh(.75, 900, 2600, peak=.5, seed=10 + i), .07, pan_sweep(int(.75 * SR), .5, -.5))
    for i, (s, d) in enumerate(SCRIBBLES):
        sfx.add(s, pencil(d, seed=10 + i), .07, pan_sweep(int(d * SR), -.2, .3))
    for i, t in enumerate(POSTED):
        sfx.add(t, pop(620 + 25 * i, 940 + 25 * i), .07, .3)
    sfx.add(FLAGGED, marimba(69), .09, .3)
    sfx.add(FLAGGED + .12, marimba(66), .09, .3)
    for i, t in enumerate(MAILS):
        sfx.add(t, bell(93, .6), .035, -.3)
    sfx.add(43.62, whoosh(.45, 900, 4500, peak=.4, seed=20), .06, .3)
    sfx.add(CIRCLE, whoosh(.9, 300, 3500, peak=.6, width=.9, seed=21), .1)
    q, a, src = CHAT
    sfx.add(q, whoosh(.35, 1200, 4000, peak=.3, seed=22), .06, .3)
    sfx.add(a, pop(500, 760), .07, -.2)
    sfx.add(src, pop(800, 1150), .05, -.2)
    sfx.add(FORM_OK, bell(88, 1.2), .06, .3)
    sfx.add(FORM_OK + .1, bell(93, 1.2), .05, .3)
    sfx.add(PANEL_FALL, whoosh(1.0, 3000, 300, peak=.55, seed=23), .09)

    return music, sfx, verb, sverb


def reverb(x, seconds=2.4, seed=5):
    """A soft hall: decaying noise, a little darker each way."""
    t = tarr(seconds)
    ir = np.zeros((2, len(t)))
    for ch in range(2):
        nz = noise(seconds, seed + ch)
        ir[ch] = filt(nz, "lowpass", 5500) * np.exp(-t / .32)
        ir[ch][: int(.018 * SR)] = 0
    ir /= np.sqrt(np.sum(ir ** 2, axis=1, keepdims=True))
    return np.vstack([signal.fftconvolve(x[ch], ir[ch])[:N] for ch in range(2)])


def finish(x):
    """Trim to the film and fade the end."""
    x = x[:, : int(LENGTH * SR)]
    x = signal.sosfilt(sos("highpass", 28), x, axis=1)
    t = np.arange(x.shape[1]) / SR
    fade = np.clip((LENGTH - t) / 1.0, 0, 1)
    x *= .5 - .5 * np.cos(np.pi * fade)
    x[:, :240] *= np.linspace(0, 1, 240)
    return x


def lufs(x):
    """Integrated loudness (EBU R128 / ITU BS.1770) of a 48 kHz stereo signal."""
    k = signal.lfilter([1.53512485958697, -2.69169618940638, 1.19839281085285], [1, -1.69065929318241, .73248077421585], x, axis=1)
    k = signal.lfilter([1, -2, 1], [1, -1.99004745483398, .99007225036621], k, axis=1)
    size, hop = int(.4 * SR), int(.1 * SR)
    power = np.array([np.sum(np.mean(k[:, i:i + size] ** 2, axis=1)) for i in range(0, k.shape[1] - size, hop)])
    lk = -.691 + 10 * np.log10(power + 1e-12)
    power = power[lk > -70]
    rel = -.691 + 10 * np.log10(power.mean()) - 10
    return -.691 + 10 * np.log10(power[-.691 + 10 * np.log10(power) > rel].mean())


def write(path, x):
    wavfile.write(path, SR, x.T.astype(np.float32))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stems", action="store_true", help="also write music.wav and sfx.wav, at the same level as the mix")
    ap.add_argument("--target", type=float, default=-16.0, help="loudness in LUFS (default -16, the usual level for online video)")
    args = ap.parse_args()
    music, sfx, verb, sverb = compose()
    music = finish(music.x + .55 * reverb(verb.x))
    sfx = finish(sfx.x + .55 * reverb(sverb.x))
    mix = music + sfx
    gain = 10 ** ((args.target - lufs(mix)) / 20)
    peak = np.max(np.abs(mix)) * gain
    if peak > .84:                                  # keep 1.5 dB of headroom
        gain *= .84 / peak
    write(os.path.join(HERE, "soundtrack.wav"), mix * gain)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", os.path.join(HERE, "soundtrack.wav"),
                    "-c:a", "aac", "-b:a", "192k", os.path.join(HERE, "soundtrack.m4a")], check=True)
    print(f"Saved soundtrack.wav and soundtrack.m4a ({lufs(mix * gain):.1f} LUFS, peak {20 * np.log10(np.max(np.abs(mix)) * gain):.1f} dBFS)")
    if args.stems:
        for name, x in (("music", music), ("sfx", sfx)):
            write(os.path.join(HERE, name + ".wav"), x * gain)
        print("Saved music.wav and sfx.wav")


if __name__ == "__main__":
    main()
