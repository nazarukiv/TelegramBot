import hashlib

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle


TOKEN_API = "6853415335:AAFuL2FRe1vy9-5jGLJJoCMkEu5OcxSB4iU"  # Token to verify Telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
