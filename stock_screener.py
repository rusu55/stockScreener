from pandas_datareader import data as pdr
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
import requests
import datetime
import time
import os

from lib.compute_RSI import computeRSI

yf.pdr_override()

exportList = pd.DataFrame(
    columns=['Stock', "RS_Rating", "Last Close", "% From 52W High", "52 Week Low", "52 week High"])

start_date = datetime.datetime.now() - datetime.timedelta(days=365)
end_date = datetime.date.today() + datetime.timedelta(days=1)
n = -1
sma = [50, 150, 200]

stocklist = si.tickers_nasdaq()
#FFEAstocklist = si.tickers_sp500()

# scanning for stocks
for stock in stocklist:
    n += 1
    try:
        print("\npulling {} with index {}".format(stock, n))
        df = pdr.get_data_yahoo(stock, start=start_date, end=end_date)
        df = df.reset_index()
        RSI = round(computeRSI(df['Adj Close'], 14), 2)

        if int(RSI) < 40:
            low_of_52week = round(min(df["Adj Close"][-260:]), 2)
            high_of_52week = round(max(df["Adj Close"][-260:]), 2)

            currentClose = round(list(df["Close"])[-1], 2)

            decrease = round(int(high_of_52week) - int(currentClose), 2)
            procentage_from_52high = round((decrease / high_of_52week) * 100, 2)

            exportList = exportList.append(
                {'Stock': stock, "RS_Rating": RSI, "Last Close": currentClose,
                 "% From 52W High": procentage_from_52high,
                 "52 Week Low": low_of_52week, "52 week High": high_of_52week}, ignore_index=True)
        print(exportList)
    except Exception:
        print('aaaaaaaaaaaaaaaaaa')
        pass
writer = ExcelWriter("ScreenOutput.xlsx")
exportList.to_excel(writer, "Sheet1")
writer.save()
