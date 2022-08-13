class Demo:
	A=10  #class Variable

	def __init__(self):
		self.B= 30   #instance variable

	def fun(self):  #instance method
		print("Inside instance method fun",Demo.B)

	@classmethod
	def gun(cls):  #class method
		print("Inside class method",Demo.A) 

def main():
	print("Value of class variable: ",Demo.A)
	Demo.gun()

	obj1 = Demo()

	print("Value of instance variable:",obj1.B)
	obj1.fun()

if __name__ == "__main__":
	main()