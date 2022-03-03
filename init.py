# Задачи на конструктор класса __init__
# Создайте класс Laptop, у которого есть:
# конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука.
# На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price
# и также атрибут laptop_name - строковое значение, вида "<brand> <model>"


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'


hp = Laptop('hp', '15-bw0xx', 57000)

print(hp.price)  # выводит 57000
print(hp.laptop_name)  # выводит "hp 15-bw0xx"


# _______________________________________________________________

# Создайте класс SoccerPlayer, у которого есть:
# конструктор __init__, принимающий 2 аргумента: name, surname. Также во время инициализации необходимо создать 2 атрибута
# экземпляра: goals и assists - общее количество голов и передач игрока, изначально оба значения должны быть 0
# метод score, который принимает количество голов, забитых игроком, по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество забитых голов игрока на переданное значение;
# метод make_assist, который принимает количество передач, сделанных игроком за матч, по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество сделанных передач игроком на переданное значение;
# метод statistics, который вывод на экран статистику игрока в виде:
# <Фамилия> <Имя> - голы: <goals>, передачи: <assists>

class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goal=1):
        self.goals += goal

    def make_assist(self, assis=1):
        self.assists += assis

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics()  # выводит "Messi Leo - голы: 700, передачи: 500"
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()  # выводит "Kokorin Alex - голы: 1, передачи: 0"


# ______________________________________________________
# Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы
# "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"

class Zebra:
    def __init__(self):
        self.count = 1

    def which_stripe(self):
        if self.count % 2 == 1:
            self.count += 1
            print('Полоска белая')
        else:
            self.count += 1
            print('Полоска черная')


z1 = Zebra()
z1.which_stripe()  # печатает "Полоска белая"
z1.which_stripe()  # печатает "Полоска черная"
z1.which_stripe()  # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()  # печатает "Полоска белая"


# _________________________________________________-
# Создайте класс Person, у которого есть:
# конструктор __init__, принимающий 3 аргумента: first_name, last_name, age.
# метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
# метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult())  # выводит "True"
