import asyncio
import multiprocessing.connection
from config.var import dp, bot


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
