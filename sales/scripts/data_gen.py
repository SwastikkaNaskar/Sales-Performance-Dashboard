import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Absolute path to save data
DATA_DIR = '/Users/swastikanaskar/Desktop/sales/data'
os.makedirs(DATA_DIR, exist_ok=True)

# Generate monthly sales data
months = pd.date_range(start="2023-01-01", periods=12, freq='MS')
products = ['Product A', 'Product B', 'Product C']
data = []

for month in months:
    for product in products:
        sales = np.random.randint(5000, 20000)
        data.append([month, product, sales])

sales_data = pd.DataFrame(data, columns=['Month', 'Product', 'Sales'])
sales_data.to_csv(f'{DATA_DIR}/sales_data.csv', index=False)

# Generate local sales data (daily)
start_date = datetime(2023, 1, 1)
local_data = []

for i in range(90):
    day = start_date + timedelta(days=i)
    city = np.random.choice(['New York', 'San Francisco', 'Los Angeles', 'Chicago'])
    local_sales = np.random.randint(200, 2000)
    local_data.append([day, city, local_sales])

local_sales_data = pd.DataFrame(local_data, columns=['Date', 'City', 'Local_Sales'])
local_sales_data.to_csv(f'{DATA_DIR}/local_sales_data.csv', index=False)

print(" Sample data created successfully!")
print(f"Files saved to: {DATA_DIR}")