#Program : File Handling

def main():
	name = input("Enter name of the file that you want to open: ")
	fd = open(name,"w") #data is preseved
				#  "a"	 (data preserved it means we append data)

	print("File get created Successfully: ",fd)
	data = input(print("Enter the data that you want to write in file: "))
	fd.write(data)

	fd.close()

if __name__ == "__main__":
	main()