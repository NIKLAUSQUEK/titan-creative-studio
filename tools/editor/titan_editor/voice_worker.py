"""Runs inside the chatterbox venv (voice.py calls it): job.json -> one wav per text chunk, cloned from the reference voice."""
import json, sys

import torchaudio as ta
from chatterbox.tts import ChatterboxTTS


def main(job_path):
    job = json.load(open(job_path, encoding="utf-8"))
    import torch
    dev = "cuda" if torch.cuda.is_available() else ("mps" if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available() else "cpu")
    model = ChatterboxTTS.from_pretrained(device=dev)
    for text, out in zip(job["chunks"], job["outs"]):
        wav = model.generate(text, audio_prompt_path=job["ref"], exaggeration=job.get("exaggeration", 0.5), cfg_weight=job.get("cfg", 0.5))
        ta.save(out, wav, model.sr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
