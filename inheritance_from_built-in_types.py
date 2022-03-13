# Создайте класс NewInt, который унаследован от целого типа int, то есть мы будем унаследовать поведение целых
# чисел и значит экземплярам нашего класса будут поддерживать те же операции, что и целые числа.
#
# Дополнительно в классе NewInt нужно создать:
# -метод repeat, который принимает одно целое положительное число n (по умолчанию равное 2), обозначающее сколько раз
# нужно продублировать данное число. Метод repeat должен возвращать новое число, продублированное n раз (см пример ниже);
#
# -метод to_bin, который возвращает двоичное представление числа в виде числа (может пригодиться функция bin)

class NewInt(int):
    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(format(self, 'b'))


a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3))  # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin())  # печатает 100011 - двоичное представление числа 35




# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:
#
# метод is_repeatance (s), который принимает 1 аргумент s и возвращает True или False в зависимости от того,
# может ли текущая строку быть получена целым количеством повторов строки s. Вернуть False, если s не является строкой.
# Считать, что пустая строка не содержит повторов.
# метод is_palindrom (), который возвращает True или False в зависимости от того, является ли строка палиндромом.
# Регистрами символов пренебрегать. Пустую строку считать палиндромом.
# Пример последовательности действий для тестирования класса:

class SuperStr(str):
    def __init__(self, val):
        self.val = val

    def is_repeatance(self, n):
        if not isinstance(n, str):
            return False
        return self.val.count(n) * len(n) == len(self.val)

    def is_palindrom(self):
        if self.val.upper() == self.val.upper()[::-1]:
            return True
        else:
            return False


s = SuperStr('123123123123')
print(s.is_repeatance('123'))  # True
print(s.is_repeatance('123123'))  # True
print(s.is_repeatance('123123123123'))  # True
print(s.is_repeatance('12312'))  # False
print(s.is_repeatance(123))  # False
print(s.is_palindrom())  # False
print(s)  # 123123123123 (строка)
print(int(s))  # 123123123123 (целое число)
print(s + 'qwe')  # 123123123123qwe
p = SuperStr('123_321')
print(p.is_palindrom())  # True
