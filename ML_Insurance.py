"""
Case Study
	- Data contains [age]	
	- Data is based on [bought_insurance]
	- From the given data [age] ,identified [bought_insurance]
"""

######################################

#Author : Neha Chandrakant Jagtap
#Date : 18-March-2022

#Classifier : Logistic Regression
#Dataset : Insurance
#Features : age
#Label : bought_insurance
#Training dataset : 28 Entries
#Testing dataset : 1 Entry

######################################

#importing some required libraries
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def MarvellousInsurance(path):
	df = pd.read_csv(path)
	print("-"*50)
	print("First few entries of data set")
	print(df.head())

	print("-"*50)
	plt.scatter(df.age,df.bought_insurance,marker="+",color="red")
	plt.show()

	X_train,X_test,y_train,y_test = train_test_split(df[["age"]],df.bought_insurance,train_size=0.5)
	print("Independent variables for training : ")
	print(X_train)

	print("-"*50)
	print("Dependent variables for training : ")
	print(y_train)

	print("-"*50)
	print("Independent variables for testing : ")
	print(X_test)

	print("-"*50)
	print("Dependent variables for testing : ")
	print(y_test)

	model = LogisticRegression()

	model.fit(X_train,y_train)

	print("-"*50)
	y_pred = model.predict(X_test)
	print("Predicted Dependent variables")
	print(y_pred)

	print("-"*50)
	print("Excepted Dependent variables")
	print(y_test)

	print("-"*50)
	data = model.predict_proba(X_test)
	print("Probability of above model is : ")
	print(data)

	print("-"*50)
	print("Classification report of Logistic Regression is : ")
	print(classification_report(y_test,y_pred))

	print("-"*50)
	print("Confusion matrix of Logistic Regression")
	print(confusion_matrix(y_test,y_pred))

	print("-"*50)
	print("Accuracy of Logistic Regression is : ")
	print(accuracy_score(y_test,y_pred))
	print("-"*50)

def main():
	print("-"*50)
	print("Probability of above model is: ")
	print("-"*50)

	print("Supervised Machine Learning")

	print("Logistic Regression om Insurance data set")
	print("-"*50)

	MarvellousInsurance("MarvellousInsurance_data.csv")

if __name__ == "__main__":
	main()