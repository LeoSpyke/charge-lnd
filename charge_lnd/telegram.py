import sys
import requests
from enum import Enum

def debug(message):
    sys.stderr.write(message + "\n")

class Emoji(Enum):
    PARTY = "\U0001F389"

class Telegram:
    bot_token = ""
    chat_ids = []

    @staticmethod
    def set_bot_token(token: str):
        if Telegram.bot_token == "" and token is not None:
            Telegram.bot_token = token

    @staticmethod
    def add_chat_id(chat_id: str):
        if Telegram.chat_ids is not None:
            Telegram.chat_ids.append(chat_id)

    @staticmethod
    def send_message(text: str):
        for chat_id in Telegram.chat_ids:
            params = {
                "text": text,
                "chat_id": chat_id,
                "parse_mode": "HTML"
            }

            requests.get(
                f"https://api.telegram.org/bot{Telegram.bot_token}/sendMessage",
                params=params
            )