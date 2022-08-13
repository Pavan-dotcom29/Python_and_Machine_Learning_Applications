from sklearn.datasets import load_iris

iris = load_iris()

print("Features name of iris datasets")
print(iris.feature_names)

print("Target names of iris datasets")
print(iris.target_names)

print("First 10 elements frim iris datasets")

for i in range(len(iris.target)):
	print("ID : %d,Label %s,Feature : %s"%(i,iris.data[i],iris.target[i]))