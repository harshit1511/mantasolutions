#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Creating an empty data frame to append into second-wise values
import pandas as pd
second_wise_price = pd.DataFrame(columns=['Price', 'Timestamp'])


import ccxt
import threading
from time import sleep
import pandas as pd

ftx   = ccxt.ftx()
time = 0 #this variable will count the number of seconds passed

second_wise_price = pd.DataFrame(columns=['Price', 'Timestamp'])

def second_ticker():
    if time < 4000: #change 4000 here by the number of seconds you want the data for
        threading.Timer(1.0, second_ticker).start()   #Timer function repeats the process every 1 second
        global second_wise_price, time
        second_wise_price = second_wise_price.append({'Price': ftx.fetch_ticker('BTC/USD')['close'], 'Timestamp': ftx.fetch_ticker('BTC/USD')['datetime']}, ignore_index=True)
        time = time+1
    else:
        text= 'complete for '+str(time) + ' seconds'
        print(text)
        global time
        del time

second_ticker()

