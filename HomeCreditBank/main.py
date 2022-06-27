import pandas as pd

from HomeCreditBank.data_uploading import Uploading
from HomeCreditBank.data_processing import Processing
from HomeCreditBank.data_visualization import Visualization


if __name__ == '__main__':

    #download .csv
    file_path='data/application_train.csv'
    file_sep=','
    raw_data = Uploading(file_path, file_sep)
    raw_data = raw_data.upload()
    print(raw_data)

    #processing
    data = Processing(raw_data)

    #without nan objects
    filtered_data = data.nan_search()
    numeric_data = data.numeric()
    categorical_data = data.category()

    #Visualization
    map_data = Visualization(numeric_data, categorical_data)
    map_data.vis_map()

