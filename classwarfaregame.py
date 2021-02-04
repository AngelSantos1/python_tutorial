#Create a text-based game using everything learned, including classes.

class Character:
	def __init__(self, name, roomindex):
		self.name = name
		self.roomindex = roomindex
		 
class Room:
	def	__init__(self, doors, description):
		self.doors = doors
		self.description = description

	 

rooms = [
	Room({"Forward":1}, "You find yourself in a rectangular undulating moist room"), 
	Room({"Backward":0, "Forward": 2}, "This is a dry dusty dank room"), 
	Room({"Backward":1, "DOOM": 3}, "Frothy clam room")
]  


inputtext = input("What's your character's name? ") 

player = Character(inputtext, 0)

print("Your character's name is", inputtext)



while True:
	print(rooms[player.roomindex].description)
	print(list(rooms[player.roomindex].doors.keys()))
	doorselect = input("Choose a door. ")
	player.roomindex = rooms[player.roomindex].doors[doorselect]


# Doorselect is in the dictionary of doors? 
# If it is set room index
# If not then print you cannot do that


"""
while True:
	print(rooms[player.roomindex].description)
	print(rooms[player.roomindex].doors)
	doorselect = int(input("Choose a door. "))
	player.roomindex = doorselect
"""


#	Doorselect is in the list of doors
# Name the doors 
# Use maps - mymap["blah"] to designate index 



