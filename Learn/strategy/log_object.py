import backtrader as bt

class BaseObject(bt.Strategy):

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: {:.2f}, Cost: {:.2f}, Comm: {:.2f}'.format(
                        order.executed.price,
                        order.executed.value,
                        order.executed.comm
                    )
                )
                self.buyprcie = order.executed.price
                self.buycomm = order.executed.comm

            else:
                self.log(
                    'SELL EXECUTED, Price: {:.2f}, Cost: {:.2f}, Comm: {:.2f}'.format(
                        order.executed.price,
                        order.executed.value,
                        order.executed.comm
                    )
                )
                self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm)
                 )
