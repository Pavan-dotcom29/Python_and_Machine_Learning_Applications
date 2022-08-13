#Instance method 
class Demo:
	A = 10
	def __init__(self):
		print("Inside constructor")
		self.B = 20  #instance varaible

	def fun_instance(self):
		print("Inside instance method")
		print(self.B)
		print(self.A)
		print(Demo.A)

	@classmethod
	def fun_class(cls):
		print("Inside class method")
		print(cls.A)
		print(Demo.A)


	@staticmethod
	def fun_static():
		print("Inside static method")
		print(Demo.A)
		#print(Demo.B) It is not accessable
		

	def __del__(self):
		print("Inside destructor")

def main():
	Demo.fun_class()
	Demo.fun_static()

	obj = Demo()
	obj.fun_instance()

if __name__ == "__main__":
	main()
	print("EnD OF APPLICATION")