
"""
Created on Sat 18 2020

@author: August Semrau Andersen
"""

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint
from main import getKey


Alpha_Key = getKey()
ts = TimeSeries(key=Alpha_Key, output_format='pandas')
ti = TechIndicators(key=Alpha_Key)


data1, meta_data1 = ts.get_intraday(symbol="AAPL", interval="1min", outputsize="full")
pprint(data1.head(2))