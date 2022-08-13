# We have to display 5 times "Hello" om screen

def Iteration():
	no = 0
	while(no < 5):
		print("Hello")
		no = no + 1
		#no += 1

def Sequence():
	print("Hello")
	print("Hello")
	print("Hello")
	print("Hello")
	print("Hello")

def main():
	#Sequence()
	Iteration()

if __name__ == "__main__":
	main()