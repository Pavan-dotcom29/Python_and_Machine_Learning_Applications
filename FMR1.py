'''Program : Accept list and check the even number using filter ,
 map(Increment), Addition by using reduce function.'''

from functools import reduce

#def CheckEven(value):
	#if(value % 2 == 0):
	#	return True
	#else:
	#	return False
#	return (value % 2 == 0)

CheckEven = lambda value : (value % 2 == 0)

#def Increment(value):
#	return value + 2

Increment = lambda value : value +2

#def Addition(a,b):
#	return a + b

Addition = lambda a,b : a+ b

def main():
	data = [5,6,7,8,4,2]
	print("Original data ",data)

	#Filter
	newdata = list(filter(CheckEven,data))

	print("Data after filter :  ",newdata)

	#Map
	incrementdata = list(map(Increment,newdata))
	print("Data after MAP: ",incrementdata)

	#Reduce
	ret = reduce(Addition,incrementdata)
	print(type(reduce))
	print("Data after Reduce: ",ret)

if __name__ == "__main__":
	main()
	