class Demo:
	A = 10
	def __init__(self):
		print("Inside constructor")
		self.B = 20  #instance varaible

	def fun_instance(self):
		print("Inside instance method")

	@classmethod
	def fun_class(cls):
		print("Inside class method")

	@staticmethod
	def fun_static():
		print("Inside static method")

	def __del__(self):
		print("Inside destructor")

def main():
	Demo.fun_class()
	#Demo.fun_static()

	obj = Demo()
	obj.fun_instance()
	obj.fun_static()

if __name__ == "__main__":
	main()
	print("EnD OF APPLICATION")