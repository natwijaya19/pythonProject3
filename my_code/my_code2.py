# download multiple stocks data from yahoo finance by using datareader
# and save them into csv files
# import libraries
import datetime
import os

import pandas_datareader.data as web

# set start and end time
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 1, 11)
# set the path
path = "C:/Users/.../my_code"
# set the stock tickers
tickers = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'NFLX', 'BBCA.JK', 'BBRI.JK', 'TLKM.JK', 'UNVR.JK', 'ASII.JK']
# download the data
for ticker in tickers:
    df = web.DataReader(ticker, 'yahoo', start, end)
    df.to_csv(os.path.join(path, ticker + '.csv'))

#%% Path: my_code\my_code3.py
# read the stocks data from csv files and append to dataframe
# import libraries
import pandas as pd
import os
for file in os.listdir(path):
    df = pd.read_csv(os.path.join(path, file), index_col=0)
    df['Ticker'] = file.split('.')[0]
    df.to_csv(os.path.join(path, file))

# plot the data by using matplotlib




# plot the data by using plotly


# plot the data by using bokeh


# plot the data by using cufflinks


# plot the data by using seaborn

# plot the data by using pandas
