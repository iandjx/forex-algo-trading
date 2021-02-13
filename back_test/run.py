import fxcmpy
import datetime as dt

con = fxcmpy.fxcmpy(config_file='../fxcm.cfg', server='demo')

start = dt.datetime(2020, 1, 1)
stop = dt.datetime(2021, 1, 21)

data = con.get_candles('EUR/USD', period='H4', start=start, end=stop)

data.rename(columns={'askopen': 'Open', 'askhigh': 'High',
                     'bidlow': 'Low', 'bidclose': 'Close'}, inplace=True)

print(data)

con.close()
