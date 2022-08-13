"""
Case Study
	- Data contains 13 indepedent features
	- Data identified based on [malignant] and [benign]
	- From this given features , identified malignant or benign
"""

######################################

#Author : Neha Chandrakant Jagtap
#Date : 24-March-2022

#Classifier : Support vector system
#Dataset : Breast cancer
#Features : 13 features
#Label : malignant and benign
#Training dataset : 569 Entries
#Testing dataset : 1 Entry

######################################

#importing some required libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

def MarvellousSVM():
	#Step 1: Load dataset
	cancer = datasets.load_breast_cancer()

	#print the names of 13 features
	print("Features of the cancer dataset  : ",cancer.feature_names)

	#print the data(feature)shape
	print("Labels of the cancer dataset : ",cancer.data.shape)

	#print the cancer data features (top 5 records)
	print("First 5 records are :")
	print(cancer.data[0:5])

	#print the labels (0:malignant,1:benign)
	print("Target of dataset : ",cancer.target)

	#Step 2 :Split dataset into training set and test set
	X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109) 
	#                                                                      70% training and 30% test

	#Create a svm classifier
	clf = svm.SVC(kernel = "linear") #Linear kernel

	#Step 3: train the model using the training data
	clf.fit(X_train,y_train)

	#Step 4 : Predict the response for test dataset
	y_predict = clf.predict(X_test)

	#Step 5 : Calculate Model Accuracy 
	print("Accuracy of the model is : ",metrics.accuracy_score(y_test,y_predict)*100)

def main():
	print("--------------Support Vector Machine----------")
	MarvellousSVM()

if __name__ == "__main__":
	main()