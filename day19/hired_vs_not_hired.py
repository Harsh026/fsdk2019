"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers , didn't went to any top-tire school, having Master's Degree with Internship.


"""



import sklearn  as sk
import pandas as pd
import numpy as np


dataset = pd.read_csv('PastHires.csv')
dataset=dataset.replace({"Y":1,"N":0,"BS":0,"MS":1,"PhD":2})
print(dataset)

features = dataset.iloc[:, 0:6].values
labels = dataset.iloc[:, -1].values

#for decisiontree
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.40)  

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 



df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df  



from sklearn.metrics import confusion_matrix  
cm=confusion_matrix(labels_test, labels_pred)
    
classifier.score(features_test,labels_pred)    



#for random.........................

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  



from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test) 


from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)


from sklearn.metrics import confusion_matrix  
cm=confusion_matrix(labels_test, labels_pred)
    
classifier.score(features_test,labels_pred) 


#>..................................


x = np.array([[10,1,4,0,1,0]])   
x=x.reshape(1,-1)
x= classifier.predict(x)

if x==0:
    print("not hired")
else:
    print("hired")    



#...........................


x = np.array([[10,0,4,1,0,1]])   
x=x.reshape(1,-1)
x= classifier.predict(x)[0]

if x==0:
    print("not hired")
else:
    print("hired")    







 

