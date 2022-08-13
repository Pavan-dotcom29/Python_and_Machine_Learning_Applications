#Program : Accept number from numbers and perform division by using decorator.

def Division(A,B): #6
	Ans = 0.0
	Ans = A/B;
	return Ans

def DivisionX(func_name):
	def Inner(a,b):  #3
		if a < b:  
			a,b = b,a
		return func_name(a,b)  # 5....func_name(Division)

	return Inner # 4  inner return hoil

Division  = DivisionX(Division)  #1

def main():
	ino1 = 0
	ino2 = 0

	ino1 = int(input("Enter first number: "))
	ino2 = int(input("Enter second number:"))

	ret = Division(ino1,ino2)#2
	print("Division is: ",ret);

if __name__ == "__main__":
	main()