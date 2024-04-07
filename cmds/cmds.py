import feedparser
from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

from config.var import dp, HELP_COMMAND, binance_client, bot
from kbds.main_kbds import inl, inl_wallets, inl_analysis_platform, inl_education_tech_analysis, educational_content

cmds_router = Router()

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

@dp.message(Command('crypto_info'))
async def crypto_info():


# Callback Query Handler for Crypto Selection
@dp.callback_query(lambda c: c.data.startswith('crypto_'))
async def handle_crypto_callback_query(callback_query: types.CallbackQuery):
    symbol = callback_query.data.split('_')[1]
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

def fetch_latest_crypto_news():
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