"""
    Main
"""
from datetime import datetime

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .settings import settings
from .schemas.status import Status
from .schemas.candlestick import Candlestick
from .services.market import get_history_candlesticks
from .services.crud import save_candlestick
from .utils.logging import setup_logging
from .database import SessionLocal, engine
from .models import models

# set up logging
logger = setup_logging()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    """Return db connection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(settings.main_url)
async def status():
    """ Status endpoint """
    return Status()


@app.get('/tickers', response_model=list[str])
async def get_ticker() -> list[str]:
    """Get tickers"""
    return ['ETH_USDT']


@app.get('/candlesticks/{ticker}', response_model=list[Candlestick])
async def get_candlesticks(ticker: str,
                           start: datetime,
                           end: datetime = datetime.utcnow(),
                           db: Session = Depends(get_db)) -> list[Candlestick]:
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
    is_rows_added = save_candlestick(db=db, candlesticks=candlesticks) # just for test
    logger.info('Rows adeed? %s', is_rows_added)
    return candlesticks
