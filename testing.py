# -*- coding: utf-8 -*-
"""
For testing stuff in general

Created on 18-04-2020
@author: August Semrau Andersen
"""

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint
from main import getKey
import csv
import os

Alpha_Key = getKey()
ts = TimeSeries(key=Alpha_Key, output_format='pandas')
ti = TechIndicators(key=Alpha_Key)


# data1, meta_data1 = ts.get_intraday(symbol="AAPL", interval="1min", outputsize="full")
# pprint(data1.head(2))
data_path = './share_data'
stock_name = 'AMZN'

data1, meta_data1 = ts.get_daily(symbol=stock_name, outputsize="full")
pprint(data1)

file_path = os.path.join(data_path, stock_name)
data1.to_csv(file_path + '.csv', index=True, header=True)


