#def Addition(value1,value2):
#	result = 0
#	result = value1+value2
#	return result

#Packages function in Addition.py File
'''Program : Accept two number from user and perform addition by using module or package file'''

import Marvellous

def main():
	print("Inside module :",__name__)
	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter seconf number: "))

	ret = Marvellous.Addition(no1,no2)
	print("Addition is :",ret)

if __name__ == "__main__":   #starter
	main()