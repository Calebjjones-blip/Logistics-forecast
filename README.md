# Logistics Demand Forecasting Project

## Overview
This project analyzes retail sales data to forecast monthly demand using a 3-month moving average. It demonstrates core skills used in logistics and supply chain analytics roles.

## Tools Used
- Python
- Pandas (data cleaning and aggregation)
- Matplotlib (data visualization)

## Dataset
Retail sales data sourced from Kaggle containing 9,800+ orders across 4 years (2015-2019), including order dates, shipping details, product categories, and sales figures.

## What I Did
1. Loaded and cleaned the raw sales data
2. Converted order dates into a proper time format
3. Grouped individual orders into monthly sales totals
4. Applied a 3-month moving average to smooth volatility and reveal the demand trend
5. Visualized actual sales vs. the forecast on a time series chart

## Key Findings
- Overall demand grew significantly from 2015 to 2019
- Clear seasonal spikes appear at the end of each year, likely driven by holiday purchasing
- The moving average forecast smooths out noise and provides a reliable baseline for planning inventory and shipping capacity

## How to Run
1. Install dependencies: `pip install pandas matplotlib`
2. Run the script: `python forecast.py`