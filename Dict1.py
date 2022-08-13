#Program : Accept batch name and show the output of fees is there or not by using dictornary.

def main():
		# [Python ,PPA, LSP, Angular]
	#fees = [12500,15000,21000,15500]
	fees = {"Python": 12500,"PPA": 15000,"LSP": 21000,"Angular": 15500}
	print(fees)

	print("Please Enter batch name")
	batch = input()

	print("Thank ypu for selecting: ",batch)

	print("Fees is:  ",fees[batch])

if __name__ == "__main__":
	main()