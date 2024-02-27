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
async def check_for_heart(message: types.Message):
    global count
    text = message.text  # the text of the message
    heart_count = text.count("<")

    if heart_count > 0:
        count += heart_count  # update the global count
        await message.answer(f"Count of '<': {heart_count}")
    else:
        await message.answer("No <")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


