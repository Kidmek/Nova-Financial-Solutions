from . import descriptive_stat
import pandas as pd

def align_date(original_data):
    data = original_data.copy()
    descriptive_stat.format_date(data, 'date' if 'date' in data.columns else 'Date', True)
    # Drop rows where 'date_parsed' could not be converted
    data = data.dropna(subset=['date_parsed'])
    return data

def calc_daily_returns(original_data):
    original_data['Daily Return'] = original_data['Adj Close'].pct_change() * 100
    return original_data


def correlation_analysis(news_data, stock_data):
    # Convert sentiment to numerical values
    sentiment_mapping = {
        'Positive': 1,
        'Neutral': 0,
        'Negative': -1
    }
    # Apply the mapping to convert sentiment to numerical scores
    news_data['Sentiment Score'] = news_data['Sentiment'].map(sentiment_mapping)
    # Aggregate sentiment scores by date (taking the mean sentiment score per day)
    daily_sentiment = news_data.groupby('date')['Sentiment Score'].mean().reset_index()
    # Merge the daily sentiment scores with the stock data on the date
    merged_df = pd.merge(stock_data, daily_sentiment, left_on='Date', right_on='date', how='inner')

    # Now you have 'Daily Return' and 'Sentiment Score' in the same DataFrame
    # Perform the correlation analysis
    correlation = merged_df['Daily Return'].corr(merged_df['Sentiment Score'])
    return correlation, merged_df