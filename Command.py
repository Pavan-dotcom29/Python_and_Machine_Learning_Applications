#Program : Accept the input from command line argument.

import sys
from sys import *

def main():
	print("Number of command line argument",len(sys.argv))

	#print("Name of Application is: ",sys.argv[0])
	print("Name of Application is: ",argv[0])
	print("First argument: ",argv[1])
	print("Second argument: ",argv[2])

if __name__ == "__main__":
	main()