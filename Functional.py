Addition = lambda a,b : a+b

def main():
	print("Enter first number: ")
	ino1 = int(input())

	print("Enter second number: ")
	ino2 = int(input())

	iret = Addition(ino1,ino2)
	print("Addition is: ",iret)

if __name__ == "__main__":
	main()