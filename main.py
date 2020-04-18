
"""
Created on Sat 18 2020

@author: August Semrau Andersen
"""

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint


from companies import companyFinder
from plotter import plotter



# Function for getting key so I dont have to push it haha
def getKey():
    return ""





if __name__ == "__main__":

    # Setup API
    Alpha_Key = getKey()
    ts = TimeSeries(key=Alpha_Key, output_format='pandas')
    ti = TechIndicators(key=Alpha_Key)

    # Choose settings for API calling
    intervals = "1min"  # Alternatives are 5min, 15min, 30min, 60min
    output_size = "full"  # Alternative is "compact"

    # Choose stocks to focus on
    companyClass = companyFinder(size=5, market="US")
    plotterClass = plotter()

    # Choose which companies should be called by the API
    # stock1, stock2, stock3, stock4, stock5 = companyClass.companies(test=False)
    # print(f'Stock 1: {stock1}\nStock 2: {stock2}\nStock 3: {stock3}\nStock 4: {stock4}\nStock 5: {stock5}')

    # For now testing stocks:
    stock1, stock2, stock3, stock4, stock5 = companyClass.companies(test=True) # Apple, Microsoft, Tesla, Google and Facebook



    # dataX is a pandas dataframe, meta_dataX is a dict
    data1, meta_data1 = ts.get_intraday(symbol=stock1, interval=intervals, outputsize=output_size)
    data2, meta_data2 = ts.get_intraday(symbol=stock2, interval=intervals, outputsize=output_size)
    data3, meta_data3 = ts.get_intraday(symbol=stock3, interval=intervals, outputsize=output_size)
    data4, meta_data4 = ts.get_intraday(symbol=stock4, interval=intervals, outputsize=output_size)
    data5, meta_data5 = ts.get_intraday(symbol=stock5, interval=intervals, outputsize=output_size)

    # smaX is a dict, meta_sma1 also a dict
    sma1, meta_sma1 = ti.get_sma(symbol=stock1)
    sma2, meta_sma2 = ti.get_sma(symbol=stock2)
    sma3, meta_sma3 = ti.get_sma(symbol=stock3)
    sma4, meta_sma4 = ti.get_sma(symbol=stock4)
    sma5, meta_sma5 = ti.get_sma(symbol=stock5)


    print(stock1)
    pprint(data1.head(2))
    print(stock2)
    pprint(data2.head(2))
    print(stock3)
    pprint(data3.head(2))
    print(stock4)
    pprint(data4.head(2))
    print(stock5)
    pprint(data5.head(2))

    # # Get the data, returns a tuple
    # # aapl_data is a pandas dataframe, aapl_meta_data is a dict
    # aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL')
    # # aapl_sma is a dict, aapl_meta_sma also a dict
    # aapl_sma, aapl_meta_sma = ti.get_sma(symbol='AAPL')



