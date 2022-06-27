from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class MainInterface(ABC):

    @abstractmethod
    def vis_map(self):
        pass


class Visualization(MainInterface):

    def __init__(self, numeric_data, categorical_data):
        self.numeric_data = numeric_data
        self.categorical_data = categorical_data

    def vis_map(self):

        #Target value
        num_list = list(self.numeric_data.select_dtypes('number'))
        for idx in range(5):
            feature = num_list[idx]
            new_data = self.numeric_data[feature]
            new_data.plot(x="Approvement", y=feature, fontsize=14)
            plt.title("feature: " + feature, fontsize=14)
            plt.xlabel("timeline", fontsize=14)
            plt.ylabel(feature, fontsize=14)
            plt.grid()
            plt.show()








