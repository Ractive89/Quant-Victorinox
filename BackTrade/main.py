import backtrader as bt
import datetime
import pandas as pd
import backtrader.analyzers as bta
from strategy import *
from util import getBinanceData,RatioAnalyse


if __name__ == "__main__":
    cerebro = bt.Cerebro()

    #data = getBinanceData('BTCUSDT',startTime=(2021,1,1),timeWindow='1h')
    data = bt.feeds.YahooFinanceData(
        dataname='^GSPC',
        fromdate=datetime.datetime(2020, 1, 1),
        todate=datetime.datetime(2022, 4, 1),
        timeframe=bt.TimeFrame.Days)

    cerebro.adddata(data)
    cerebro.addstrategy(KetlerCross)

    cerebro.broker.setcash(1000.0)
    cerebro.broker.setcommission(commission=0.0001)
    cerebro.addsizer(bt.sizers.PercentSizer, percents=50)

    ratio = RatioAnalyse(cerebro)

    ratio.run()
    ratio.ratioPrint()

    cerebro.plot(style="candle")
