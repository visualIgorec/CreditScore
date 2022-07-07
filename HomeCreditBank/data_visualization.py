from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class MainInterface(ABC):

    @abstractmethod
    def vis_map(self):
        pass


class Visualization(MainInterface):

    def __init__(self, feature, name, num_fraction, range_list):
        # self.target = target.iloc[:time_range]
        self.feature = feature.to_numpy()
        # self.time_range = time_range
        self.num_fraction = num_fraction
        self.range_list = range_list
        self.name = name

    def vis_map(self):

        x_list = []
        # y_list = []
        chunks_x = np.array_split(self.feature, self.num_fraction)

        # chunks_y = np.array_split(self.target, self.num_fraction)

        def chunk_split():
            for idx in range(self.num_fraction):
                x_list.append(chunks_x[idx])
                # y_list.append(chunks_y[idx])

        chunk_split()

        # split data for groups

        range_dict = {'0-1': [], '1-2': [], '2-3': [], '3-4': []}
        group_list = []

        def check(obj, range_):
            if range_[0] <= obj < range_[1]: range_dict['0-1'].append(obj/chunk_itm.shape[0])
            else: range_dict['0-1'].append(None)
            if range_[1] <= obj < range_[2]: range_dict['1-2'].append(obj/chunk_itm.shape[0])
            else: range_dict['1-2'].append(None)
            if range_[2] <= obj < range_[3]: range_dict['2-3'].append(obj/chunk_itm.shape[0])
            else: range_dict['2-3'].append(None)
            if range_[3] <= obj < range_[4]: range_dict['3-4'].append(obj/chunk_itm.shape[0])
            else: range_dict['3-4'].append(None)

        for chunk_itm in chunks_x:
            for inner_idx in range(chunk_itm.shape[0]):
                check(chunk_itm[inner_idx], self.range_list)
            group_list.append(range_dict)
            range_dict = {'0-1': [], '1-2': [], '2-3': [], '3-4': []}


        wspace = 0.3
        hspace = 0.4
        nfont = 12
        wsize = 3
        hsize = 77

        for idx,itm in enumerate(group_list):
            for key, value in itm.items():
                plt.subplot(self.num_fraction, 2, idx + 1)
                sns_plot = sns.kdeplot(value, shade=False)
                sns_plot.set_xlabel(f'Признак {self.name} для интервала {idx + 1} из {self.num_fraction}', fontsize=nfont)
                sns_plot.set_ylabel(f"Частота признака", fontsize=nfont)
                sns_plot.tick_params(labelsize=nfont)
                fig = sns_plot.get_figure()
                fig.set_size_inches(wsize, hsize)
                plt.subplots_adjust(wspace=wspace, hspace=hspace)
                plt.legend(labels=[f'Группа: {self.range_list[0]}-{self.range_list[1]}',
                                   f'Группа: {self.range_list[1]}-{self.range_list[2]}',
                                   f'Группа: {self.range_list[2]}-{self.range_list[3]}',
                                   f'Группа: {self.range_list[3]}-{self.range_list[4]}'])
        plt.show()



