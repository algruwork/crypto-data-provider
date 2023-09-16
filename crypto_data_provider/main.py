"""
    Main
"""
from datetime import datetime

from fastapi import FastAPI
from .settings import settings
from .models.status import Status
from .models.candlestick import Candlestick
from .services.market import get_history_candlesticks
from .utils.logging import setup_logging

# set up logging
logger = setup_logging()

app = FastAPI()


@app.get(settings.main_url)
async def status():
    """ Status endpoint """
    return Status()


@app.get('/tickers')
async def get_ticker() -> list[str]:
    """Get tickers"""
    return ['ETH_USDT']


@app.get('/candlesticks/{ticker}')
async def get_candlesticks(ticker: str,
                           start: datetime,
                           end: datetime = datetime.utcnow()) -> list[Candlestick]:
    """Get candlesticks"""
    raw_candlesticks = get_history_candlesticks(ticker, start, end)
    candlesticks = []
    for row_candle in raw_candlesticks:
        candlestick = Candlestick(
            time=row_candle[0],
            open=row_candle[1],
            hight=row_candle[2],
            low=row_candle[3],
            close=row_candle[4]
                    )
        candlesticks.append(candlestick)
    return candlesticks
