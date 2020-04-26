# -*- coding: utf-8 -*-
"""
Created on 26-04-2020
@author: August Semrau Andersen
"""
import pandas as pd
import csv

finnhub_key = 'bqitk0frh5r89luqqe40'







class DataLoader:
    def __init__(self, work_dir):
        self.work_dir = work_dir



    def alpha_load_data(self, share_name, sort_by_date=True, type=csv):
        file_path = self.work_dir + '/' + share_name + '.csv'
        if type == csv:
            df = pd.read_csv(file_path, index_col='date')

            if sort_by_date:
                df = df.sort_values(by=['date'])

        return df

