"""Sqlachemy models"""
from sqlalchemy import Float, BigInteger, Column
from ..database import Base


class Candlestick(Base):
    """ Represent Candlestick table """
    __tablename__ = "candlesticks_5_min"

    time = Column(BigInteger, primary_key=True, index=True, comment='Candlestic datetime')
    open = Column(Float, nullable=False, comment='Open price')
    hight = Column(Float, comment='Highest price')
    low = Column(Float, comment='Lowest price')
    close = Column(Float, comment='Close price')
