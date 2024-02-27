from aiogram import Bot, Dispatcher, types
import string
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command

TOKEN_API = "6853415335:AAFuL2FRe1vy9-5jGLJJoCMkEu5OcxSB4iU" #token to verify telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/start'), KeyboardButton(text='/help')],
        [KeyboardButton(text='/description'), KeyboardButton(text='/photo')],
        [KeyboardButton(text='/give')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True  # making the keyboard disappear after a button is pressed
)



keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Button 1', url="https://www.youtube.com/@SerhiiNemchynskyi")],
    [InlineKeyboardButton(text='Button 2', url="https://www.youtube.com/@sbermarket_tech")],
])

HELP_COMMAND = """
<b>/help</b>-<em>list of commands</em>
<b>/give</b>-<em>send the picture of cat</em>
<b>/start</b>-<em>start the bot</em>
<b>/description</b>-<em>description of bot</em>
<b>/photo</b>-<em>photo</em>"""

@dp.message(Command("start")) #handle
async def start_command(message: types.Message): #parse_mode allow to add html tags
    await bot.send_message(message.from_user.id,
                         text='Hello World',
                        reply_markup=keyboard_inline)
    await message.delete()

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()

@dp.message(Command("description"))
async def description_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="Our bot know how to send a photo",
                           parse_mode="HTML")
    await message.delete()

@dp.message(Command("photo"))
async def photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo="https://m.media-amazon.com/images/I/81AheVnqHXL._AC_UF894,1000_QL80_.jpg")
    await message.delete()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

