# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


class Player:
    def __init__(self, name, room):
        self.name = name  # string
        self.room = room  # class

    def travelRooms(self, room, direction):
        if getattr(room, f"{direction}_to") != None:
            newRoom = getattr(room, f"{direction}_to")
            self.room = newRoom
        else:
            print("\n*Invalid movement input*")

    def dies(self):
        print("You are dead, not big surprise")

    def __repr__(self):
        return self.name + " Class"