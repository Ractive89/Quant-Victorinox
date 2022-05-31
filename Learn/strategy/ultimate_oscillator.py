import backtrader as bt
from strategy.log_object import BaseObject


class UltimateOscillator(BaseObject):

    params = (
        ('p1', 7),
        ('p2', 14),
        ('p3', 28)
    )

    def __init__(self):
        self.ULTOSC = bt.talib.ULTOSC(self.data.high, self.data.low, self.data.close,
                                      timeperiod1=self.params.p1,
                                      timeperiod2=self.params.p2,
                                      timeperiod3=self.params.p3)

    def next(self):
        if not self.position:
            if self.ULTOSC < 30:
                self.buy()

        elif self.ULTOSC > 70:
            self.close()
