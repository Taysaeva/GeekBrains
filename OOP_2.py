# class WinDoor:
#
#     def __init__(self, w, l):
#         self.square = w * l
#
# class Room:
#     def __init__(self, l1, l2, h):
#         self.square = 2 * h * (l1 + l2)
#         self.wd = []
#     def add_wd(self, w, l):
#         self.wd.append(WinDoor(w, l))
#     def coomon_square(self):
#         main_square = self.square
#         for el in self.wd:
#             main_square -= el.square
#         return main_square
#
# r = Room(10, 4, 3)
# print(r.square)
# r.add_wd(2, 2)
# r.add_wd(2, 1)
# r.add_wd(1, 1)
# r.add_wd(1, 1)
# print(r.wd)
# print(r.coomon_square())



# Создание матриц, сложение, вывод

# class Matrix:
#     def __init__(self,mat):
#         if isinstance(mat, list):
#             self.model = mat
#             print('Матрица создана')
#
#
#     def __str__(self):
#         vivod = ''
#         for row in self.model:
#             s = ' '.join(map(str, row))
#             vivod = vivod + s + '\n'
#             self.show = vivod
#         return self.show
#
#     def __add__(self, other):
#         self.w = len(self.model)
#         other.w = len(other.model)
#         self.h = len(self.model[0])
#         other.h = len(other.model[0])
#
#         if self.w == other.w and self.h == other.h:
#
#             matrix0 = [[0] * self.w for i in range(self.h)]
#             for i in range(self.w):
#                 for j in range(self.h):
#                     matrix0[i][j] = self.model[i][j] + other.model[i][j]
#
#         return matrix0
#
# matrix1 = Matrix([[2, 1], [3, 4]])
# matrix2 = Matrix([[2, 2], [2, 2]])
# matrix3 = Matrix(matrix1 + matrix2)
# print(matrix3)

# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

#
# from abc import ABC, abstractmethod
#
# class Wear(ABC):
#     @abstractmethod
#     def rashod(self):
#         pass
# class Cloat(Wear):
#
#     def rashod(self, siz):
#         self.rashod_ = siz / 6.5 + 0.5
#         return self.rashod_
#
# class Dress(Wear):
#     def rashod(self, hig):
#         self.rashod_ = hig * 2 + 0.3
#         return self.rashod_
#
# class Rashod:
#     def __init__(self):
#         self.rashod = []
#     def v(self, value):
#         self.rashod.append(Cloat.rashod(self, value))
#     def h(self, value):
#         self.rashod.append(Dress.rashod(self, value))
#     @property
#     def sum_rashod(self):
#         x = 0
#         for el in self.rashod:
#             x += el
#             print(el)
#         return x
#
# t = Rashod()
# t.v(2)
# t.v(1)
# t.h(2)
# t.h(5)
# print(t.sum_rashod)


# Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.
#
# class Cel:
#     def __init__(self, value):
#         self.sz = value
#     def __add__(self, other):
#         return Cel(self.sz + other.sz).sz
#         self.sz + other.sz
#     def __sub__(self, other):
#         if (self.sz - other.sz) >= 0:
#             return Cel(self.sz - other.sz).sz
#         else:
#             print('Разность меньше 0')
#     def __mul__(self, other):
#         return Cel(self.sz * other.sz).sz
#     def __floordiv__(self, other):
#         return Cel(self.sz // other.sz).sz
#     def make_order(self, x):
#         self.l = self.sz // x
#         self.ll = self.sz % x
#         t = '\n'.join(['*' * x for i in range(self.l)]) + '\n' + '*' * self.ll
#         return t
#
# a = Cel(56)
# b = Cel(10)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a.make_order(10))
import random
#
a = [[1,2],[3,4],[5,6,7]]

b = int(input())
if b in a:
    print('yes')