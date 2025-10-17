class Item:

    def __init__(self):
        self.name = "<ITEM>"


class Key(Item):

    def __init__(self, name):
        super().__init__()
        self.name = name

class Treasure(Item):

    def __init__(self):
        super().__init__()
        self.name = "Shining Treasure"
