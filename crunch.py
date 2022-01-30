from matplotlib import pyplot as plt
from typing import NewType
import requests, json
from time import gmtime, strftime
import time, datetime

from requests.api import request
import algo as algo

key ="oKJJp6ykR9pKoYWL_RHONSrSiepfTgYB"
tickers = ["SHIB","ADA","ETH","BTC","LUNA", "XRP"]

def getCorrectDate(currDate, decrease, count):
    year = currDate.rsplit("-")[0]    
    month = currDate.rsplit("-")[1]
    day = currDate.rsplit("-")[2]
    newDay= int(day)-decrease
    newMonth = int(month)
    newYear = int(year)

    Previous_Date = datetime.datetime.today()-datetime.timedelta(decrease)
    Previous_Date = Previous_Date.strftime("%Y-%m-%d")

    return Previous_Date

def plotFunc(x,y,currency, buys, sells):

    plt.plot(y, x, label=currency)

    setOfValues = [x[0] for x in sells]
    setOfDates = [x[1] for x in sells]
    buyDates = [x[1] for x in buys]
    buyValues = [x[0] for x in buys]

    plt.plot(buyDates,buyValues, 'bo',label="buy points")
    plt.plot(setOfDates,setOfValues, 'ro',label="sell points")
    plt.xlabel('Days')
    plt.ylabel('Value')
    plt.title("Analysis")
    plt.legend()
    plt.xticks(rotation = 45)

    print(sells)

    plt.show()



def getData(currency, maxDays):
    if not currency:
        currency="BTC"
    if not maxDays:
        maxDays=5
    dayOpen = []
    x = []
    y = []
    

    for i in range(0,maxDays):
        currDate = getCorrectDate(strftime("%Y-%m-%d", gmtime()),maxDays-i, i)
        r = requests.get(f"https://api.polygon.io/v1/open-close/crypto/{currency}/USD/{currDate}?adjusted=true&apiKey={key}");
        data = json.loads(r.text)
        x.append(data["open"])
        y.append(currDate.rsplit("-")[1]+"-" + currDate.rsplit("-")[2])
        time.sleep(13)

    projections = algo.getProjection(x,y)
    buy_oppo = projections[0]
    sell_oppo = projections[1]

    plotFunc(x,y,currency,buy_oppo, sell_oppo)
    
    return True
