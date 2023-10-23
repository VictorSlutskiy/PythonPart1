class Circle:
    def sqr(self, rad):
        self.rad = rad
        return 3.14 * rad ** 2

    def len(self, rad):
        self.rad = rad
        return 2 * 3.14 * rad


while 1:
    try:
        rad = float(input("Введите радиус окружности"))
        if (rad > 0):
            break
        else:
            print("Введите положительное значение ")
    except ValueError:
        print("Введите корректное значение")

c = Circle()
print("Площадь окружности", c.sqr(rad), " Длина окружности", c.len(rad))
