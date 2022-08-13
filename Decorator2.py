#Program : Accept number from numbers and perform addition by using decorator.

def Addition(A):
	ans=0
	ans=A + 1;
	return ans
def Sub(B):
	ans = 0
	ans = B-1
	return ans

def SmartAddition(func_name):
	def Inner(x):
		temp = func_name(x)
		return temp
	return Inner

Addition = SmartAddition(Addition)
Sub = SmartAddition(Sub)

def main():
	ino1=0
	ino2=0

	iret = Addition(3)
	iret=0
	iret1= Sub(5)
	print("Addition is: ",iret)
	print("Subtraction is :",iret1)
	
if __name__ == "__main__":
	main()