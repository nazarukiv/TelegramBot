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

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text='Button 1', callback_data="btn_1")],
   [InlineKeyboardButton(text='Button 2', callback_data="btn_2")],
])

@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer(text=f"Hello {message.from_user.id}",
                         reply_markup=keyboard_inline)

@dp.callback_query()
async def cmd_callback(callback: types.CallbackQuery):
    if callback.data == "btn_1":
        await callback.answer(text="Hello")
    elif callback.data == "btn_2":
        await callback.answer(text="World")


#InlineQuery
@dp.inline_query()
async def inline_echo(inline_query: types.InlineQuery):
    text = inline_query.query or 'Echo' # Text received from the user's inline query input
    if not text:
        return  # If the query is empty, don't respond

    input_content = InputTextMessageContent(message_text=text)  # Correct content creation
    result_id = hashlib.md5(text.encode()).hexdigest()  # Generate a unique result ID


    item = InlineQueryResultArticle(
        id=result_id,
        title="Echo: " + text,  # Set the title of the result as "Echo: <input text>"
        input_message_content=input_content  # Set the content of the message to be sent
    )

    # Use bot.answer_inline_query to send the result back to the user
    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
