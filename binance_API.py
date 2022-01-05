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
candles = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MINUTE, start_str="1 Jan, 2017")

print("candles len: ", len(candles))
print("info: ", candles[-1])

with open('BTC_USDT_1MINUTE_SINCE_2017.json', 'w') as f:
    json.dump(candles, f)
'''
'''
candles = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1DAY, start_str="1 Jan, 2017")

print("candles len: ", len(candles))
print("info: ", candles[-1])

with open('BTC_USDT_1DAY_SINCE_2017.json', 'w') as f:
    json.dump(candles, f)
'''

with open('BTC_USDT_1MINUTE_SINCE_2017.json', 'r') as f:
    candles = json.load(f)


sell_counter = 0
low_price = 100000000
my_USDT = 10000 # USDT
my_BTC = 0
buy_price = 0
buy_flag = False

# 無限做多
for candle in candles:
    if buy_flag == False:
        if float(candle[3]) < low_price: # 如果一分鐘內最低價小於 low_price，則更新
            low_price = float(candle[3])
            print("low_price: ", low_price)

    if buy_flag == False:
        if float(candle[3]) / low_price > 1.005: # 如果一分鐘內最低價是 low_price 的 1.01 倍，則買進
            print("***********************")
            print("buy price: ", candle[4])
            buy_price = float(candle[4])
            my_BTC = my_USDT / float(buy_price)
            my_USDT = 0
            print("get ", float(my_BTC), " BTC")
            buy_flag = True

    if float(candle[3]) / low_price > 1.015: # 如果一分鐘內最低價是 low_price 的 1.015 倍，則賣出並重置 low_price
        print("-----------------------")
        print("sell price: ", candle[4])
        my_USDT = float(candle[4]) * my_BTC
        my_BTC = 0
        print("get ", float(my_USDT), " USDT")
        low_price = 100000000
        buy_flag = False
        sell_counter += 1
        
print("sell counter: ", sell_counter)

'''
buy_counter = 0
high_price = 0
my_USDT = 0
my_BTC = 1
sell_price = 0
sell_flag = False

# 無限做空
for candle in candles:
    if sell_flag == False:
        if float(candle[2]) > high_price: # 如果一分鐘內最高價大於 high_price，則更新
            high_price = float(candle[2])
            print("high_price: ", high_price)
    
    if sell_flag == False:
        if float(candle[2]) / high_price < 0.995: # 如果一分鐘內最高價是 high_price 的 0.995 倍，則賣出
            print("***********************")
            print("sell price: ", candle[4])
            sell_price = float(candle[4])
            my_USDT = my_BTC * float(sell_price)
            my_BTC = 0
            print("get ", float(my_USDT), " USDT")
            sell_flag = True

    if float(candle[2]) / high_price < 0.985: # 如果一分鐘內最高價是 high_price 的 0.985 倍，則買進並重置 high_price
        print("-----------------------")
        print("buy price: ", candle[4])
        my_BTC = my_USDT / float(candle[4])
        my_USDT = 0
        print("get ", float(my_BTC), " BTC")
        high_price = 0
        sell_flag = False
        buy_counter += 1
    
        
print("buy counter: ", buy_counter)
'''

git_try = 0
git_try += 1

git_dev = 0