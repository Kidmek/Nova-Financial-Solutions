# Nova Financial Solutions

## Overview

**Nova Financial Solutions** is a data-driven project aimed at analyzing the impact of news sentiment on stock price movements. The project involves two main tasks:

1. **Sentiment Analysis**: Perform sentiment analysis on the `headline` text to quantify the tone and sentiment expressed in financial news. This analysis uses natural language processing (NLP) techniques to derive sentiment scores, which are then associated with the respective `Stock Symbol` to understand the emotional context surrounding stock-related news.

2. **Correlation Analysis**: Establish statistical correlations between the sentiment derived from news articles and the corresponding stock price movements. This involves tracking stock price changes around the date the article was published and analyzing the impact of news sentiment on stock performance. The analysis considers the publication date and potentially the time the article was published if such data is available.

## Project Structure

The project is organized into four branches:

- **`main`**: Contains the final merged code from all tasks.
- **`task-1`**: Handles the initial data analysis, including descriptive statistics and time series analysis.
- **`task-2`**: Focuses on quantitative analysis related to stock price movements.
- **`task-3`**: Implements correlation analysis between news sentiment and stock price movements.

### Folder Structure

- **`notebooks/`**: Contains Jupyter notebooks with analytical outputs for specific tasks:
  - `correlation.ipynb`: (Task-3) Correlation analysis.
  - `descriptive_stat.ipynb`: (Task-1) Descriptive statistics.
  - `publisher_analysis.ipynb`: (Task-1) Analysis of article publishers.
  - `quantitative_analysis.ipynb`: (Task-2) Quantitative stock analysis.
  - `text_analysis.ipynb`: (Task-1) Sentiment analysis of headlines.
  - `time_series.ipynb`: (Task-1) Time series analysis of stock prices.

- **`scripts/`**: Contains Python scripts that execute the core functionalities of the project. These scripts are imported into the Jupyter notebooks and are designed to be reloaded using the `importlib.reload()` function to reflect any code changes without restarting the notebook kernel.

## Getting Started

### Prerequisites

Make sure you have Python installed. All required Python libraries are listed in the `requirements.txt` file. Install them using the following command:

```bash
pip install -r requirements.txt

## Setting Up the Project

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/Nova-Financial-Solutions.git
   cd Nova-Financial-Solutions

2. **Install the Required Libraries**:

   ```bash
   pip install -r requirements.txt

3. **Add Data Files**:

   - `notebooks/`: Contains Jupyter notebooks for analyzing and visualizing data.
     - `correlation.ipynb` (Task-3)
     - `descriptive_stat.ipynb` (Task-1)
     - `publisher_analysis.ipynb` (Task-1)
     - `quantitative_analysis.ipynb` (Task-2)
     - `text_analysis.ipynb` (Task-1)
     - `time_series.ipynb` (Task-1)
   - `scripts/`: Contains Python scripts that perform data processing and analysis.
   - `Data/`: Directory for data files.
     - `raw_analyst/`: Folder for raw analyst data CSV files.
     - `yfinance_data/`: Folder for Yahoo Finance data CSV files.
