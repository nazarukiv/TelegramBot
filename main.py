import hashlib
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from aiogram.types import InputMediaPhoto
import feedparser
from binance.client import Client
import asyncio

TOKEN_API = "#"  # Token to verify Telegram API
BINANCE_API_KEY = '#'  #Binance API Key
BINANCE_API_SECRET = '#'  #Binance API Secret
binance_client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

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


def fetch_latest_crypto_news():
    # RSS feed URL of your chosen crypto news source
    news_url = "https://www.coindesk.com/arc/outboundfeeds/rss/?outputType=xml"
    news_feed = feedparser.parse(news_url)
    latest_news = []

    for entry in news_feed.entries[:3]:
        news_item = {
            'title': entry.title,
            'link': entry.link,
        }
        latest_news.append(news_item)

    return latest_news


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
<b>/education</b>-<em>information for study crypto trading</em>
<b>/latest_news</b>-<em>shows latest crypto news</em>
<b>/top_cryptos</b>-<em>shows info about top crypto-currencies</em>
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

@dp.message(Command("latest_news"))
async def show_latest_news(message: types.Message) -> None:
    news_items = fetch_latest_crypto_news()
    response_text = "<b>Latest Cryptocurrency News:</b>\n\n"
    for news in news_items:
        response_text += f"• <a href='{news['link']}'>{news['title']}</a>\n"
    await message.answer(text=response_text, parse_mode="HTML")

# Fetching Top 15 Cryptocurrencies from Binance
async def get_top_15_crypto_symbols():
    tickers = binance_client.get_ticker()
    sorted_tickers = sorted(tickers, key=lambda x: float(x['quoteVolume']), reverse=True)[:15]
    symbols = [ticker['symbol'] for ticker in sorted_tickers]
    return symbols

# Command Handler for '/top_cryptos'
@dp.message(Command('top_cryptos'))
async def send_top_cryptos(message: types.Message):
    symbols = await get_top_15_crypto_symbols()
    keyboard = InlineKeyboardMarkup()

    # Generating the inline keyboard in rows with 2 buttons each
    buttons = [InlineKeyboardButton(text=symbol, callback_data=f"crypto_{symbol}") for symbol in symbols]
    while buttons:
        row = buttons[:2]  # Take up to 2 buttons for a row
        keyboard.inline_keyboard.append(row)
        buttons = buttons[2:]  # Remove the buttons that were just added

    await message.answer("Select a cryptocurrency:", reply_markup=keyboard)
    print("Crypto was send")

# Callback Query Handler for Crypto Selection
@dp.callback_query(lambda c: c.data.startswith('crypto_'))
async def handle_crypto_callback_query(callback_query: types.CallbackQuery):
    symbol = callback_query.data.split('_')[1]
    # Fetch and display cryptocurrency details here...
    await callback_query.message.answer(f"You selected {symbol}.")
    await callback_query.answer()
async def main():
    await dp.start_polling()

@dp.callback_query()
async def process_callback(callback_query: types.CallbackQuery):
    await callback_query.answer()

    topic_key = callback_query.data
    if topic_key in educational_content:
        content = educational_content[topic_key]

        # Send all photos in a media group
        media_group = [InputMediaPhoto(media=url) for url in content["photo_urls"]]
        await bot.send_media_group(callback_query.from_user.id, media=media_group)

        video_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Watch Video", url=content['video_url'])]
            ]
        )

        await bot.send_message(
            callback_query.from_user.id,
            content['brief'],
            reply_markup=video_keyboard
        )


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
