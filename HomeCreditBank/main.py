import pandas as pd
import numpy as np


from HomeCreditBank.data_uploading import Uploading
from HomeCreditBank.data_processing import Processing
from HomeCreditBank.data_visualization import Visualization

if __name__ == '__main__':
    # download .csv
    file_path = 'data/application_train.csv'
    file_sep = ','
    raw_data = Uploading(file_path, file_sep)
    raw_data = raw_data.upload()
    print(raw_data)

    # processing
    data = Processing(raw_data)

    # without nan objects
    filtered_data = data.nan_search()

    #target variable
    name_list = filtered_data.columns
    #time_range = 1000
    num_fraction = 4 # according to quartiles
    feature = filtered_data[name_list[7]]   # AMT_INCOME_TOTAL
    range_list = [0, 500000, 800000, 1000000, 4500000]
    #target = filtered_data['TARGET']     # TARGET

    # Visualization
    map_data = Visualization(feature, name_list[7], num_fraction, range_list)
    map_data.vis_map()


    #numeric_data = data.numeric()
    #categorical_data = data.category()

