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


inl = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Binance', url="https://www.binance.com/en"),
        InlineKeyboardButton(text='ByBit', url="https://www.bybit.com/en/")
    ],
    [
        InlineKeyboardButton(text='KuCoin', url="https://www.kucoin.com/"),
        InlineKeyboardButton(text='BitGet', url="https://www.bitget.site/uk/")
    ],
    [
        InlineKeyboardButton(text='CoinBase', url="https://www.coinbase.com/en-gb/"),
        InlineKeyboardButton(text='CEX.IO', url="https://cexio.uk/")
    ]
])

inl_wallets = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='MetaMask', url="https://metamask.io/"),
        InlineKeyboardButton(text='Phantom Wallet', url="https://phantom.app/")
    ],
    [
        InlineKeyboardButton(text='Trust Wallet', url="https://trustwallet.com/uk"),
        InlineKeyboardButton(text='Cake Wallet', url="https://cakewallet.com/")
    ],
])

inl_analysis_platform = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='TradingView', url="https://www.tradingview.com/markets/stocks-united-kingdom/"),
        InlineKeyboardButton(text='Coin Market Cap', url="https://coinmarketcap.com/")
    ],
    [
        InlineKeyboardButton(text='Crypto Bubbles', url="https://cryptobubbles.net/"),
        InlineKeyboardButton(text='Coin Gecko', url="https://www.coingecko.com/")
    ],
])

HELP_COMMAND = """
<b>/help</b>-<em>list of commands</em>
<b>/start</b>-<em>start the bot</em>
<b>/cryptocurrency_exchanges</b>-<em>list of best cryptocurrency exchanges</em>
<b>/crypto_wallets</b>-<em>list of best crypto wallets</em>
<b>/crypto_analysis</b>-<em>list of best crypto analysis platforms</em>
"""


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer(text="<b>Welcome to CryptoBot!</b>\n\n<i>Explore the world of cryptocurrencies with us.</i>\n\nFeel free to start exploring! 🚀.\n\nWrite down /help to get a list with all commands!📜", parse_mode="HTML")
    await message.delete()

@dp.message(Command("help"))
async def cmd_help(message: types.Message) -> None:
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")

@dp.message(Command("cryptocurrency_exchanges"))
async def exchanges_cmd(message: types.Message) -> None:
    await message.answer(text="The top bitcoin trading platforms are listed below. Please select one and click the button to be directed to a new page🧑‍💻",
                         reply_markup=inl)

@dp.message(Command("crypto_wallets"))
async def wallet_cmd(message: types.Message) -> None:
    await message.answer(
        text="The top crypto wallet platforms are listed below. Please select one and click the button to be directed to a new page 💼🔒",
        reply_markup=inl_wallets)

@dp.message(Command("crypto_analysis"))
async def wallet_cmd(message: types.Message) -> None:
    await message.answer(
        text="The top crypto analysis platforms are listed below. Please select one and click the button to be directed to a new page 📈🔍",
        reply_markup=inl_analysis_platform)



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
