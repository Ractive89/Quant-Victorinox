import imp
import backtrader as bt
from strategy.log_object import BaseObject
from Indicator import Ketler

class KetlerCross(BaseObject):
    params = (
        ('ema', 15),
        ('atr', 20),
    )

    
    def __init__(self):
        self.ketler = Ketler(ema=self.params.ema,atr=self.params.atr)
        self.close = self.datas[0].close

    def next(self):
        if not self.position:
            if self.close[0] > self.ketler.upper[0]:
                self.order = self.buy()
        else:
            if self.close[0] < self.ketler.expo[0]:
                self.order = self.sell()
