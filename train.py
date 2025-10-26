#!/usr/bin/env python3
"""One-time (re)training script for the ChatterBot.
You can extend training by adding pairs to the `small_talk` list or
by adding more YAML files under ./data and pointing CorpusTrainer to them.
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os

DB_PATH = os.environ.get("CHATTERBOT_DB", "db.sqlite3")

bot = ChatBot(
    "TerminalBot",
    read_only=False,
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri=f"sqlite:///{DB_PATH}",
    logic_adapters=[
        {"import_path": "chatterbot.logic.BestMatch"}
    ],
)

# 1) Small talk pairs
small_talk = [
    ("Hi", "Hello!"),
    ("How are you doing?", "I am doing very well, thank you for asking."),
    ("You're welcome.", "Do you like hats?"),
]

print("Training with small talk examples...")
ListTrainer(bot).train([x for pair in small_talk for x in pair])

# 2) Custom YAML corpus
print("Training with custom YAML corpus in ./data ...")
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train("./data")

print("Training complete. You can now run `python bot.py`.")
