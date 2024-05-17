# Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")
class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")
class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon
    def attack(self):
        self.weapon.attack()
    def changeWeapon(self, weapon):
        self.weapon = weapon
class Monster:
    def defeated(self):
        print("Монстр побежден!")

def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeated()

sword = Sword()
bow = Bow()
fighter = Fighter(sword)  # Изначально боец вооружен мечом
monster = Monster()

print("Боец выбирает меч.")
battle(fighter, monster)

print("\nБоец выбирает лук.")
fighter.changeWeapon(bow)  # Меняем оружие на лук
battle(fighter, monster)
