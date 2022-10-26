from game_classes.begger import Begger
from game_classes.mage import Mage
import random

player_1 = Begger()
computer = Mage("Hagred")

while player_1.health > 0 and computer.health > 0:
    response = ""
    while not response == "1" and not response == "2"
    print("would you like 1) Attack or 2) Heal")
    response = input(">>>>")
    print(response)
    if response == "1":
        player_1.attack(computer)
    elif response == "2"
        player_1.heal()

    roll = random.randint(1,2)
    if roll == 1:
        computer.attack(player_1)
    else:
        computer.heal()

if player_1.health > 0:
    prints("congrats")
elif computer.health <= 0:
    