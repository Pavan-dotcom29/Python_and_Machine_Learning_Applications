#Named function   ...Salon madhe jaun
def Add(a,b):
	return a + b

#Lambda Function
AddX = lambda a,b : a+b #Dhadi wala baba ...speedy approcah

def main():
	ret = Add(10,20)
	print("Addition is: ",ret)
	print(type(Add))

	ret = AddX(10,20)
	print("Addition is: ",ret)
	print(type(AddX))
	print(type(lambda a,b : a+b))
	print(lambda a,b : a+b)

if __name__ == "__main__":
	main()