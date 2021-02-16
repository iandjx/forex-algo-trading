import fxcmpy
import time
import datetime as dt


###### USER PARAMETERS ######
token = 'INSERT-TOKEN-HERE'
symbol = 'GBP/USD'
timeframe = "m1"                    # (m1,m5,m15,m30,H1,H2,H3,H4,H6,H8,D1,W1,M1)
#############################

# Global Variables
pricedata = None
numberofcandles = 300


con = fxcmpy.fxcmpy(config_file='../fxcm.cfg', server='demo')

# This function runs once at the beginning of the strategy to run initial one-time processes
def Prepare():
    global pricedata

    print("Requesting Initial Price Data...")
    pricedata = con.get_candles(symbol, period=timeframe, number=numberofcandles)
    print(pricedata)
    print("Initial Price Data Received...")

# Get latest close bar prices and run Update() function every close of bar/candle
def StrategyHeartBeat():
    while True:
        currenttime = dt.datetime.now()
        if timeframe == "m1" and currenttime.second == 0 and getLatestPriceData():
            Update()
        elif timeframe == "m5" and currenttime.second == 0 and currenttime.minute % 5 == 0 and getLatestPriceData():
            Update()
            time.sleep(240)
        elif timeframe == "m15" and currenttime.second == 0 and currenttime.minute % 15 == 0 and getLatestPriceData():
            Update()
            time.sleep(840)
        elif timeframe == "m30" and currenttime.second == 0 and currenttime.minute % 30 == 0 and getLatestPriceData():
            Update()
            time.sleep(1740)
        elif currenttime.second == 0 and currenttime.minute == 0 and getLatestPriceData():
            Update()
            time.sleep(3540)
        time.sleep(1)