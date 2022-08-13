#import Marvellous
from Marvellous import *
#import Marvellous as M
#import Marvellous1
from Marvellous1 import *

#Importing module of Marvellous.py/Marvellous1.py and function Addition and Subtraction.
'''Program : Accept two number from user and perform addition by using module or package file'''

def main():
	print("Inside module :",__name__)
	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number: "))

	#ret1 = Marvellous.Addition(no1,no2)   #import krtoy i line madhun
	ret1 = Addition(no1,no2)   # * he sagl  gheun yetoy
	print("Addition is :",ret1)

	#ret2 = Marvellous1.Subtraction(no1,no2)
	#print("Subtraction :",ret2)

	#ret3 = Marvellous1.Addition1(no1,no2)
	#print("Addition1 :",ret3)
	
	ret2 = Subtraction(no1,no2)
	print("Subtraction :",ret2)

	ret3 = Addition1(no1,no2)
	print("Addition1 :",ret3)

if __name__ == "__main__":   #starter
	main()