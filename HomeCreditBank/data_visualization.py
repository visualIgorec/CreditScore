from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class MainInterface(ABC):

    @abstractmethod
    def vis_map(self):
        pass


class Visualization(MainInterface):

    def __init__(self, feature, name, num_fraction):
        # self.target = target.iloc[:time_range]
        self.feature = feature
        #self.time_range = time_range
        self.num_fraction = num_fraction
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

        if self.num_fraction % 2 != 0:
            self.num_fraction += 1

        wspace = 0.3
        hspace = 0.8
        nfont = 12
        wsize = 20
        hsize = 60

        for idx in range(self.num_fraction):
            plt.subplot(self.num_fraction, 2, idx + 1)
            sns_plot = sns.kdeplot(x_list[idx], shade=True)
            sns_plot.set_xlabel(f'Признак {self.name} для интервала {idx+1} из {self.num_fraction}', fontsize=nfont)
            sns_plot.set_ylabel(f"Частота признака", fontsize=nfont)
            sns_plot.tick_params(labelsize=nfont)
            fig = sns_plot.get_figure()
            fig.set_size_inches(wsize, hsize)
            plt.grid()
            plt.subplots_adjust(wspace=wspace, hspace=hspace)
        plt.show()


        # plt.figure(figsize=(6, 15))
        # for idx in range(self.num_fraction):
        #     plt.figure(figsize=(6, 15))
        #     #plt.subplot(self.num_fraction, 2, idx + 1)
        #     plt.hist(x_list[idx], ls='-')
        #     plt.xlabel('AMT_INCOME_TOTAL', fontsize=13)
        #     plt.ylabel('Частота признака', fontsize=13)
        #     plt.title(f'Изменчивость признака AMT_INCOME_TOTAL в {idx+1} диапазоне', fontsize=13)
        #     plt.subplots_adjust(wspace=0.6, hspace=3)
        #     #fig.set_figwidth(8)  # ширина Figure
        #     #fig.set_figheight(5)  # высота Figure
        #     plt.grid()
        #     plt.show()
