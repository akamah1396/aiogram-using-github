from aiogram import Bot
import os
from dotenv import load_dotenv
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

class CreateBot:
    def __init__(self):
        load_dotenv(".env")
        self.BOT_TOKEN =os.getenv("BOT_TOKEN")
        self.bot = Bot(token= self.BOT_TOKEN,
                       default=DefaultBotProperties("HTML"))

    def get_bot(self):
        return self.bot


