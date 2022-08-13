#Program : File Handling

def main():
	name = input("Enter name of the file that you want to open: ")
	fd = open(name,"r") 
		
	print("File get created Successfully: ",fd)

	data = fd.read(5)
	print("Data is: ",data)

	fd.close()

if __name__ == "__main__":
	main()