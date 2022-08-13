def Addition(value1,value2):  #function definition
	ans = value1 + value2
	return ans

#python suports call by value, not call by reference

def main():
	print("Enter first number:  ")
	ino1 = int(input())

   #ino1 = float(input())
   # ino1 = (type(ino1)) ....float

	print(type(ino1))

	print("Enter second number:  ")
	ino2 = int(input())

	iret = Addition(value1 = ino2,value2 = ino1)  #function call
				# Keyword argument
	print("Addition is: ",iret)

if __name__ =="__main__":
	main()