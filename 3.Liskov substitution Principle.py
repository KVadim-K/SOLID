class Bird():
    def fly(self):
        print("Эта птица летает")

class Duck(Bird):# наследование от Bird():
    def fly(self):
        print("Эта утка летает быстро")
def fly_in_the_sky(animal):
    animal.fly() # любой класс сюда можно передать и программа может корректно работать

b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)
