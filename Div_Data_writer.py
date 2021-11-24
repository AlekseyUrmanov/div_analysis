import numpy as np
import xlsxwriter as xl
import math as m
import pandas as pd
import FinancialFunctions as ff


import FinancialFunctions_2 as ff2
import TDgetdata as td


from TDgetdata import CONSUMER_KEY as CK


import Evaluation as Ev
import NASDAQ_SCRAPE as NS
import NASDAQ_SCRAPE_SORT as NSS



#workbook= xl.Workbook('Div_Data.xlsx')
#worksheet = workbook.add_worksheet('Data')

def print_data_to_excel(stock_list,terms,file_name):
    
    #terms is how many transactions u want
    # stock = ticker
    #stock dataa frames
    
    #a_type is analyze low, medium, high yeidl stocks.
    
    all_data_frames =[]
    
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    
    
    analyzed_data = Ev.LOW_HIGH_MEDIUM_YIELD_STOCKS(stock_list,'df')
    analyzed_data.to_excel(writer,sheet_name="All Data", index_label='time', startrow = 0,startcol=0)
    
    
    validity_list = test_errors(stock_list)
    
    stock_list = validity_list[0]
    

    term = terms
    terms = terms-1
    for i in stock_list:
        stock = i
        
        stock_data_frames = []
        
        real_stock_date_data = NSS.NASDAQ_SCRAPE_SORT_DATES(stock,term)
        
        
        epoch_stock_date_data = ff2.excel_date_data_too_epoch_dollar_data(real_stock_date_data)
        
        
        #limit entries to 24, because td does not have so much historical data
        # chnagfe limit based on frequency of dividend, if medium or low payout then 24 = 6 years. asusming 4x year
        
        
        
        x_dates = epoch_stock_date_data[0]
        r_dates = epoch_stock_date_data[1]
        d_amounts = epoch_stock_date_data[2]
        
        print(x_dates)
        print(r_dates)
        print(d_amounts)
        
        x_dates.pop(0)
        r_dates.pop(0)
        d_amounts.pop(0)
        print(i)
    
        print(x_dates)
        print(r_dates)
        print(d_amounts)
    
        
        
        
        final_data = ff.dividend_capture(x_dates, r_dates, stock, 100, 1, d_amounts,terms)
        final_data.to_excel(writer,sheet_name=stock, index_label='Strat 1', startrow = 0,startcol=0)
        
        
        final_data2 = ff.dividend_capture(x_dates, r_dates, stock, 100, 2, d_amounts,terms)
        final_data2.to_excel(writer,sheet_name=stock, index_label='Strat 2', startrow = 0,startcol=8)
        
        
        final_data3 = ff.dividend_capture(x_dates, r_dates, stock, 100, 3, d_amounts,terms)
        final_data3.to_excel(writer,sheet_name=stock, index_label='Strat 3', startrow = terms+4,startcol=0)
        
        
        final_data4 = ff.dividend_capture(x_dates, r_dates, stock, 100, 4, d_amounts,terms)
        final_data4.to_excel(writer,sheet_name=stock, index_label='Strat 4', startrow = terms+4,startcol=8)
       
        stock_data_frames=[final_data,final_data2,final_data3,final_data4]
        all_data_frames.append(stock_data_frames)
        # an array, of stock arrays, of data frames
    
    
    performance = Ev.comparison(all_data_frames, stock_list)
    performance.to_excel(writer,sheet_name="Summary", index_label='Top Pics', startrow = 0,startcol=0)
    
    top = performance.get('Stock')
    top_strat = performance.get('Best Strategy')
    top_data_frames = []
    
    
    atp = 4 #amount of top picks, reduce range size if sample size is too small
    
    if len(stock_list)<4:
        atp = len(stock_list)
    
    
    
    for i in range(atp):
        ticker = top[i]
        strat_for_stock = int(top_strat[i])
        og_index = stock_list.index(ticker)
        strats_for_index = all_data_frames[og_index]
        top_data_frame = strats_for_index[strat_for_stock-1]
        top_data_frames.append(top_data_frame)
        
        
    for i in range(atp):
    
        top_data_frames[i].to_excel(writer,sheet_name="Summary", index_label=f'# {i+1}', startrow = i*(terms+3),startcol=5)
        
    
    #print(performance)
    
    writer.save()



def test_errors(stock_list):
    return_arr = []
    
    failed_twice = []
    failed_once_or_passed = []
    
    invalid_dont_exist = []
    
    
    for stock in stock_list:
        try:
            x = NSS.NASDAQ_SCRAPE_SORT_DATES(stock,2)
            fail = 0
            y = ff2.excel_date_data_too_epoch_dollar_data(x)
            for i in range(2):
                try:
                        exd = y[0]
                        rcd = y[1]
                        test_date = exd[i]
                        test_date2 = rcd[i]
                        z = ff.div_diff_price_data(test_date2, (test_date-82800000), stock)
            
                except KeyError:
                        fail = fail+1
                        pass
                else:
                        pass
                    
            if fail ==2:
                failed_twice.append(stock)
            else:
                failed_once_or_passed.append(stock)
                   
                
        except TypeError:
            invalid_dont_exist.append(stock)
                 
        
    return_arr = [failed_once_or_passed,failed_twice,invalid_dont_exist]
    return return_arr



#AEL -pass 1 future date 
#DDS - fail 2 future dates


sss = ['CCU','AEL','DDS','ORCL']

#print(test_errors(sss))



scraped_list = NS.scrape_upcoming_divs('2021-11-26')
processed_scraped_list = NSS.NASDAQ_SCRAPE_DIV_LIST(scraped_list)

low_yield_stocks = Ev.LOW_HIGH_MEDIUM_YIELD_STOCKS(processed_scraped_list,'l')
#print(high_yield_stocks)

print(low_yield_stocks)

stkl = []
#low_yield_stocks

s = low_yield_stocks

print_data_to_excel(s,4,'Big_Data.xlsx')



