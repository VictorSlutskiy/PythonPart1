import math

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Значение введено не корректно. Пожалуйста, введите число.")


print("Введите a, b, c в уравнение ax^2 + bx + c = 0")
a = get_float_input("a = ")
b = get_float_input("b = ")
c = get_float_input("c = ")


def solve(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return sorted([root1, root2])
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root]
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return [root1, root2]


print(solve(a, b, c))
