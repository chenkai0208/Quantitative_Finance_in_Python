# Quantitative_Finance_in_Python
In this repository, I share some practice that I have done in Python for quantitative finance research purpose. If any of the topics are studied thoroughly enough, I will split off a new repository.

## "kelly_model.py": 
This is a simulation of the famous kelly model, which is a formula used to determine the optimal size of a series of bets in order to maximise the logarithm of wealth (https://en.wikipedia.org/wiki/Kelly_criterion). It is widely used in practice to determine an optimal investment strategy. It was named after its creator J. L. Kelly, Jr, a researcher at Bell Labs in 1956. However, Kelly's idea was actually inspired by the research in information theory done by his colleague, Claude Shannon (https://en.wikipedia.org/wiki/Claude_Shannon). Rumor says that the two of them even made a big fortune using this formula when investing. I used to be an engineering student. Shannon to the old me is like Black-Scholes-Merton to the current me. This was the first bridge that I found connecting information engineering and mathematical finance, which encouraged me to choose quant as a path.

## "bsm_mcs_euro.py": 
This is a simple application of pricing a European option by Monte Carlo Simulation (https://en.wikipedia.org/wiki/Monte_Carlo_methods_in_finance). Pricing is studied thoroughly in Computational_Finance repository in a C++ configuration.

## "ARIMA.py": 
ARIMA (autoregressive integrated moving average) is a very important model in finance time series analysis (https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average). This program provides the set up of ARIMA model and also a simple optimization framework to search for the optimal parameters in the model.

## "portfolio_optimization.py": 
This is an optimization framework for portfolio construction (https://en.wikipedia.org/wiki/Portfolio_optimization). This program is a test version for our CQA (Chicago Quantitative Alliance) investment challenge.

## "implied_volatility.py": 
Implied volatility is an essential concept in pricing and fixed income modeling. In this program, I test a package that can provide implied volatility conveniently.
