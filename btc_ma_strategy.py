import yfinance as yf
import matplotlib.pyplot as plt

# Fetch BTC-USD data
data = yf.download('BTC-USD', period='max')

# Compute 20-day and 50-day moving averages
data['MA_50'] = data['Close'].rolling(window=50).mean()
data['MA_200'] = data['Close'].rolling(window=200).mean()

# Plot the closing price and moving averages
plt.figure(figsize=(14,7))
plt.plot(data['Close'], label='Bitcoin Price')
plt.plot(data['MA_50'], label='50-Day Moving Average', color='orange')
plt.plot(data['MA_200'], label='200-Day Moving Average', color='blue')
plt.title('Bitcoin Closing Price and Moving Averages')
plt.legend()

# Save the figure as 'btc_ma.png'
plt.savefig('btc_ma.png')

# Show the plot
plt.show()