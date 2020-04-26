# -*- coding: utf-8 -*-
"""
Created on 18-04-2020
@author: August Semrau Andersen
"""

from yahoo_finance import Share


class companyFinder:
    def __init__(self, size, market):
        self.size = size
        self.market = str(market)


    def stock_chooser(self):


        return


    def companies(self, test=False):
        if test:
            stock1, stock2, stock3, stock4, stock5 = "AAPL", "MSFT", "TSLA", "GOOGL", "FB"  # Apple, Microsoft, Tesla, Google and Facebook

        else:
            num_stocks = self.size
            # TODO: Implement chosen share_data for return here
            names = ""
        return stock1, stock2, stock3, stock4, stock5

