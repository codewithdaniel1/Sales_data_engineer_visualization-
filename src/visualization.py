import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def visualization_func():
    # Load the data
    df = pd.read_csv('daily_sales_data_all.csv')

    # Initialize the Dash app
    app = dash.Dash(__name__)

    # Define regions for the radio button
    regions = ['all', 'north', 'east', 'south', 'west']

    # Layout of the Dash app with radio buttons and chart
    app.layout = html.Div(
        children=[
            html.H1(
                children='Pink Morsel Sales Data Visualization',
                style={'textAlign': 'center', 'color': '#1f77b4'}
            ),
            html.Div(
                children="Filter sales data by region:",
                style={'fontSize': '20px', 'marginTop': '20px', 'textAlign': 'center'}
            ),
            dcc.RadioItems(
                id='region-filter',
                options=[{'label': region.capitalize(), 'value': region} for region in regions],
                value='all',
                style={'textAlign': 'center', 'margin': '20px'},
                labelStyle={'display': 'inline-block', 'marginRight': '10px', 'fontSize': '18px'}
            ),
            dcc.Graph(
                id='sales-trend-chart'
            ),
        ],
        style={
            'width': '80%',
            'margin': 'auto',
            'padding': '20px',
            'fontFamily': 'Arial, sans-serif'
        }
    )

    # Define the callback to update the chart based on the region selected
    @app.callback(
        Output('sales-trend-chart', 'figure'),
        [Input('region-filter', 'value')]
    )
    def update_chart(selected_region):
        # Filter the data based on the selected region
        if selected_region == 'all':
            filtered_df = df
        else:
            filtered_df = df[df['region'] == selected_region]

        # Create the line chart
        fig = px.line(
            filtered_df, 
            x="date", 
            y="sales", 
            color="region", 
            title=f"Pink Morsel Sales Trend for {selected_region.capitalize()} Region" if selected_region != 'all' else "Pink Morsel Sales Trend for All Regions"
        )
        # Customize the layout of the chart
        fig.update_layout(
            title_font_size=24,
            title_x=0.5,
            xaxis_title="Date",
            yaxis_title="Sales ($)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=18),
        )

        return fig

    # Run the app
    app.run_server(debug=True)
