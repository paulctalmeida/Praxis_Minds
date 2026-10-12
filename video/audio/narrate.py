#!/usr/bin/env python3
"""
Praxis Minds film: the Portuguese narration mix.

Takes the ElevenLabs recording (narration-pt.mp3, all 15 sentences of ../narration-pt.md in one
file), cuts it into its 15 clips, places each clip where it belongs in the film, lowers the music
under the voice and saves soundtrack-pt.m4a, which render.js uses for the Portuguese version.

  python3 soundtrack.py --stems    first, for music.wav and sfx.wav
  python3 narrate.py               -> soundtrack-pt.m4a (and soundtrack-pt.wav)

If you record the voice again, the pauses move: update CLIPS below (the start and end of each
clip in the recording, in seconds; a pause detector such as ffmpeg's silencedetect finds them).
"""
import os
import subprocess

import numpy as np
from scipy import signal
from scipy.io import wavfile

from soundtrack import HERE, LENGTH, SR, lufs, sos, write

VOICE = os.path.join(HERE, "narration-pt.mp3")

# clip: (start in the recording, end in the recording, where it starts in the film, speed)
CLIPS = [
    (0.00, 7.08, 0.15, 1.06),    # 01 Faturas à mão. ... Todas as semanas.
    (7.58, 11.05, 7.00, 1.0),    # 02 Neste exemplo: treze horas e meia ...
    (11.64, 16.54, 10.80, 1.0),  # 03 Com a Praxis, a IA faz a maior parte ... (just after the click)
    (17.11, 21.50, 18.50, 1.0),  # 04 Trabalhamos sempre em três passos ...
    (22.04, 26.34, 23.50, 1.0),  # 05 Primeiro, descobrimos ...
    (26.84, 33.26, 30.80, 1.0),  # 06 Depois, construímos ...
    (33.78, 38.86, 38.40, 1.0),  # 07 Cada email chega classificado ...
    (39.38, 48.04, 45.20, 1.0),  # 08 O dashboard junta os dados ...
    (48.57, 51.94, 57.30, 1.0),  # 09 O assistente responde ...
    (52.44, 54.84, 62.80, 1.0),  # 10 E ensinamos a sua equipa ...
    (55.29, 59.39, 67.80, 1.0),  # 11 Neste exemplo, uma só tarefa ...
    (59.85, 63.79, 73.40, 1.0),  # 12 Com cinco tarefas ...
    (64.29, 68.26, 78.30, 1.0),  # 13 Preço fixo. Linguagem clara ...
    (68.74, 70.97, 82.45, 1.0),  # 14 Diga-nos qual é a tarefa ...
    (71.48, 74.45, 88.90, 1.0),  # 15 Práxis Minds. IA, posta em prática.
]
VOICE_LUFS = -17.0     # the voice on its own
DUCK = .32             # the music under the voice (about -10 dB)
SFX_DUCK = .7          # the effects under the voice


def load(path):
    raw = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).astype(np.float64)


def speed_up(y, rate):
    """Faster without raising the pitch (ffmpeg's atempo)."""
    if rate == 1.0:
        return y
    p = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-f", "f64le", "-ar", str(SR), "-ac", "1", "-i", "-",
                        "-af", f"atempo={rate}", "-f", "f64le", "-"], input=y.tobytes(), capture_output=True, check=True)
    return np.frombuffer(p.stdout, dtype=np.float64)


def main():
    rec = load(VOICE)
    rec = signal.sosfilt(sos("highpass", 80), rec)
    n = int(LENGTH * SR)
    voice, active = np.zeros(n), np.zeros(n)
    for i, (a, b, at, rate) in enumerate(CLIPS):
        y = rec[int(max(0, a - .04) * SR): int((b + .12) * SR)].copy()
        y = speed_up(y, rate).copy()
        y[:240] *= np.linspace(0, 1, 240)
        y[-2400:] *= np.linspace(1, 0, 2400)
        j = int(at * SR)
        end = j + len(y)
        if i + 1 < len(CLIPS) and end > CLIPS[i + 1][2] * SR:
            print(f"Note: clip {i + 1:02d} runs into clip {i + 2:02d}")
        if end > n:
            print(f"Note: clip {i + 1:02d} runs past the end of the film")
        voice[j:min(end, n)] += y[: min(end, n) - j]
        active[j:min(end, n)] = 1

    # the music dips just before each clip and comes back gently after it
    env = signal.sosfiltfilt(sos("lowpass", 1.2), active)
    env = np.clip(env / max(env.max(), 1e-9), 0, 1)
    duck_m = 1 - (1 - DUCK) * env
    duck_s = 1 - (1 - SFX_DUCK) * env

    _, music = wavfile.read(os.path.join(HERE, "music.wav"))
    _, sfx = wavfile.read(os.path.join(HERE, "sfx.wav"))
    music, sfx = music.T[:, :n].astype(np.float64), sfx.T[:, :n].astype(np.float64)
    v = np.vstack([voice, voice])
    v *= 10 ** ((VOICE_LUFS - lufs(v)) / 20)
    mix = music * duck_m + sfx * duck_s + v

    # -16 LUFS, with a limiter catching the few voice peaks above -1.5 dBFS
    raw = os.path.join(HERE, "soundtrack-pt-raw.wav")
    write(raw, mix * 10 ** ((-16.0 - lufs(mix)) / 20))
    out = os.path.join(HERE, "soundtrack-pt.wav")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", raw, "-af", "alimiter=limit=0.84:attack=3:release=60:level=false",
                    "-c:a", "pcm_f32le", out], check=True)
    os.remove(raw)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", out, "-c:a", "aac", "-b:a", "192k",
                    os.path.join(HERE, "soundtrack-pt.m4a")], check=True)
    print("Saved soundtrack-pt.wav and soundtrack-pt.m4a")


if __name__ == "__main__":
    main()
