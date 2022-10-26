class Human:
    def __init__(self):
        self.name = "Generic Human"
        self.health = 100
        self.strength = 10
        self.defence = 2
        self.magic = 10 

#heal
#attack
    def attack(self, target):
        print(f"{self.name} is attacking {target.name}")
        #target.health -= self.strength
        target.defend(self.strength)
        #defend
    def defend(self, damage):
        damage -= self.armor
        self.health -= damage
        print(f"{self.name} defends for {self.armor} and takes {damage}")
        print(f"{self.name} now has {self.health}")

    def heal(self):
        self.health += self.mana
        print(f"{self.name} heals for ")