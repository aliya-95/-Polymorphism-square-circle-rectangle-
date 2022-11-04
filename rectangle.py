class Rectangle:          #Нам необходимо рассчитать площадь геометрической фигуры на основе полиморфизма:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self,a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2  #возведение в степень **2 (в квадрат)
#Добавим в нашу программу еще один объект, например Square (квадрат), который принимает в качестве аргумента одну сторону.

#нахождение радиуса для круга

import math

class Сircle:
    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(self):
        return math.pi * (self.radius ** 2)

