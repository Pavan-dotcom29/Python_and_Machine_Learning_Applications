#				 Default argument  ..Nationality india sarkh
def Area(radius, PI = 3.14):
	ans =0.0
	ans = PI * radius * radius
	return ans

def main():
	print("Enter radius OF circle: ")
	ino = float(input())

	ret = 0.0
   #ret = Area(ino) #value nhi dili tr default

   #ret = Area(ino,3.45)  # Value dili tr value change  hoil

	ret = Area(PI = 7.10, radius = ino)
	#keyvalue use keli tr asa lihu shkto = imp aah
	
	print("Area is:  ",ret)


if __name__ == "__main__":
	main()