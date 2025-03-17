# Stock Data Downloader

This Python script allows you to download historical stock data for multiple tickers from Yahoo Finance using the yfinance library.

## Features

- Download historical stock data for multiple tickers
- Specify custom date ranges
- Output includes: Date, Ticker, Open, Close, Volume, High, and Low
- Data is saved to a CSV file

## Installation

1. Ensure you have Python 3.6 or later installed on your system.

2. Install the required libraries:

`pip install yfinance pandas`

3. Download the `stock_downloader.py` script to your local machine.

## Usage

Run the script from the command line with the following syntax:

python stock_downloader.py TICKER1 TICKER2 ... TICKERN START_DATE END_DATE

- TICKER1, TICKER2, etc.: Stock ticker symbols (e.g., AAPL, MSFT, GOOGL)
- START_DATE: Start date for data collection (format: YYYY-MM-DD)
- END_DATE: End date for data collection (format: YYYY-MM-DD)

Example:

python stock_downloader.py AAPL MSFT GOOGL 2024-01-01 2025-03-16

This command will download data for Apple, Microsoft, and Google stocks from January 1, 2024, to March 16, 2025.

## Output

- The script will display a preview of the data in the console.
- A CSV file named `stock_data_START_DATE_END_DATE.csv` will be created in the same directory as the script.
