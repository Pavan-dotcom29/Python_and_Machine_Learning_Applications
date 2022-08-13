#Simple program without decorator
def Division(A,B):
	Ans = 0.0
	Ans = A/B;
	return Ans

def main():
	ino1 = 0
	ino2 = 0

	ino1 = int(input("Enter first number: "))
	ino2 = int(input("Enter second number:"))

	ret = Division(ino1,ino2)
	print("Division is: ",ret);

if __name__ == "__main__":
	main()