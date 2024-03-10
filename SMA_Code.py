import pandas as pd
import pymysql
import numpy as np
import matplotlib.pyplot as plt

mydb = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="369852147",
    database="INVESTO_DATA"
)
db_cursor = mydb.cursor()

df = pd.read_excel("Data.xlsx") #give file path where your .xlsx file is save

for index, row in df.iterrows():
    datetime_val = row['datetime'].date()
    close = float(row['close'])
    high = float(row['high'])
    low = float(row['low'])
    open_val = float(row['open'])
    volume = int(row['volume'])
    instrument = row['instrument']
    
    sql = "INSERT INTO HINDALCO_DATA (datetime, close, high, low, open, volume, instrument) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (datetime_val, close, high, low, open_val, volume, instrument)
    
def SMA(data, period=30, column='close'):  
    sma = data[column].rolling(window=period, min_periods=1).mean()
    return sma
df['SMA50'] = SMA(df, 50)
df['SMA200'] = SMA(df, 200)
df['Signal'] = np.where(df['SMA50'] > df['SMA200'], 1, 0)
df['Position'] = df['Signal'].diff()

df['Buy'] = np.where(df['Position'] == 1, df['close'], np.nan)
df['Sell'] = np.where(df['Position'] == -1, df['close'], np.nan)
buy_signals = df[df['Position'] == 1]
sell_signals = df[df['Position'] == -1]

plt.figure(figsize=(10, 5))
plt.title('HINDALCO - SMA Crossover', fontsize=18)
plt.plot(df['datetime'], df['close'], alpha=0.5, label='Close',color='grey')
plt.plot(df['datetime'], df['SMA50'], alpha=1, label='SMA50', color='red')
plt.plot(df['datetime'], df['SMA200'], alpha=1, label='SMA200', color='green')
plt.scatter(buy_signals['datetime'], buy_signals['close'], alpha=1, label='Buy Signal', marker='^', color='green')
plt.scatter(sell_signals['datetime'], sell_signals['close'], alpha=1, label='Sell Signal', marker='v', color='red')
plt.xlabel('datetime', fontsize=10)
plt.ylabel('Close Price', fontsize=10)
plt.legend()
plt.grid(True)  
plt.show()

