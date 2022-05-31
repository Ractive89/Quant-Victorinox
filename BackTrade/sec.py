import backtrader as bt
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import backtrader.analyzers as btanalyzers


class Ketler(bt.Indicator):
    params = dict(ema = 20, atr = 17)
    lines = ('expo', 'atr', 'upper', 'lower')
    plotinfo = dict(subplot=False)
    plotlines = dict(
        upper = dict(ls = '--'),
        lower = dict(_samecolor = True)
    )

    def __init__(self):
        self.l.expo = bt.talib.EMA(self.datas[0].close, timeperiod=self.params.ema)
        self.l.atr = bt.talib.ATR(self.data.high, self.data.low, self.data.close, timeperiod=self.params.atr)
        self.l.upper = self.l.expo + self.l.atr
        self.l.lower = self.l.expo - self.l.atr


class Strategy(bt.Strategy):
    
    def __init__(self):
        self.ketler = Ketler()
        self.close = self.data.close

    def next(self):
        if not self.position:
            if self.close[0] > self.ketler.upper[0]:
                self.order = self.order_target_percent(target=0.95)
        else:
            if self.close[0]< self.ketler.expo[0]:
                self.order = self.sell()


if __name__ == '__main__':
    cerebro = bt.Cerebro()

    data = bt.feeds.YahooFinanceData(
        dataname = 'AAPL',
        fromdate = datetime.datetime(2015, 1, 1),
        todate = datetime.datetime(2020,12,14),
        timeframe = bt.TimeFrame.Days
    )

    cerebro.adddata(data)


    cerebro.addstrategy(Strategy)
    cerebro.broker.setcash(1000000)
    cerebro.broker.setcommission(commission=0)
    cerebro.addsizer(bt.sizers.PercentSizer, percents=98)

    print('Starte Portfolio Value {}'.format(cerebro.broker.getvalue()))
    back = cerebro.run()
    print('end portfolio value {}'.format(cerebro.broker.getvalue()))

    cerebro.plot(style='candle')