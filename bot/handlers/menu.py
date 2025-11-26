from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

menu_router = Router()

@menu_router.message(Command("menu"))
async def menu(message: Message):
    text = (
        "*Main Menu*\n"
        "Choose an option:\n"
        "- Option 1\n"
        "- Option 2"
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Option 1", callback_data="opt1")],
        [InlineKeyboardButton(text="Option 2", callback_data="opt2")]
    ])

    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")