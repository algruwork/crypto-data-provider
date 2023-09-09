from datetime import datetime
import time
import json
import pytz

import okx.MarketData as MarketData
from ..utils.utils import get_time_points, timeframe_to_seconds

FLAG = '0'  # live trading: 0, demo trading: 1
SLEEP_PER_REQUEST_IN_SEC = 1  # rate limit 2 request per sec
marketDataAPI = MarketData.MarketAPI(flag=FLAG, debug=False)

async def get_history_candlesticks(start: datetime, end: datetime) -> list[list]:
    pass