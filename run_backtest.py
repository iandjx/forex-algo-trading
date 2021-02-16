from backtesting.backtesting import Backtest
import fxcmpy
import datetime as dt
from back_test.strategies.SMA import SmaCross


con = fxcmpy.fxcmpy(config_file='./fxcm.cfg', server='demo')

start = dt.datetime(2020, 1, 1)
stop = dt.datetime(2021, 1, 21)

data = con.get_candles('EUR/USD', period='H4', start=start, end=stop)

data.rename(columns={'askopen': 'Open', 'askhigh': 'High',
                     'bidlow': 'Low', 'bidclose': 'Close'}, inplace=True)

print(data)

con.close()


bt = Backtest(data, SmaCross, cash=10_000, commission=.002)
output = bt.run()
print(bt)
bt.plot()
