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

df = pd.read_excel("Data.xlsx")

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
    db_cursor.execute(sql, values)
  
sql_query = "SELECT * FROM HINDALCO_DATA"

df = pd.read_sql(sql_query, mydb)
mydb.commit()
db_cursor.close()
mydb.close()

df.sort_values(by='datetime', inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)

def SMA(data, period=30, column='close'):  
    return data[column].rolling(window=period).mean()


df['SMA100'] = SMA(df, 100)
df['SMA400'] = SMA(df, 400)


df['Signal'] = np.where(df['SMA100'] > df['SMA400'], 1, 0)
df['Position'] = df['Signal'].diff()

df['Buy'] = np.where(df['Position'] == 1, df['close'], np.nan)
df['Sell'] = np.where(df['Position'] == -1, df['close'], np.nan)


buy_signals = df[df['Position'] == 1]
sell_signals = df[df['Position'] == -1]

plt.figure(figsize=(10, 5))
plt.title('HINDALCO - SMA Crossover', fontsize=18)
plt.plot(df['datetime'], df['close'], alpha=0.5, label='Close',color='blue')
plt.plot(df['datetime'], df['SMA100'], alpha=0.7, label='SMA100', linestyle = '--',color='green')
plt.plot(df['datetime'], df['SMA400'], alpha=0.7, label='SMA400', linestyle = '--',color='red')
plt.scatter(buy_signals['datetime'], buy_signals['close'], alpha=1, label='Buy Signal', marker='^', color='green')
plt.scatter(sell_signals['datetime'], sell_signals['close'], alpha=1, label='Sell Signal', marker='v', color='red')
plt.xlabel('datetime', fontsize=10)
plt.ylabel('Close Price', fontsize=10)
plt.legend()
plt.grid(True)  
plt.show()

