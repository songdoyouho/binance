import pandas as pd
import matplotlib
import mplfinance
import json

with open('BTC_USDT_1DAY_SINCE_2017.json', 'r') as f:
    BTC_candles = json.load(f)

with open('ETH_USDT_1DAY_SINCE_2017.json', 'r') as f:
    ETH_candles = json.load(f)

with open('BNB_USDT_1DAY_SINCE_2017.json', 'r') as f:
    BNB_candles = json.load(f)

BTC_candles = BTC_candles[len(BTC_candles)-len(BNB_candles):]
ETH_candles = ETH_candles[len(ETH_candles)-len(BNB_candles):]

df = pd.DataFrame({'Date': [i[0] for i in BTC_candles]})   

BTC_data = {
    'Date': [i[0] for i in BTC_candles],
    'Open': [float(i[1]) for i in BTC_candles],
    'High': [float(i[2]) for i in BTC_candles],
    'Low': [float(i[3]) for i in BTC_candles],
    'Close': [float(i[4]) for i in BTC_candles],
    'Volume': [float(i[5]) for i in BTC_candles]
}

BTC_data = pd.DataFrame(BTC_data)
BTC_data = BTC_data.set_index(pd.to_datetime(df['Date'], unit='ms'))

target_stock = 'BTC/USDT'
mc = mplfinance.make_marketcolors(up='r',down='g',inherit=True)
s  = mplfinance.make_mpf_style(base_mpf_style='yahoo',marketcolors=mc)
kwargs = dict(type='candle', mav=(20, 60, 120), volume=True, title=target_stock, style=s)
mplfinance.plot(BTC_data.tail(365), **kwargs)