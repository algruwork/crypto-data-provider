"""
    Main
"""
from datetime import datetime

from fastapi import FastAPI
from .settings import settings
from .models.status import Status
from .models.candlestick import Candlestick

app = FastAPI()


@app.get(settings.main_url)
async def status():
    """ Status endpoint """
    return Status()


@app.get('/tickers')
async def get_ticker() -> list[str]:
    return ['ETH_USDT']


@app.get('/candlesticks/{ticker}')
async def get_candlesticks(start: datetime, end: datetime = datetime.now) -> list[Candlestick]:
    pass