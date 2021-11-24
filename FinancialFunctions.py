from TDgetdata import CONSUMER_KEY as CK
import requests
from time import time,sleep
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd


#content = requests.get(url=url, params=payload)
#data = content.json()
#data = data[f'{stock}']

stock_list = ['ORCL','AEIS','AFT','AIF','ALSN','AOMR','ARDC','BGB','BGX','BSL','BWG',
                 'CDRE','CEM','CTR','DFP','DLX','DX','EHI','EMD','EMO','FFC','FHB','FLC']


def dividned_data(stock_list):
    
    div_yield,div_amount,price_data = [],[],[]
    div_list = ['Stock','Price$','Dividend$','DividendYield','Date']

    for stock in stock_list:

        url = r'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format(stock)
        payload = {'apikey':CK}
        content = requests.get(url=url, params=payload)
        data = (content.json())[f'{stock}']
        a,b,c,d = data['askPrice'],data['divAmount'],data['divYield'],data['divDate']
        
        var = [stock,a,b,c,d]
        div_list = np.vstack([div_list,var])
        
        
    return div_list



def create_date_time_object(y,m,d):
    
    
    date_time_obj = datetime.datetime(y,m,d)
    
    
    return date_time_obj


def epoch_to_datetime(x):
    
    epoch_time = x
    datetime_time = datetime.datetime.fromtimestamp(epoch_time)
    return datetime_time



def price_data_day(x,y):
    # x is days into the past
    # y is stock name
    
    
    #END// date is November 19th
    price_data_close_arr=[]
    price_data_open_arr= []
    price_data_high_arr= []
    price_data_low_arr = []
    price_data_vol_arr = []
    
    days = x
    stock = y
    priceurl = r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(stock)
    end_date = 1637298000000  #make today the current day
    
    
    
    #start_date = end_date - (x*86400000)
    
    week_counter =0
    
    price_list =['Close','Open','High','Low','Volume']

    
    for i in range(days):
        
        
        payload = {'apikey': CK,
            'periodType':'month',
            'frequencyType': 'daily',
            'endDate':end_date,
            'startDate' : end_date}
        
        content = requests.get(url = priceurl, params = payload)
        tmp_data = content.json()
        tmp_data = tmp_data['candles']
        #print((tmp_data[0])['datetime'])
        
        Close = (tmp_data[0])['close']
        price_data_close_arr.append(Close)
        
        Open = (tmp_data[0])['open']
        price_data_open_arr.append(Open)
        
        High = (tmp_data[0])['high']
        price_data_high_arr.append(High)
        
        Low = (tmp_data[0])['low']
        price_data_low_arr.append(Low)
        
        Vol =(tmp_data[0])['volume']
        price_data_vol_arr.append(Vol)
        
        end_date = end_date - 82800000
        week_counter = week_counter+1
        #print(week_counter)
        
        if week_counter == 0:
            pass
        else:
                
            if week_counter% 5 ==0:   #Every 5 days we jump 2 days to skip the weekend
                end_date = end_date - (2*82800000)
                #print(end_date)
                #print(week_counter)
                
                
        var =[Close,Open,High,Low,Vol]
        price_list = np.vstack([price_list,var])
        
        
        
        # To compute with data set array equal to column
        # use  for i in ( np.flip(pl_data[:,0],0) )for column to row flip
        # float(i) for conversion of str to float. 
        
    return price_list
    



def div_diff_price_data(end,start,Stock):
    
    #END// date is November 19th
    price_data_close_arr=[]
    price_data_open_arr= []
    price_data_high_arr= []
    price_data_low_arr = []
    price_data_vol_arr = []
    
    
    stock = Stock
    priceurl = r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(stock)
    end_date = end
    start_date = start
    
    
    
    price_list =['Close','Open','High','Low','Volume']
    
            
        
    payload = {'apikey': CK,
            'periodType':'month',
            'frequencyType': 'daily',
            'endDate':end_date,
            'startDate' : start_date}
        
    content = requests.get(url = priceurl, params = payload)
    tmp_data = content.json()
    #print(tmp_data)
    
    tmp_data = tmp_data['candles']
        #print((tmp_data[0])['datetime'])
        
    for i in tmp_data:
        
    
        Close = (i)['close']
        price_data_close_arr.append(Close)
        
        Open = (i)['open']
        price_data_open_arr.append(Open)
        
        High = (i)['high']
        price_data_high_arr.append(High)
        
        Low = (i)['low']
        price_data_low_arr.append(Low)
        
        Vol =(i)['volume']
        price_data_vol_arr.append(Vol)
        
        
        var =[Close,Open,High,Low,Vol]
        price_list = np.vstack([price_list,var])
        
        
        
        # To compute with data set array equal to column
        # use  for i in ( np.flip(pl_data[:,0],0) )for column to row flip
        # float(i) for conversion of str to float. 
        

    return price_list

'''
def dividend_capture(ex_dates,record_dates,stock,share,strat,div_values):
    entire_div_capture_data = ['Shares','Initial Value','Ending Value','Change in Value','Dividends Earned','Earnings']
    
    print(ex_dates)
    print(record_dates)
    print(stock)
    print(strat)
    print(div_values)
    
    
    if strat ==1:
        
        
        #strat parameter for future implementation
        
        for i in range(len(ex_dates)):
            data = div_diff_price_data(record_dates[i], (ex_dates[i]-82800000), stock)
            #print(data)
            
            
            #The default strategy is buying before x date at close, and selling at open on record date
            
            shares = share
            
            #print(shares)
            
            initial_value_of_shares = shares*(float(data[1,0]))
            
            #print(initial_value_of_shares)
            
            #print(len(ex_dates)-1)
            x = len(data)
            #print(x)
            
        
            new_value_of_shares = shares*(float(data[x-1,1]))
            
            
            dividend_value_earned = shares*div_values[i]
            
            
            pl = new_value_of_shares-initial_value_of_shares
            
            
            total_earned = pl+dividend_value_earned
            
            
            
            
            var = [shares,round(initial_value_of_shares,2),round(new_value_of_shares,2),
                   round(pl,), dividend_value_earned, round(total_earned,2)]
            
            entire_div_capture_data = np.vstack([entire_div_capture_data, var])
            
    return entire_div_capture_data'''


def dividend_capture(ex_dates,record_dates,stock,share,strat,div_values,terms):
    #['Shares','Initial Value','Ending Value','Change in Value','Dividends Earned','Earnings']
    # return pandas data frame
    
    # Strat 1 = Buy ( before ex-date at close  ) Sell ( At open on record date)
    # Strat 2 = Buy ( before ex-date at close  ) Sell ( At close on record date)
    # Strat 3 = Buy ( before ex-date at open  ) Sell ( At open on record date)
    # Strat 4 = Buy ( before ex-date at open  ) Sell ( At close on record date)
    
    #strat parameter for future implementation
    # Terms represents the amount of dividend cycles to calculate, because some histroical data may not exist
    
    if strat ==1:
        
        s = []
        Iv = []
        Ev = []
        Civ = [] 
        De = []
        Ear = []
        
        for i in range(terms):
            
            data = div_diff_price_data(record_dates[i], (ex_dates[i]-82800000), stock)
            
            shares = share
           
            initial_value_of_shares = shares*(float(data[1,0]))
            
            x = len(data)
        
            new_value_of_shares = shares*(float(data[x-1,1]))
            
            dividend_value_earned = shares*div_values[i]
            
            pl = new_value_of_shares-initial_value_of_shares
            
            total_earned = pl+dividend_value_earned
            
            s.append(shares)
            Iv.append(initial_value_of_shares)
            Ev.append(new_value_of_shares)
            De.append(dividend_value_earned)
            Civ.append(pl)
            Ear.append(total_earned)
            
        numpy_data_arr = np.array([s,Iv,Ev,Civ,De,Ear]).T
   
        df = pd.DataFrame(data=numpy_data_arr,index=np.arange(terms), columns=["Shares", "Initial Value", 
                                                                               "Ending Value","Change in Value",
                                                                               "Dividends Earned","Earnings"])

    elif strat ==2:
        
        s = []
        Iv = []
        Ev = []
        Civ = [] 
        De = []
        Ear = []
        
        for i in range(terms):
            
            data = div_diff_price_data(record_dates[i], (ex_dates[i]-82800000), stock)
        
            shares = share
        
            initial_value_of_shares = shares*(float(data[1,0])) #buying at close so index is 0
            
            x = len(data)
           
            new_value_of_shares = shares*(float(data[x-1,0])) #Selling at close so index is 0
           
            dividend_value_earned = shares*div_values[i]
            
            pl = new_value_of_shares-initial_value_of_shares
            
            total_earned = pl+dividend_value_earned
            
            s.append(shares)
            Iv.append(initial_value_of_shares)
            Ev.append(new_value_of_shares)
            De.append(dividend_value_earned)
            Civ.append(pl)
            Ear.append(total_earned)
        
        numpy_data_arr = np.array([s,Iv,Ev,Civ,De,Ear]).T
    
        df = pd.DataFrame(data=numpy_data_arr,index=np.arange(terms), columns=["Shares", "Initial Value", 
                                                                               "Ending Value","Change in Value",
                                                                               "Dividends Earned","Earnings"])

    elif strat ==3:
        
        s = []
        Iv = []
        Ev = []
        Civ = [] 
        De = []
        Ear = []
        
        for i in range(terms):
            
            data = div_diff_price_data(record_dates[i], (ex_dates[i]-82800000), stock)
            
            shares = share
        
            initial_value_of_shares = shares*(float(data[1,1])) #buying at open so index is 1
        
            x = len(data)
        
            new_value_of_shares = shares*(float(data[x-1,1])) #Selling at open so index is 1
            
            dividend_value_earned = shares*div_values[i]
            
            pl = new_value_of_shares-initial_value_of_shares
            
            total_earned = pl+dividend_value_earned
            
            s.append(shares)
            Iv.append(initial_value_of_shares)
            Ev.append(new_value_of_shares)
            De.append(dividend_value_earned)
            Civ.append(pl)
            Ear.append(total_earned)
        
        numpy_data_arr = np.array([s,Iv,Ev,Civ,De,Ear]).T
        df = pd.DataFrame(data=numpy_data_arr,index=np.arange(terms), columns=["Shares", "Initial Value", 
                                                                               "Ending Value","Change in Value",
                                                                               "Dividends Earned","Earnings"])
            
    else:
        
        s = []
        Iv = []
        Ev = []
        Civ = [] 
        De = []
        Ear = []
        
        for i in range(terms):
            
            data = div_diff_price_data(record_dates[i], (ex_dates[i]-82800000), stock)

            shares = share
        
            initial_value_of_shares = shares*(float(data[1,1])) #buying at open so index is 1
        
            x = len(data)
        
            new_value_of_shares = shares*(float(data[x-1,0])) #Selling at close so index is 0
            
            dividend_value_earned = shares*div_values[i]
            
            pl = new_value_of_shares-initial_value_of_shares 
            
            total_earned = pl+dividend_value_earned
            
            s.append(shares)
            Iv.append(initial_value_of_shares)
            Ev.append(new_value_of_shares)
            De.append(dividend_value_earned)
            Civ.append(pl)
            Ear.append(total_earned)
        
        numpy_data_arr = np.array([s,Iv,Ev,Civ,De,Ear]).T
        df = pd.DataFrame(data=numpy_data_arr,index=np.arange(terms), columns=["Shares", "Initial Value", 
                                                                               "Ending Value","Change in Value",
                                                                               "Dividends Earned","Earnings"])
        #.get('') to pull a column       
        #print(np.shape(numpy_data_arr))
        
    return df





    

