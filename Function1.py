def Addition(value1,value2):  #function definition
	ans = value1 + value2
	return ans

#python suports call by value, not call by reference

def main():
	print("Enter first number:  ")
	ino1 = int(input())
	print("Enter second number:  ")
	ino2 = int(input())
	iret = Addition(ino1,ino2)  #function call
				# postional argument...ino1,ino2
	print("Addition is: ",iret)

if __name__ =="__main__":
	main()