def Addition(*value): # kiti pn gheyy te arbitary(random) * mhanje sagl gheun yee
	sum = 0
	for i in value:
		sum = sum + i;

	return sum
	

def main():
	iret = Addition(10,20,30,40,50)  #type tuple
	print("Addition is:  ",iret)

	iret = Addition(10,20,30,40)  #type tuple
	print("Addition is:  ",iret)

	iret = Addition()  #type tuple
	print("Addition is:  ",iret)


if __name__ == "__main__":
	main()