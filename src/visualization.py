import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

def visualization_func():
    # Load the data
    df = pd.read_csv('daily_sales_data_all.csv')

    # Initialize the Dash app
    app = dash.Dash(__name__)

    # Create a line chart of sales over time, separated by region
    fig = px.line(df, x="date", y="sales", color="region", title="Pink Morsel Sales Trend by Region")

    # Layout of the Dash app
    app.layout = html.Div(children=[
        html.H1(children='Sales Data Visualization'),

        dcc.Graph(
            id='sales-trend-chart',
            figure=fig
        )
    ])

    # Run the app
    app.run_server(debug=True)

