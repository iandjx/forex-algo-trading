import fxcmpy
import socketio
import datetime as dt
print(fxcmpy.__version__)
print(socketio.__version__)
# print(TOKEN)
start = dt.datetime(2020, 8, 1, 0, 0, 0)
stop = dt.datetime(2020, 10, 2, 0, 0, 0)

con = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='demo')

# con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='info', server='demo', log_file='log.txt')
# con = fxcmpy.fxcmpy(access_token=TOKEN_REAL, log_level='info', server='real', log_file='log.txt')

# data = con.get_candles('USD/JPY', period='D1')  # daily data
data = con.get_candles('EUR/USD', period='D1')
print(data)

con.close()