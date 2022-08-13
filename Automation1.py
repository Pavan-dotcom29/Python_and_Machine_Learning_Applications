#import statement if necessary
import sys
from sys import * 

def Addition(ino1,ino2):
	ans=0;
	ians=ino1 + ino2
	return ians
	

#Entry point of automation script
def main():
	print("------Marvellous Infosystem--------")
	print("Script name: ",argv[0])
	print("Number of argument accepted:",len(argv)-1);

	if(len(argv)>3) or(len(argv)<2):
		print("Invalid line of arguments")
		print("Use -u or -U for usage")
		print("Use -h or -H for help")
		exit()

	if (argv[1]=="-u") or (argv[1]=="-U"):
		print("Usage: Script is used to perform the addition of 2 numbers")
		exit()

	if (argv[1]=="-h") or (argv[1]=="-H"):
		print("Help: Name_of_Script_Argument First_ Second_Argument")
		exit()

	try:
		iret = Addition(int(argv[1]),int(argv[2]))
		print("Addition is: ",iret)

	except:
		print("Exception While excuting the script")
		print("Plz check the input or contact the developer")


if __name__ == "__main__":
	main()