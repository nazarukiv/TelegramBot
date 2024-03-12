import hashlib
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from aiogram.types import InputMediaPhoto


TOKEN_API = "6853415335:AAFuL2FRe1vy9-5jGLJJoCMkEu5OcxSB4iU"  # Token to verify Telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher()
educational_content = {
    "trend_lines": {
        "brief": "Learn how to find trend lines which are crucial for technical analysis.",
        "photo_urls": [
            "https://goodcrypto.app/wp-content/uploads/2021/06/trade_lines_4.jpg",
            "https://bravenewcoin.com/wp-content/uploads/2023/11/Good_Crypto_App_Chart_10-min.png",
            "https://www.investopedia.com/thmb/toYyJTxg7Q_aNWkRygJPd9bVbxE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/dotdash_final_The_Utility_Of_Trendlines_Dec_2020-01-1af756d4fd634df78d1ea4479d6af76c.jpg",
            "https://s3.tradingview.com/z/ZrWydUXQ_mid.png"
        ],
        "video_url": "https://youtu.be/65V39ZBp6aM"
    },
    "crypto_volume": {
        "brief": "Discover how to trade using crypto volume indicators.",
        "photo_urls": [
            "https://blackbull.com/wp-content/plugins/phastpress/phast.php/c2VydmljZT1pbWFnZXMmc3JjPWh0dHBzJTNBJTJGJTJGYmxhY2tidWxsLmNvbSUyRndwLWNvbnRlbnQlMkZ1cGxvYWRzJTJGMjAyMyUyRjA4JTJGQlRDVVNEXzIwMjItMTItMDhfMTAtMjgtMzQucG5nJmNhY2hlTWFya2VyPTE2OTcyMzE4NDktMjk1NDAmdG9rZW49OTM1NzdhMjNjYTEwNzA3Mw.q.png",
            "https://public.bnbstatic.com/image/cms/crawler/COINEDITION_NEWS/image-26.png"
        ],
        "video_url": "https://youtu.be/739MO1TTiLQ"
    },
    "day_trading_indicators": {
        "brief": "Explore the top indicators used by successful crypto day traders.",
        "photo_urls": [
            "https://www.wallstreetzen.com/blog/wp-content/uploads/2022/09/T8jrtz3q_mid.png",
            "https://cdn.britannica.com/00/240600-050-864A98B5/Charts-of-financial-instruments-with-various-type-of-indicators.jpg"
        ],
        "video_url": "https://youtu.be/djKoPtWQa1o"
    },
    "crypto_charts": {
        "brief": "Gain the skills to read crypto charts like a pro.",
        "photo_urls": [
            "https://s3.tradingview.com/q/QCAk3rsy_mid.png",
            "https://s3.tradingview.com/n/nAbfy1kq_mid.png"
        ],
        "video_url": "https://youtu.be/TuWZzPBunvc"
    },
    "messari_screener": {
        "brief": "Get an inside look at the new Messari Screener.",
        "photo_urls": [
            "https://messari.io/_next/static/media/default-og.9b766420.png",
        ],
        "video_url": "https://youtu.be/yahTcJJkmj0"
    },
    "technical_analysis_beginners": {
        "brief": "Start your journey into the world of crypto with this technical analysis tutorial.",
        "photo_urls": [
            "https://www.investopedia.com/thmb/8dG15_kWfeUz-SLHcogluoscGCY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/dotdash_Final_Technical_Analysis_Strategies_for_Beginners_Sep_2020-01-412a1ba6af834a74a852cbc32e5d6f7c.jpg",
            "https://cdn.corporatefinanceinstitute.com/assets/Picture1.png",
            "https://www.investopedia.com/thmb/7Oi9CPPtWyjOcCeIECSxAcivijs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/dotdash_Final_Introductio_to_Technical_Analysis_Price_Patterns_Sep_2020-02-59df8834491946bcb9588197942fabb6.jpg",
            "https://static.ifxdb.com/static-content/305/d--Zx_800.jpg",
            "https://miro.medium.com/v2/resize:fit:2000/0*fGOH_EZ-GIQ3EePJ"
        ],
        "video_url": "https://youtu.be/40fP_iKaK1I"
    }
}


inl_education_tech_analysis = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='How to Find Trend Lines', callback_data='trend_lines'),
        InlineKeyboardButton(text='How To Trade Crypto Volume', callback_data='crypto_volume')
    ],
    [
        InlineKeyboardButton(text='Best Indicators for Crypto Day Trading', callback_data='day_trading_indicators'),
        InlineKeyboardButton(text='How to Read Crypto Charts', callback_data='crypto_charts')
    ],
    [
        InlineKeyboardButton(text='Introduction to the New Messari Screener', callback_data='messari_screener'),
        InlineKeyboardButton(text='Technical Analysis Tutorial for Beginners', callback_data='technical_analysis_beginners')
    ]
])


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


@dp.message(Command('education'))
async def education_command(message: types.Message):
    await message.answer("Select a topic to learn more:", reply_markup=inl_education_tech_analysis)


@dp.callback_query()
async def process_callback(callback_query: types.CallbackQuery):
    await callback_query.answer()

    topic_key = callback_query.data
    if topic_key in educational_content:
        content = educational_content[topic_key]

        # Send all photos in a media group
        media_group = [InputMediaPhoto(media=url) for url in content["photo_urls"]]
        await bot.send_media_group(callback_query.from_user.id, media=media_group)

        # Send brief description and video link
        video_keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Watch Video", url=content['video_url']))
        await bot.send_message(callback_query.from_user.id, content['brief'], reply_markup=video_keyboard)
    else:
        await bot.send_message(callback_query.from_user.id, "Sorry, I couldn't find information on that topic.")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
