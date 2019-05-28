import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


dataset = pd.read_csv('bluegills.csv')
features = dataset.iloc[:, 0:1 ].values
labels = dataset.iloc[:, 1:].values
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)

plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('age')
plt.ylabel('length')
plt.show()

lst=np.array([5])
lst=lst.reshape(1,-1)
lin_reg_2.predict(poly_object.fit_transform(lst))
