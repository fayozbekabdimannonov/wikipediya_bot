import aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
import asyncio
import logging
import sys
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
import time 
from wiki import wiki

TOKEN = "6632943217:AAFFo8SRjTxfvSq2_fjY9N4z0ufnnc3et1E"

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    await message.answer(text="Assalomu alaykum! Wikipedia botiga xush kelibsiz! So'z yozib ko'ring!")




@dp.message(F.text)
async def answer_translate(message: Message):
    text = wiki(message.text)
    await message.answer(text=text)


async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
    




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
