import asyncio

from aiogram import Bot, Dispatcher, types
import string
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command

TOKEN_API = "6853415335:AAFuL2FRe1vy9-5jGLJJoCMkEu5OcxSB4iU" #token to verify telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher()

HELP_COMMAND = """
<b>/help</b>-<em>list of commands</em>
<b>/start</b>-<em>start the bot</em>
<b>/choose</b>-<em>list of cryptocurrencies</em>
<b>/crypto_com</b>-<em>location of crypto.com office</em>
<b>/vote</b>-<em>allow user to rate binance and their blog</em>
"""

welcome_message = (
        "<b>Welcome to my Crypto Bot!</b>\n\n"
        "This bot was created by <i>Ivan Nazaruk</i>.\n\n"
        "Here you can get information and updates about cryptocurrency."
    )

keyboard = ReplyKeyboardMarkup(
   keyboard=[
       [KeyboardButton(text='/start'), KeyboardButton(text='/help')],
   ],
   resize_keyboard=True,
   one_time_keyboard=True  # Making the keyboard disappear after a button is pressed
)

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text='Binance', url="https://www.binance.com/en-GB")],
   [InlineKeyboardButton(text='ByBit', url="https://www.bybit.com/en/")],
    [InlineKeyboardButton(text='Kraken', url="https://www.kraken.com/")],
    [InlineKeyboardButton(text='Coinbase', url="https://www.coinbase.com/en-gb/")]
])

@dp.message(Command("start")) #handle
async def start_command(message: types.Message): #parse_mode allow to add html tags
    await bot.send_message(message.from_user.id,
                         text= welcome_message,
                            parse_mode="HTML",
                           reply_markup=keyboard)
    await message.delete()

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()

@dp.message(Command("choose"))
async def crypto_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://bs-uploads.toptal.io/blackfish-uploads/components/blog_post_page/content/cover_image_file/cover_image/1303387/regular_1708x683_Untitled-e7fde53f1e5631a8728cc9aefc1538e8.png")
    await bot.send_message(chat_id=message.from_user.id,
                           text="Please choose a cryptocurrency exchange from the options below:",
                           reply_markup=keyboard_inline)

@dp.message(Command("crypto_com"))
async def location_of_binance(message: types.Message):
    await message.answer(text="Here is location of crypto.com main office")
    await bot.send_location(chat_id=message.from_user.id,
                            longitude=103 + (51/60) + (8.3/3600),
                            latitude= 1 + (16/60) + (51.9/3600))

@dp.message(Command("vote"))
async def vote_command(message: types.Message):
   keyboard_inline1 = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='❤️', callback_data="like")],
       [InlineKeyboardButton(text='👎', callback_data="dislike")],
   ])


   await bot.send_photo(chat_id=message.from_user.id,
                        photo="https://public.bnbstatic.com/image/cms/blog/20210923/4d355307-c090-47d9-aeaa-88bcdb17751e.png",
                        caption="Do you like binance?",
                        reply_markup=keyboard_inline1)

@dp.callback_query()
async def vote_callback(callback: types.CallbackQuery):
   if callback.data == 'like':
       return await callback.answer(text="Cool!, you will be redirected")
   else:
       await callback.answer("Sad!I will try to impress you next time!")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asynhron
    asyncio.run(main())

