from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

menu_router = Router()

@menu_router.message(Command("menu"))
async def menu(message: Message):
    text = (
        "*منوی اصلی*\n"
        "لطفا یک گزینه را انتخاب کنید:\n"
        "- گزینه 1\n"
        "- گزینه 2"
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="گزینه 1", callback_data="opt1")],
        [InlineKeyboardButton(text="گزینه 2", callback_data="opt2")]
    ])

    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")