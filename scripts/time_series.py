import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from . import descriptive_stat

def analyze_publication_frequency_over_time(data, time_interval='D'):
   
    descriptive_stat.format_date(data)
    
    # Drop rows where 'date_parsed' could not be converted
    data = data.dropna(subset=['date_parsed'])

    # Group by the desired time interval
    frequency = data.groupby(pd.Grouper(key='date_parsed', freq=time_interval)).size().reset_index(name='Frequency')
    
    if time_interval == 'ME':
          # Format the date to show only Year-Month
        frequency['Month'] = frequency['date_parsed'].dt.to_period('M').astype(str)
        frequency = frequency[['Month','Frequency']]
    else:
        # Rename column for other intervals
        frequency = frequency.rename(columns={'date_parsed': 'Date'})
    

    # Filter out rows with zero frequency
    frequency = frequency[frequency['Frequency'] > 0]

   

    # Perform seasonal decomposition
    frequency.set_index('Date' if time_interval == 'D' else 'Month', inplace=True)
    decomposition = seasonal_decompose(frequency['Frequency'], model='additive', period=1)

    # Plotting the components
    plt.figure(figsize=(12, 8))
    plt.subplot(411)
    plt.plot(decomposition.observed, label='Original')
    plt.legend(loc='upper left')

    plt.subplot(412)
    plt.plot(decomposition.trend, label='Trend')
    plt.legend(loc='upper left')

    plt.subplot(413)
    plt.plot(decomposition.seasonal, label='Seasonal')
    plt.legend(loc='upper left')

    plt.subplot(414)
    plt.plot(decomposition.resid, label='Irregular')
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

    # Sort by frequency from highest to lowest for the table
    frequency = frequency.sort_values(by='Frequency', ascending=False)

    
    return frequency