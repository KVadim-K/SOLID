from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

### Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")
class Axe(Weapon):
    def attack(self):
        print("Боец рубит топором.")

### Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
    def attack(self):
        self.weapon.attack()
    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

### Шаг 4: Реализация боя
class Monster:
    def defeated(self):
        print("Монстр побежден!")
def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    print("Монстр пытается защититься.")
    monster.defeated()

# Пример использования
if __name__ == "__main__":
    sword = Sword()
    bow = Bow()
    axe = Axe()
    fighter = Fighter(sword)  # Изначально боец вооружен мечом
    monster = Monster()

    print("Боец выбирает меч.")
    battle(fighter, monster)

    print("\nБоец выбирает лук.")
    fighter.changeWeapon(bow)  # Меняем оружие на лук
    battle(fighter, monster)

    print("\nБоец выбирает топор.")
    fighter.changeWeapon(axe)  # Меняем оружие на топор
    battle(fighter, monster)