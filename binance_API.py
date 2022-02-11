import key
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import json

client = Client(key.api_key, key.api_secret)

# Open time
# Open
# High
# Low
# Close
# Volume
# Close time
# Quote asset volume
# Number of trades
# Taker buy base asset volume
# Taker buy quote asset volume
# Can be ignored
#candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1DAY)

'''
# get historical klines in minutes from 2017/01/01
candles = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MINUTE, start_str="1 Jan, 2017")

print("candles len: ", len(candles))
print("info: ", candles[-1])

with open('BTC_USDT_1MINUTE_SINCE_2017.json', 'w') as f:
    json.dump(candles, f)
'''
'''
# get historical klines in days from 2017/01/01
candles = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1DAY, start_str="1 Jan, 2017")

print("candles len: ", len(candles))
print("info: ", candles[-1])

with open('BTC_USDT_1DAY_SINCE_2017.json', 'w') as f:
    json.dump(candles, f)

candles = client.get_historical_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_1DAY, start_str="1 Jan, 2017")

print("candles len: ", len(candles))
print("info: ", candles[-1])

with open('ETH_USDT_1DAY_SINCE_2017.json', 'w') as f:
    json.dump(candles, f)

candles = client.get_historical_klines(symbol='BNBUSDT', interval=Client.KLINE_INTERVAL_1DAY, start_str="1 Jan, 2017")

print("candles len: ", len(candles))
print("info: ", candles[-1])

with open('BNB_USDT_1DAY_SINCE_2017.json', 'w') as f:
    json.dump(candles, f)
'''

# read the json file and get the klines from the last day
with open('BTC_USDT_1DAY_SINCE_2017.json', 'r') as f:
    old_candles = json.load(f)

new_candles = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1DAY, start_str=str(old_candles[-2][0]))
candles = old_candles + new_candles

with open('BTC_USDT_1DAY_SINCE_2017.json', 'w') as w:
    json.dump(candles, w)

with open('ETH_USDT_1DAY_SINCE_2017.json', 'r') as f:
    old_candles = json.load(f)

new_candles = client.get_historical_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_1DAY, start_str=str(old_candles[-2][0]))
candles = old_candles + new_candles

with open('ETH_USDT_1DAY_SINCE_2017.json', 'w') as w:
    json.dump(candles, w)
    
with open('BNB_USDT_1DAY_SINCE_2017.json', 'r') as f:
    old_candles = json.load(f)

new_candles = client.get_historical_klines(symbol='BNBUSDT', interval=Client.KLINE_INTERVAL_1DAY, start_str=str(old_candles[-2][0]))
candles = old_candles + new_candles

with open('BNB_USDT_1DAY_SINCE_2017.json', 'w') as w:
    json.dump(candles, w)

'''
with open('BTC_USDT_1MINUTE_SINCE_2017.json', 'r') as f:
    old_candles = json.load(f)

new_candles = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MINUTE, start_str=str(old_candles[-2][0]))
candles = old_candles + new_candles

with open('BTC_USDT_1MINUTE_SINCE_2017.json', 'w') as w:
    json.dump(candles, w)
'''

