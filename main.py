import asyncio
from aiogram import Dispatcher,Router, html, F
from bot.my_bot import CreateBot

from aiogram.types import (
Message,
ReplyKeyboardMarkup,
KeyboardButton,
ReplyKeyboardRemove,
KeyboardButton)

from aiogram.filters import Command
from bot.handlers.send_photo import send_photo_router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

""" implement fsm and handling it"""
class FormState(StatesGroup):
    name = State()
    like_bot = State()
    language = State()

""" my keyboard """
keyboard = [[KeyboardButton(text="yes"),KeyboardButton(text="no")]]
reply_keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


form_router = Router()


@form_router.message(Command("register"))
async def register_handler(message: Message, state: FSMContext)->None:
    await state.set_state(FormState.name)
    await message.answer("hello what is your name?")

@form_router.message(FormState.name)
async def process_name(message: Message, state:FSMContext)-> None:
    await state.update_data(name = message.text)
    await state.set_state(FormState.like_bot)
    await message.answer(f"خوش امدی {html.quote(message.text)} \nدوست داری ربات بنویسی؟",
    reply_markup=reply_keyboard                   )

@form_router.message(FormState.like_bot,F.text.casefold() == "yes")
async def yes_handler(message: Message, state:FSMContext)-> None:
    await state.set_state(FormState.language)
    await message.answer("عالیه!\n با چه زبانی دوست داری بنویسی؟",reply_markup=ReplyKeyboardRemove())

@form_router.message(FormState.like_bot, F.text.casefold() == "no")
async def no_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    await message.answer("خیلی خری مگه میشه دوست نداشت",reply_markup=ReplyKeyboardRemove())

@form_router.message(FormState.like_bot, F.text != "yes" & F.text != "no")
async def all_handler(message: Message, state:FSMContext):

   await message.answer("چرت ننویس جون مادرت")

router_magic = Router()

@router_magic.message(F.text.contains("choni"))
async def choni_handler(messag):
    await messag.answer("من خاسم تو خاسی")

    

@form_router.message(FormState.language)
async def language_handler(message: Message, state:FSMContext):
    data = await state.update_data(language = message.text)
    data = await state.get_data()
    await show_summary(message,data)
    await state.clear()
    


async def show_summary(message: Message, data: dict, positive: bool = True) -> None:
    name = data["name"]
    language = data["language"]
    text = f"I'll keep in mind that, {html.quote(name)},your preferred language is: {language}"

    await message.answer(text=text)

router_test = Router()

@router_test.message(Command("yek"))
@router_test.message(Command("do"))
def yek_do_handler(message: Message):
    message.answer("this means you might have written yek or do")
    


    



bot = CreateBot().get_bot()

dp = Dispatcher()

@dp.message(Command("start"))
async def reply_start(message: Message)->None:
    await message.answer(f"<code>سلام</code>{html.bold(message.from_user.first_name)} \n{html.bold("ربات شما فعال شد.")} ")

def register_routers():
    dp.include_router(send_photo_router)
    dp.include_router(form_router)
    dp.include_router(router_magic)
    dp.include_router(router_test)

async def main():
    register_routers()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())