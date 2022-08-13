#import statement if necessary
import sys
from sys import * 

#Entry point of automation script
def main():
	print("------Marvellous Infosystem--------")
	print("Script name: ",argv[0])
	print("Number of argument accepted:",len(argv)-1);
	
	if(len(argv)>3) or(len(argv)<2):
		print("Invalid line of arguments")
		exit()

	if (argv[1]=="-u") or (argv[1]=="-U"):
		print("Usage: Script is used to perform the addition of 2 numbers")
		exit()

	if (argv[1]=="-h") or (argv[1]=="-H"):
		print("Help: Name_of_Script_Argument First_ Second_Argument")
		exit()

if __name__ == "__main__":
	main()