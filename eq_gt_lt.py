# Давайте с вами реализуем класс ChessPlayer и научимся сравнивать рейтинги шахматистов между собой.
# И так, ваша задача реализовать класс ChessPlayer, который состоит из:
#
# метода инициализации, принимающего аргументы name, surname, rating;
#
# магического  метода __eq__, который будет позволять сравнивать экземпляры класса ChessPlayer с числами и другими
# экземплярами этого класса. Если сравнение происходит с целым числом и атрибут rating с ним совпадает, то необходимо вернуть
# True, в противном случае - False. Если же сравнение идет с другим шахматистом(экземпляром класса ChessPlayer)
# и значения атрибутов rating равны, то возвращается True, в противном случае - False. А если же сравнивается с другим типом данных,
# верните ‘Невозможно выполнить сравнение’;
#
# магического  метода __gt__. Если сравнение происходит с целым числом и атрибут rating больше его, необходимо вернуть значение True,
# в противном же случае - False. Если сравнение происходит с другим шахматистом(экземпляром класса ChessPlayer) и атрибут rating у
# нашего экземпляра больше, то верните True, в противном случае - False. В случае если сравнение идет с остальными типами данных, верните
# ‘Невозможно выполнить сравнение’
#
# магического  метода __lt__. Если сравнение происходит с целым числом и атрибут rating меньше его, необходимо
# вернуть значение True, в противном же случае - False. Если сравнение происходит с другим шахматистом(экземпляром класса ChessPlayer)
# и атрибут rating у нашего экземпляра меньше, то верните True, в противном случае - False. В случае если сравнение идет с остальными
# типами данных, верните ‘Невозможно выполнить сравнение’.

class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return 'Невозможно выполнить сравнение'





magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)  # False
print(ian == 2789)  # True
print(magnus == ian)  # False
print(magnus > ian)  # True
print(magnus < ian)  # False
print(magnus < [1, 2])  # печатает "Невозможно выполнить сравнениe"
print(magnus>5)
