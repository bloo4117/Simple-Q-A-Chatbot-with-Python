#!/usr/bin/env python3
"""Terminal chat client using ChatterBot.
Run after you have trained the bot with `python train.py`.
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# SQLite storage in local file
DB_PATH = os.environ.get("CHATTERBOT_DB", "db.sqlite3")

bot = ChatBot(
    "TerminalBot",
    read_only=True,  # don't learn during chat; training is in train.py
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri=f"sqlite:///{DB_PATH}",
    logic_adapters=[
        {"import_path": "chatterbot.logic.BestMatch"},
        {"import_path": "chatterbot.logic.MathematicalEvaluation"},
        {"import_path": "chatterbot.logic.TimeLogicAdapter"},
    ],
)

BANNER = (
    "ChatterBot CLI — type 'exit' or 'quit' to leave\n"
    "------------------------------------------------"
)

def main():
    print(BANNER)
    while True:
        try:
            user_input = input("user: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nbot: Goodbye!")
            break

        if user_input.lower() in {"exit", "quit"}:
            print("bot: Goodbye!")
            break

        response = bot.get_response(user_input)
        print(f"bot: {response}")

if __name__ == "__main__":
    main()
