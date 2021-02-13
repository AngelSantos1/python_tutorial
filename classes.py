class MySecondClass:
	def __init__(self):
		self.blah = "blarg"

class MyClass:
	def __init__(self): 
		self.first = 2
		self.second = 5
		self.thingy = MySecondClass()
	
	def myfunc(self):
		print(self.first)
		print(self.second)


c = MyClass()
c.myfunc()
 
print(c.first) 
print(c.second)
print(c.thingy.blah)





myint = 0 
my float = 0.0
mylist = []

def myfunc()
	# block of code goes here

myfunc()

if
while
