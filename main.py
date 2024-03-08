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


user_data = ''

@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer('Write down number!')


@dp.message()
async def text_handler(message: types.Message) -> None:
    global user_data
    user_data = message.text
    await message.reply("Your data was saved!")


@dp.inline_query()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or "Echo"
    result_id = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(message_text=f'<b>{text}</b> - {user_data}',
                                            parse_mode="HTML")
    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title="Echo Bot!",
        description= "Hello, I'm not simple bot!"
    )


    await  bot.answer_inline_query(results=[item],
                                   inline_query_id=inline_query.id,
                                   cache_time=1)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
