from datetime import datetime
import time

import okx.MarketData as MarketData
from ..utils.utils import get_time_points, timeframe_to_seconds

FLAG = '0'  # live trading: 0, demo trading: 1
SLEEP_PER_REQUEST_IN_SEC = 1  # rate limit 2 request per sec
marketDataAPI = MarketData.MarketAPI(flag=FLAG, debug=False)


def get_history_candlesticks(ticker: str,
                                   start: datetime,
                                   end: datetime) -> list[list]:
    """Combining all together to API call"""
    time_points = get_time_points(start=start,
                                  end=end,
                                  timeframe='15m',
                                  rate_limit=100)
    data = collect_data(ticker, time_points, timeframe='15m')
    return data


def collect_data(ticker: str,
                 time_points: list[int],
                 timeframe='15m',
                 rate_limit: int = 100) -> list[list]:
    """Collect data from requests"""
    data = []
    for i, _points in enumerate(time_points):
        history_candles = get_history_data(
            ticker=ticker,
            start=time_points[i],
            timeframe=timeframe,
            limit=rate_limit
            )
        time.sleep(SLEEP_PER_REQUEST_IN_SEC)
        print(f'Load batch #{i+1} from {len(time_points)}')
        if history_candles:
            for candel in history_candles['data']:
                data.append(candel)
    return data


def get_history_data(ticker: str,
                           start: int,
                           timeframe: str = '15m',
                           limit: int = 100) -> dict:
    """Make single request"""
    try:
        history_candles = marketDataAPI.get_history_candlesticks(
            instId=ticker,
            bar=timeframe,
            after=(start - timeframe_to_seconds(timeframe))*1000,  # use ONLY AFTER, befor is broken
            # Pagination of data to return records earlier than the requested
            limit=limit
            )
        return history_candles
    except IndexError as err:
        print(f'Got IndexError: {err}. Could be an empty answer from API?')
