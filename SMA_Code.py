import pandas as pd
import matplotlib.pyplot as plt

# Load your data into a Pandas dataframe
df = pd.read_xlsx(r"Data.xlsx")

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Calculate the 50-day and 200-day simple moving averages
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

# Create a new column to store the buy/sell signals
df['Signal'] = 0

# Generate buy/sell signals based on the SMA crossover
for i in range(1, len(df)):
    if df['SMA_50'].iloc[i] > df['SMA_200'].iloc[i] and df['SMA_50'].iloc[i-1] <= df['SMA_200'].iloc[i-1]:
        df['Signal'].iloc[i] = 1  # Buy signal
    elif df['SMA_50'].iloc[i] < df['SMA_200'].iloc[i] and df['SMA_50'].iloc[i-1] >= df['SMA_200'].iloc[i-1]:
        df['Signal'].iloc[i] = -1  # Sell signal

# Plot the close price, SMA_50, and SMA_200
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.plot(df['Date'], df['SMA_50'], label='SMA_50')
plt.plot(df['Date'], df['SMA_200'], label='SMA_200')

# Plot the buy/sell signals
plt.plot(df.loc[df['Signal'] == 1, 'Date'], df.loc[df['Signal'] == 1, 'Close'], 'g^', label='Buy', markersize=10)
plt.plot(df.loc[df['Signal'] == -1, 'Date'], df.loc[df['Signal'] == -1, 'Close'], 'rv', label='Sell', markersize=10)

# Set the title and labels
plt.title('SMA Crossover Signals')
plt.xlabel('Date')
plt.ylabel('Price')

# Show the legend
plt.legend(loc='best')

# Show the plot
plt.show()
