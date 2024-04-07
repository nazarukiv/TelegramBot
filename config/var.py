from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from binance import Client

TOKEN_API = "6853415335:AAFuL2FRe1vy9-5jGLJJoCMkEu5OcxSB4iU"
BINANCE_API_KEY = 'RtnyF7Ec59b2NLQGOgfIbdO3c98J5TnsdumQ1XPkdkvZpTtFSkGCYSDPX6PN48KV'
BINANCE_API_SECRET = 'zCLYr9q2wysx0pSV4ng8gDonaYhikKAxow32FAFWirDnGj1pAnWC92dOMkDR1E9I'

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(storage=MemoryStorage())

binance_client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)


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