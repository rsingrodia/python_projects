# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:03:14 2019
"""
stocks = ["IBM","GOOG","FB","AAPL","TSLA"]

print("The stocks in the portfolio are",stocks)

change = 'y'
change = input("Do you want to change a stock in the portfolio? y for Yes: ")

while change=='y':
    loser = input('Which stock should I change? ')

    try:
        loser_index = stocks.index(loser)
        
        newst = str(input("Enter the new stock: "))
        
      
        stocks[loser_index] = newst
        
        print("Now the stocks in the portfolio are",stocks)
        change = input("Do you want to change another stock? y for Yes: ")
        
    
    
    except ValueError:
        print('That stock is not in the portfolio!')