class warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 10
        self.power += 5
    def eat(self):
        print(f"{self.name} сел поесть")
        self.endurance += 3
        self.power += 10
    def hit(self):
        print(f"{self.name} нанес удар")
        self.endurance -= 6
        self.power -= 8
    def wolk(self):
        print(f"{self.name} идет")
    def info(self):
        print(f"Имя война: {self.name}")
        print(f"Сила война: {self.power}")
        print(f"Выносливость война: {self.endurance}")
        print(f"Цвет волос война: {self.hair_color}")
war1 = warrior( "Вадим", 100, 100, hair_color = "блондин")
war2 = warrior( "Антон", 80, 75, hair_color = "шатен")

print(war1.name, war1.power, war1.endurance, war1.hair_color)
war1.sleep()
war1.eat()
war1.hit()
war1.wolk()
print(war1.name, war1.power, war1.endurance, war1.hair_color)
print(war2.name, war2.power, war2.endurance, war2.hair_color)
war2.sleep()
war2.eat()
war2.hit()
war2.wolk()
print(war2.name, war2.power, war2.endurance, war2.hair_color)

war1.info()
war2.info()
