import pandas as pd
import matplotlib.pyplot as plt

def format_date(data):
    # Simplify the date strings by removing timezone information
    def simplify_date(date_str):
        if pd.isna(date_str):
            return date_str
        # Remove timezone info if present
        data_arr= date_str.split(' ')
        data_arr[1] = data_arr[1].split('-')[0]
        return data_arr[0] + ' ' + data_arr[1]
        

    # Apply the simplification function
    data['date'] = data['date'].apply(simplify_date)

    # Define the simplified date format
    simplified_date_format = "%Y-%m-%d %H:%M:%S"

    # Parse the simplified date format
    data['date_parsed'] = pd.to_datetime(data['date'], format=simplified_date_format, errors='coerce')

    # Check for any rows that couldn't be parsed
    if data['date_parsed'].isna().any():
        print("Some dates could not be parsed:")
        print(data[data['date_parsed'].isna()])

    return data

def basic_stats(original_data):
    data = original_data.copy()
    data['headline_length'] = data['headline'].apply(len)
    headline_stats = data['headline_length'].describe()
    headline_stats_formatted = headline_stats.apply(lambda x: f"{int(x)} chars")
    return pd.DataFrame({
        'Stat': headline_stats_formatted.index,
        'Value': headline_stats_formatted.values})

def articles_per_publisher(original_data):
    data = original_data.copy()
    publisher_counts = data['publisher'].value_counts()
    publisher_counts_df = pd.DataFrame({'Publisher': publisher_counts.index, 'Article Count': publisher_counts.values})
    return publisher_counts_df

def pub_date_analysis(original_data):
    # Copy the data to avoid modifying the original DataFrame
    data = original_data.copy()
    
    format_date(data)
    
    # Extract day of the week and month
    data['day_of_week'] = data['date_parsed'].dt.day_name()
    data['month'] = data['date_parsed'].dt.to_period('M')
    

    # Articles published by day of the week
    day_counts = data['day_of_week'].value_counts().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    day_counts_df = pd.DataFrame({'Day of week': day_counts.index, 'Article Count': day_counts.values})
    print(day_counts_df)

    # Plot articles per day of the week
    plt.figure(figsize=(10, 6))
    day_counts.plot(kind='bar')
    plt.title('Number of Articles per Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Articles')
    plt.show()

    # Articles published by month
    monthly_counts = data['month'].value_counts().sort_index()

    monthly_counts_df = pd.DataFrame({'Month': monthly_counts.index, 'Article Count': monthly_counts.values})
    print(monthly_counts_df)

    # Plot articles per month
    plt.figure(figsize=(10, 6))
    monthly_counts.plot(kind='line')
    plt.title('Number of Articles per Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Articles')
    plt.show()

    return