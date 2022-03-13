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





# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
# (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
# а иначе отобразится следующая фраза: «Обычная газировка».

class Soda:
    def __init__(self, topping=None):
        if isinstance(topping, str):
            self.topping = topping
        else:
            self.topping = None

    def show_my_drink(self):
        if self.topping:
            print(f'Газировка и {self.topping}')
        else:
            print(f'Обычная газировка')


drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()


#_______________________________________________-
# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.
class TriangleChecker:
    def __init__(self, value):
        self.value = value

    def is_triangle(self):
        if not all([isinstance(i,int) for i in self.value]):
            return 'Нужно вводить только числа!'
        if not all([i>0 for i in self.value]):
            return 'С отрицательными числами ничего не выйдет!'
        self.value=sorted(self.value)
        if self.value[2]<(self.value[1]+self.value[0]):
            return 'Ура, можно построить треугольник!'
        return 'Жаль, но из этого треугольник не сделать.'




triangle1 = TriangleChecker([2, 3, 4])
print(triangle1)
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77, 3, 4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())
