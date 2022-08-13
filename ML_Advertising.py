import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def MarvellousAdversitingPredictor():

	data = pd.read_csv("Advertising.csv")
	print(data)

	print(data.head())
	print(data.shape)

	X = data['sales'].values
	#print(X)
	W = data['TV'].values
	Y = data['radio'].values
	Z = data['newspaper'].values
	
	X = X.reshape((-1,1))

	n = len(X)
	reg = LinearRegression()
	reg = reg.fit(X,W,Y)
	y_pred = reg.predict(X) 
	r2 = reg.score(X,W,Y)
	print(r2)

#Y,Z = 0.287
#Z,Y = 0.020
#W,Z = 0.655
#Z,W = 0.092
#Y,W = 0.671
#W,Y = 0.767
# The sales features of increased sale amount of R2 is 0.767(W,Y)


def main():
	print("Linear Regression Supervised Machiine Learning")
	MarvellousAdversitingPredictor()

if __name__ == "__main__":
	main()
