"""
Case Study
	- Diabetes dataset determine [Outcomes] either 0 or 1
	- Diabetes based on [Glucose],[BloodPressure],[SkinThickness],[Insulin],[BMI],[DiabetesPedigreeFunction],[Age]
	- From the diabetes [Glucose],[BloodPressure],[SkinThickness],[Insulin],[BMI],[DiabetesPedigreeFunction],[Age],identify the [Outcomes]
"""

######################################

#Author : Neha Chandrakant Jagtap
#Date : 26-Feb-2022

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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from warnings import simplefilter

simplefilter(action="ignore",category=FutureWarning)

print("Diabetes predictor by using Random Forest Classifier")

#Step 1 : Reading csv file
diabetes = pd.read_csv("Marvellous_diabetes.csv")

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 enteries from Dataset")
print(diabetes.head())

print("Dimension of diabetes data : {}".format(diabetes.shape))

#Step 2 : Data Training
X_train,X_test,y_train,y_test = train_test_split(diabetes.loc[:,diabetes.columns!="Outcome"],diabetes["Outcome"],stratify=diabetes["Outcome"],random_state=0)

#Step 3: Algorithm
rf = RandomForestClassifier(n_estimators=100,random_state=0)

#Step 4 : Train the Algorithm
rf.fit(X_train,y_train)

#Step 5 : Calculate Accuracy
print("Accuracy on training set : {:.3f}".format(rf.score(X_train,y_train)))
print("Accuracy on test set : {:.3f}".format(rf.score(X_test,y_test)))

#################################################

#Step 1 : Algorithm(RandomForestClassifier : clustering of 3)
rf1 = RandomForestClassifier(max_depth=3,n_estimators=100,random_state=0)

#Step 2 : Train the Algorithm
rf1.fit(X_train,y_train)

#Step 3 : Calculate Accuracy
print("Accuracy on training set : {:.3f}".format(rf1.score(X_train,y_train)))
print("Accuracy on test set : {:.3f}".format(rf1.score(X_test,y_test)))

def plot_feature_importances_diabetes(model):
	plt.figure(figsize=(8,6))
	n_feature = 8
	plt.barh(range(n_feature),model.feature_importances_,align="center")
	diabetes_features = [x for i,x in enumerate(diabetes.columns) if i!=8]
	plt.yticks(np.arange(n_feature),diabetes_features)
	plt.xlabel("Feature Importance")
	plt.ylabel("Feature")
	plt.ylim(-1,n_feature)	
	plt.show()

plot_feature_importances_diabetes(rf1)