import asyncio
from config.var import dp, bot
import cmds

async def main():
    from cmds.cmds import cmds_router
    dp.include_router(cmds_router)


    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
