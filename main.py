import json
import plotly.graph_objects as go
import datetime

def validate(s,start,end):
      s=s.split("-")
      start=start.split("-")
      end=end.split("-")
      d1=datetime.datetime(int(s[0]), int(s[1]), int(s[2]))
      d2= datetime.datetime(int(start[0]), int(start[1]), int(start[2]))
      d3= datetime.datetime(int(end[0]), int(end[1]), int(end[2]))
      if d1>=d2 and d1<=d3:
          return True
      else:
          return False

def switch(close,low,open,high,symbol,date):
    while(True):
        print('''Enter 1 for OHLC\nEnter 2 for Candlestick Chart\nEnter 3 for Hollow Candle\nEnter 4 for Exit\n''')
        s=int(input())
        if s==1:
            fig = go.Figure(data=go.Ohlc(x=date, open=open, high=high, low=low, close=close))
            fig.show()
        elif s==2:
            fig = go.Figure(data=[go.Candlestick(x=date, open=open, high=high, low=low, close=close)])
            fig.show()
        elif s==3:
            fig = go.Figure(data=[go.Candlestick(x=date, open=open, high=high, low=low, close=close,increasing_line_color= 'white', decreasing_line_color= 'white')])
            fig.show()
        else:
            break


f=open("Stock List.json",'r')

f=json.load(f)

symbols=[]

for i in f:
    symbols.append((i['symbol']))

symbols=set(symbols)
symbols=list(symbols)
symbols.sort()
print(symbols)

print("Enter the Symbol of Stock : ")
s=input()

print("Starting Date (YYYY-MM-DD)")
start=input()

print("Closing Date (YYYY-MM-DD)")
end=input()

date=[]
close=[]
high=[]
symbol=[]
open=[]
low=[]


for i in f:
    if i['symbol'] == s:
        m=validate(i['date'],start,end)
        if m:
            close.append(i['close'])
            open.append(i['open'])
            low.append(i['low'])
            high.append(i['high'])
            symbol.append(i['symbol'])
            date.append(i['date'])
        else:
            continue

switch(close,low,open,high,symbol,date)




