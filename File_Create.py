#Program : File Handling
def main():
	name = input("Enter name of the file that you want to create: ")
	fd = open(name,"x")

	print("File get created Successfully: ",fd)

if __name__ == "__main__":
	main()