import pandas as pd
import numpy as np
from scipy.stats import zscore
from abc import ABC, abstractmethod


class MainInterface(ABC):

    @abstractmethod
    def nan_search(self):
        pass

    @abstractmethod
    def numeric(self):
        pass

    @abstractmethod
    def category(self):
        pass


class Processing(MainInterface):

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def nan_search(self):
        self.raw_data = self.raw_data.dropna()
        print(f'Data without NaN rows: {self.raw_data}')
        return self.raw_data

    def numeric(self):
        self.numeric_columns = list(self.raw_data.select_dtypes('number'))
        numeric_data = self.raw_data[self.numeric_columns]
        print(f'Only nemeric Data: {numeric_data}')
        return numeric_data

    def category(self):
        self.cat_columns = list(self.raw_data.select_dtypes('object'))
        cat_data = self.raw_data[self.cat_columns]
        print(f'Only categorical Data: {cat_data}')
        return cat_data



