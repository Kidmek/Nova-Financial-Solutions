import talib
import matplotlib.pyplot as plt
import pynance as pn
import pandas as pd

def add_technical_indicators(original_data):
    data = original_data.copy()
    # Load and prepare data
    # Check if 'Close' column exists
    if 'Close' not in data.columns:
        raise ValueError("'Close' column is missing from the data")
    
    # Calculate Simple Moving Average (SMA)
    data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)
    data['SMA_200'] = talib.SMA(data['Close'], timeperiod=200)

    # Calculate Exponential Moving Average (EMA)
    data['EMA_50'] = talib.EMA(data['Close'], timeperiod=50)
    data['EMA_200'] = talib.EMA(data['Close'], timeperiod=200)
    # Calculate RSI
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    # Calculate MACD
    data['MACD'], data['MACD_Signal'], data['MACD_Hist'] = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

    # Visualize
    
    return data

def visualize_with_indicators(data):

    # Plot closing price and moving averages
    plt.figure(figsize=(14,7))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['SMA_50'], label='50-Day SMA')
    plt.plot(data['SMA_200'], label='200-Day SMA')
    plt.title('Close Price and Moving Averages')
    plt.legend(loc='upper left')
    plt.show()

    # Plot RSI
    plt.figure(figsize=(14,7))
    plt.plot(data['RSI'], label='RSI (14)')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title('RSI (Relative Strength Index)')
    plt.legend(loc='upper left')
    plt.show()

    # Plot MACD
    plt.figure(figsize=(14,7))
    plt.plot(data['MACD'], label='MACD')
    plt.plot(data['MACD_Signal'], label='MACD Signal')
    plt.bar(data.index, data['MACD_Hist'], label='MACD Histogram')
    plt.title('MACD (Moving Average Convergence Divergence)')
    plt.legend(loc='upper left')
    plt.show()


def financial_metrics(original_data):
    data = original_data.copy()
    # Convert the 'Date' column to datetime format if it isn't already
    data['Date'] = pd.to_datetime(data['Date'])

    # Set the 'Date' column as the index
    data.set_index('Date', inplace=True)

    prices = data[['Adj Close']]
    try:
        # data['Bollinger'] = pn.tech.bollinger(prices, window=20)
        data['SMA'] = pn.tech.sma(prices, window=50)
        data['EMA'] = pn.tech.ema(prices, window=50)
        # data['Growth'] = pn.tech.growth(prices)
        # data['Return'] = pn.tech.ret(prices)
        data['Vol'] = pn.tech.volatility(prices)
    except KeyError as e:
        print(f"KeyError: {e}. Check if the required columns are present or expected by the functions.")

    return data