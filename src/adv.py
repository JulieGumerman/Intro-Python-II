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

    'pool': Room("Lake of Forgotten Dreams", """If you shine your light on the lake, you see it reflecting in intoxicating swirls on the ceiling"""),
    
    'tunnel': Room("Wormhole Tunnel", """You find a tunnel no wider than your shoulders...but if it's here, it has to go somewhere. It'd just be nice if we could get there quicker...""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['pool']
room['pool'].e_to = room['foyer']
room['pool'].w_to = room['tunnel']
room['tunnel'].e_to = room['treasure']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].w_to = room['tunnel']

#
# Main
#




# Make a new player object that is currently in the 'outside' room.

new_player= input("What is your name??? ~~~>" )

player = Player(new_player, room['outside'])
print(player)

reverie = Item("Reverie", "super-powered poodle mix")
flashlight = Item("headlamp", "because light makes it easier to see")
multitool = Item("multitool", "like a knife...only cooler")
old_map = Item("map", "an old map of the cave system, complete with notes")
hooded_sweatshirt = Item("hooded sweatshirt", "a black hoodie with the old Lambda logo. I bet this is worth some cash")

room['outside'].items.append(reverie)
room['foyer'].items.append(flashlight)
room['overlook'].items.append(multitool)
room['narrow'].items.append(old_map)

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
print("[n] North [e] East [s] South [w] West; [i] inventory; drop [item]; get [item] ")
directions = input("~~~>")

def reset():
    print("[n] North [e] East [s] South [w] West; [i] inventory; drop [item]; get [item] ")
    global directions
    directions = input("~~~>")




while not directions == "q":
    #directions logic
    if directions == "w":
        try:
            player.location = player.location.w_to
            print(player)
        except:
            print("no go bro")
        reset()
    elif directions == "n":
        try:
            player.location = player.location.n_to
            print(player)
        except:
            print("no go bro")
        reset()
    elif directions == "e":
        try:
            player.location = player.location.e_to
            print(player)
        except:
            print("no go bro")
        reset()
    elif directions == "s":
        try:
            player.location = player.location.s_to
            print(player)
        except:
            print("no go bro")
        reset()
    elif directions == "i":
        print("You have these items in your stash:", player.items)
        reset()

    #get and drop logic
    elif " " in directions:
        if "get" in directions:
            command_line = directions.split(" ")
            player.pick_up(command_line[1])
            reset()
        elif "drop" in directions:
            command_line = directions.split(" ")
            player.put_down(command_line[1])
            reset()
        else:
            print("Please enter a valid command!")
            reset()
    else:
        print("please enter a valid command")
        reset()


print("game over")



