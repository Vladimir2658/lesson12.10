"""
Задание 1
Создать базовый класс Фигура с методом для подсчета
площади. Создать производные классы: прямоугольник,
круг, прямоугольный треугольник, трапеция со своими
методами для подсчета площади.
Задание 2
Для классов из задания 1 нужно переопределить маги-
ческие методы int(возвращает площадь) и str (возвращает
информацию о фигуре).
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

    def __int__(self):
        return self.square()

    def __str__(self):
        return f"Прямоугольник w={self.width} h={self.heigth} s={self.square()}"

class Circle(Figura):
    def __init__(self, r):
        self.radius = r

    def square(self):
        return math.pi * math.pow(self.radius, 2)

    def __int__(self):
        return int(self.square())

    def __str__(self):
        return f"Круг r={self.radius} s={self.square()}"

class RightTriangle(Figura):
    def __init__(self, cat1, cat2):
        self.cat1 = cat1
        self.cat2 = cat2

    def square(self):
        return self.cat1 * self.cat2 / 2

    def __int__(self):
        return int(self.square())

    def __str__(self):
        return f"Прямоугольный треугольник cat1={self.cat1} cat2={self.cat2} s={self.square()}"

class Trapeze(Figura):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def square(self):
        return (self.a + self.b)*self.h/2

    def __int__(self):
        return int(self.square())

    def __str__(self):
        return f"Трапеция a={self.a} b={self.b} h={self.h} s={self.square()}"

rec = Rectangle(2, 4)
print("Площадь прямоугольника:", int(rec))
print(rec)

cir = Circle(3)
print("Площадь круга:", int(cir))
print(cir)

rtri = RightTriangle(2, 5)
print("Площадь прямоугольного треугольника", int(rtri))
print(rtri)

tra = Trapeze(3, 6, 3)
print("Площадь трапеции", int(tra))
print(tra)

