import requests
import pandas as pd
import json
import datetime as dt
import backtrader as bt

def getBinanceBar(symbol, interval, startTime, endTime):
    url = "https://api.binance.com/api/v3/klines"
    startTime = str(int(startTime.timestamp()*1000))
    endTime = str(int(endTime.timestamp()*1000))
    limit = '1000'

    req_params = {'symbol': symbol, 'interval': interval,
                  'startTime': startTime, 'endTime': endTime, 'limit': limit}
    df = pd.DataFrame(json.loads(requests.get(url, params=req_params).text))

    if(len(df.index) == 0):
        return None

    df = df.iloc[:, 0:6]
    df.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']
    df.open = df.open.astype('float')
    df.high = df.high.astype('float')
    df.low = df.low.astype('float')
    df.close = df.close.astype('float')
    df.volume = df.volume.astype('float')
    df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.datetime]

    return df


def getBinanceData(symbol='BTCUSDT',startTime=(2020,1,1),timeWindow='4h'):
    df_list = []
    startTimeYear,startTimeMonth,startTimeDay=startTime
    last_datatime = dt.datetime(startTimeYear, startTimeMonth, startTimeDay)
    while True:
        new_df = getBinanceBar(
            symbol, timeWindow, last_datatime, dt.datetime.now())
        if new_df is None:
            break

        df_list.append(new_df)
        last_datatime = max(new_df.index)+dt.timedelta(0, 1)

    df = pd.concat(df_list)

    return bt.feeds.PandasData(dataname=df)
