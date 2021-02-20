  
from item import Item

class Lightsource(Item):
    def __init__(self, name, description, is_light):
        super().__init__(name, description)
        self.is_light = is_light

    def toggle(self):
        self.is_light = not self.is_light
        if self.is_light == True:
            print(f"\nYou turned the {self.name} on")
        else:
            print(f"\nYou turned the {self.name} off")

    def Take(self):
        print(f"\nYou picked up the {self.name}. \nTry: '{self.name}' to use.")

    def Drop(self):
        print(f"\nIt's not wise to drop your source of light!")

    def __repr__(self):
        return self.name + " " + self.is_light