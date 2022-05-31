import backtrader as bt
from strategy.log_object import BaseObject


class EMACross(BaseObject):

    params = (
        ('fast', 7),
        ('slow', 14),
    )

    def __init__(self):
        fast = bt.ind.EMA(period=self.params.fast)
        slow = bt.ind.EMA(period=self.params.slow)
        self.crossover = bt.ind.CrossOver(fast,slow)

    def next(self):
        if not self.position:
            if self.crossover>0:
                self.buy()

        elif self.crossover<0:
            self.close()

