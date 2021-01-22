from datetime import datetime
import MetaTrader5 as mt5
from pyti.simple_moving_average import  simple_moving_average as sma
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from pyti.exponential_moving_average import exponential_moving_average as ema


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
    print(rate)
    print(type(rate))
    close_array.append(rate[4])

print(close_array)
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
                           
# display data


period = 15
res = ema(close_array, period)
print(res)
rates_frame.insert(5, "15ema", res, True)

period = 200
res = ema(close_array, period)
rates_frame.insert(6, "200ema", res, True)

print("\nDisplay dataframe with data")
print(rates_frame)  

plt.plot(rates_frame['time'], rates_frame['close'], 'r-', label='close')
plt.plot(rates_frame['time'], rates_frame['15ema'], 'b-', label='15ema')
plt.plot(rates_frame['time'], rates_frame['200ema'], 'g-', label='200ema')


plt.show()

