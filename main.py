# Importing the necessary libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Getting input for file location and company name
c_name = input("Enter the name of the company: ")
File = input("Enter the file address along with file name in pd.read_csv format: ")

# Data Reading
df = pd.read_csv(File)

print(df.shape)
print(df.isnull().sum())
print(df.isna().sum())

# Checking for duplicate rows in the dataset
df_dupplicates = df[df.duplicated()]
df_dupplicates.count()

# ANALYSIS

# 1) Investment returns if you invested 100 rupees in the stock in year 2004

df['Date'] = pd.to_datetime(df['Date'])
data = df[df['Date'].dt.year >= 2004]


start_price = data['Adj Close'].iloc[0]
end_price = data['Adj Close'].iloc[-1]

# method to Scale down to an initial investment of 100 rupees
# Create a copy of the DataFrame
data = data.copy()

initial_investment = 100
final_value = (end_price / start_price) * initial_investment

data['Scaled Investment'] = (data['Adj Close'] / start_price) * initial_investment

# Calculating the percentage return
percentage_return = ((final_value / initial_investment) - 1) * 100

# Calculating scaled investment over time
data['Scaled Investment'] = (data['Adj Close'] / start_price) * initial_investment

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Scaled Investment'], label='Investment Growth (Initial ₹100)', color='purple')
plt.title('Investment Growth Over Time for ' + str(c_name), fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Investment Value (₹)', fontsize=12)

print(f"Final Return for {c_name}: {final_value}")
print(f"Percentage Return for {c_name}: {percentage_return} %")

# 2) Annual traded volume for the fund

data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
annual_volume = data.groupby('Year')['Volume'].sum()

plt.figure(figsize=(12, 6))
annual_volume.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Annual Traded Volume for ' + str(c_name), fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Volume (in shares)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 3) Annual average volatality including annual average open-close difference of the fund

data['Open-Close Difference'] = data['Close'] - data['Open']

# Calculate daily percentage volatility
data['Volatility (%)'] = ((data['High'] - data['Low']) / data['Open']) * 100

annual_volatility_analysis = data.groupby('Year').agg(Avg_Open_Close_Difference=('Open-Close Difference', 'mean'),Avg_Volatility_Percent=('Volatility (%)', 'mean')).reset_index()

# To plot average volatility over years
plt.figure(figsize=(12, 6))
plt.plot(annual_volatility_analysis['Year'], annual_volatility_analysis['Avg_Volatility_Percent'], marker='o', label='Avg Volatility (%)')
plt.title('Annual Average Volatility (%) for ' + str(c_name), fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Volatility (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

# To plot average open-close difference over years
plt.figure(figsize=(12, 6))
plt.plot(annual_volatility_analysis['Year'], annual_volatility_analysis['Avg_Open_Close_Difference'], marker='o', label='Avg Open-Close Difference', color='pink')
plt.title('Annual Average Open-Close Difference for ' + str(c_name), fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Open-Close Difference', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

# Display the annual volatility analysis table
# tools.display_dataframe_to_user(name="Annual Volatility and Open-Close Difference Analysis", dataframe=annual_volatility_analysis)

# 4) Calculate 20-day and 50-day simple moving averages

# Calculate 20-day and 50-day simple moving averages
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['Date'], data['SMA_20'], label='SMA 20', linestyle='--')
plt.plot(data['Date'], data['SMA_50'], label='SMA 50', linestyle='--')
plt.title('Moving Averages (20-day and 50-day) for ' + str(c_name))
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.show()

# 5) Calculate 30-day rolling standard deviation as volatility

data['Rolling Volatility'] = data['Close'].rolling(window=30).std()

# Plot Rolling Volatility
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Rolling Volatility'], label='30-Day Rolling Volatility')
plt.title('30-Day Rolling Volatility for ' + str(c_name))
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

# 6) Average annual return rate

# Calculate daily percentage change
data['Daily Return (%)'] = data['Close'].pct_change() * 100

# Calculate annualized return
annualized_return = (1 + data['Daily Return (%)'].mean()/100)**252 - 1
print(f"Annualized Return for {c_name}: {annualized_return * 100:.2f}%")

# 7) Average Close Price by Months respectively

data['Month'] = data['Date'].dt.month
monthly_avg = data.groupby('Month')['Close'].mean()

monthly_avg.plot(kind='bar', figsize=(12, 6), color = 'yellow')
plt.title('Average Close Price by Month for ' + str(c_name))
plt.xlabel('Month')
plt.ylabel('Average Close Price')
plt.tight_layout()
plt.show()

# 8) Calculating correlation between Volume and Close price

correlation = data['Volume'].corr(data['Close'])
f"Correlation between Volume and Close Price for {c_name}: {correlation:.2f}"

# 9) Correlation matrix for numerical columns

correlation_matrix = data[['Open', 'High', 'Low', 'Close', 'Volume']].corr()

# Plotting correlation heatmap

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for ' + str(c_name))
plt.tight_layout()
plt.show()

# 10) Calculating Drawdown for the fund

data['Cumulative Return'] = (1 + data['Daily Return (%)']/100).cumprod()
data['Drawdown'] = data['Cumulative Return'] / data['Cumulative Return'].cummax() - 1

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Drawdown'], label='Drawdown', color='orange')
plt.title('Maximum Drawdown for ' + str(c_name))
plt.xlabel('Date')
plt.ylabel('Drawdown')
plt.tight_layout()
plt.show()

# 11) Calculate biggest crash and climb

data['Daily Return (%)'] = data['Close'].pct_change() * 100

# Find the day with the biggest crash
biggest_crash = data.loc[data['Daily Return (%)'].idxmin()]

# Find the day with the biggest climb
biggest_climb = data.loc[data['Daily Return (%)'].idxmax()]

print(f"Biggest One-Day Crash for {c_name}:")
print(biggest_crash[['Date', 'Daily Return (%)', 'Close']])

print(f"\nBiggest One-Day Climb for {c_name}:")
print(biggest_climb[['Date', 'Daily Return (%)', 'Close']])

# 12) Relative Strength Index

delta = data['Close'].diff()

gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()

data['RSI'] = 100 - (100 / (1 + avg_gain / avg_loss))

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['RSI'], label='RSI (14-Day)', color='violet')
plt.axhline(70, color='red', linestyle='--', label='Overbought')
plt.axhline(30, color='green', linestyle='--', label='Oversold')
plt.title('Relative Strength Index (RSI) for ' + str(c_name))
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend()
plt.tight_layout()
plt.show()

# 13) Identifying Bullish and Bearish Signals respectively

# Calculating moving averages
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# Identifying crossover points
data['Golden Cross'] = (data['SMA_50'] > data['SMA_200']) & (data['SMA_50'].shift(1) <= data['SMA_200'].shift(1))
data['Death Cross'] = (data['SMA_50'] < data['SMA_200']) & (data['SMA_50'].shift(1) >= data['SMA_200'].shift(1))

golden_crosses = data[data['Golden Cross']]
death_crosses = data[data['Death Cross']]

print(f"Golden Crosses (Bullish Signals) for {c_name}:")
print(golden_crosses[['Date', 'Close']])

print(f"\nDeath Crosses (Bearish Signals) for {c_name}:")
print(death_crosses[['Date', 'Close']])
