import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split

from sklearn import metrics

df=pd.read_csv('/content/diabetes.csv')

df.columns

df.isnull().sum()

plt.hist([x, y], color=['red', 'green'], label = ['exit', 'not_exit'])

X = df.drop('Outcome',axis = 1)
y1 = df['Outcome']

x = df[df['Outcome']==1]['BMI']
y= df[df['Outcome']==0]['BMI']

plt.hist([x, y], color=['red', 'green'], label = ['exit', 'not_exit'])

x = df[df['Outcome']==1]['Glucose']
y= df[df['Outcome']==0]['Glucose']

plt.hist([x, y], color=['red', 'green'], label = ['exit', 'not_exit'])

from sklearn.preprocessing import scale
X = scale(X)

# split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y1, test_size = 0.3, random_state = 42)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=7)

knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("Confusion matrix: ")
cs = metrics.confusion_matrix(y_test,y_pred)
print(cs)

print("Acccuracy ",metrics.accuracy_score(y_test,y_pred))

total_misclassified = cs[0,1] + cs[1,0]
print(total_misclassified)
total_examples = cs[0,0]+cs[0,1]+cs[1,0]+cs[1,1]
print(total_examples)
print("Error rate",total_misclassified/total_examples)
print("Error rate ",1-metrics.accuracy_score(y_test,y_pred))

print("Precision score",metrics.precision_score(y_test,y_pred))

print("Recall score ",metrics.recall_score(y_test,y_pred))

print("Classification report ",metrics.classification_report(y_test,y_pred))
