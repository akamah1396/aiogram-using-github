from aiogram import Bot
import os
from dotenv import load_dotenv

class CreateBot:
    def __init__(self):
        load_dotenv(".env")
        self.BOT_TOKEN =os.getenv("BOT_TOKEN")
        self.bot = Bot(token= self.BOT_TOKEN)

    def get_bot(self):
        return self.bot


