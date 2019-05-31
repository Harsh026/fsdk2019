import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk  

dataset = pd.read_csv('affairs.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6])
features = onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder = OneHotEncoder(categorical_features = [11])
features = onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

probability = classifier.predict_proba(features_test)

labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
a=classifier.score(features_train,labels_train)
