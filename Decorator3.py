#Program : Accept number from numbers and perform factorail by using decorator.

def Factorial(A):
	ifact = 1
	i=1
	while(i<=A):
		ifact = ifact * i
		i =i+1
	return ifact

def SmartFactorial(func_name):
	def Inner(a):
		temp = func_name(a)
		return temp
	return Inner

Factorial = SmartFactorial(Factorial)

def main():
	ino = int(input("Enter number: "))
	iret = Factorial(ino)
	print("Factorial is: ",iret)

if __name__ =="__main__":
	main()