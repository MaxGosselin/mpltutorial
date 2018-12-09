#%%
import matplotlib.pyplot as plt
import numpy as np

import urllib
import matplotlib.dates as mdates

#%%
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

#%%
def graph_data():

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    
    stock_data = []
    split_source = source_code.split('\n')
    
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Volume' not in line:
                stock_data.append(line)
    
    date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0: bytespdate2num('%Y-%m-%d')})
    ax1.plot_date(date, closep, '-', label='Price')


    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1.grid(True) #, color='g', linestyle='-')

    # We can change axis label colors by:
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')

    # We can set custom ranges for our axes
    ax1.set_yticks([0,100, 200, 300, 400, 500, 600, 700])

    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('AAPL')
    plt.legend()
    plt.show()


#%%
graph_data()

#%%
def graph_fill_between():

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    
    stock_data = []
    split_source = source_code.split('\n')
    
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Volume' not in line:
                stock_data.append(line)
    
    date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0: bytespdate2num('%Y-%m-%d')})
    #ax1.plot_date(date, closep, '-', label='Price')
    ax1.fill_between(date, closep, 0)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1.grid(True) #, color='g', linestyle='-')

    # We can change axis label colors by:
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')

    # We can set custom ranges for our axes
    ax1.set_yticks([0,100, 200, 300, 400, 500, 600, 700])

    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('AAPL')
    plt.legend()
    plt.show()


#%%

# Fill the area under the price and 0.
graph_fill_between()

#%%
def graph_fill_between_start():

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    
    stock_data = []
    split_source = source_code.split('\n')
    
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Volume' not in line:
                stock_data.append(line)
    
    date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0: bytespdate2num('%Y-%m-%d')})
    #ax1.plot_date(date, closep, '-', label='Price')
    ax1.fill_between(date, closep, closep[0], alpha=0.85)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1.grid(True) #, color='g', linestyle='-')

    # We can change axis label colors by:
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')

    # We can set custom ranges for our axes
    ax1.set_yticks([0,100, 200, 300, 400, 500, 600, 700])

    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('AAPL')
    plt.legend()
    plt.show()


#%%

# This time we graph the area between the first closing price and the rest.
graph_fill_between_start()

#%%

# Fill the area under the price and 0.
graph_fill_between()

#%%
def graph_fill_between_condition():

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    
    stock_data = []
    split_source = source_code.split('\n')
    
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Volume' not in line:
                stock_data.append(line)
    
    date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0: bytespdate2num('%Y-%m-%d')})
    
    
    # Fill positive growth
    ax1.fill_between(date, closep, closep[0],
                     where=(closep>closep[0]),
                     facecolor='g',
                     alpha=0.98)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1.grid(True) #, color='g', linestyle='-')

    # We can change axis label colors by:
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')

    # We can set custom ranges for our axes
    ax1.set_yticks([0,100, 200, 300, 400, 500, 600, 700])

    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('AAPL')
    plt.legend()
    plt.show()


#%%

# This time we graph only the positive area between the first closing price and the rest.
graph_fill_between_condition()

#%%
def graph_fill_pnl():

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    
    stock_data = []
    split_source = source_code.split('\n')
    
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Volume' not in line:
                stock_data.append(line)
    
    date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0: bytespdate2num('%Y-%m-%d')})
    
    # Price line
    plt.plot_date(date, closep, '-', label='Price')
    
    # Fill positive growth
    ax1.fill_between(date, closep, closep[0],
                     where=(closep>closep[0]),
                     facecolor='g',
                     alpha=0.98)
    
    # Fill negative growth
    ax1.fill_between(date, closep, closep[0],
                     where=(closep<closep[0]),
                     facecolor='r',
                     alpha=0.98)

    # Add some labels
    ax1.plot([],[], label='profit', color='g', alpha=0.99)
    ax1.plot([],[], label='loss', color='r', alpha=0.99)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1.grid(True) #, color='g', linestyle='-')

    # We can change axis label colors by:
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')

    # We can set custom ranges for our axes
    ax1.set_yticks([0,100, 200, 300, 400, 500, 600, 700])

    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('AAPL')
    plt.legend()
    plt.show()



#%%
graph_fill_pnl()

#%%
