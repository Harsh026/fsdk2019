import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


dataset = pd.read_csv('Female_Stats.csv')
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0:1].values
regressor = LinearRegression()  
regressor.fit(features, labels) 
features = sm.add_constant(features)
features_opt = features[:, [0,1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
print("both independent variables are important")
print(regressor.coef_)
