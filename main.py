from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio
import random

TOKEN_API = "6853415335:AAFuL2FRe1vy9-5jGLJJoCMkEu5OcxSB4iU"  # Token to verify Telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher()

number = 1000

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='❤️', callback_data="like"),
     InlineKeyboardButton(text='👎', callback_data="dislike")],
])

def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Random number', callback_data="btn_random"),
     InlineKeyboardButton(text='1000', callback_data="btn_hun")],
])
    return ikb

@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer(f"The current number is {number}",
                         reply_markup=get_inline_keyboard())

@dp.callback_query()
async def ikb_callback(callback: types.CallbackQuery) -> None:
    global number
    if callback.data == "btn_random":
        await callback.message.edit_text(f"The current number is {random.randint(1,10)}",
                                         reply_markup=get_inline_keyboard())
    elif callback.data == "btn_hun":
        await callback.message.edit_text(f"The current number is {number}",
                                         reply_markup=get_inline_keyboard())
    else:
        1/0




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
