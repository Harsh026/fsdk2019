import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


dataset = pd.read_csv('iq_size.csv')
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0].values
regressor = LinearRegression()  
regressor.fit(features, labels) 
features = sm.add_constant(features)
features_opt = features[:, [0,1, 2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
features_opt = features[:, [0,1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
features_opt = features[:, [1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
print("brain size is more important")
plt.scatter(features_opt,labels)
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features_opt)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('bs')
plt.ylabel('iq')
plt.show()

lst=np.array([90])
lst=lst.reshape(1,-1)

a=lin_reg_2.predict(poly_object.fit_transform(lst))

print("at brain size 90 : ",a[0])