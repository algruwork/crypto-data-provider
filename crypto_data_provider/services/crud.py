"""crud module"""
from sqlalchemy.orm import Session

from ..models import models
from ..schemas import candlestick


def get_candlestick(db: Session, start: int, end: int):
    """Return candlestick from db"""
    return db.query(models.Candlestick).filter(models.Candlestick.time >= start, models.Candlestick.time <= end)


def save_candlestick(db: Session, candlesticks: list[candlestick.Candlestick]):
    """Save candlestick to db"""
    rows = []
    for candle in candlesticks:
        row = models.Candlestick(
            time=candle.time,
            open=candle.open,
            hight=candle.hight,
            low=candle.low,
            close=candle.close
            )
        rows.append(row)
    db.add_all(rows)
    db.commit()
    return True
