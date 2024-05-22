import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона. У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        #return self.health > 0
        if self.health > 0:
            return True
        else:
            return False

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            attacker = random.choice([self.player, self.computer])
            if attacker == self.player:
                self.player_turn()
            else:
                self.computer_turn()

            if not self.computer.is_alive():
                print("Игрок победил!")
                break

            if not self.player.is_alive():
                print("Компьютер победил!")
                break

    def player_turn(self):
        self.player.attack(self.computer)

    def computer_turn(self):
        self.computer.attack(self.player)

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()