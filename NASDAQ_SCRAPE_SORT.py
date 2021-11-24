import NASDAQ_SCRAPE as NS
import pandas as pd
import numpy as np
import FinancialFunctions_2 as ff2
import FinancialFunctions as ff
import NASDAQ_SCRAPE as NS

def NASDAQ_SCRAPE_SORT_DATES(stock,terms):
    
    #terms to shorten array due to historical data issues
    # Datar will equal to NS.scrape_div_dates(stock)
    datar = NS.scrape_div_dates(stock)
    '''
    datar ={'data': {'exDividendDate': '10/08/2021',
                 'dividendPaymentDate': '10/26/2021', 'yield': '1.34%', 'annualizedDividend': '1.28',
                 'payoutRatio': '19.95', 'dividends': {'headers': {'exOrEffDate': 'Ex/EFF DATE', 
                'type': 'TYPE', 'amount': 'CASH AMOUNT', 'declarationDate': 'DECLARATION DATE',
                'recordDate': 'RECORD DATE', 'paymentDate': 'PAYMENT DATE'}, 
                 'rows': [{'exOrEffDate': '10/08/2021', 
                'type': 'CASH', 'amount': '$0.32', 'declarationDate': '09/13/2021', 
                'recordDate': '10/12/2021', 'paymentDate': '10/26/2021'}, {'exOrEffDate': '07/14/2021',
                'type': 'CASH', 'amount': '$0.32', 'declarationDate': '06/15/2021', 'recordDate': '07/15/2021', 'paymentDate': '07/29/2021'}, {'exOrEffDate': '04/07/2021', 'type': 'CASH', 'amount': '$0.32', 'declarationDate': '03/10/2021', 'recordDate': '04/08/2021', 'paymentDate': '04/22/2021'}, {'exOrEffDate': '01/06/2021', 'type': 'CASH', 'amount': '$0.24', 'declarationDate': '12/10/2020', 'recordDate': '01/07/2021', 'paymentDate': '01/21/2021'}, {'exOrEffDate': '10/07/2020', 'type': 'CASH', 'amount': '$0.24', 'declarationDate': '09/10/2020', 'recordDate': '10/08/2020', 'paymentDate': '10/22/2020'}, {'exOrEffDate': '07/14/2020', 'type': 'CASH', 'amount': '$0.24', 'declarationDate': '06/16/2020', 'recordDate': '07/15/2020', 'paymentDate': '07/28/2020'}, {'exOrEffDate': '04/08/2020', 'type': 'CASH', 'amount': '$0.24', 'declarationDate': '03/12/2020', 'recordDate': '04/09/2020', 'paymentDate': '04/23/2020'}, {'exOrEffDate': '01/08/2020', 'type': 'CASH', 'amount': '$0.24', 'declarationDate': '12/12/2019', 'recordDate': '01/09/2020', 'paymentDate': '01/23/2020'}, {'exOrEffDate': '10/09/2019', 'type': 'CASH', 'amount': '$0.24', 'declarationDate': '09/11/2019', 'recordDate': '10/10/2019', 'paymentDate': '10/24/2019'}, {'exOrEffDate': '07/16/2019', 'type': 'CASH', 'amount': '$0.24', 'declarationDate': '06/18/2019', 'recordDate': '07/17/2019', 'paymentDate': '07/31/2019'}, {'exOrEffDate': '04/10/2019', 'type': 'CASH', 'amount': '$0.24', 'declarationDate': '03/14/2019', 'recordDate': '04/11/2019', 'paymentDate': '04/25/2019'}, {'exOrEffDate': '01/15/2019', 'type': 'CASH', 'amount': '$0.19', 'declarationDate': '12/17/2018', 'recordDate': '01/16/2019', 'paymentDate': '01/30/2019'}, {'exOrEffDate': '10/15/2018', 'type': 'CASH', 'amount': '$0.19', 'declarationDate': '09/17/2018', 'recordDate': '10/16/2018', 'paymentDate': '10/30/2018'}, {'exOrEffDate': '07/16/2018', 'type': 'CASH', 'amount': '$0.19', 'declarationDate': '06/19/2018', 'recordDate': '07/17/2018', 'paymentDate': '07/31/2018'}, {'exOrEffDate': '04/16/2018', 'type': 'CASH', 'amount': '$0.19', 'declarationDate': '03/16/2018', 'recordDate': '04/17/2018', 'paymentDate': '05/01/2018'}, {'exOrEffDate': '01/09/2018', 'type': 'CASH', 'amount': '$0.19', 'declarationDate': '12/14/2017', 'recordDate': '01/10/2018', 'paymentDate': '01/24/2018'}, {'exOrEffDate': '10/10/2017', 'type': 'CASH', 'amount': '$0.19', 'declarationDate': '09/12/2017', 'recordDate': '10/11/2017', 'paymentDate': '10/25/2017'}, {'exOrEffDate': '07/17/2017', 'type': 'CASH', 'amount': '$0.19', 'declarationDate': '06/22/2017', 'recordDate': '07/19/2017', 'paymentDate': '08/02/2017'}, {'exOrEffDate': '04/10/2017', 'type': 'CASH', 'amount': '$0.19', 'declarationDate': '03/16/2017', 'recordDate': '04/12/2017', 'paymentDate': '04/26/2017'}, {'exOrEffDate': '01/03/2017', 'type': 'CASH', 'amount': '$0.15', 'declarationDate': '12/16/2016', 'recordDate': '01/05/2017', 'paymentDate': '01/26/2017'}, {'exOrEffDate': '10/07/2016', 'type': 'CASH', 'amount': '$0.15', 'declarationDate': '09/16/2016', 'recordDate': '10/12/2016', 'paymentDate': '10/26/2016'}, {'exOrEffDate': '07/01/2016', 'type': 'CASH', 'amount': '$0.15', 'declarationDate': '06/16/2016', 'recordDate': '07/06/2016', 'paymentDate': '07/27/2016'}, {'exOrEffDate': '04/12/2016', 'type': 'CASH', 'amount': '$0.15', 'declarationDate': '04/11/2016', 'recordDate': '04/14/2016', 'paymentDate': '04/28/2016'}, {'exOrEffDate': '01/04/2016', 'type': 'CASH', 'amount': '$0.15', 'declarationDate': '12/16/2015', 'recordDate': '01/06/2016', 'paymentDate': '01/27/2016'}, {'exOrEffDate': '10/09/2015', 'type': 'CASH', 'amount': '$0.15', 'declarationDate': '11/03/2015', 'recordDate': '10/14/2015', 'paymentDate': '10/28/2015'}, {'exOrEffDate': '07/06/2015', 'type': 'CASH', 'amount': '$0.15', 'declarationDate': '06/17/2015', 'recordDate': '07/08/2015', 'paymentDate': '07/29/2015'}, {'exOrEffDate': '04/02/2015', 'type': 'CASH', 'amount': '$0.15', 'declarationDate': '03/17/2015', 'recordDate': '04/07/2015', 'paymentDate': '04/28/2015'}, {'exOrEffDate': '01/05/2015', 'type': 'CASH', 'amount': '$0.12', 'declarationDate': '12/18/2014', 'recordDate': '01/07/2015', 'paymentDate': '01/28/2015'}, {'exOrEffDate': '10/06/2014', 'type': 'CASH', 'amount': '$0.12', 'declarationDate': '09/18/2014', 'recordDate': '10/08/2014', 'paymentDate': '10/29/2014'}, {'exOrEffDate': '07/07/2014', 'type': 'CASH', 'amount': '$0.12', 'declarationDate': '06/20/2014', 'recordDate': '07/09/2014', 'paymentDate': '07/30/2014'}, {'exOrEffDate': '04/04/2014', 'type': 'CASH', 'amount': '$0.12', 'declarationDate': '03/19/2014', 'recordDate': '04/08/2014', 'paymentDate': '04/29/2014'}, {'exOrEffDate': '01/03/2014', 'type': 'CASH', 'amount': '$0.12', 'declarationDate': '12/19/2013', 'recordDate': '01/07/2014', 'paymentDate': '01/28/2014'}, {'exOrEffDate': '10/04/2013', 'type': 'CASH', 'amount': '$0.12', 'declarationDate': '09/19/2013', 'recordDate': '10/08/2013', 'paymentDate': '10/29/2013'}, {'exOrEffDate': '07/10/2013', 'type': 'CASH', 'amount': '$0.12', 'declarationDate': '06/21/2013', 'recordDate': '07/12/2013', 'paymentDate': '08/02/2013'}]}}, 'message': None, 'status': {'rCode': 200, 'bCodeMessage': None, 'developerMessage': None}}
                                                                           
           '''            
                                                                           
    data = datar['data']

    ex_div_date = []
    rec_div_date = []
    div_amount = []

    data  = data['dividends']
    data = data['rows']

    #print(len(data))
    #data = data['']
    
    limiter = 0
    for i in data:
        
        if limiter < terms:
        
            ex_div_date.append(i['exOrEffDate'])
            rec_div_date.append(i['recordDate'])
            div_amount.append(i['amount'])
            limiter = limiter +1   
        else:
            break
     
        
    # creates pandas data frame with theses 3 column names
    #passes it into the date to epoch function for future use
    
    # ['Ex Date']
    # ['Rec Date']
    # ['Div$']

    l = len(div_amount)
    numpy_data_arr = np.array([ex_div_date,rec_div_date,div_amount]).T
    #print(np.shape(numpy_data_arr))
    
    
    df = pd.DataFrame(data=numpy_data_arr,index=np.arange(l), columns=["Ex Date", "Rec Date", "Div$"])
    #.get('')
    #print(df)
    return df


def NASDAQ_SCRAPE_DIV_LIST(scraped_list):
    
    #Returns list of stocks to be used in Evaluation
    #This will be equal to NS.scrape_upcoming_divs(date)
    
    stock_div_list = []
    datar_stocks_divs = scraped_list
    
    #datar_stocks_divs = {'data': {'calendar': {'headers': {'symbol': 'Symbol', 'companyName': 'Name',
    #'dividend_Ex_Date': 'Ex-Dividend Date', 'payment_Date': 'Payment Date', 'record_Date': 'Record Date',
    #'dividend_Rate': 'Dividend', 'indicated_Annual_Dividend': 'Indicated Annual Dividend', 
    #'announcement_Date': 'Announcement Date'}, 'rows': [{'companyName': 'Itau Unibanco Banco Holding SA',
    #'symbol': 'ITUB', 'dividend_Ex_Date': '11/22/2021', 'payment_Date': 'N/A', 'record_Date': '11/23/2021',
    #'dividend_Rate': 0.035, 'indicated_Annual_Dividend': 0.136, 'announcement_Date': '11/01/2021'},
    
    data = datar_stocks_divs['data']
    data = data['calendar']
    data = data['rows']
    
    for i in data:
        stock_div_list.append(i['symbol'])
    
    
    return stock_div_list
    



'''
real_stock_date_data = NASDAQ_SCRAPE_SORT_DATES()
#print(real_stock_date_data)


epoch_stock_date_data = ff2.excel_date_data_too_epoch_dollar_data(real_stock_date_data)


#limit entries to 24, because td does not have so much historical data
# chnagfe limit based on frequency of dividend, if medium or low payout then 24 = 6 years. asusming 4x year

x_dates = epoch_stock_date_data[0]
r_dates = epoch_stock_date_data[1]
d_amounts = epoch_stock_date_data[2]


final_data = ff.dividend_capture(x_dates, r_dates, 'ORCL', 100, 1, d_amounts,24)


print(final_data)'''











