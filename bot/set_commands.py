from aiogram.types import BotCommand
from bot_instance import bot



async def set_my_bot_commands():
    await bot.set_my_commands([BotCommand(command="auth", description="درخواست ادمینی")],
                              BotCommand(command="help", description="درخواست کمک")
                              )
    