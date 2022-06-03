import backtrader as bt


class Ketler(bt.Indicator):
    params = dict(ema=20, atr=17)
    lines = ('expo', 'atr', 'upper', 'lower')
    plotinfo = dict(subplot=False)
    plotlines = dict(
        upper=dict(ls='--'),
        lower=dict(_samecolor=True)
    )

    def __init__(self):
        self.lines.expo = bt.talib.EMA(
            self.datas[0].close, timeperiod=self.params.ema)
        self.lines.atr = bt.talib.ATR(
            self.datas[0].high, self.datas[0].low, self.datas[0].close, timeperiod=self.params.atr)
        self.lines.upper = self.lines.expo + self.lines.atr
        self.lines.lower = self.lines.expo - self.lines.atr
