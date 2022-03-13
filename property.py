# Создайте класс UserMail, у которого есть:
#
# конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес.
# Их необходимо сохранить в экземпляр как атрибуты login и __email (обратите внимание, защищенный атрибут)
# метод геттер get_email, которое возвращает защищенный атрибут __email ;
# метод сеттер set_email, которое принимает в виде строки новую почту.
# Метод должен проверять, что в новой почте есть только один символ @ и после нее есть точка.
# Если данные условия выполняются, новая почта сохраняется в атрибут __email, в противном случае выведите сообщение "Ошибочная почта";
# создайте свойство email, у которого геттером будет метод get_email, а сеттером - метод set_email

class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_mail(self):
        return self.__email

    def set_email(self, value):
        if value.count('@') == 1 and '.' in value[value.index('@'):]:
            self.__email = value
        else:
            print("Ошибочная почта")

    email = property(fget=get_mail, fset=set_email)


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3]  # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait


# Создайте класс Money, у которого есть:
# конструктор __init__, принимающий 2 аргумента: dollars, cents. По входным аргументам вам необходимо создать атрибут экземпляра total_cents.
# свойство геттер dollars, которое возвращает количество имеющихся долларов;
# свойство сеттер dollars, которое принимает целое неотрицательное число - количество долларов и устанавливает при помощи него
# новое значение в атрибут экземпляра total_cents, при этом значение центов должно сохранятся.
# В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error dollars";
# свойство геттер cents, которое возвращает количество имеющихся центов;
# свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100 - количество центов и устанавливает
# при помощи него новое значение в атрибут экземпляра total_cents, при этом значение долларов должно сохранятся.
# В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран сообщение "Error cents";
# метод __str__ (информация по данному методу), который возвращает строку вида "Ваше состояние составляет {dollars} долларов {cents} центов".
# Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами
# В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = (dollars * 100) + cents

    @property
    def dollars(self):
        return self.total_cents //100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:

            self.total_cents=value*100+self.cents
            return self.total_cents
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and value <= 99 and value >= 0:
            self.total_cents=(self.dollars*100)+value
        else:
            print('Error cents')

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"



Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов



#_____________________________________________________________________________
# Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм, а с помощью метода
# to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной “kg” она реализовала методы set_kg() -
# для задания нового значения килограммов, get_kg()  - для вывода текущего значения кг. Из-за этого возникло неудобство:
# нам нужно теперь использовать эти 2 метода для задания и вывода значений. Помогите ей переделать класс с использованием
# функции property() и свойств-декораторов. Код приведен ниже.

# class KgToPounds:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def set_kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             raise ValueError('Килограммы задаются только числами')
#
#     def get_kg(self):
#         return self.__kg


# Чтобы не задавать новые значения или не получать к ним доступ через два метода, можно реализовать предложенный класс через
# функцию property() или свойства-декораторы.

class KgToPounds:

    def __init__(self, kg):
        self.kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self.__kg * 2.205

weight = KgToPounds(12)
print(weight.to_pounds())   #26.46
print(weight.kg)         #12
weight.kg = 41
print(weight.kg)         #41
weight.kg = 'десять'      #ValueError: Килограммы задаются только числами
