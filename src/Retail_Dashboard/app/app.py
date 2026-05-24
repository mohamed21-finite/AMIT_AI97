import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px


FILE_PATH = r"C:\Users\DELL\Desktop\AI97\AMIT_AI97\src\Retail_Dashboard\datasets\retail_analytics_20k.csv"

df = pd.read_csv(FILE_PATH)

data =df.groupby('quarter')['profit_egp'].sum().reset_index()

fig = px.bar(data, x='quarter', y='profit_egp')

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Profit per Quarter'),
    dcc.Dropdown(
        id='dropdown_region',
        options=[
        {'label': r, 'value':r} for r in df['region'].unique()
    ],
    value=df['region'].unique()[0]),
    dcc.Graph(id='profit_per_region_fig',figure=fig),
    dcc.Interval(
        id='interval_component',
        interval=5000,
        n_intervals=0
    )
])


@app.callback(
        Output('profit_per_region_fig', 'figure'),
        Input('dropdown_region', 'value'),
        Input('interval_component', 'n_intervals')
)
def update_dashboard(selected_region, n_intervals):

    if selected_region == None:
        df = pd.read_csv(FILE_PATH)
        data =df.groupby('quarter')['profit_egp'].sum().reset_index()
        fig = px.bar(data, x='quarter', y='profit_egp')

    else:
        df = pd.read_csv(FILE_PATH)
        filtered_data = df[df['region'] == selected_region]
        profit_per_region = filtered_data.groupby('quarter')['profit_egp'].sum().reset_index()
        fig = px.bar(profit_per_region, x='quarter', y='profit_egp')
    
    return fig

app.run()