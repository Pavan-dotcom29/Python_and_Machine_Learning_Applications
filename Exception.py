#Program : Accept number from user and perfrom division bu using exception handling.

def Division(A,B):

	ans = 0.0
	 
	try:
		ans = A/B
	
	except ZeroDivisionError:
		print("Exception Occured")
	
	finally:
		print("Inside finally")	
	return ans

def main():
	ino1 = int(input("Enter first number: "))
	ino2 = int(input("Enter second number:"))

	ret = Division(ino1,ino2)

	print("Division is: ",ret)

if __name__ == "__main__":
	main()