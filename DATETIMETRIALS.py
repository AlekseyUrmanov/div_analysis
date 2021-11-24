import FinancialFunctions as ff
from datetime import datetime
from TDgetdata import CONSUMER_KEY as CK   #importning the consumer key
import requests





stock = 'DX'
quoteurl = r'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format(stock)
payload1 = {'apikey':CK}
content1 = requests.get(url=quoteurl, params=payload1)
data_q = (content1.json())[f'{stock}']

fulldate1 = data_q['divDate']
fulldate2 = datetime.fromisoformat(f'{fulldate1}')
print(fulldate2)



epochydater = fulldate2.timestamp()


day_after_div = int(epochydater + (1*86400))*1000
day_before_div = int(epochydater - (1*86400))*1000


pricerurl =  r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(stock)
#"https://api.tdameritrade.com/v1/marketdata/ORCL/pricehistory?apikey=Y1KS0BMRKRBSI6CVNYIHHN1NVF3VUI2J&periodType=month&frequencyType=daily&endDate=1464825600000&startDate=1464148800000"



payload2 = {'apikey': CK,                  
           'periodType':'month',
           'frequencyType': 'daily',
           'endDate':day_after_div,
           'startDate' : day_before_div,}
            #1464825600000 required
            #1633579200    given --> required (*1000) --> use ff to datetime to convert.


content2 = requests.get(url=pricerurl,params = payload2)
data_p = content2.json()
data_p = data_p['candles']
print((data_p[0])['open'])
ld = len(data_p)-1
print((data_p[ld])['close'])

a = int(((data_p[0])['datetime']) /1000)
b = int(((data_p[ld])['datetime']) /1000)


print(ff.epoch_to_datetime(a))
print(ff.epoch_to_datetime(b))











'''
i = 0
while i <1:
    
    
    stock = 'TSLA'
    url = r'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format(stock)
    payload = {'apikey':CK}
    content = requests.get(url=url, params=payload)
    data = (content.json())[f'{stock}']
    
    print(data['askPrice'])
    
    '''
    
    
    #ask q aboutt area under / above shape