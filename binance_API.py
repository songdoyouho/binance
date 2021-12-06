import key
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

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
candles = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1DAY, start_str="1 Jan, 2017")

print("candles len: ", len(candles))
print("info: ", candles[-1])

counter = 0
for candle in candles:
    #print((float(candle[2]) - float(candle[3])) / ((float(candle[2]) + float(candle[3])) / 2) * 100)
    swing = (float(candle[2]) - float(candle[3])) / ((float(candle[2]) + float(candle[3])) / 2) * 100
    if swing > 3:
        counter += 1

print(counter)