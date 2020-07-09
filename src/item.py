
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def Take(self):
        print(f"\nPicked up the {self.name}.")

    def Drop(self):
        print(f"\nDropped the {self.name}.")

    def __repr__(self):
        return self.name 