#Program : Accept the input from command line argument.

import sys
from sys import *

def main():
	print("Number of command line argument",len(sys.argv))
	#print("Nmae of Application is: ",sys.argv[0])
	print("Nmae of Application is: ",argv[0])
	#print("First argument: ",argv[1])
	#print("Second argument: ",argv[2])

	print("Commnad line argument: ")
	for i in argv:
		print(i)

if __name__ == "__main__":
	main()