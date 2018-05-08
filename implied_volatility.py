#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wallstreet package can be found in the following link
https://pypi.python.org/pypi/wallstreet/0.1.5
@author: chenkai
"""
from wallstreet import Stock, Call, Put
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
g = Call('SPX', d=20, m=7, y=2018,source='yahoo');

x = g.strikes;
y = np.zeros(len(x));
for i in range(len(x)):
    g.set_strike(x[i]);
    y[i] = g.implied_volatility();

plt.plot(x,y);
plt.scatter(x,y);