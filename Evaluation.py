from TDgetdata import CONSUMER_KEY as CK
import requests
from time import time,sleep
import matplotlib.pyplot as plt
import numpy as np
import NASDAQ_SCRAPE_SORT as NSS
import pandas as pd
import math as m


#content = requests.get(url=url, params=payload)
#data = content.json()
#data = data[f'{stock}']


#dividend_list = NSS.NASDAQ_SCRAPE_DIV_LIST()

def LOW_HIGH_MEDIUM_YIELD_STOCKS(dividend_list,value):
    
    # value is either l (low) m (medium) or h (high)
    # or df if they want the entire pandas data frame
    
    div_yield = []
    div_amount = []
    price_data = []
    
    #For displaying data not used in calcs
    bid_Prices = []
    volats = []
    peRatios = []
    bid_ask_spreads = []
    
    for i in dividend_list:
        stock = i
        url = r'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format(stock)
        payload = {'apikey':CK}
        
        content = requests.get(url=url, params=payload)
        data = content.json()
        data = data[f'{stock}']
        
        
        #print(data['divAmount'])
        #Required
        dividend_yield = data['divYield']
        dividend_amount = data['divAmount']
        price_of_stock = data['askPrice']
        
        div_yield.append(dividend_yield)
        div_amount.append(dividend_amount)
        price_data.append(price_of_stock)
        ####
        
        #Extra
        bid_Price = data['bidPrice']
        volat = data['volatility']
        peRatio = data['peRatio']
        
        bid_Prices.append(bid_Price)
        volats.append(volat)
        peRatios.append(peRatio)
        #####
        
        #bid ask apread calculation
        bas = round(price_of_stock-bid_Price,3)
        bid_ask_spreads.append(bas)
        
        
        
        
    
    numpy_data_arr = np.array([div_yield,div_amount,price_data]).T
    
    df_return = np.array([dividend_list,div_yield,div_amount,price_data,bid_Prices,bid_ask_spreads,volats,peRatios]).T
    
    #print(np.shape(numpy_data_arr))
    
    l = len(dividend_list)
    
    df = pd.DataFrame(data=numpy_data_arr,index=np.arange(l), columns=["Div Yield", "Div Amount","Ask Price"])
    
    full = pd.DataFrame(data=df_return,index=np.arange(l), columns=["Stock","Div Yield", "Div Amount",
                                                                    "Ask Price","Bid Price","Bid Ask Spread",
                                                                    "Volatility","peRatio"])
    
    #.get('')
    

    
    index = df.index
    
    
    condition = df["Div Yield"] >= 5
    
    high_indices = index[condition]
    
    high_indices_list = high_indices.tolist()
    
    h_yield_stocks = []
    for i in high_indices_list:
        
        h_yield_stocks.append(dividend_list[i])
        
        
    condition = df["Div Yield"] < 5 
    
    medium_indices = index[condition]
    
    medium_indices_list = medium_indices.tolist()
    
    
    
    condition = df["Div Yield"] < 1
    
    low_indices = index[condition]
    
    low_indices_list = low_indices.tolist()
    
    l_yield_stocks = []
    for i in low_indices_list:
        
        l_yield_stocks.append(dividend_list[i])
        
    
    
    for i in range(len(low_indices_list)):
        
    
        val = low_indices_list[i]
        index = medium_indices_list.index(val)
        medium_indices_list.pop(index)
        
        
    m_yield_stocks = []
    for i in medium_indices_list:
        
        m_yield_stocks.append(dividend_list[i])
        
    #l_yield_stocks
    #m_yield_stocks
    #h_yield_stocks

    if value== 'l':

        return l_yield_stocks
    elif value == 'm':
        return m_yield_stocks
    
    elif value == 'h':
        return h_yield_stocks
    else:
        return full
    
    

#data = LOW_HIGH_MEDIUM_YIELD_STOCKS(dividend_list,'df')
def main_points(values):
    points_arr = []
    per_arr = []
    long_index = 4
    short_index = 0
    
    duration = int((len(values)/4))
    for i in range(duration):
        tempr = []
        
        tempr = values[short_index:long_index]
        big = max(tempr)
        #print(big)
        
        for i in tempr:
            
            if big ==0:
                x = 0
            else:
                
                x = round((i/big)*100,2)
            #print(x)
            point_val = sub_points(x)
            points_arr.append(point_val)
        short_index = short_index +4
        long_index = long_index+ 4
        
    return points_arr


def sub_points(x):
    #  0 - 12 points
    bx = [-5,0,10,20,30,40,50]
    bxx = [60,70,80,90,100]
    
    if x>50:
        c = 7
        for percentage in bxx:
            if x>=percentage:
                c = c+1
                pass
            else:
                break
        
    else:
        c = 0
        for percentage in bx:
            if x>=percentage:
                c = c+1
                pass
            else:
                break
 
    return c

def comparison(arr,stocks):
    top_stock_pics = []
    profit_per_strategy = []
    price_loss_ratio = []
    win_loss_ratio = []
    strength = []
    
    lenostk = len(stocks)
    
    for i in arr:
        
        
        for dataframe in i:
            wins = 0
            
            won = 0
            lost = 0
            p =dataframe.get('Earnings')
            earnings = p.sum()
            #print(p)
            total = len(p)
            
            for x in p:
            
                if x> 0:
                    won = won + x
                    wins = wins+1
                else:
                    lost = lost + abs(x)
            
            
            if won == 0:
                
                profit = round(earnings,3)
                price_loss = round((lost),3)
                win_loss = round(((wins/total)*100),2)
                
            else:
                profit = round(earnings,3)
                price_loss = round((lost/won),3)
                win_loss = round(((wins/total)*100),2)
                
            
            profit_per_strategy.append(profit)
            price_loss_ratio.append(price_loss)
            win_loss_ratio.append(win_loss)
            
            '''print(profit)
            print(price_loss)
            print(win_loss)'''
        
    points_of_profit = main_points(profit_per_strategy)
    points_of_wlr =main_points(win_loss_ratio)
    points_of_plr = main_points(price_loss_ratio)
    #calculated the same way, but less points is better
    
    final_point_arr = []
    best_strategy_arr = []
    
    dd = int(len(points_of_profit))
    for i in range(dd):
        a = points_of_profit[i]
        b = points_of_wlr[i]
        c = points_of_plr[i]
        
        estimate = a+b-c
        final_point_arr.append(estimate)
    
    #print(final_point_arr)
    index_c = 4
    for i in range(lenostk):
        temp = []
        temp = final_point_arr[(index_c-4):index_c]
        #print(temp)
        best_pic = max(temp)
        strength.append(best_pic)
        iobp = temp.index(best_pic)+1
        best_strategy_arr.append(iobp)
        index_c = index_c+4
        
        
        
    best_strategy_arr_arranged = []
    rating = []
    
    
    
    for i in range(lenostk):
        top = max(strength)
        index_of_top = strength.index(top)
        top_stock_pics.append(stocks[index_of_top])
        rating.append(strength[index_of_top])
        strength[index_of_top] = 0
        
        
    for i in top_stock_pics:
        val = stocks.index(f'{i}')
        best_strategy_arr_arranged.append(best_strategy_arr[val])
    
    
    numpy_data_arr = np.array([top_stock_pics,rating,best_strategy_arr_arranged]).T
    
    l = len(top_stock_pics)
    df = pd.DataFrame(data=numpy_data_arr,index=np.arange(l), columns=["Stock", "Rating","Best Strategy"])
    
    
    return df




