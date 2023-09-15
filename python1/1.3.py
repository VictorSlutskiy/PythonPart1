from math import prod

my_list = list()
while 1:
    print("Меню\n"
          "1 - Создать список\n"
          "2 - Показать список\n"
          "3 - Произведение элементов с нечетными номерами\n"
          "4 - Найдите наибольший элемент списка, затем удалите его и выведите новый список.\n"
          "5 - Вывести три наибольших элемента\n"
          "0 - Завершить программу\n"
          )
    choice = input()
    if choice == "1":
        while True:
            try:
                amount = int(input("Введите количество элементов: "))
            except ValueError:
                print("Введите только положительное число")
                continue
            for i in range(amount):
                while True:
                    try:
                        item = float(input("Введите элемент: "))
                        my_list.append(item)
                        break
                    except ValueError:
                        print("Введите только числа")
    elif choice == "2":
        print("My list - ", my_list)
    elif choice == "2":
        print("My list - ", my_list)
    elif choice == "3":
        product = 1
        ns = list(map(int, my_list))
        print("product - ", prod(ns[::2]))
    elif choice == "4":
        print("before -", my_list)
        my_list.remove(max(my_list))
        print("after -", my_list)
    elif choice == "5":
        my_list.sort()
        print(my_list)
        print("Три наибольших - ", my_list[-3:])
    elif choice == "0":
        print("работа завершена")
        break
    else:
        print("неверный пункт меню")
