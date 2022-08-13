#Program : Accept the input from command line argument and perform addition.

import sys
from sys import *

def main():
	print("Number of command line argument",len(sys.argv))
	print("First argument: ",argv[1])
	print("Second argument: ",argv[2])
	
	print("Datatype of argument: ",type(argv[1]))
	
	ians = int(argv[1]) + int(argv[2])
	
	print("Datatype of argument: ",type(argv[1]))
	print("Addition is: ",ians)

if __name__ == "__main__": #starter
	main()