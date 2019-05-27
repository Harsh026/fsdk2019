import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt    
from sklearn.linear_model import LinearRegression 
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  
features = dataset.iloc[:, :-2].values  
labels = dataset.iloc[:, 1].values 
model1=regressor.fit(features, labels)
prediction=np.array([10])
prediction=prediction.reshape(1,-1)
print (regressor.coef_*prediction + regressor.intercept_)
print ('bahubali', regressor.predict(prediction))
features1 = dataset.iloc[:, :-2].values  
labels1 = dataset.iloc[:, 2].values 
model2=regressor.fit(features1, labels1)
prediction1=np.array([10])
prediction1=prediction1.reshape(1,-1)
print (regressor.coef_*prediction1 + regressor.intercept_)
print ("dangal", regressor.predict(prediction1))
