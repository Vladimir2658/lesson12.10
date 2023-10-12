"""
Задание 3
Создайте базовый класс Shape для рисования плоских фигур.
Определите методы:
■ Show() — вывод на экран информации о фигуре;
■ Save() — сохранение фигуры в файл;
■ Load() — считывание фигуры из файла.
Определите производные классы:
■ Square — квадрат, который характеризуется коорди-
натами левого верхнего угла и длиной стороны;
■ Rectangle — прямоугольник с заданными координа-
тами верхнего левого угла и размерами;
■ Circle — окружность с заданными координатами цен-
тра и радиусом;
■ Ellipse — эллипс с заданными координатами верхнего
угла описанного вокруг него прямоугольника со сто-
ронами, параллельными осям координат, и размерами
этого прямоугольника.
Создайте список фигур, сохраните фигуры в файл,
загрузите в другой список и отобразите информацию о
каждой из фигур.
"""
class Shape:
    def Show(self):
        return self.__str__()

    def Load(self):
        lst = []
        with open("out.txt", "r") as f:
            for line in f:
                lst.append(line)
        return lst

    def Save(self, lst):
        with open("out.txt", "w") as f:
            for item in lst:
                f.writelines(str(item)+"\n")

class Square(Shape):
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l

    def __str__(self):
        return f"Квадрат x={self.x}, y={self.y}, l={self.l}"

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return f"Прямоугольник x={self.x}, y={self.y}, w={self.w}, h={self.h}"

class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"Окружность x={self.x}, y={self.y}, r={self.r}"

class Ellipse(Rectangle):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def __str__(self):
        return "Эллипс x={}, y={}, w={}, h={}".format(self.x, self.y, self.h, self.w)

sq = Square(10, 10, 5)
print(sq.Show())

re = Rectangle(5, 6, 4, 7)
print(re.Show())

ci = Circle(5, 5, 3)
print(ci.Show())

el = Ellipse(1, 1, 3, 5)
print(el.Show())

lst = [sq, re, ci, el]
print(lst)
obj = Shape()
obj.Save(lst)
lst2 = obj.Load()
print("-------------------")
for line in lst2:
    print(line, end="")

