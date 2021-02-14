#Create a text-based game using everything learned, including classes.

class Character:
	def __init__(self, name, roomindex, inventory):
		self.name = name
		self.roomindex = roomindex
		self.inventory = inventory
		
	
class Room:
	def	__init__(self, doors, items, description):
		self.doors = doors
		self.description = description
		self.items = items
				 
class Item:
	def __init__(self, description):
		self.description = description


inputtext = input("What's your character's name? ")  

player = Character(inputtext, 0, [])
print("Your character's name is", inputtext)

items = { 
	"Rusty Spoon": Item("A Rusty Spoon. A capable and efficient tool for the working class cannibal!")

}

rooms = [
	Room({"Forward":1}, ["Rusty Spoon"], 

"You find yourself in a rectangular undulating moist room. A large neon sign infront of you is stapled to the organic pulsating walls reads: 'Welcome to the Jungle, baby!'"

	),
 
	Room({"Backward":0, "Forward": 2}, [], "This is a dry dusty dank room"),
	Room({"Backward":1, "DOOM": 3}, [], "Frothy clam room")
]  

while True:
	print(rooms[player.roomindex].description)
	print(list(rooms[player.roomindex].doors.keys()))
	print(rooms[player.roomindex].items)
	
	resolved = False 
	while not resolved: 
		action = input("What do you do? ")
		if " " in action:
			idx = action.index(" ")
			cmd = action[0:idx]
			sel = action[idx + 1:]
		else:
			cmd = action 
			sel = ""
		
		
		if cmd == "go": 
			if sel in rooms[player.roomindex].doors:
				player.roomindex = rooms[player.roomindex].doors[sel]
				resolved = True
			else:
				print(list(rooms[player.roomindex].doors.keys()))
		elif cmd == "get":
			if sel in rooms[player.roomindex].items:
				player.inventory.append(sel)
				rooms[player.roomindex].items.remove(sel)
				resolved = True
			else:
				print(list(rooms[player.roomindex].items))
		elif cmd == "drop":
			if sel in player.inventory:
				player.inventory.remove(sel)
				rooms[player.roomindex].items.append(sel)
				resolved = True
			else:
				print(list(rooms[player.roomindex].items))
	
		elif cmd == "list": 
			#print(player.inventory)
			for itemname in player.inventory:
				print(items[itemname].description)

			# itemname is our Rusty Spoon
			# items is our dictionary of item definitions
			# items[itemname] is Item class that we looked up with name itemname
 
		elif cmd == "help":
			print("go ---; Move player to another room.")
			print("help; Display this message.")
		else:
			print("Wtf???")

# Homework
# Drop the Rusty Spoon
# Bonus put NPCs into rooms 



