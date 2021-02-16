import fxcmpy


con = fxcmpy.fxcmpy(config_file='../fxcm.cfg', server='demo')

con.subscribe_market_data('EUR/USD')

data = con.get_prices('EUR/USD')

print(data)
