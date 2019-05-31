
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

df = pd.read_fwf("Auto_mpg.txt")
df.columns=[ "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
print("car name:",df['car name'][df['mpg']==max(df['mpg'])])
features=df.drop(['car name','mpg'],axis=1)
labels=df['mpg']
features['horsepower']=features['horsepower'].replace(['?'],features['horsepower'].mode()) 
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 
from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})    
lst=[6,215,100,2630,22.2,80,3]
lst=np.array(lst)
lst=lst.reshape(1,-1)
regressor.predict(lst)




