def Batches1(name,fees):
	print("Batches1 name: ",name)
	print("Batches1 fees: ",fees)

def Batches2(name,fees):
	print("***************Keyworf argument****************")
	print("Batches1 name: ",name)
	print("Batches1 fees: ",fees)


def Batches3(name,fees,Nationality="India"):
	print("**************Default argument****************")
	print("Batches3 name:",name)
	print("Batches3 fees: ",fees)
	print("Batches3 Nationality: ",Nationality)

def Addition(*ino):
	print("**************Variable argument*****************")
	ians=0
	for i in ino:
		ians = ians + i
	return ians

def StudentInfo(**other):
	print("*************Key variable***********")
	for i,j in other.items():
		print(i,j)


def main():
	#Postional argument
	Batches1("Python",5000)
	Batches1(5000,"Lb")

	Batches2(fees = 7000,name="PPA")
	Batches2(name= "LSP",fees=8000)

	Batches3("Neha",12000)
	Batches3("Rohit",15000,"Maldives")

	ret = Addition(10,20,30)
	print("Addition is: ",ret)

	StudentInfo(age="15",Address="Mira road",Mobile="34464578743",City="Mumbai")
if __name__ == "__main__":
	main()