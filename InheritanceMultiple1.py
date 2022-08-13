class Base1:
	def __init__(self):
		print("Inside Base1")
		self.A = 10

	def fun(self):
		print("Fun Base1")

class Base2:
	def __init__(self):
		print("Inside Base2")
		self.B = 20

	def fun(self):
		print("Fun Base12")

class Derived(Base1,Base2):  
	def __init__(self):
		self.C= 30
		Base1.__init__(self)
		Base2.__init__(self)
		print("Inside Derived")

	def sun(self):
		print("Inside SUN")

def main():
	dobj = Derived()
	dobj.fun()
	print(dobj.A)

if __name__ == "__main__":
	main()