""" 
Case Study
	- Data contain two types of Ball : [Tennis] and [Cricket]
	- Ball can be identified based on [Weight] and [Surface]
	- From  the given [Weight] and [Surface] ,identify type of ball (Tennis or Cricket)
"""

######################################

#Author : Neha Chandrakant Jagtap
#Date : 01-Feb-2022

#Classifier : Decision Tree
#Dataset : Ball set
#Features : Weight and Surface
#Label : Tennis and Cricket
#Training dataset : 15 Entries
#Testing dataset : 1 Entry

######################################

#importing some required libraries
from sklearn import tree

def MarvellousMl(weight,surface):
	# Step 1 : Get the Data
	BallFeatures = [[35,1],[47,1],[90,0],[56,1],[67,0],[34,0],[78,1],[53,1]]

	Names = [1,1,0,1,0,0,1,1]

	# Step 2 : Algorithm
	clf = tree.DecisionTreeClassifier()

	# Step 3 : Train the Algorithm
	# [fit] method is use to train algorithm
	clf = clf.fit(BallFeatures,Names)

	# Step 4 : Data Testing
	result = clf.predict([[weight,surface]])

	if result == 1:
		print("Your objects looks like Tennis ball")

	elif result == 0:
		print("Your objects looks like Cricket ball")

def main():
	print("Enter the weight of object")
	weight = input()

	print("What is the surface type of your object Rough or Smooth")
	surface = input()

	if surface.lower() =="rough":
		surface =1
	elif surface.lower() == "smooth":
		surface =0
	else:
		print("Error : Wrong input")
		exit()

	MarvellousMl(weight,surface)

if __name__ == "__main__":
	main()