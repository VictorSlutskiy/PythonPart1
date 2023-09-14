def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
        return None
    finally:
        print("Этот блок выполнится в любом случае, независимо от исключения или его отсутствия.")

    return result

while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = divide_numbers(num1, num2)
        if result is not None:
            print(f"Результат деления: {result}")
    except ValueError:
        print("Значение введено не корректно. Пожалуйста, введите число.")