"""
Задание 1
Создать базовый класс Фигура с методом для подсчета
площади. Создать производные классы: прямоугольник,
круг, прямоугольный треугольник, трапеция со своими
методами для подсчета площади.
"""
import math

class Figura:
    def square(self):
        pass

class Rectangle(Figura):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def square(self):
        return self.width * self.heigth

class Circle(Figura):
    def __init__(self, r):
        self.radius = r

    def square(self):
        return math.pi * math.pow(self.radius, 2)

class RightTriangle(Figura):
    def __init__(self, cat1, cat2):
        self.cat1 = cat1
        self.cat2 = cat2

    def square(self):
        return self.cat1 * self.cat2 / 2

class Trapeze(Figura):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def square(self):
        return (self.a + self.b)*self.h/2


rec = Rectangle(2, 4)
print("Площадь прямоугольника:", rec.square())

cir = Circle(3)
print("Площадь круга:", cir.square())

rtri = RightTriangle(2, 5)
print("Площадь прямоугольного треугольника", rtri.square())

tra = Trapeze(3, 6, 3)
print("Площадь трапеции", tra.square())

