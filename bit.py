import pyupbit

print(pyupbit.get_current_price("KRW-BTC"))
df = pyupbit.get_ohlcv("KRW-BTC")
with open("key.txt",'r') as f:
    access_key=f.readline().rstrip()
    secret_key=f.readline().rstrip()
upbit = pyupbit.Upbit(access_key, secret_key)



balances = upbit.get_balances()


print("보유 KRW : {}".format(upbit.get_balance(ticker="KRW")))          # 보유 KRW
print("총매수금액 : {}".format(upbit.get_amount('ALL')))
print(f"손익 : {-upbit.get_amount('ALL')+upbit.get_balance(ticker='KRW-BTC')*pyupbit.get_current_price('KRW-BTC')}")
print("비트수량 : {}".format(upbit.get_balance(ticker="KRW-BTC")))      # 비트코인 보유수량
# import matplotlib as mpl
# import numpy as np
# import matplotlib.pyplot as plt
# # plt.rcParams["axes.grid"] = True
# plt.rcParams["figure.figsize"] = (12,6)
# plt.rcParams["axes.formatter.limits"] = -10000, 10000
#
# import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
# print(df)
#
# # 가격 차트 그리기
# df = pyupbit.get_ohlcv("KRW-BTC", interval='day', count=100)
# # print("\n---BTC 가격---")
# # print(df)
# # df.head(10)
#
# df[["close", "volume"]].plot(secondary_y=["volume"])
# # df["close"].plot()
# plt.show()
