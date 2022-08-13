class Base:
	def __init__(self):
		print("Inside Base Constructor")
		self.A  = 10

	def fun(self):
		print("Base fun")

class Derived(Base):
	def __init__(self):
	#	Base.__init__(self)
		super().__init__()
		print("Inside Derived Constructor")
		self.B = 20

	def gun(self):
		print("Derived gun")

def main():
	dobj = Derived()
	print(dobj.A)
	dobj.fun()

if __name__ == "__main__":
	main()