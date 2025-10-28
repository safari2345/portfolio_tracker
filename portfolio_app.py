import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#początek strony streamlit
st.set_page_config(page_title="Portfolio Tracker", layout="wide")

st.title("My Portfolio Tracker")


#Lista aktywów
portfolio = {
    'GOOG': 0.08,
    'AMZN': 0.08,
    'AAPL': 0.07,
    'AVGO': 0.09,
    'CSCO': 0.08,
    'IBM': 0.08,
    'META': 0.10,
    'MSFT': 0.09,
    'NVDA': 0.10,
    'ORCL': 0.08,
    'PLTR': 0.08,
    'QCOM': 0.07
}

start_date = '2020-01-01'
end_date = '2025-10-01'

#wczytywanie danych
st.write("Gathering Data")

tickers = list(portfolio.keys())
try:
    data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True, progress=False)['Close']
except Exception as e:
    st.error(f"Failed to download the stock data{e}")
    st.stop()

#jeśli błąd
data = data.dropna(axis=1, how='any')
if data.empty:
    st.error("Error no ticker downloaded")
    st.stop()

# Wycena portfela
returns = data.pct_change().dropna()

# Waga aktywów
valid_tickers = [t for t in portfolio.keys() if t in data.columns]
weights = np.array([portfolio[t] for t in valid_tickers])


weights = weights / weights.sum()

# zysk/strata portfela
portfolio_returns = (returns[valid_tickers] * weights).sum(axis=1)
portfolio_value = (1 + portfolio_returns).cumprod()


# Wczytaj S&P 500
try:
    benchmark = yf.download('^GSPC', start=start_date, end=end_date, auto_adjust=True, progress=False)['Close']
except Exception as e:
    st.error(f"Failed to download data{e}")
    st.stop()

benchmark_returns = benchmark.pct_change().dropna()
benchmark_value = (1 + benchmark_returns).cumprod()

#Dane o ryzyku i zmienności
def portfolio_metrics(returns: pd.Series):
    if isinstance(returns, pd.DataFrame):
        returns = returns.squeeze()

    mean_return = returns.mean() * 252
    volatility = returns.std() * np.sqrt(252)
    sharpe_ratio = mean_return / volatility if volatility != 0 else np.nan
    return float(mean_return), float(volatility), float(sharpe_ratio)

mean_ret, vol, sharpe = portfolio_metrics(portfolio_returns)
bench_ret, bench_vol, bench_sharpe = portfolio_metrics(benchmark_returns)

# UI danych
st.subheader("Portfolio Performance Data")
col1, col2 = st.columns(2)

with col1:
    st.metric("Annual Return", f"{mean_ret:.2%}")
    st.metric("Volatility", f"{vol:.2%}")
    st.metric("Sharpe Ratio", f"{sharpe:.2f}")

with col2:
    st.metric("S&P 500 Return", f"{bench_ret:.2%}")
    st.metric("S&P 500 Volatility", f"{bench_vol:.2%}")
    st.metric("S&P 500 Sharpe", f"{bench_sharpe:.2f}")

# graf SP 500 i portfela

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(portfolio_value, label="My Portfolio", linewidth=2)
ax.plot(benchmark_value / benchmark_value.iloc[0], label="S&P 500", linestyle='--')
ax.set_title("Portfolio Growth per $1")
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.legend()
st.pyplot(fig)

#dokładne dane portfela
st.subheader("Portfolio Data ")
st.dataframe(data.tail())


