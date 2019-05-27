import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression 

#imports the CSV dataset using pandas

dataset = pd.read_csv('Foodtruck.csv') 
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 
regressor = LinearRegression()  
regressor.fit(features, labels) 
print(regressor.intercept_)  
print (regressor.coef_)
a=np.array([3.073])
a=a.reshape(1,-1)

print (regressor.coef_*a + regressor.intercept_)
print (regressor.predict(a))