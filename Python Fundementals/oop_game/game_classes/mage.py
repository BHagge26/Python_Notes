from human import Human


class Mage(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name 
        self.health = 50
        self.strength = 6
        self.mana = 15

    def attack(self, target):
        print(f"{self.name} is attacking {target.name}")
        target.defend(self.mana)



mage1 = Mage("Albus")
mage2 = Mage("Snape")

mage1.attack(mage2)