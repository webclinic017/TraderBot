# -*- coding: utf-8 -*-
"""
Created on 18-04-2020
@author: August Semrau Andersen
"""

import matplotlib.pyplot as plt
from load_data import DataLoader

class Plotter:
    def __init__(self, state=True):
        self.state = state


    def visualize(self, data, share_name, stamp='4. close'):
        # plt.figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k', label=share_name)
        data[stamp].plot()
        plt.tight_layout()
        plt.legend()
        plt.grid()
        plt.show()



'''
For testing plotting setups.
'''
if __name__ == '__main__':
    DataLoader = DataLoader(work_dir='./share_data')
    Plotter = Plotter()

    share_name1 = 'AMZN'
    df = DataLoader.alpha_load_data(share_name=share_name1)#, sort_by_date=False)
    print(df)


    Plotter.visualize(data=df, share_name=share_name1)
