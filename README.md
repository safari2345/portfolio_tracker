## Portfolio Tracker Application 

This simple application calculates performance metrics of a custom portfolio against the S&P 500 benchmark, with visualization.

Features:
- Downloads historical daily closing prices for a predefined list of tickers
- Calculates weighted portfolio returns based on custom allocation percentages
- Computes key performance metrics:
  - Annualized return
  - Annualized volatility
  - Sharpe ratio
- Benchmarks portfolio performance against the S&P 500 (`^GSPC`)
- Visualizes cumulative growth of $1 invested in the portfolio vs. the S&P 500
- Displays the most recent raw price data in an interactive table

## Demo Portfolio

The prebuilt portfolio for the application (tickers and weights can be edited directly in the code):

| Ticker | Weight |
|--------|--------|
| GOOG   | 8%     |
| AMZN   | 8%     |
| AAPL   | 7%     |
| AVGO   | 9%     |
| CSCO   | 8%     |
| IBM    | 8%     |
| META   | 10%    |
| MSFT   | 9%     |
| NVDA   | 10%    |
| ORCL   | 8%     |
| PLTR   | 8%     |
| QCOM   | 7%     |

## Libraries used

- [Streamlit](https://streamlit.io/) — web app framework
- [yfinance](https://pypi.org/project/yfinance/) — Yahoo Finance market data
- [pandas](https://pandas.pydata.org/) / [NumPy](https://numpy.org/) — data processing
- [Matplotlib](https://matplotlib.org/) — charting

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/safari2345/portfolio_tracker.git
   cd portfolio_tracker
```
2. Install the dependencies:
```bash
   pip install streamlit yfinance pandas numpy matplotlib
```
## Usage

Run the app with Streamlit:
```bash
streamlit run portfolio_app.py
```
Then open the local URL shown in the terminal in your browser.

## Configuration

You can customize the app by editing the following variables at the top of the script:

- `portfolio` — dictionary of ticker symbols and their allocation weights
- `start_date` / `end_date` — the historical date range to analyze

## How It Works

1. Downloads adjusted closing prices for all portfolio tickers and the S&P 500 over the specified date range.
2. Drops any tickers with missing data to avoid calculation errors.
3. Calculates daily percentage returns, then combines them using the normalized portfolio weights.
4. Calculates cumulative growth of for both the portfolio and the benchmark.
5. Calculates annualized return, volatility, and Sharpe ratio for both.
6. Displays performance metrics, a comparison chart, and a data table using the streamlit library.

## Notes & Limitations

- Requires an internet connection to fetch live data from Yahoo Finance.
- The Sharpe ratio calculation assumes a risk-free rate of 0%. It is highly recommended to change it to a level like 3.5% as an approximation of a 3 month US treaury bill. The sharpe ratio was left at 0%, due to simplification, since the project's focus was benchmarking and portfolio construction and not precise risk-return measurement.
- It assumes the stocks were purchased in the same time period, without 


## License

This project was made for educational and personal purposes. Feel free to use and modify this project as you please.
