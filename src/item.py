class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return self.name + '\n' + self.description

class Wealth(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.category = wealth

class Weapon(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.category = weapon

class Tool(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.category = tool