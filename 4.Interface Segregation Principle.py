# class SmartHouse():
#     def turn_on_light(self):
#         pass
#     def heat_food(self):
#         pass
#     def turn_on_music(self):
#         pass

# Различие в том, что теперь у нас для работы с каждой отдельной частью умного дома функции разнесены:
# есть отдельный пульт для работы с освещением,
# отдельный для разогрева еду и отдельный — для работы с музыкой.
# Это и есть принцип разделения интерфейсов, который считается одним из базовых.


class Light():
    def turn_on_light(self):
        print("Свет включен")
class Food():
    def heat_food(self):
        print("Еда начала разогреваться")
class Music():
    def turn_on_music(self):
        print("Вкючаю подборку ваших любимых песен")