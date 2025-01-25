# Stock-Analysis

## Overview
This Python script analyzes stock data for a list of predefined tickers. It calculates key Simple Moving Averages (SMAs) and identifies stocks that meet specific conditions, such as being within a certain range of their 150-day SMA or showing "Golden Cross" or "Red Cross" patterns. The results are output in a tabular format.

## Features
* Stock Data Fetching:
- The script fetches historical stock price data for the past year using the Yahoo Finance API via the yfinance library.

* Key Calculations:
- Calculates the 50-day, 150-day, and 200-day Simple Moving Averages (SMAs) for each stock.
- Identifies stocks that:
    Are within 5% of their 150-day SMA.
    Have a rising 150-day SMA (i.e., steadily increasing over the last 10 days).
    Exhibit "Golden Cross" (50-day SMA crossing above 200-day SMA) or "Red Cross" (50-day SMA crossing below 200-day SMA)       patterns in the last 10 days.

* Result Formatting:
- Outputs the results in a structured DataFrame format for further analysis or display.

## Installation
Prerequisites: Ensure the following Python libraries are installed:
requests
yfinance
pandas
tabulate

## Usage
### Input

The script processes a predefined list of stock tickers:
tickers = ["ADBE", "AMD", "ABNB", "GOOGL", "GOOG", "AMZN", "AEP", "AMGN", "ADI", "ANSS",...]
You can customize this list by adding or removing stock tickers.

### Output

The script returns a table with stocks meeting specific criteria:
- The stock ticker.
- A label indicating its condition:
    - Gold Stock: Indicates a "Golden Cross."
    - Red Stock: Indicates a "Red Cross."

Example output:

+--------+-------------+
| Stock  | Label       |
+--------+-------------+
| AAPL   | Gold Stock  |
| MSFT   | Red Stock   |
+--------+-------------+


## Code Details

### Main Functionality

* Data Fetching:
- Historical stock data is fetched using yfinance for the past year to ensure sufficient data for SMA calculations.

* SMA Calculation:
- Three SMAs are calculated:
    SMA_50: 50-day SMA.
    SMA_150: 150-day SMA.
    SMA_200: 200-day SMA.
- Missing values (NaN) in the SMAs are handled using forward and backward filling (ffill and bfill).

* Condition Checks:
- Range Check: Stocks within 5% of the 150-day SMA.
- Rising SMA: The 150-day SMA is steadily increasing.
- Golden/Red Cross:
    - Golden Cross: SMA_50 crosses above SMA_200.
    - Red Cross: SMA_50 crosses below SMA_200.

* Output:
Results are stored in a DataFrame and displayed as a formatted table.

## Limitations
- Incomplete Data:
    If a stock lacks sufficient historical data, it is skipped.
- Hardcoded Tickers:
    The list of tickers is static and must be manually updated in the script.
- Processing Time:
    Analyzing a large number of tickers may take significant time due to API calls.


Potential Enhancements
Dynamic Ticker Input:
Allow users to input tickers via a file or command line.
Enhanced Analysis:
Add more technical indicators, such as RSI or MACD.
Visualization:
Provide graphical outputs, such as price charts with SMA overlays.
