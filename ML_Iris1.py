"""
Case Study
	- Data contains three types of flower : [setosa],[versicolor] and [virginica]
	- Flower can be based on : [sepal-length] ,[sepal-width],[petal-length] and [petal-width]
	- From the given [sepal] and [petal], identify types of flower [setosa],[versicolor] and [virginica]
"""
######################################

#Author : Neha Chandrakant Jagtap
#Date : 04-Feb-2022

#Classifier : Decision Tree
#Dataset : Iris set
#Features : sepal and petal
#Label : Iris-setosa, Iris-versicolor and Iris-virginica
#Training dataset : 150 Entries
#Testing dataset : 3 Entry

######################################

#importing some required libraries
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

#Step 1 : Loading datasets
iris = load_iris()

print("Features name of iris datasets")
#printing the features name of iris data
print(iris.feature_names) #sepal,petal

print("Target names of iris datasets")
#printing the target name of iris data
print(iris.target_names) #setosa,virnica

for i in range(len(iris.target)):
	print("ID : %d,Features %s,Label: %s"%(i,iris.data[i],iris.target[i]))

#Step 2 : Loading the data
test_index = [1,51,101]  #data gheto aah
print(test_index)

#features : sepal,petal, 
#target [iris flower cha different names] ani data(label) mhanje[0,1,2] ((Both meaning is same but features is string and data is numeric so,we want numeric data to exceute ))

train_target = np.delete(iris.target,test_index) # 0(0),1(51),2(101) delete
print(train_target)
train_data = np.delete(iris.data,test_index,axis=0) #[[6.4,3.3,4.5,1.][],[]]
print(train_data)
#1 by 3

test_target = iris.target[test_index]  #delete features kela aah [0,1,2]
print(test_target)
#trainingo,
test_data = iris.data[test_index] #delete [[6.4,3.3,4.5][],[]] delete kela aah data 
print(test_data) #disto ekde

classifier = tree.DecisionTreeClassifier() #parat shuffle kela aah data laaa

classifier.fit(train_data,train_target)  #manipulate kela aah data
#              (features,    label or target)
#             (sepal,petal),(setosa,virginca)
#       ([6.9][3.4][2.6][8.5])  ,(0,1,2)
              
print("Values that we removed for testing")
print(test_target) #delete means test_target distat
print(test_data)

print("Result of testing")
print(classifier.predict(test_data)) #ith tya delete valus predict krtoy aah
#print(classifier.predict(test_target))

