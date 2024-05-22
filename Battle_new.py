from abc import ABC, abstractmethod
import random

class Hero(ABC):
    @abstractmethod
    def attack(self, other):
        pass
class Warrior(Hero):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other): #Реализация метода `attack`, который был определен как абстрактный в классе `Hero`. Метод принимает параметр `other`, представляющий другого воина.
        damage = random.randint(1, self.attack_power) #Генерация случайного значения урона в диапазоне от 1 до значения `self.attack_power`.
        other.health -= damage # Уменьшение здоровья другого воина (`other`) на величину урона.
        print(f"{self.name} наносит {damage} урона по {other.name}у. У {other.name}а осталось {other.health} здоровья.") # Вывод информации о нанесенном уроне и оставшемся здоровье другого воина.
        if other.health <= 0: # Проверка, является ли здоровье другого воина меньше или равно нулю. Если это так, то другой воин погиб.
            print(f"{self.name} победил! {other.name} повержен!" ) # Если здоровье другого воина меньше или равно нулю, вывод сообщения о его поражении и победе текущего воина.

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.health}")
        print(f"Атака: {self.attack_power}")

def fight(warrior1, warrior2): # Реализация метода `fight`, который был определен как абстрактный в классе `Hero`.
    current_attacker, next_attacker = random.choice([(warrior1, warrior2), (warrior2, warrior1)]) # Случайный выбор атакующего первым
    while warrior1.health > 0 and warrior2.health > 0: # Пока здоровья обоих воинов не равны нулю, бой продолжается.
        current_attacker.attack(next_attacker) # Атакующий атакует защищающегося
        if next_attacker.health <= 0: # Проверка, является ли здоровье защищающегося меньше или равно нулю. Если это так, то защищающийся погиб.
            break
        current_attacker, next_attacker = next_attacker, current_attacker # Меняем атакующего и защищающегося

warrior1 = Warrior("Ахиллес", 100, 50)
warrior2 = Warrior("Гектор", 100, 40)

fight(warrior1, warrior2) # Начало боя

warrior1.info()
warrior2.info()