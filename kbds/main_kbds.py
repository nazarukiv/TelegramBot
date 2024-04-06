from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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