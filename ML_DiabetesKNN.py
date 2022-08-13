"""
Case Study
	- Diabetes dataset determine [Outcomes] either 0 or 1
	- Diabetes based on [Glucose],[BloodPressure],[SkinThickness],[Insulin],[BMI],[DiabetesPedigreeFunction],[Age]
	- From the diabetes [Glucose],[BloodPressure],[SkinThickness],[Insulin],[BMI],[DiabetesPedigreeFunction],[Age],identify the [Outcomes]
"""

######################################

#Author : Neha Chandrakant Jagtap
#Date : 27-Feb-2022

#Classifier : Decision Tree
#Dataset : Diabetes dataset
#Features : Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
#Label : Outcomes
#Training dataset : 769 Entries
#Testing dataset : 1 Entry

######################################

#importing some required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

print("Diabetes predictor by using K Nearesr Neighbors")

#Step 1 : Reading csv file
diabetes = pd.read_csv("Marvellous_diabetes.csv")

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 enteries from Dataset")
print(diabetes.head())

print("Dimension of diabetes data : {}".format(diabetes.shape))

#Step 2 : Data Training
X_train,X_test,y_train,y_test = train_test_split(diabetes.loc[:,diabetes.columns!="Outcome"],diabetes["Outcome"],stratify=diabetes["Outcome"],random_state=66)

training_accuracy = []
test_accuracy = []

#try_neighbors from 1 to 10
neighbors_settings = range(1,11)

for n_neighbors in neighbors_settings:
	#build the model
	knn = KNeighborsClassifier(n_neighbors=n_neighbors)
	knn.fit(X_train,y_train)
	#record training set accuracy
	training_accuracy.append(knn.score(X_train,y_train))
	#record test set accuracy
	test_accuracy.append(knn.score(X_test,y_test))

plt.plot(neighbors_settings,training_accuracy,label = "training_accuracy")
plt.plot(neighbors_settings,test_accuracy,label = "test_accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.savefig("knn_compare_model")
plt.show() 

#Algorithm
knn = KNeighborsClassifier(n_neighbors=9)

#Train Algorithm
knn.fit(X_train,y_train)

#Calculate Accuracy
print("Accuracy of KNN classifier on training set : {:.2f}".format(knn.score(X_train,y_train)))
print("Accuracy of KNN classifier on test set : {:.2f}".format(knn.score(X_test,y_test)))