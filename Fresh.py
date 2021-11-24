#starter
CONSUMER_KEY = 'Y1KS0BMRKRBSI6CVNYIHHN1NVF3VUI2J'

import requests

import pandas as pd
import math as m
import numpy as np


def menu():
    print('\n Do you want to get more data or exit')
    options = ['GET DATA','EXIT']
    choice = choose(options)
    
    if choice =='GET DATA':
        get_data()
    else:
        return


def choose(options):
    
    for i in range(len(options)):
        print(f'Choice {i+1} : {options[i]}')
        
    choice = int(input('Choice : '))
    
    return options[choice-1]


def get_data():
    
    
    options = ['fundamental','symbol-search']
    stock_options = ['GOOG','AAPL','CRTX','BABA']
    
    print('\nChoose Projection:')
    projection_choice = choose(options)

    print('\nChoose a stock\n')
    stock_choice = choose(stock_options)


    url = 'https://api.tdameritrade.com/v1/instruments'



    payload = {'apikey':CONSUMER_KEY, 
       'symbol': stock_choice,
       'projection': f'{projection_choice}'}


    content = requests.get(url=url, params=payload)


    data = content.json()

    data = data[f'{stock_choice}']


    print(f'Here is ur data : {data}')
    
    menu()
    
    
menu()

