import os
from aiogram.filters import Command
from bot.my_bot import CreateBot
from aiogram import Dispatcher, Router, types
import asyncio
import logging
from dotenv import load_dotenv
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

load_dotenv(".env")

bot = CreateBot().get_bot()

DOMAIN_NAME = os.getenv("DOMAIN_NAME")


WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://aiogram-using-github-production.up.railway.app{WEBHOOK_PATH}"


router = Router()

@router.message(Command("start"))
async def echo(message: types.Message):
    await message.answer("این ربات داره از وب هوک استفاده میکنه!")

dp = Dispatcher()
dp.include_router(router)



#-------------------------------------------------------------




async def on_startup(app: web.Application):
    await bot.set_webhook(WEBHOOK_URL)
    logging.info("Webhook set!")


async def on_shutdown(app: web.Application):
    await bot.delete_webhook()
    logging.info("Webhook deleted!")


def main():
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    web.run_app(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()

