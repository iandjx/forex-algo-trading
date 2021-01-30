from datetime import datetime
import MetaTrader5 as mt5
from pyti.simple_moving_average import  simple_moving_average as sma
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from pyti.exponential_moving_average import exponential_moving_average as ema
from backtesting import Strategy, Backtest
from backtesting.lib import resample_apply
from backtesting.lib import crossover


# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# import pytz module for working with time zone
import pytz
 
# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 1, tzinfo=timezone)
utc_to = datetime(2021, 1, 21, tzinfo=timezone)

# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
# rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, utc_from, 40)
rates = mt5.copy_rates_range("EURUSD", mt5.TIMEFRAME_H4, utc_from, utc_to)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
# display each element of obtained data in a new line
print("Display obtained data 'as is'")
close_array = []
for rate in rates:
    close_array.append(rate[4])

# print(close_array)
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
# print(rates_frame)
# rates_frame['time']=pd.to_datetime(rates_frame['time'])
                           
# display data


# period = 15
# res = ema(close_array, period)
# print(res)
# rates_frame.insert(5, "15ema", res, True)

# period = 200
# res = ema(close_array, period)
# rates_frame.insert(6, "200ema", res, True)

print("\nDisplay dataframe with data a")
rates_frame.set_index('time', inplace=True)
rates_frame.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close'}, inplace=True)

# rates_frame.columns['Open', 'High','Low', 'Close']
del rates_frame['tick_volume']
del rates_frame['spread']
del rates_frame['real_volume']

print(rates_frame)  

# plt.plot(rates_frame['time'], rates_frame['close'], 'r-', label='close')
# plt.plot(rates_frame['time'], rates_frame['15ema'], 'b-', label='15ema')
# plt.plot(rates_frame['time'], rates_frame['200ema'], 'g-', label='200ema')


# plt.show()

def SMA(values, n):
    """
    Return simple moving average of `values`, at
    each step taking into account `n` previous values.
    """
    return pd.Series(values).rolling(n).mean()

class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 20
    
    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()


bt = Backtest(rates_frame, SmaCross, cash=10_000, commission=.002)
stats = bt.run()
print(stats)
bt.run()
bt.plot()