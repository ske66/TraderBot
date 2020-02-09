import backtrader
from Strategies import TestStrategy


class Trader():

    total_value = None

    def __init__(self, ticker):
        self.ticker = ticker

    def run_test(self):
        cerebro = backtrader.Cerebro()

        cerebro.broker.set_cash(1000)

        data = backtrader.feeds.GenericCSVData(
            dataname='history/{}.csv'.format(self.ticker),
            dtformat='%Y-%m-%d',
            datetime=0,
            open=1,
            high=2,
            low=3,
            close=4,
            volume=5
        )

        cerebro.adddata(data)
        cerebro.addstrategy(TestStrategy)
        cerebro.addsizer(backtrader.sizers.FixedSize, stake=4)

        cerebro.run()

        self.total_value = cerebro.broker.getvalue()

        # cerebro.plot()
