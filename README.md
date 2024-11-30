# Investment Analysis Toolkit

## Overview
This project provides a comprehensive toolkit for analyzing stock market investments. It includes various analyses, visualizations, and statistical computations to gain insights into historical stock performance.

## Features
1. **Investment Growth Simulation**: Calculates the growth of an investment made in 2004 and visualizes the returns over time.
2. **Annual Traded Volume**: Analyzes and visualizes the annual trading volume.
3. **Volatility Analysis**: Includes annual average volatility and open-close differences for better market understanding.
4. **Moving Averages**: Computes 20-day and 50-day simple moving averages for trend analysis.
5. **Rolling Volatility**: Calculates 30-day rolling standard deviation to capture market fluctuations.
6. **Annualized Returns**: Computes the average annual return rate for the fund.
7. **Monthly Analysis**: Provides average close prices by month.
8. **Correlation Analysis**: Identifies relationships between key numerical variables, including a heatmap visualization.
9. **Drawdown Analysis**: Calculates maximum drawdown and visualizes the drawdown over time.
10. **Market Extremes**: Identifies the biggest single-day price crashes and climbs.
11. **Relative Strength Index (RSI)**: Computes the RSI to indicate overbought or oversold conditions.
12. **Golden Cross and Death Cross**: Detects bullish and bearish signals using SMA (50-day and 200-day).

## File Descriptions
- `main.py`: The main Python script that performs the analyses and generates visualizations.
- `IWM.csv`, `SPY.csv`, `VO.csv`: Historical stock data set files for analysis.

## Requirements
- Python 3.8 or above
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/investment-analysis.git
   cd investment-analysis
   ```
2. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Provide inputs for:
   - Company name
   - File path of the stock data (e.g., `IWM.csv`)

## Outputs
- Interactive visualizations such as line charts, bar charts, and heatmaps.
- Key insights printed in the console, including:
  - Investment growth
  - Annualized returns
  - RSI signals
  - Bullish and bearish market indicators

## Contributions
Feel free to fork the repository and submit pull requests for additional analyses or improvements.
