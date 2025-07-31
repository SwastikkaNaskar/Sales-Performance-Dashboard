import pandas as pd
import plotly.express as px
import plotly.io as pio
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sales_data_path = os.path.join(BASE_DIR, '../data/sales_data.csv')
local_sales_data_path = os.path.join(BASE_DIR, '../data/local_sales_data.csv')
output_html_path = os.path.join(BASE_DIR, '../outputs/dashboard.html')


sales_data = pd.read_csv(sales_data_path, parse_dates=['Month'])
local_sales_data = pd.read_csv(local_sales_data_path, parse_dates=['Date'])


monthly_sales = sales_data.groupby('Month')['Sales'].sum().reset_index()
product_sales = sales_data.groupby('Product')['Sales'].sum().reset_index()
city_sales = local_sales_data.groupby('City')['Local_Sales'].sum().reset_index()

fig1 = px.line(monthly_sales, x='Month', y='Sales', title='Monthly Sales')
fig2 = px.bar(product_sales, x='Product', y='Sales', title='Product-wise Sales')
fig3 = px.pie(city_sales, names='City', values='Local_Sales', title='City-wise Local Sales')


with open(output_html_path, 'w') as f:
    f.write("<html><head><title>Sales Dashboard</title></head><body>")
    for fig in [fig1, fig2, fig3]:
        inner_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
        f.write(inner_html)
    f.write("</body></html>")

print(f" Dashboard saved to: {output_html_path}")