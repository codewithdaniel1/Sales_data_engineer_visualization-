import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the data
df = pd.read_csv('src/daily_sales_data_all.csv')

# Define the function that updates the chart (made standalone)
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

def visualization_func():
    # Initialize the Dash app
    app = dash.Dash(__name__)

    # Define regions for the radio button
    regions = ['all', 'north', 'east', 'south', 'west']

    # Layout of the Dash app with radio buttons and chart
    app.layout = html.Div(
        children=[
            html.H1(
                children='Pink Morsel Sales Data Visualization',
                id='app-title',  # Added id for the header
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
        style={'textAlign': 'center', 'color': '#1f77b4'}
    )

    # Define the callback to update the chart based on the region selected
    @app.callback(
        Output('sales-trend-chart', 'figure'),
        [Input('region-filter', 'value')]
    )
    def update_chart_callback(selected_region):
        return update_chart(selected_region)

    # Run the app
    app.run_server(debug=True)
