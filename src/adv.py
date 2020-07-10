from room import Room
from player import Player
from item import Item
from lightsource import Lightsource 
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", True),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
}

overlook = room['overlook']
foyer = room['foyer']
outside = room['outside']
treasure = room['treasure']
narrow = room['narrow']


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
player = Player(input("Enter player name: "), outside)
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
directions = ["n", "s", "e", "w"]

rock = Item("rock","Its a rock")
bigrock = Item("BigRock","It's slightly bigger than the other rock")
bottle = Item("bottle","It's empty")
stick = Item("stick","it is a stick")
lamp = Lightsource("lamp","It is a lamp",False)
gold = Item("GoldRock","It smells like gold but it looks like a rock")

room['outside'].items = [rock,bigrock]
room['foyer'].items = [bottle]
room['overlook'].items = [stick,lamp]
room['narrow'].items = [gold]

while True:
    room_items = player.room.items
    player_items = player.items
    

    print(f"\nYou are in the {player.room.name}.")
    print(f"{player.room.description}...")

    user_input = input(f"\nWhich direction do you travel? ").lower()
    #check if lightsource is on
    def is_lightsource_on():
        result = 0
        for item in player_items:
            if item.name == "lamp" and item.is_light == True:
                result += 1
        if result == 0:
            return False
        else:
            return True

    cmd = user_input.split(" ")
    # move input
    if user_input in directions:
        player.travel(player.room, user_input)
    #check items
    elif user_input == "i" or user_input == "inventory":
        print("\nInventory:")
        if len(player_items) == 0:
            print("No items in your inventory")
        for i in range(len(player_items)):
            print(
                f'{i + 1}) {player_items[i].name}: {player_items[i].description}')
    #check room
    elif user_input == "c" or user_input == "check":
        if player.room.is_light == True or is_lightsource_on():

            print("\nItems in room:")
            # no items in room
            if len(room_items) == 0:
                print("No items in room\n")
            # list of items
            for i in range(len(room_items)):
                print(
                    f'{i + 1}) {room_items[i].name}: {room_items[i].description}')
        else:
            print("\nIt's pitch black!")
    #take item
    elif len(cmd) == 2 and cmd[0] == "get" or cmd[0] == "take":
        list_length = len(player_items)
        if player.room.is_light == True or is_lightsource_on():
            for item in room_items:

                if item.name.lower() == cmd[1]:
                    player_items.append(item)
                    room_items.remove(item)
                    item.Take()

            if list_length == len(player_items):
                print(f"\nNo {cmd[1]} in this room.")  
        else:
            print("\nGood luck finding that in the dark!")

    #drop item
    elif len(cmd) == 2 and cmd[0] == "drop":
        list_length = len(player_items)
        # check if item exists
        for item in player_items:
        # adds item to inventory
            if item.name.lower() == cmd[1]:
                room_items.append(item)
                player_items.remove(item)
                item.Drop()
        # return error
        if list_length == len(player_items):
            print(f"\nThere is no {cmd[1]} in your inventory.")
    #toggle light
    elif user_input == "lamp":
        result = 0
        for item in player_items:
            if item.name == "lamp":
                result += 1
                lamp.toggle()
        if result == 0:
            print("\nYou don't have a lamp in your inventory.")
    #quit game
    elif user_input == "q":
        print("quitting")
        break

    else:
        print("\nInput Invalid")