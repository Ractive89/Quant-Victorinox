import backtrader as bt


class Ketler(bt.Indicator):
    params = dict(ema=20, atr=17)
    lines = ('expo', 'atr', 'upper', 'lower')
    plotinfo = dict(subplot=False)
    plotlines = dict(
        upper=dict(ls='--'),
        lower=dict(_samecolor=True)
    )

    def __init__(self, params):
        if params == None:
            params = self.params
        self.l.expo = bt.talib.EMA(
            self.data.close, timeperiod=params.ema)
        self.l.atr = bt.talib.ATR(
            self.data.high, self.data.low, self.data.close, timeperiod=params.atr)
        self.l.upper = self.l.expo + self.l.atr
        self.l.lower = self.l.expo - self.l.atr
