# ChatterBot CLI (Django/Python) — Advanced AI Assignment

This repo contains a **terminal client** that lets you chat with a bot powered by **ChatterBot**. It also includes a minimal Django project stub so your environment matches the assignment’s setup notes, even though the client itself runs in the terminal.

## Quick start

```bash
# 1) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# 2) Install pinned dependencies (tested with Python 3.8–3.10)
pip install -r requirements.txt

# 3) (Optional) Download NLTK data used by ChatterBot
python -m nltk.downloader punkt

# 4) Train the bot (loads custom corpus + small greetings)
python train.py

# 5) Chat in the terminal
python bot.py
```

> **Tip:** If `spacy` requests a language model for advanced pipelines, you can skip it for this assignment. ChatterBot list/corpus training works without additional models.

## Files
- `bot.py` — Terminal chat client
- `train.py` — One-time training script (safe to re-run)
- `data/custom_corpus.yml` — Small domain phrases for the bot
- `requirements.txt` — Pinned versions to avoid breakage
- `manifest.json` — What to grade and how to run
- `README.md` — This file
- `sample_terminal_screenshot.png` — Example screenshot for your report

## Notes on Django
The assignment references Django installation. We include Django in `requirements.txt` so your environment matches instructions, but the **client is terminal-based** per the prompt. If your instructor requires a Django app, you can wrap `bot.py` logic in a Django view or management command later.

## Troubleshooting
- If you see `sqlalchemy 2.x` errors, ensure version `1.3.24` is installed (provided by `requirements.txt`).
- If Apple Silicon build errors occur for `blis` or `thinc`, upgrade pip and wheel, then try again:
  ```bash
  pip install --upgrade pip setuptools wheel
  pip install -r requirements.txt
  ```
- If `nltk` tokenizer errors appear, run `python -m nltk.downloader punkt`.
