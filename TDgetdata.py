import requests #for request info from url
CONSUMER_KEY = 'Y1KS0BMRKRBSI6CVNYIHHN1NVF3VUI2J'

#consumer is key is  information

import json   #for future use
OBJECT_DATA = []  #array will be filled with objects
OBJECT_DATA_VARIABLE = []
import xlsxwriter #excel writer

#Initialize some global arrays and import libraries


#Class for creating object of search instrument type
class search_instruments:
    def __init__ (self, ticker, projection, CK):        # class name witht passed variables
        self.ticker = ticker                            # Ticker is stock symbol
        self.projection = projection                    # Projection is a data type choice
        self.CK = CK                                    # CK is the consumer key

    def payload(x):
        rurl = 'https://api.tdameritrade.com/v1/instruments' 
        #url specific for a search instrument request
        payload = {'apikey':f'{x.CK}',
       'symbol': f'{x.ticker}',
       'projection': f'{x.projection}'}
        #payload parameter structure
        
        #logic loop to send payload and fomrat it on the way back
        
        if x.projection == 'fundamental':
            content = requests.get(url=rurl, params=payload)
            data = content.json()
            data = data[f'{x.ticker}']
            data = data[f'{x.projection}']
            
        else:
            content = requests.get(url=rurl, params=payload)
            data = content.json()
            data = data[f'{x.ticker}']

        return data

#choose stock
def choose_stock():

    stock_choice = input('Enter stock ticker symbol: ')
    stock_choice = stock_choice.upper()
    
    return str(stock_choice)

#choses projection for data
def choose_projection():
    print('\n----------Choose Projection----------\n')
    options = ['fundamental','symbol-search']
    choice = choose_value(options)
    
    return choice

#function that recieves arrays and outputs an options menu, then returns the choice
   
def choose_value(options):
    options = options
    choice = None
    all_values = len(options)
    print('\nChoose an option.\n')
    for i in range(all_values):
        print(f'Option {i+1}: {options[i]}')
    choice = int(input('------> '))-1

    return options[choice]

#choose type of data to retrieve
def choose_type():
    print('\n----------Choose Data Type----------\n')
    options = ['Basic Information','Historical Price Data']
    choice = choose_value(options)
    return choice

#choses period type for historical infomration
def choose_period_type():
    print('-----Choose Period Type-----')
    #Can only select either day or month data type, or else it would be too complex
    
    options  = ['day','month']
    choice = choose_value(options)
    return choice

#chooses the amounts of periods
def choose_period(x):
    print('-----Choose How Many Periods-----')
    if x == 'day':
        # for day value can only select 1-5 days
        options = ['1','2','3','4','5']
        choice = choose_value(options)
        
    else:
        #for month value, can only select 1 or 2 months
        options = ['1','2']
        choice = choose_value(options)
    return choice


#chooses a candle type
def choose_freq_type(x):
    print('-----Choose Candle Type-----')
    if x == 'day':
        options = ['minute']
        choice = choose_value(options)

    else:
        options = ['daily','weekly']
        choice = choose_value(options)
    return choice

#chooses the frequency of that candle
def choose_freq(x):
    #x is the period type
    print('-----Choose Frequency Of Candle Type-----')
    if x == 'minute':
        options = ['1','5','10','30']
        choice = choose_value(options)
    elif x == 'daily':
        options = ['1']
        choice = choose_value(options)
    else:
        options = ['1']
        choice = choose_value(options)
        
    return choice


#function for choosing if one wants extended hours data or not
def choose_extended_hours():
    print('------Do You Want Extended Hours Data------       plz say no... have merrcy on computer')
    options = ['true','false']
    choice = choose_value(options)
    return choice

#choosing variable options for price history, for construction of an object, then payload
def choose_ph_options():
    return_options = []  #empty array that will be populated later and returned
    print('\n-----Choose Options For Price History-----\n\n')
    pt = choose_period_type()
    p = choose_period(pt)
    tf = choose_freq_type(pt)
    f = choose_freq(tf)
    exthrsdta = choose_extended_hours()
    return_options = [pt,p,tf,f,exthrsdta]
    return return_options
    

#class for creating objects of type oorice history
#payload is then called on them and they return real data
class get_price_history:
    
    def __init__(self,CK, period_type, period, frequency_type, frequency, EHD, ticker):
        self.CK = CK 
        self.period_type = period_type 
        self.period = period
        self.frequency_type = frequency_type 
        self.frequency = frequency 
        self.EHD = EHD 
        self.ticker = ticker
        
        
    def payload(x):
        #url for specific call of data
        rurl =r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(x.ticker)
            # format tocker inserts the stock ticker variable, r is raw string. 
            
        payload = {'apikey': CONSUMER_KEY,                  #Simple payload structuring
                   'periodType':f'{x.period_type}',
                   'period':f'{x.period}', 
                   'frequencyType': f'{x.frequency_type}',
                   'frequency': f'{x.frequency}',
                   'needExtendedHoursData' : f'{x.EHD}'}
            
        content = requests.get(url=rurl, params=payload)
        data = content.json()
        data = data['candles']
        
        return data
        
    

#        Hard Coded Dictionaries



#--------------------------------------------------------------------------------------

col = ['A', 'B','C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE']


#this abc value array is for indexing the columns in excel, to move outputs to the right



# these are the variable values of the data that is returned from td ameritrade when i call fundamental infmoration
#I need t have these variables hard coded so i can extract them from their list, and append them to a difefrent array

fundamental_data_var_values = []
fundamental_data_var = ['symbol','high52','low52','dividendAmount','dividendYield','dividendDate',
                        'peRatio','pegRatio','pbRatio','prRatio','pcfRatio','grossMarginTTM',
                        'netProfitMarginMRQ','operatingMarginTTM','operatingMarginMRQ',
                        'returnOnEquity','returnOnAssets','returnOnInvestment','quickRatio',
                        'currentRatio','interestCoverage','totalDebtToCapital','ltDebtToEquity',
                        'totalDebtToEquity','epsTTM','epsChangePercentTTM','epsChangeYear',
                        'revChangeYear','revChangeTTM','revChangeIn','sharesOutstanding',
                        'marketCapFloat','marketCap','bookValuePerShare','shortIntToFloat',
                        'shortIntDayToCover','divGrowthRate3Year','dividendPayAmount',
                        'dividendPayDate','beta','vol1DayAvg','vol10DayAvg','vol3MonthAvg']

#Same concept but for fundmanetal data request

symbolsearch_data_var_values = []
symbolsearch_data_var =['cusip','symbol','description','exchange','assetType']


#Same concept but for historical price requets
price_history_var_values = []
price_history_var = ['open','high','low','close','volume','datetime']

#--------------------------------------------------------------------------------------


# Printing data the main function for printing to an excel sheet

def print_data():
    if len(OBJECT_DATA ) == 0:
        print('No data')
        return
    
    
    workbook= xlsxwriter.Workbook('CompanyData.xlsx')

    Basic_Company_Data= workbook.add_worksheet('Basic_Company_Information')

    #formating and excel sheet
    bold = workbook.add_format({'bold': True})
    #setting a bold variable
    Basic_Company_Data.set_column('A:A',20,bold)
    #setting column A to be width 20 and bold
    Basic_Company_Data.set_column('C:C',20,bold)
    Basic_Company_Data.set_column('E:E',20,bold)
    Basic_Company_Data.set_column('G:G',20,bold)
    Basic_Company_Data.set_column('I:I',20,bold)
    #Setting coljumn B-D-F to be width 27
    Basic_Company_Data.set_column('B:B',27)
    Basic_Company_Data.set_column('D:D',27)
    Basic_Company_Data.set_column('F:F',27)
    
    
    
    c = 0  #c is a counter for the data in OBJECT_DATA
    abc = 0   #abc is a counter to index columns in excel
    
    for i in OBJECT_DATA_VARIABLE:
        if i == 'fundamental':
            data = OBJECT_DATA[c].payload()
            #takes data at index c
            c = c+1
            for y in range(len(fundamental_data_var)):
                fundamental_data_var_values.append(data[fundamental_data_var[y]])
                Basic_Company_Data.write(f'{col[abc+1]}{y+1}',f'{fundamental_data_var_values[y]}')
                Basic_Company_Data.write(f'{col[abc]}{y+1}',f'{fundamental_data_var[y]}')
                
            fundamental_data_var_values.clear()
            abc = abc+2
        
            #{col[abc+1]}   is B column index value
            #{col[abc]}     is A column index value

        elif i =='symbol-search':
             data = OBJECT_DATA[c].payload()
             c = c+1
             for y in range(len(symbolsearch_data_var)):
                symbolsearch_data_var_values.append(data[symbolsearch_data_var[y]])
                Basic_Company_Data.write(f'{col[abc+1]}{y+1}',f'{symbolsearch_data_var_values[y]}')
                Basic_Company_Data.write(f'{col[abc]}{y+1}',f'{symbolsearch_data_var[y]}')
                
             symbolsearch_data_var_values.clear()   #clears array to prepare for the next data values that will be appended into it
             abc = abc+2
        
        else:
            data = OBJECT_DATA[c].payload()
            #takes data at index c
            c = c+1
            i = 0
            #temp_price_history = []
            
            for y in range(len(data)):
                tdata = data[y]
                
                for d in (price_history_var):
                    
                    xxx = tdata[f'{d}']
                    #temp_price_history.append(tdata[f'{d}'])
                    Basic_Company_Data.write(f'{col[abc]}{i+1}',f'{d}')
                    #print(f'{i}')
                    Basic_Company_Data.write(f'{col[abc+1]}{i+1}',f'{xxx}')
                    i = i + 1
                    #increases i to write to the next row
                #printing blanks
                Basic_Company_Data.write(f'{col[abc]}{i}','')
                Basic_Company_Data.write(f'{col[abc+1]}{i}','')
                i = i+1 #indexes i at the end to compensate for the blank spot
            
            abc = abc+2  
            
    workbook.close() #proper syntax for closing the excel sheet
    print('\nData Printed\n')
    


        


