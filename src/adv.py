from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#




# Make a new player object that is currently in the 'outside' room.

player = Player("mara_jade", room['outside'])
item = Item("Reverie", "whoodle")
room['outside'].items.append(item)
print(player.name, player.location)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
directions = input("[n] North [e] East [s] South [w] West :")

def pick_up(item):
    player.items.append(item)
    player.location.items.pop()
    print("LOCATION ITEMS!!!", player.location.items)
    print("PLAYER ITEMS!!!", player.items)

def put_down(item):
    player.location.items.append(item)
    player.items.remove(item)
    print("ITEMS IN LOCATION NOW", player.location.items)
    print("No Longer in Player Items???", player.items)

while not directions == "q":
    if directions == "w":
        try:
            player.location = player.location.w_to
            print(player)
        except:
            print("no go bro")
        directions = input("[n] North [e] East [s] South [w] West :")
    elif directions == "n":
        try:
            player.location = player.location.n_to
            print(player)
        except:
            print("no go bro")
        directions = input("[n] North [e] East [s] South [w] West :")
    elif directions == "e":
        try:
            player.location = player.location.e_to
            print(player)
        except:
            print("no go bro")
        directions = input("[n] North [e] East [s] South [w] West :")
    elif directions == "s":
        try:
            player.location = player.location.s_to
            print(player)
        except:
            print("no go bro")

        directions = input("[n] North [e] East [s] South [w] West :")
    elif " " in directions:
        if "get" in directions:
            command_line = directions.split(" ")
            pick_up(command_line[1])
            print("Items!!!!", player.items)
        elif "drop" in directions:
            command_line = directions.split(" ")
            put_down(command_line[1])
        directions = input("[n] North [e] East [s] South [w] West :")
    else:
        print("please enter valid directions")
        directions = input("[n] North [e] East [s] South [w] West :")

print("game over")
directions = input("[n] North [e] East [s] South [w] West :")