while 1:
    num = input("Введите число: ")
    rev_num = num[::-1] #число в обратном порядке
    if num.isdigit() and int(num) > 0: #проверка на число
        break
    else:
        print("Вводите только натуральные числа ")
max_digit = 0
for digit in str(num): #поиск максимального числа
    if int(digit) > max_digit:
        max_digit = int(digit)
print("Максимальная цифра ", max_digit, "Число наоборот", rev_num)
