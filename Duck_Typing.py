'''Program : Duck typing 
If it walks like a duck,swims like duck and quacks like a duck ,then probably it is a ducks
'''
print("-------------Demostration of Duck typing-----------")

#def fly(self):
#		print("Sparrow flying")

class Sparrow():
	def fly(self):
		print("Sparrow flying")

class Airplane():
	def fly(self):
		print("Airplane flying")

class Whale:
	def fly(self):
		print("Whale Swimming")

def fun(entity):
	entity.fly()

sparrow = Sparrow()
airplane = Airplane()
whale = Whale()

fun(sparrow) #print"Sparrow flying"
fun(airplane) #print"Airplane flying"
fun(whale) #print""