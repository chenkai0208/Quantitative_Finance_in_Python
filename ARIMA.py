#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 21:58:37 2018

@author: chenkai
"""

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas.tools.plotting import autocorrelation_plot
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from arch import arch_model
from sklearn.metrics import mean_squared_error
import pandas
import numpy as np

def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

def _get_best_model(TS):
    best_aic = np.inf 
    best_order = None
    best_mdl = None

    pq_rng = range(5) # [0,1,2,3,4]
    d_rng = range(3) # [0,1]
    for i in pq_rng:
        for d in d_rng:
            for j in pq_rng:
                try:
                    tmp_mdl = ARIMA(TS, order=(i,d,j)).fit(
                        method='mle', trend='nc'
                    )
                    tmp_aic = tmp_mdl.aic
                    if tmp_aic < best_aic:
                        best_aic = tmp_aic
                        best_order = (i, d, j)
                        best_mdl = tmp_mdl
                except: continue
    print('aic: {:6.5f} | order: {}'.format(best_aic, best_order))                    
    return best_aic, best_order, best_mdl


# plot the data
#series = read_csv('shampoo-sales.csv',  header=0, nrows=36, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
df = read_csv('result.csv')
p1 = df['P1_Value'].values.tolist()
date = df['Date'].values.tolist()
series = pandas.Series(data=p1,index=date)
series.index = pandas.to_datetime(series.index)
print(series.head())
series.plot()
pyplot.show()

# res_tup = _get_best_model(series) # get the best parameters for ARIMA. Failed...

#am = arch_model(series, p=1, o=0, q=1, dist='StudentsT')
#res = am.fit(update_freq=5)
#print(res.summary())


# plot the autocorrelation
autocorrelation_plot(series)
pyplot.show()

# fit model
model = ARIMA(series, order=(20,2,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())

"""
# new data
p2 = df['P3_Value'].values.tolist()
series2 = pandas.Series(data=p2,index=date)
series2.index = pandas.to_datetime(series2.index)
Y = series2.values
series2.plot()
pyplot.show()

# make some predictions
X = series.values
size = int(len(X) * 0.90)
train, test = X[0:size], Y[size:len(X)]

# use exponential function to replace test set
# test_index = np.array([i for i in range(len(test))])
# test = test_index * test_index

history = [x for x in train]
predictions = list()
for t in range(len(test)):
    #model = arch_model(series, p=1, o=0, q=1, dist='StudentsT')
    model = ARIMA(history, order=(5,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]    # output format for ARIMA
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()
"""
