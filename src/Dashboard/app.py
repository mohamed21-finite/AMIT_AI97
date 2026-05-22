import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px


df = pd.read_csv(r'C:\Users\DELL\Desktop\AI97\AMIT_AI97\src\Dashboard\city_sustainability_geospatial.csv')

app = Dash(__name__)

population_vs_co2 = px.scatter(df, x="population_millions", y="co2_tons_per_capita", color='continent', size='avg_temp_c', hover_name='city',
hover_data=['renewable_energy_share', 'air_quality_index'])

pop_hist = px.histogram(df, x='population_millions', nbins=40, color='continent', marginal='box')


app.title = "City Sustainability Dashboard"
app.layout = html.Div([
    html.H1("Renewable Energy and CO2 Emissions in Global Cities"),
    dcc.Graph(figure=population_vs_co2),
    dcc.Graph(figure=pop_hist)
])

app.run()