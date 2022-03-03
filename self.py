'''Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
В классе Counter нужно определить метод start_from, который принимает один необязательный аргумент
- значение, с которого начинается подсчет, по умолчанию равно 0
Также нужно создать метод increment, который увеличивает счетчик на 1.
Затем необходимо создать метод display, который печатает фразу "Текущее значение счетчика = <value>"
и метод reset,  который обнуляет экземпляр счетчика
Пример работы с классом Counter'''

class Counter:

    def start_from(self, start=0):
        self.value = start
        return self.value

    def increment(self):
        self.value += 1
        return self.value

    def display(self):
        print(f'Текущее значение счетчика = {self.value}')

    def reset(self):
        self.value = 0
        return self.value


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display()  # печатает "Текущее значение счетчика = 0"

c2 = Counter()
c2.start_from(3)
c2.display()  # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display()  # печатает "Текущее значение счетчика = 4"