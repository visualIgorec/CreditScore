import pandas as pd
from abc import ABC, abstractmethod


class MainInterface(ABC):

    @abstractmethod
    def upload(self):
        pass


class Uploading(MainInterface):
    def __init__(self, file_path='data/application_train.csv', file_sep=','):
        self.file_path = file_path
        self.file_sep = file_sep

    def upload(self):
        raw_data = pd.read_csv(self.file_path, self.file_sep)
        print(f'Size of Raw DataSet is {raw_data.shape}')
        return raw_data