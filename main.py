from aiogram import Bot, Dispatcher, types

TOKEN_API = "6853415335:AAFuL2FRe1vy9-5jGLJJoCMkEu5OcxSB4iU"

bot = Bot(TOKEN_API)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message): #give answer as well as you type.
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


