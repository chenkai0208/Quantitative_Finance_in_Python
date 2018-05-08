#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 2017

Description:
Input: symbols of chosen stocks
    Randomly assign weights to given stocks. 
    Calculate portfolio return, volatility, and Sharp Ratio.
Output: portfolio with maximum SR or minimum volatility

@author: chenkai
"""
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt


#list of stocks in portfolio, i.e. stocks = ['AAPL','AMZN','MSFT','YHOO']
my_position = pd.read_csv('/Users/chenkai/Documents/Financial Analysis/cqa_challenge/OpenPosition_11_26_2017.csv')
stocks = my_position['Symbol']

#download daily price data for each of the stocks in the portfolio
data = web.DataReader(stocks,data_source='google',start='01/01/2010')['Close']

#convert daily stock prices into daily returns
returns = data.pct_change()

#calculate mean daily return and covariance of daily returns
mean_daily_returns = returns.mean()
cov_matrix = returns.cov()

#set number of runs of random portfolio weights
num_portfolios = 25000

#set up array to hold results
#We have increased the size of the array to hold the weight values for each stock
results = np.zeros((4+len(stocks)-1,num_portfolios))

for i in range(num_portfolios):
    #select random weights for portfolio holdings
    weights = np.array(np.random.random(len(stocks)))
    #rebalance weights to sum to 1
    weights /= np.sum(weights)
    
    #calculate portfolio return and volatility
    portfolio_return = np.sum(mean_daily_returns * weights) * 250
    portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights))) * np.sqrt(250)
    
    #store results in results array
    results[0,i] = portfolio_return
    results[1,i] = portfolio_std_dev
    #store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
    results[2,i] = results[0,i] / results[1,i]
    #iterate through the weight vector and add data to results array
    for j in range(len(weights)):
        results[j+3,i] = weights[j]

#convert results array to Pandas DataFrame
results_frame = pd.DataFrame(results.T)
result_list = pd.Series(['ret','stdev','sharpe'])
result_list = result_list.append(stocks)
result_list = result_list.reset_index(drop=True)
results_frame.rename(columns=result_list,inplace=True)


#locate position of portfolio with highest Sharpe Ratio
max_sharpe_port = results_frame.iloc[results_frame['sharpe'].idxmax()]
#locate positon of portfolio with minimum standard deviation
min_vol_port = results_frame.iloc[results_frame['stdev'].idxmin()]

#create scatter plot coloured by Sharpe Ratio
plt.scatter(results_frame.stdev,results_frame.ret,c=results_frame.sharpe,cmap='RdYlBu')
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.colorbar()
#plot red star to highlight position of portfolio with highest Sharpe Ratio
plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=1000)
#plot green star to highlight position of minimum variance portfolio
plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=1000)