import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the data
df = pd.read_csv('src/daily_sales_data_all.csv')

# Define the function to update the chart
def update_chart(selected_region, selected_product):
    # Filter the data based on the selected region and product
    filtered_df = df
    if selected_region != 'all':
        filtered_df = filtered_df[filtered_df['region'] == selected_region]
    if selected_product != 'all':
        filtered_df = filtered_df[filtered_df['product'] == selected_product]

    # Create the line chart
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        color="region", 
        title=f"Sales Trend for {selected_product.capitalize()} in {selected_region.capitalize()} Region" if selected_region != 'all' and selected_product != 'all' else "Sales Trend"
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

    # Define regions and products for the radio button
    regions = ['all', 'north', 'east', 'south', 'west']
    products = ['all', 'pink morsel', 'gold morsel', 'magenta morsel', 'chartreuse morsel', 'periwinkle morsel', 'vermilion morsel', 'lapis morsel']

    # Layout of the Dash app with radio buttons and chart
    app.layout = html.Div(
        children=[
            html.H1(
                children='Sales Data Visualization',
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
            html.Div(
                children="Filter sales data by product:",
                style={'fontSize': '20px', 'marginTop': '30px', 'textAlign': 'center'}
            ),
            dcc.RadioItems(
                id='product-filter',
                options=[{'label': product.capitalize(), 'value': product} for product in products],
                value='all',
                style={'textAlign': 'center', 'margin': '30px'},
                labelStyle={'display': 'inline-block', 'marginRight': '20px', 'fontSize': '18px'}
            ),
            dcc.Graph(
                id='sales-trend-chart'
            ),
        ],
        style={'textAlign': 'center', 'color': '#1f77b4'}
    )

    # Define a single callback to update the chart based on both region and product selected
    @app.callback(
        Output('sales-trend-chart', 'figure'),
        [Input('region-filter', 'value'), Input('product-filter', 'value')]
    )
    def update_chart_callback(selected_region, selected_product):
        return update_chart(selected_region, selected_product)

    # Run the app
    app.run_server(debug=True)
