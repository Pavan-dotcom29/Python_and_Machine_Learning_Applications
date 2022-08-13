
def MarvellousTitanicPredictor():
	#step1 : Load Data
	titanic_data = pd.read_csv("MarvellousTitanic.csv")

	print("First 5 enteries from load datasets")
	print(titanic_data.head())
	print(titanic_data.shape)

	#step2 : Analyze data
	print("Visualisation : Survived and non - survved passengers")
	figure()
	target = "Survived"

def main():
	print("Supervised Machine Learning")
	print("Logistic Regression")
	MarvellousTitanicPredictor()


if __name__ =="__main__":
	main()