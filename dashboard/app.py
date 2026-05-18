import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from analysis.queries import (
    get_latest_prices,
    get_top_gainers,
    get_volatility,
    get_moving_average,
    get_price_trends
)

st.set_page_config(
    page_title="Consumer Banking Analytics",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Consumer Banking Analytics Dashboard")
st.caption("Real-time financial data pipeline — inspired by enterprise DART reporting systems")

# ── Row 1: KPI Cards ──────────────────────────────────────
latest = get_latest_prices()
gainers = get_top_gainers()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Tickers Tracked", len(latest))
col2.metric("Top Gainer", gainers.iloc[0]["ticker"], f"+{gainers.iloc[0]['pct_gain']}%")
col3.metric("Highest Price", f"${latest.iloc[0]['close']:.2f}", latest.iloc[0]["ticker"])
col4.metric("Most Volume", latest.loc[latest['volume'].idxmax()]['ticker'])

st.divider()

# ── Row 2: Latest Prices + Top Gainers ───────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Latest Closing Prices")
    fig = px.bar(latest, x="ticker", y="close", color="close",
                 color_continuous_scale="blues", title="Closing Price by Ticker")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🚀 Top Gainers (3 Months)")
    fig2 = px.bar(gainers, x="ticker", y="pct_gain", color="pct_gain",
                  color_continuous_scale="greens", title="% Gain Over 3 Months")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ── Row 3: Price Trend + Moving Average ──────────────────
st.subheader("📈 Price Trend & Moving Averages")

tickers = latest["ticker"].tolist()
selected = st.selectbox("Select a ticker", tickers)

ma_df = get_moving_average(selected)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=ma_df["date"], y=ma_df["close"], name="Close Price", line=dict(color="royalblue")))
fig3.add_trace(go.Scatter(x=ma_df["date"], y=ma_df["MA_7"], name="7-Day MA", line=dict(color="orange", dash="dash")))
fig3.add_trace(go.Scatter(x=ma_df["date"], y=ma_df["MA_21"], name="21-Day MA", line=dict(color="red", dash="dot")))
fig3.update_layout(title=f"{selected} — Price Trend & Moving Averages", xaxis_title="Date", yaxis_title="Price (USD)")
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ── Row 4: Volatility Table ───────────────────────────────
st.subheader("⚡ Volatility & Volume Analysis")
vol_df = get_volatility()
st.dataframe(vol_df, use_container_width=True)