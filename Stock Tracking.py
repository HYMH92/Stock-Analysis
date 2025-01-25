import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from tabulate import tabulate

# nasdaq100:

tickers = [
    "ADBE", "AMD", "ABNB", "GOOGL", "GOOG", "AMZN", "AEP", "AMGN", "ADI", "ANSS",
    "AAPL", "AMAT", "APP", "ARM", "ASML", "AZN", "TEAM", "ADSK", "ADP", "AXON",
    "BKR", "BIIB", "BKNG", "AVGO", "CDNS", "CDW", "CHTR", "CHKP", "CTAS", "CSCO",
    "CTSH", "CMCSA", "CEG", "CPRT", "COST", "CRWD", "DDOG", "DXCM", "DOCU", "DLTR",
    "EA", "ENPH", "EXC", "EXPE", "FAST", "FTNT", "GILD", "HON", "ILMN", "INTC",
    "INTU", "ISRG", "JD", "KDP", "KLAC", "LRCX", "LCID", "LULU", "MRVL", "MTCH",
    "META", "MCHP", "MU", "MSFT", "MRNA", "MDLZ", "NTES", "NFLX", "NVDA", "NXPI",
    "OKTA", "ODFL", "ON", "ORLY", "PANW", "PAYX", "PYPL", "PDD", "PEP", "QCOM",
    "REGN", "ROP", "ROST", "SBUX", "SNPS", "TTWO", "TMUS", "TSLA", "TXN", "TTD",
    "VRSK", "VRTX", "WBD", "WDAY", "XEL", "ZS"
]




def get_stock_analysis(tickers):
    results = []
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)  # Ensure enough data for SMA calculations

    for ticker in tickers:
        # Fetch historical data
        data = yf.download(ticker, start=start_date, end=end_date)

        if data.empty:
            print(f"No data found for {ticker}")
            continue

        # Calculate SMAs
        data['SMA_50'] = data['Close'].rolling(window=50).mean()
        data['SMA_150'] = data['Close'].rolling(window=150).mean()
        data['SMA_200'] = data['Close'].rolling(window=200).mean()

        # Handle NaN values by filling forward and backward
        data['SMA_150'] = data['SMA_150'].ffill().bfill()
        data['SMA_50'] = data['SMA_50'].ffill().bfill()
        data['SMA_200'] = data['SMA_200'].ffill().bfill()

        # Get the most recent values
        try:
            latest_price = data['Close'].iloc[-1]  # Latest stock price
            latest_sma_50 = data['SMA_50'].iloc[-1]  # 50-day SMA
            latest_sma_150 = data['SMA_150'].iloc[-1]  # 150-day SMA
            latest_sma_200 = data['SMA_200'].iloc[-1]  # 200-day SMA
            
            
            # Check if stock is within 5% range of SMA_150
            if ((latest_sma_150 <= latest_price) & (latest_price <= 1.05 * latest_sma_150)).bool():
            
            # Check if the 150-day SMA is rising
                is_rising_150 = (
                data['SMA_150'].iloc[-1] > data['SMA_150'].iloc[-2] and
                data['SMA_150'].iloc[-2] > data['SMA_150'].iloc[-10]
            )

                if is_rising_150:
                    # Check for "Gold Stock" or "Red Stock" criteria

                    recent_data = data.tail(10)

                    crossed_gold = (
                        ((recent_data['SMA_50'] > recent_data['SMA_200']) &
                            (recent_data['SMA_50'].shift(1) <= recent_data['SMA_200'].shift(1))).any()
                    )
                    crossed_red = (
                        ((recent_data['SMA_50'] < recent_data['SMA_200']) &
                            (recent_data['SMA_50'].shift(1) >= recent_data['SMA_200'].shift(1))).any()
                    )

                    stock_label = ''
                    if crossed_gold:
                        stock_label = 'Gold Stock'
                    elif crossed_red:
                        stock_label = 'Red Stock'

                    results.append({'Stock': ticker, 'Label': stock_label})
                


        except IndexError:
            print(f"Not enough data for {ticker}. Skipping...")

    # Create and return a DataFrame from the results
    return pd.DataFrame(results)


result_df = get_stock_analysis(tickers)

# convert the lists in the 'fruits' column into strings
print(tabulate(result_df, headers='keys', tablefmt='grid'))
