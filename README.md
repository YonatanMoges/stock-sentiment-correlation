# Stock Sentiment Correlation

**Analyzing the correlation between financial news sentiment and daily stock returns for major tech companies.**

## Author
Yonatan Moges

## Overview
This project investigates the relationship between daily stock returns and financial news sentiment for seven major technology stocks: **AAPL**, **AMZN**, **GOOG**, **META**, **MSFT**, **NVDA**, and **TSLA**. The goal is to assess whether news sentiment scores have a measurable impact on short-term stock performance using correlation analysis.

## Project Structure
- `data/`: Historical stock prices and sentiment datasets.
- `notebooks/`: Jupyter notebooks for analysis and visualization.
- `scripts/`: Code for data processing and computations.

## Objectives
- Load and preprocess stock and sentiment data.
- Compute daily stock returns.
- Aggregate daily news sentiment.
- Calculate Pearson correlation coefficients between returns and sentiment.

## Data Sources
- **Stock Data**: Historical prices for selected tech stocks.
- **News Sentiment**: Labeled sentiment scores from a dataset provided by 10 Academy.

## Methodology
1. **Preprocessing**
   - Convert date columns to `datetime` objects.
   - Align dataframes based on date ranges.

2. **Analysis**
   - Calculate daily returns for each stock.
   - Aggregate sentiment scores by day.
   - Use Pearson correlation to assess relationships.

## Results

| Ticker | Correlation |
|--------|-------------|
| AAPL   | 0.106       |
| AMZN   | 0.042       |
| GOOG   | 0.073       |
| META   | 0.094       |
| MSFT   | 0.088       |
| NVDA   | 0.034       |
| TSLA   | 0.060       |

- All results show **weak positive correlations**, suggesting that news sentiment has limited predictive power for daily stock returns.

## Interpretation
- The sentiment scores do not strongly correlate with next-day stock movements.
- Market dynamics may be influenced more heavily by macroeconomic events, investor behavior, and other financial metrics.

## Future Work
- Improve sentiment scoring using advanced NLP techniques (e.g., transformer-based models).
- Expand the dataset with more companies or sectors.
- Incorporate additional features (e.g., trading volume, volatility).
- Run experiments over longer time periods to explore long-term patterns.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/YonatanMoges/stock-sentiment-correlation.git
   cd stock-sentiment-correlation
   ```
2. Set up a Python environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebooks in the notebooks/ directory to replicate the analysis.
   
