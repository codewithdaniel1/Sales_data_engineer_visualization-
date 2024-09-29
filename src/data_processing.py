import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def data_processing_func():
    # List of CSV files
    csv_files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']

    # Empty DataFrame to hold the concatenated data
    all_data = pd.DataFrame(columns=["product","price","quantity","date","region"])

    # Loop through each CSV file
    for file in csv_files:
        # Read each CSV file into a DataFrame
        df = pd.read_csv(file)

        # Filter for "PINK MORSELS" and calculate sales
        pink_morsels = df[df['product'] == 'pink morsel'].copy()
        pink_morsels['sales'] = pink_morsels['price'].str.replace('$', '').astype(float) * pink_morsels['quantity'].astype(float)

        # Select only the necessary columns
        pink_morsels = pink_morsels[['sales', 'date', 'region']]

    # Write the final concatenated data to a new CSV file
    pink_morsels.to_csv('daily_sales_data_all.csv', index=False)
