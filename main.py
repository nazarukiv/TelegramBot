from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio

TOKEN_API = "6853415335:AAFuL2FRe1vy9-5jGLJJoCMkEu5OcxSB4iU"  # Token to verify Telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher()

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='❤️', callback_data="like"),
     InlineKeyboardButton(text='👎', callback_data="dislike")],
])

@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://www.muchbetteradventures.com/magazine/content/images/size/w2000/2019/10/29122602/iStock-971053374.jpg",
                         caption="Do you like this photo?",
                         reply_markup=keyboard_inline)

@dp.callback_query()
async def ikb_cb_handler(callback: types.CallbackQuery):
    print(callback)
    if callback.data == 'like':
        await callback.answer("You like it!That's cool")
    else:
        await callback.answer("You don't like it :(")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
