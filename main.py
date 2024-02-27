from aiogram import Bot, Dispatcher, types
import string
import random

from aiogram.filters import Command

TOKEN_API = "6853415335:AAFuL2FRe1vy9-5jGLJJoCMkEu5OcxSB4iU" #token to verify telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher()

count = 0

@dp.message(Command("start")) #handle
async def start_command(message: types.Message): #parse_mode allow to add html tags
    await message.answer('<em>Hello, <b>welcome to my bot</b>, done by Ivan Nazaruk!</em>', parse_mode="HTML")


@dp.message()
async def change_sticker(message: types.Message):
    if message.text == "❤️":
        await message.answer("🪇")
    else:
        await message.answer("This command only handle red heart")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


