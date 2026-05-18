# 🏦 Consumer Banking Analytics Dashboard

A real-time financial data pipeline and interactive analytics dashboard
built to simulate enterprise-grade DART (Data, Analytics & Reporting)
workflows used in consumer banking environments.

## 🎯 Project Overview

This project automates the collection, storage, analysis, and visualization
of financial market data across major banking and payments institutions —
enabling data-backed decision making through an interactive dashboard.

## 🏗️ Architecture

Data Source (yfinance/NSE APIs)
↓
Python Pipeline (fetch + transform)
↓
SQLite Database (structured storage)
↓
SQL Analytics Layer (trends, volatility, gainers)
↓
Streamlit Dashboard (interactive visualization)
↓
Scheduler (automated daily refresh)

## ✨ Features

- 📥 Automated data ingestion for 10 banking & payments tickers
- 🗄️ Structured SQL storage with optimized queries
- 📊 Interactive dashboard with KPI cards, bar charts, trend lines
- 📈 Moving average analysis (7-day & 21-day MA)
- ⚡ Volatility & volume risk indicators
- 🔄 Daily scheduled pipeline refresh
- 🛡️ Error handling & retry logic for API failures

## 🛠️ Tech Stack

| Layer           | Technology         |
| --------------- | ------------------ |
| Data Ingestion  | Python, yfinance   |
| Storage         | SQLite, SQLAlchemy |
| Analysis        | Pandas, NumPy, SQL |
| Visualization   | Plotly, Streamlit  |
| Automation      | Schedule library   |
| Version Control | Git/GitHub         |

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

# Clone the repository

git clone https://github.com/yourusername/consumer-banking-analytics.git
cd consumer-banking-analytics

# Create virtual environment

python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows

# Install dependencies

pip install -r requirements.txt

### Run the Pipeline

python -m pipeline.store_data

### Launch Dashboard

streamlit run dashboard/app.py

### Run Automated Scheduler

python scheduler.py

## 📊 Dashboard Preview

[Dashboard Preview]
/dashboard-preview
.png files

## 🔍 SQL Analytics Implemented

- Latest closing prices across all tickers
- Top gainers by % change over 3-month window
- Volatility scoring via average daily high-low range
- Moving averages (7-day, 21-day) for trend detection
- Volume analysis for liquidity assessment

## 💡 Key Learnings

- Designed repeatable, serverless-style automation pipelines
- Implemented analytical SQL queries for financial insight generation
- Built stakeholder-ready dashboards from raw market data
- Applied data engineering principles to consumer banking context

## 📌 Future Enhancements

- Migrate to PostgreSQL for production scale
- Add AWS Lambda + S3 for cloud deployment
- Integrate real banking transaction datasets
- Add anomaly detection using ML models
