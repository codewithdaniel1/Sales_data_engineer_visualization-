import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from data_processing import data_processing_func
from visualization import visualization_func

# Call the function to process the data
if __name__ == "__main__":
    data_processing_func()
    visualization_func()
