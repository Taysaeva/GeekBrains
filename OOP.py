# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.

# class Road:
#     def __init__(self, road_length, road_width):
#         self._length = road_length
#         self._width = road_width
#     def massa_asfalta(self):
#         massa = self._length * self._width * 25 * 5
#         print(massa)
#
# asfalt = Road(20, 5000)
# asfalt.massa_asfalta()
# print(type(asfalt))

# Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
#
# class Worker:
#     def __init__(self, name, surname, position):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {'wage': 1000, 'bonus': 3000}
#
# class Position(Worker):
#     def get_full_name(self):
#         full_name = f'{self.name} {self.surname}'
#         return full_name
#     def get_total_income(self):
#         total_income = self._income['wage'] + self._income['bonus']
#         return total_income
#
# worker = Position('Oleg', 'Petrov', 'boss')
# print(worker.get_full_name())
# print(worker.get_total_income())

# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# class Stationery:
#     def __init__(self, title):
#         self.title = title
#     def draw(self):
#         print('Запуск отрисовки')
#
# class Pen(Stationery):
#     def draw(self):
#         print('Рисует ручка')
#
# class Pencil(Stationery):
#     def draw(self):
#         print('Рисует карандаш')
#
# class Hangle(Stationery):
#     def draw(self):
#         print('Рисует маркер')
#
# pen = Pen('Ручка')
# pensil = Pencil('Карандаш')
# hangle = Hangle('Маркер')
# pen.draw()
# pensil.draw()
# hangle.draw()

# Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#     def go(self):
#         print(self.name, 'поехала')
#     def stop(self):
#         print(self.name, 'остановилась')
#     def turn(self, direction):
#         print(self.name, 'повернула', direction)
#     def show_speed(self):
#         print('Скорость', self.name, 'равна', self.speed)
# class TownCar(Car):
#     def show_speed(self):
#         super().show_speed()
#         if self.speed > 60:
#             print('Cкорость превышена!!!')
# class SportCar(Car):
#     pass
# class WorkCar(Car):
#     def show_speed(self):
#         super().show_speed()
#         if self.speed > 40:
#             print('Cкорость превышена!!!')
# class PoliceCar(Car):
#     pass
#
# Создать класс TrafficLight (светофор):
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
from itertools import cycle
import time
class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']
    def running(self):
        light_color = cycle(self.__color)
        for i in range(3):
            print(next(light_color))
            time.sleep(7)
            print(next(light_color))
            time.sleep(2)
            print(next(light_color))
            time.sleep(5)
trafficlight = TrafficLight()
trafficlight.running()