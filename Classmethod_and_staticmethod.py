# Создайте класс Robot, у которого есть:
# атрибут класса population. В этом атрибуте будет хранится общее количество роботов, изначально принимает значение 0;
# конструктор __init__, принимающий 1 аргумент name. Данный метод должен сохранять атрибут name и печатать сообщение вида
# "Робот <name> был создан". Помимо инициализации робота данный метод должен увеличивать популяцию роботов на единицу;
# метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида "Робот <name> был уничтожен"
# метод say_hello, которой печатает сообщение вида "Робот <name> приветствует тебя, особь человеческого рода"
# метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')

    def destroy(self):
        print(f'Робот {self.name} был уничтожен')
        del self
        Robot.population -= 1


r2 = Robot("R2-D2")  # печатает "Робот R2-D2 был создан"
r2.say_hello()  # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many()  # печатает "1, вот сколько нас еще осталось"
r2.destroy()  # печатает "Робот R2-D2 был уничтожен"



#________________________________________________-

from string import ascii_uppercase, digits, ascii_lowercase

# Давайте создадим класс Registration, который поможет зарегистрировать пользователя с безопасным паролем
# В классе Registration необходимо реализовать
# Конструктор __init__ принимающий 2 аргумента (login, password). В конструкторе вы сохраняете переданные
# login и password через сеттеры
# Cвойство геттер login, которое возвращает значение self.__login;
# Свойство сеттер login, принимает значение емайла в случае если:
# Емайл(login) содержит хотя бы 1 символ "@". В случае ошибки выводим ValueError("Login must include at least one ' @ '")
# Email(login) содержит хотя бы 1 символ " . ".В случае ошибки выводим ValueError("Login must include at least one ' . '")
# Если значение проходит проверку новое значение логина сохраняется в атрибут (self.__login)
# Свойство геттер password, которое возвращает значение self.__password;
# Свойство сеттер password, принимает значение пароля в случае если:
# Password является строкой(не список, словарь и т.д. ) в противном случае вызываем исключение
# TypeError("Пароль должен быть строкой")
# Длина password должна быть от 5 до 11 символов, в противном случае вызывать исключение
# ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# Должен содержать хотя бы одну цифру. Для этого нужно в staticmethod создать функцию is_include_digit которая,
# которая проходит по всем элементам строки и проверяет их наличие в digits. В случае ошибки выводим:\
#     ValueError('Пароль должен содержать хотя бы одну цифру')
# Строка password должна содержать элементы верхнего и нижнего регистра. В staticmethod создаем метод
# (is_include_all_register), который с помощью цикла проверяет элемента строчки на регистр.
# В случае ошибки выводит: ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
# Строка password должна содержать только латинские символы. Импортируем библиотеку string ,в staticmethod
# создаем метод(is_include_only_latin), которым проверяем, каждый элемент на наличие в string(проверка должна быть как в верхнем, так и нижнем регистре). В случае ошибки ValueError('Пароль должен содержать только латинский алфавит')
# Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt.
# Сохраните данный файл к себе в папку с вашей программой. С помощью staticmethod создаем метод
# check_password_dictionary и проверяем наличие нашего пароля в данном файле.
# Если значение совпадет со значением из файла, то в сеттер добавляем исключение и выводим ошибку:\
#     ValueError('Ваш пароль содержится в списке самых легких')
class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if '@' not in value:
            raise ValueError("Login must include at least one ' @ '")
        if '.' not in value:
            raise ValueError("Login must include at least one ' . '")
        self.__login = value

    @staticmethod
    def is_include_digit(val):
        return any([i for i in val if i in digits])

    @staticmethod
    def is_include_all_register(val):
        return len([i for i in val if i in ascii_uppercase]) >= 2

    @staticmethod
    def is_include_only_latin(val):
        return all(list(map(lambda x: x in ascii_lowercase or x in digits or x in ascii_uppercase, val)))

    @staticmethod
    def check_password_dictionary(val):
        n = ['123456', 'password', '123456789', '12345', '12345678', 'qwerty', '1234567', '111111', '1234567890',
             '123123', 'abc123', '1234', 'password1', 'iloveyou', '1q2w3e4r', '000000', 'qwerty123', 'zaq12wsx',
             'dragon', 'sunshine', 'princess', 'letmein', '654321', 'monkey', '27653', '1qaz2wsx', '123321',
             'qwertyuiop', 'superman', 'asdfghjkl']
        return val not in n

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 5 or len(value) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = value



