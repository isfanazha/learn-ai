# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
from sklearn import datasets
dataset = datasets.load_wine()
X = dataset.data
y = dataset.target

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier
# Choose the best K parameter
classifier = KNeighborsClassifier(n_neighbors=7)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

# Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Evaluate model
from sklearn import metrics
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))



