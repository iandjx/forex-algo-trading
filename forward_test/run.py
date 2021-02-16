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