import yfinance as yf
import pandas as pd
import argparse
from datetime import datetime

def download_stock_data(tickers, start_date, end_date):
    data_frames = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        data = data.reset_index()
        data['Date'] = data['Date'].dt.date  # Convert to date only
        data['Ticker'] = ticker
        selected_data = data[['Date', 'Ticker', 'Open', 'Close', 'Volume', 'High', 'Low']]
        data_frames.append(selected_data)

    return pd.concat(data_frames, ignore_index=True)

def valid_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date format. Use YYYY-MM-DD")

parser = argparse.ArgumentParser(description="Download historical stock data")
parser.add_argument("tickers", nargs="+", help="Stock ticker symbols")
parser.add_argument("start_date", type=valid_date, help="Start date (YYYY-MM-DD)")
parser.add_argument("end_date", type=valid_date, help="End date (YYYY-MM-DD)")

args = parser.parse_args()

df = download_stock_data(args.tickers, args.start_date, args.end_date)

output_file = f"stock_data_{args.start_date}_{args.end_date}.csv"
df.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")
