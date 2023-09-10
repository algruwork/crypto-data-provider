from datetime import datetime
from pydantic import BaseModel


class Candlestick(BaseModel):
    """ Represent Candlestick"""
    time: datetime  # Opening time of the candlestick
    open: float  # Open price
    hight: float  # Highest price
    low: float  # Lowest price
    close: float  # Close price
