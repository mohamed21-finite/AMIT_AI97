import pandas as pd 
from dash import Dash, html, dcc
import plotly.express as px


app = Dash(__name__)

df = pd.read_csv(r'C:\Users\DELL\Desktop\AI97\AMIT_AI97\src\project_dashboard\retail_dataset_realistic.csv')
df['date_cleaned'] = pd.to_datetime(df['date'])

revenue_by_region_data = df.groupby('region')['revenue'].sum().reset_index()

revenue_by_region_figure = px.bar(revenue_by_region_data, x='region', y='revenue', color='region')

revenue_by_category_data = df.groupby('category')['revenue'].sum().reset_index()
revenue_by_category_figure = px.pie(revenue_by_category_data, values='revenue', names='category')

price_vs_quantity_figure = px.scatter(df, x='price', y='quantity', color='category')

sales_trend_over_time_data = df.groupby('date')['revenue'].sum().reset_index()
sales_trend_over_time_figure = px.line(sales_trend_over_time_data, x='date', y='revenue')

sales_trend_by_month = df.groupby(df['date_cleaned'].dt.to_period('M'))['revenue'].sum().reset_index()
sales_trend_by_month['date_cleaned'] = sales_trend_by_month['date_cleaned'].astype(str)
sales_trend_by_month_figure = px.line(sales_trend_by_month, x='date_cleaned', y='revenue')

sales_by_region = px.scatter_geo(df, lat='latitude', lon='longitude', size='revenue', hover_name='region')

app.title = 'Retail Analysis Dashboard'
app.layout = html.Div([
    html.H1('Retail Analysis Dashboard'),
    html.Div([
        html.H2('Revenue by Region'),
        dcc.Graph(figure=revenue_by_region_figure)
    ]),
    html.Div([
        html.H2('Revenue by Category'),
        dcc.Graph(figure=revenue_by_category_figure)
    ]),
    html.Div([
        html.H2('Price vs Quantity'),
        dcc.Graph(figure=price_vs_quantity_figure)
    ]),
    html.Div([
        html.H2('Sales Trend Over Time'),
        dcc.Graph(figure=sales_trend_over_time_figure)
    ]),
    html.Div([
        html.H2('Sales Trend by Month'),
        dcc.Graph(figure=sales_trend_by_month_figure)
    ]),
    html.Div([
        html.H2('Sales by Region'),
        dcc.Graph(figure=sales_by_region)
    ])

])

app.run()