# -*- coding: utf-8 -*-
"""
Created on 26-04-2020
@author: August Semrau Andersen
"""


import requests
r = requests.get('https://finnhub.io/api/v1/stock/exchange?token=bqitk0frh5r89luqqe40')
print(r.json())