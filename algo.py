from typing import Tuple
import pandas as pd
import numpy as np


def projecting(macd,signal,value,date):
    sell_point=[]
    buy_point=[]
    flag=-1

    for i in range(0, len(signal)):
        if macd[i] < signal[i]:
            buy_point.append((np.nan,np.nan))
            if flag != 0:
                sell_point.append((value[i],date[i]))
                flag = 0
            else:
                sell_point.append((np.nan,np.nan))
        elif macd[i] > signal[i]:
            sell_point.append((np.nan,np.nan))
            if flag != 1:
                buy_point.append((value[i],date[i]))
                flag = 1
            else:
                buy_point.append((np.nan,np.nan))
        else:
            buy_point.append((np.nan,np.nan))
            sell_point.append((np.nan,np.nan))
            
    return (buy_point,sell_point)

def getProjection(value,date):
    value_set = value
    date_set = date

    value_series = pd.Series(value_set)

    short_EMA = value_series.ewm(span=12, adjust=False).mean() #, alpha=0.5
    long_EMA = value_series.ewm(span=26, adjust=False).mean() #, alpha=0.5 span=26
    MACD = short_EMA-long_EMA
    signal = MACD.ewm(span=9, adjust=False).mean()

    toBeReturned = projecting(MACD.to_list(),signal.tolist(),value_set,date_set)

    return toBeReturned

def test():
    arr = [8,7,6,5,4,3,2,1]
  
# Convert array of integers to pandas series
    numbers_series = pd.Series(arr)
  
# Get the moving averages of series
# of observations till the current time, alpha is how much weight to put on recent 
    moving_averages = round(numbers_series.ewm(
    alpha=0.9, adjust=False).mean(), 2)

    ## MACD Line ##
    ShortEMA = numbers_series.ewm(span=12, adjust=False).mean() #, alpha=0.5
    LongEMA = numbers_series.ewm(span=26, adjust=False).mean() #, alpha=0.5
    MACD = ShortEMA - LongEMA
    signal = MACD.ewm(span=9, adjust=False).mean()

# Convert pandas series back to list
    moving_averages_list = moving_averages.tolist()
