import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('kaggleext.csv')

# Convert Order Date to a date format Python understands
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Group sales by month
df.set_index('Order Date', inplace=True)
monthly_sales = df['Sales'].resample('ME').sum()

# Calculate 3-month moving average (our forecast line)
moving_avg = monthly_sales.rolling(window=3).mean()

# Plot the chart
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales, label='Actual Monthly Sales', color='steelblue')
plt.plot(moving_avg, label='3-Month Moving Average (Forecast)', color='orange', linewidth=2)
plt.title('Logistics Demand Forecast')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.legend()
plt.tight_layout()
plt.savefig('demand_forecast.png', dpi=150, bbox_inches='tight')
plt.show()