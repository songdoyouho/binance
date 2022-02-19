import json
import statistics
import math

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

with open('BTC_USDT_1DAY_SINCE_2017.json', 'r') as f:
    BTC_candles = json.load(f)

with open('ETH_USDT_1DAY_SINCE_2017.json', 'r') as f:
    ETH_candles = json.load(f)

with open('BNB_USDT_1DAY_SINCE_2017.json', 'r') as f:
    BNB_candles = json.load(f)

# align BTC and ETH to BNB
BTC_candles = BTC_candles[len(BTC_candles)-len(BNB_candles):]
ETH_candles = ETH_candles[len(ETH_candles)-len(BNB_candles):]

day_interval = [i for i in range(10, 190, 10)]
BTC_percentage = 0.1
ETH_percentage = 0.2
BNB_percentage = 0.2

last_USDT_list = []
all_sharp_ratio = []

for interval in day_interval:
    my_USDT = 10000
    my_BTC = 0
    my_ETH = 0
    
    day_counter = 0

    my_USDT_list = []

    last_USDT = 0
    for candle_index in range(len(BTC_candles)):
        BTC_candle = BTC_candles[candle_index]
        ETH_candle = ETH_candles[candle_index]
        BNB_candle = BNB_candles[candle_index]

        if day_counter == 0:
            ori_USDT = my_USDT
            #print("***********************")
            #print("buy BTC price: ", BTC_candle[4])
            buy_price = float(BTC_candle[4])
            my_BTC = ori_USDT * BTC_percentage / float(buy_price)
            my_USDT = my_USDT - ori_USDT * BTC_percentage
            #print("get ", float(my_BTC), " BTC")

            #print("buy ETH price: ", ETH_candle[4])
            buy_price = float(ETH_candle[4])
            my_ETH = ori_USDT * ETH_percentage / float(buy_price)
            my_USDT = my_USDT - ori_USDT * ETH_percentage
            #print("get ", float(my_ETH), " ETH")

            #print("buy BNB price: ", BNB_candle[4])
            buy_price = float(BNB_candle[4])
            my_BNB = ori_USDT * BNB_percentage / float(buy_price)
            my_USDT = my_USDT - ori_USDT * BNB_percentage
            #print("get ", float(my_BNB), " BNB")

            #print("left ", my_USDT, " USDT")
            day_counter = day_counter + 1

        elif day_counter == interval:
            day_counter = 0
            #print("-----------------------")
            #print("sell BTC price: ", BTC_candle[4])
            my_USDT = float(BTC_candle[4]) * my_BTC + my_USDT
            my_BTC = 0

            #print("sell ETH price: ", ETH_candle[4])
            my_USDT = float(ETH_candle[4]) * my_ETH + my_USDT
            my_ETH = 0

            #print("sell BNB price: ", BNB_candle[4])
            my_USDT = float(BNB_candle[4]) * my_BNB + my_USDT
            my_BNB = 0

            #print("get ", float(my_USDT), " USDT")
            last_USDT = my_USDT

            my_USDT_list.append(my_USDT)

        else:
            day_counter = day_counter + 1

    last_USDT_list.append(last_USDT)
    all_reward_percentages = []
    for i in range(len(my_USDT_list) - 1):
        reward_percentage = (my_USDT_list[i+1] / my_USDT_list[i] - 1) * 100
        all_reward_percentages.append(reward_percentage)

    reward_avg = sum(all_reward_percentages) / len(all_reward_percentages)
    reward_stdev = statistics.stdev(all_reward_percentages)
    sharp_ratio = ((reward_avg - 0.02 * interval) / reward_stdev) * math.sqrt(365)
    all_sharp_ratio.append(sharp_ratio)
    print("reward_avg: ", reward_avg)
    print("reward_stdev: ", reward_stdev)
    print("my_USDT_list: ", my_USDT_list)

print("++++++++++++++++++++++++++++++++++")
print("all_sharp_ratio: ", all_sharp_ratio)
print("last_USDT_list: ", last_USDT_list)


'''
BTC_all_reward_percentages = []
ETH_all_reward_percentages = []
BNB_all_reward_percentages = []
# get daily reward percentage
for i in range(len(BTC_candles) - 1):
    BTC_day_reward_percentage = (float(BTC_candles[i+1][4]) / float(BTC_candles[i][4]) - 1) * 100
    ETH_day_reward_percentage = (float(ETH_candles[i+1][4]) / float(ETH_candles[i][4]) - 1) * 100
    BNB_day_reward_percentage = (float(BNB_candles[i+1][4]) / float(BNB_candles[i][4]) - 1) * 100
    BTC_all_reward_percentages.append(BTC_day_reward_percentage)
    ETH_all_reward_percentages.append(ETH_day_reward_percentage)
    BNB_all_reward_percentages.append(BNB_day_reward_percentage)

BTC_reward_avg = sum(BTC_all_reward_percentages) / len(BTC_all_reward_percentages)
ETH_reward_avg = sum(ETH_all_reward_percentages) / len(ETH_all_reward_percentages)
BNB_reward_avg = sum(BNB_all_reward_percentages) / len(BNB_all_reward_percentages)

BTC_reward_stdev = statistics.stdev(BTC_all_reward_percentages)
ETH_reward_stdev = statistics.stdev(ETH_all_reward_percentages)
BNB_reward_stdev = statistics.stdev(BNB_all_reward_percentages)

BTC_sharp_ratio = ((BTC_reward_avg - 0.02) / BTC_reward_stdev) * math.sqrt(365)
ETH_sharp_ratio = ((ETH_reward_avg - 0.02) / ETH_reward_stdev) * math.sqrt(365)
BNB_sharp_ratio = ((BNB_reward_avg - 0.02) / BNB_reward_stdev) * math.sqrt(365)

print("123")
'''

'''
# only BTC version
day_interval = [i for i in range(10, 190, 10)]

last_USDT_list = []
for interval in day_interval:
    my_USDT = 10000
    my_BTC = 0

    BTC_percentage = 0.7
    day_counter = 0

    last_USDT = 0
    for candle in candles:
        if day_counter == 0:
            print("***********************")
            print("buy price: ", candle[4])
            buy_price = float(candle[4])
            my_BTC = my_USDT * BTC_percentage / float(buy_price)
            my_USDT = my_USDT - my_USDT * BTC_percentage
            print("get ", float(my_BTC), " BTC")
            print("left ", my_USDT, " USDT")
            day_counter = day_counter + 1
        elif day_counter == interval:
            day_counter = 0
            print("-----------------------")
            print("sell price: ", candle[4])
            my_USDT = float(candle[4]) * my_BTC + my_USDT
            my_BTC = 0
            print("get ", float(my_USDT), " USDT")
            last_USDT = my_USDT
        else:
            day_counter = day_counter + 1

    last_USDT_list.append(last_USDT)

print("last_USDT_list: ", last_USDT_list)
'''

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