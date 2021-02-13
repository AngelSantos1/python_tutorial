"""
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
print(c.thingy.blah)
c.thingy.blah = ";alksdjgaslkfg"
print(c.thingy.blah)

c1 = MyClass()
print(c1.thingy.blah)
"""

for:
mylist = [1, 2, 3]
mydict = {
"key1": "value",
"key2": 2,
}

mylist[1] # 2
mydict["key1"] # "value"


class Car:
def __init__(self, owner, doors):
self.owner = owner
self.doors = doors

def myfunc():
# stuff

class ToyotaPrius2010(Car):
def __init__(self, owner, price):
super().__init__(owner, 4)
self.price = price
super().myfunc()

neds_car = ToyotaPrius2010("Ned", 3000)
bobs_car = ToyotaPrius2010("Bob", 8000)
print(neds_car.owner)
print(neds_car.price)
print(neds_car.doors)

print(bobs_car.owner)
print(bobs_car.price)
	
	
	

