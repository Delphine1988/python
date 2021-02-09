from random import randint
# creationd'un dé on peut choisir le nombre de faces du dés et le lancer on affiche sa valeur '
class Dice:

    def __init__(self, face = 6):
        self.value = randint(1, face)
        self.__face = face

    def display_value(self):
        print(f"Valeur: {self.value}") #autre syntaxe print("Valeur: %s" % self.value)
        print(self.__face)

    def launch_dice(self):
        self.display_value()


class DiceHundred(Dice):
    def __init__(self):
        super().__init__(100)

class Game:

    def __init__(self):
        self.dice = Dice()

    def throw_dices(self):
        self.dice.launch_dice()


my_game = Game()
my_game.throw_dices()

my_dice = my_game.dice
my_dice.value = 4
print(my_game.dice.value)
# game = Dice(4)
# game.display_value()
# game.launch_dice()
# new_dice = DiceHundred()
# new_dice.launch_dice()