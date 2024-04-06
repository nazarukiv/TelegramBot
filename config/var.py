from multiprocessing.connection import Client

from aiogram import Bot, Dispatcher

TOKEN_API = "#"  # Token to verify Telegram API
BINANCE_API_KEY = '#'  #Binance API Key
BINANCE_API_SECRET = '#'  #Binance API Secret
binance_client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

bot = Bot(TOKEN_API)
dp = Dispatcher()

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