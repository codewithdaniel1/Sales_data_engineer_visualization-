# Sales Data Engineering and Visualization

## Introduction

This project is designed to analyze and visualize sales data for Pink Morsels. By providing a user-friendly dashboard, stakeholders can easily filter through the sales data by region and understand trends over time. The tool ensures that sales performance is clearly visualized, helping in decision-making and identifying key regional sales patterns.

## Overview

This project is a data visualization and analysis tool for Pink Morsel sales data across different regions. It allows users to filter and visualize sales trends using interactive dashboards built with Dash and Plotly. The project includes:

1. **Data Processing:** 
   - Aggregating and cleaning raw sales data using custom Python scripts to ensure the data is ready for analysis.
   - Handling missing values, filtering irrelevant data, and converting data types where necessary to maintain data integrity.
   - Utilizing efficient ETL (Extract, Transform, Load) techniques to optimize data flow and ensure smooth transitions between different stages of the pipeline.

2. **Data Visualization:** 
   - An interactive Dash application that allows users to filter sales data by region (North, East, South, West, or All) through a dynamic radio button interface.
   - Visualizing trends over time with line charts that dynamically adjust based on the selected region, providing insights into region-specific performance.
   - Utilizing Plotly's rich visualization capabilities to enhance data interpretation with interactive features like zooming, hovering, and tooltips.
   - Custom CSS styles applied to enhance the user interface, making the dashboard both functional and visually appealing.

3. **Test Suite:**
   - A comprehensive test suite built using Dash’s testing framework to ensure the correctness and reliability of the app.
   - Tests include verifying the presence of key UI components (header, region picker, and visualizations) and checking that the callback functions work as expected.

## Features

- **Sales Data Filtering:** A radio button interface lets users filter sales data by specific regions: North, East, South, West, or All.
- **Interactive Visualizations:** The app provides an interactive line chart showing the sales trends of Pink Morsel over time, with customization options based on region.
- **Custom Styling:** The Dash app includes basic CSS to enhance visual appeal, such as centralized text and color styling.
- **Testing Suite:** A Pytest-based testing suite ensures the application works as expected, with tests for the presence of core components and callback functionality.

This tool aims to simplify the process of analyzing and interpreting sales data, making it easy for stakeholders to gain insights into trends and patterns across different regions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/codewithdaniel1/Sales_data_engineer_visualization.git
    ```

2. Navigate into the project directory:
    ```bash
    cd Sales_data_engineer_visualization
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
    ```bash
    python src/main.py
    ```


## Usage

1. Start the Dash app:
    ```bash
    python src/main.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:8050/` to access the interactive dashboard.

3. Use the radio buttons to filter sales data by region (North, East, South, West, or All).

4. The line chart will automatically update based on your selection, providing a visual representation of the sales trends for the selected region.


## Dependencies

- Python 3.9+
- Dash 2.18.1
- Plotly
- Pandas
- Pytest

To install all dependencies, run:
```bash
pip install -r requirements.txt
```


## Testing

This project includes a Pytest-based testing suite. To run the tests:

1. Ensure all dependencies are installed.
2. Run the following command:

    ```bash
    pytest
    ```

The tests verify the presence of the header, region picker, and visualizations, as well as ensure that callback functions work as expected.

## Running Tests

To run the test suite for this project, follow these steps:

1. Ensure all dependencies are installed and your virtual environment is activated.
2. Run the provided `run_test.sh` script to execute the test suite.

### Steps to Run:

1. **Activate the virtual environment** (if it's not activated):
    ```bash
    source venv/Scripts/activate  # For Windows
    ```

2. **Run the test suite**:
    ```bash
    ./src/run_test.sh
    ```

The script will:
- Activate the virtual environment.
- Run the test suite using Pytest.
- Return a success code `0` if all tests pass or `1` otherwise.

### Example Output:

```bash
=========== test session starts ============
platform win32 -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\danie\OneDrive\Desktop\Quantium\Sales_data_engineer_visualization, configfile: pytest.ini
plugins: anyio-3.5.0, dash-2.18.1
collected 3 items

test_visualization.py ...                                            [100%]

=================== 3 passed in 5.54s ===================
