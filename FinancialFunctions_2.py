import FinancialFunctions as ff
import numpy as np
from datetime import datetime #--> to convert to epoch .timestamp()
import xlsxwriter as xl
import xlrd
import pandas as pd

#example of what pasisng arrays shold look like
'''
orcl_div_dates_ex = [1633687200000,1626256800000,1617789600000,1609930800000]
orcl_div_dates_record = [1634032800000,1626343200000,1617876000000,1610017200000]
dividend_amount = [.32,.32,.32,.32]

'''

# file name with the data


#excel_div_date_data = pd.read_excel (r'/Users/nadia/Desktop/TD Code/Div_Dates.xlsx') 


#place "r" before the path string to address special character, such as '\'. 
#Don't forget to put the file name at the end of the path + '.xlsx'

#print((excel_div_date_data))



def excel_date_data_too_epoch_dollar_data(excel_div_date_data):

    exdates = pd.DataFrame(excel_div_date_data, columns= ['Ex Date'])
    recdates = pd.DataFrame(excel_div_date_data, columns= ['Rec Date'])
    div_dollar = pd.DataFrame(excel_div_date_data, columns= ['Div$'])

    ex_dates_arr = []
    rec_dates_arr = []
    div_amount_arr = []

    return_data = []  #returns  exdates, recdates, div dollars

    for i in range(len(div_dollar)):
        xx = (div_dollar.values[i])
        
        for i in xx:
            
            i = i.replace('$','')
            i = float(i)
            
            div_amount_arr.append(i)
    

    div_date_data = [exdates,recdates]
    epoch_datetime_data = []


    for i in (div_date_data):
    
        length_o_data = len(i)
        #print(length_o_data)
    
        for j in range(length_o_data):
            
            time = (i.values[j])
            
            #print(time)
            # print(time)
            for w in time:
                
                #convert w to a date time object
                
                w = w.split('/')
                #print(w)
                
                year = int(w[2])
                month = int(w[0])
                day = int(w[1])
                
                w = ff.create_date_time_object(year, month, day)
                #print(w)
                
                w = w.timestamp()
                
                epochy_time = int((w*1000))
                epoch_datetime_data.append(epochy_time)
        
        
    for i in range(length_o_data):
        ex_dates_arr.append(epoch_datetime_data[i])
        rec_dates_arr.append(epoch_datetime_data[i+length_o_data])

    
    return_data = [ex_dates_arr,rec_dates_arr,div_amount_arr]
    
    return return_data

        # Copy paste data into excel
        #read data from excel into arrays
        #create date-time objects
        #reconstruct arrays with epoch dates
        #Execute dividned strategy
        #reap benefits
        
        