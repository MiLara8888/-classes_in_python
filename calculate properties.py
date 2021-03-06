#Класс реализующий вычисление площади квадрата с кешированием данных при повторном извлечении площади
class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self,value):
        self.__side=value
        self.__area=None

    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area=self.__side**2
        return self.__area