# API for Nasdaq Dividend Data.

import quandl
import requests
import pandas as pd



stock = 'ORCL'


def scrape_div_dates(stock):
    

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://www.nasdaq.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.nasdaq.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Cache-Control': 'max-age=0',
        'TE': 'trailers',
        }
    
    params = (
    ('assetclass', 'stocks'),
                )
    
    url = r'https://api.nasdaq.com/api/quote/{}/dividends'.format(stock)
    response = requests.get(url, headers=headers, params=params)

    content = response.json()
    return content
    

    #print(content)


def scrape_upcoming_divs(date):
    
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'https://www.nasdaq.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.nasdaq.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Cache-Control': 'max-age=0',
    }
    #2021-11-22 format of date call
    
    params = (
    ('date', date),
    )
    
    response = requests.get('https://api.nasdaq.com/api/calendar/dividends', headers=headers, params=params)
    content = response.json()
    
    
    return content
    
    













    