import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def data_processing_func():
    # List of CSV files
    csv_files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']

    # Empty DataFrame to hold the concatenated data
    all_data = pd.DataFrame(columns=["product", "price", "quantity", "date", "region", "sales"])

    # Loop through each CSV file
    for file in csv_files:
        # Read each CSV file into a DataFrame
        df = pd.read_csv(file)

        # Calculate sales: Remove '$' and convert 'price' to float
        df['price'] = df['price'].str.replace('$', '').astype(float)
        df['sales'] = df['price'] * df['quantity']

        # Filter only necessary columns
        df = df[["product", "price", "quantity", "date", "region", "sales"]]

        # Append to the combined DataFrame
        all_data = pd.concat([all_data, df])

    # Write the final concatenated data to a new CSV file
    all_data.to_csv('src/daily_sales_data_all.csv', index=False)

# Call the data processing function
data_processing_func()
