import backtrader as bt
import datetime
import pandas as pd
import backtrader.analyzers as bta

class RatioAnalyse():
    cerebro=None
    back=None

    def __init__(self,cerebro):
        self.cerebro=cerebro
        self.ratioAdd()
        

    def ratioAdd(self):
        self.cerebro.addanalyzer(bta.SharpeRatio, _name="sharpe")
        self.cerebro.addanalyzer(bta.DrawDown, _name="drawdown")
        self.cerebro.addanalyzer(bta.Returns, _name="returns")

    def run(self):
        print('Start Portfolio value  {}'.format(self.cerebro.broker.getvalue()))
        self.back = self.cerebro.run()
        print('End Portfolio value  {}'.format(self.cerebro.broker.getvalue()))

    def ratioPrint(self):
        ratioList = [
            [
                i.analyzers.returns.get_analysis()['rtot'],
                i.analyzers.returns.get_analysis()['rnorm100'],
                i.analyzers.drawdown.get_analysis()['max']['drawdown'],
                i.analyzers.sharpe.get_analysis()['sharperatio']
            ]
            for i in self.back
        ]

        print(pd.DataFrame(ratioList, columns=[
              'Total_Return', 'APR', 'Drawdown', 'Sharpe_Ratio']))
