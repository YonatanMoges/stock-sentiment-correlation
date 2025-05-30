# Correlation Analysis between Stock Returns and News Sentiment

## Author
Yonatan Moges

## Overview
This project explores the relationship between daily stock returns and news sentiment for seven major technology stocks: **AAPL**, **AMZN**, **GOOG**, **META**, **MSFT**, **NVDA**, and **TSLA**. The analysis aims to determine whether news sentiment has any significant linear correlation with stock performance.

## Project Structure
- `data/`: Contains the historical stock prices and news sentiment datasets.
- `notebooks/`: Jupyter notebooks for data loading, analysis, and visualization.
- `scripts/`: Python scripts used for data preprocessing and correlation computation.

## Objectives
- Load and preprocess historical stock price and news sentiment data.
- Calculate daily stock returns.
- Perform sentiment analysis on news articles.
- Compute the Pearson correlation coefficient between stock returns and sentiment scores.

## Data Sources
- **Stock Data**: Historical price data for the selected companies.
- **News Data**: Sentiment scores derived from a corpus of financial news articles provided by 10 Academy.

## Methodology
1. **Data Loading & Cleaning**
   - Convert date columns to datetime format.
   - Align stock and news data to the same date range.
2. **Analysis**
   - Compute daily stock returns.
   - Aggregate average daily sentiment scores.
   - Calculate Pearson correlation coefficients for each stock.

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

- All correlations are weak and positive, suggesting minimal influence of sentiment on returns.

## Interpretation
- The weak correlations imply that daily news sentiment, as captured in this dataset, has limited predictive power for daily stock returns.
- This could be due to market complexity, sentiment analysis limitations, or external economic factors.

## Future Work
- Implement more advanced NLP techniques for better sentiment scoring.
- Extend analysis to different sectors or a broader range of stocks.
- Incorporate additional financial indicators (e.g., volume, volatility).
- Conduct a longitudinal study over a longer time period.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/YonatanMoges/financial-news-dataset.git
   cd financial-news-dataset
   ```
2. Set up a Python environment and install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Run the Jupyter notebooks in the notebooks/ directory to replicate the analysis.
   
