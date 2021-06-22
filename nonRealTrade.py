import pyupbit
import datetime
import os
import sys
import time
import curses
def GetBuyPoint(df,k=0.5):
    larry=list((df["high"]-df["low"])*k+df["open"])[0]
    return larry
seedMoney=3000000
curBtc=0
alreadyBought=False
lastTime=datetime.datetime.now()
df = pyupbit.get_ohlcv("KRW-BTC", interval='day', count=1)
larry=GetBuyPoint(df)

stdscr = curses.initscr()
count=0
curTime=datetime.datetime.now()
endTime=curTime
endTime=endTime.replace(day = endTime.day+1)
endTime=endTime.replace(hour = 9)
endTime=endTime.replace(minute=0)


print(endTime)

while True:
    star=["*"*i for i in range(0,80,10)]
    time.sleep(0.2)
    curTime=datetime.datetime.now()
    stdscr.addstr(0, 0, f"""
    현재 시각 {curTime}
    마감 시간 {endTime}
    보유 btc: {curBtc}
    보유 총 평가: {seedMoney+curBtc*pyupbit.get_current_price('KRW-BTC')}
    보유 KRW: {seedMoney}
    매수할 시점: {larry}
    BTC가격 {pyupbit.get_current_price('KRW-BTC')}
    전고가: {list(df['high'])}
    전저가: {list(df['low'])}
    시가: {list(df['open'])}
    읽은 ohlcv:{df}
    {star[count]}
    """)
    count+=1
    if count==len(star): count=0
    stdscr.refresh()
    time.sleep(0.2)

    if curTime<=endTime:
        time.sleep(0.2)
        stdscr.addstr(0, 0, f"""진입""")
        if pyupbit.get_current_price('KRW-BTC')>=larry and not alreadyBought:
            #buy all
            stdscr.addstr(0, 0, f"""buy all""")
            curses.beep()
            time.sleep(0.2)
            buyPrices=pyupbit.get_current_price('KRW-BTC')
            curBtc+=seedMoney/buyPrices
            seedMoney=0
            alreadyBought=True
    else:
        endTime=curTime
        endTime=endTime.replace(day = endTime.day+1)
        endTime=endTime.replace(hour = 9)
        endTime=endTime.replace(minute=0)
        stdscr.addstr(0, 0, f"""sell all""")
        time.sleep(0.2)
        df = pyupbit.get_ohlcv("KRW-BTC", interval='day', count=1)
        larry=GetBuyPoint(df)
        time.sleep(0.2)
        curTime=pyupbit.get_ohlcv("KRW-BTC", interval='day', count=1).index[0]
        alreadyBought=False
        time.sleep(0.2)
        seedMoney+=curBtc*pyupbit.get_current_price('KRW-BTC')
        curBtc=0
