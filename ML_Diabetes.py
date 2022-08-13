"""
Case Study
	- Diabetes dataset determine [Outcomes] either 0 or 1
	- Diabetes based on [Glucose],[BloodPressure],[SkinThickness],[Insulin],[BMI],[DiabetesPedigreeFunction],[Age]
	- From the diabetes [Glucose],[BloodPressure],[SkinThickness],[Insulin],[BMI],[DiabetesPedigreeFunction],[Age],identify the [Outcomes]
"""

######################################

#Author : Neha Chandrakant Jagtap
#Date : 25-Feb-2022

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
from sklearn.tree import DecisionTreeClassifier

def MarvellousDiabetes():
	#Step 1 : Reading the csv file
	diabetes = pd.read_csv("Marvellous_diabetes.csv")
	print("Columns of Dataset")
	print(diabetes.columns)

	print("First 5 enteries from Dataset")
	print(diabetes.head())

	print("Dimension of diabetes data : ") 
	print(diabetes.shape) #row,col numbers

	#Step 2 : Data Training
	X_train,X_test,y_train,y_test  = train_test_split(diabetes.loc[:,diabetes.columns!="Outcome"],diabetes["Outcome"],stratify=diabetes["Outcome"],random_state=66)

	#Step 3 : Algorithm
	tree = DecisionTreeClassifier(random_state=0) #Random
	
	#Step 4 : Train the Algorithm
	tree.fit(X_train,y_train)

	#Step 5 : Calculate Accuracy 
	print("Accuracy on training set : {:.3f}".format(tree.score(X_train,y_train)))

	print("Accuracy on testing set : {:.3f}".format(tree.score(X_test,y_test)))

 #####################################################################
	#Step 1: Algorithm
	tree1 = DecisionTreeClassifier(max_depth = 3,random_state=0)
	
	#Step 2 : Train the Algorithm
	tree1.fit(X_train,y_train)

	#Step 3 : Calculate Accuracy
	print("Accuracy on training set : {:.3f}".format(tree1.score(X_train,y_train)))
	print("Accuracy on testing set : {:.3f}".format(tree1.score(X_test,y_test)))

	print("Feature importances :\n{}".format(tree1.feature_importances_))

#def plot_feature_importances_diabetes(model):
	plt.figure(figsize=(8,6))
	n_features = 8
	plt.barh(range(n_features),tree.feature_importances_,align="center") #sagle dislay krel
	diabetes_feature = [x for i,x in enumerate(diabetes.columns) if i!=8]
	plt.yticks(np.arange(n_features),diabetes_feature)
	plt.xlabel("Feature Importance")
	plt.ylabel("Feature")
	plt.ylim(-1,n_features)
	plt.show()

	plt.figure(figsize=(8,6))
	n_features = 8
	plt.barh(range(n_features),tree1.feature_importances_,align="center") #max_depth = 3,mhanun 3 display
	diabetes_feature = [x for i,x in enumerate(diabetes.columns) if i!=8]
	plt.yticks(np.arange(n_features),diabetes_feature)
	plt.xlabel("Feature Importance")
	plt.ylabel("Feature")
	plt.ylim(-1,n_features)
	plt.show()	

def main():
	print("Supervised Machine Learning")
	print("Diabetes Data set : Decision Tree ")
	MarvellousDiabetes()
	#plot_feature_importances_diabetes()

if __name__ == "__main__":
	main()