# -*- coding: utf-8 -*-
"""
Created on Sat 18 2020

@author: August Semrau Andersen
"""

import matplotlib.pyplot as plt


class plotter:
    def __init__(self):
        return

    def visualize(self, data, stock_name, stamp='4. close'):
        plt.figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k', label=stock_name)
        data[stamp].plot()
        plt.tight_layout()
        plt.legend()
        plt.grid()
        plt.show()

