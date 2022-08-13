#Program : File Handling

def main():
	name = input("Enter name of the file that you want to seek: ")
	#fd = open(name,"r") 
	fd = open(name,"rb") 
		
	
	print("Cuurent offset: ",fd.tell())
	data = fd.read(5)

	print("Data is: ",data)
	print("Cuurent offset: ",fd.tell())


	#fd.seek(5,0)
#	fd.seek(-5,2)  #last ch print
	fd.seek(-3,2)

	print("Cuurent offset: ",fd.tell())
	data = fd.read()
	print(data)
              
if __name__ == "__main__":
	main()  

	#same code  file delelte all such files greater than one mb
	#accept directory anme,display such maximun size and delete maximum file size
	#move the file from source to destination source
	#accept folder name .png,.jpg, ,sgl pdf,.jpg, ektine kryach 
	#create the directory/folder .txt, .pdf
	