
jewelery = {"Rolex": ["Платина", 300000, 1],
            "Кольцо": ["Золото", 1150, 5],
            "Подвеска": ["Серебро", 270, 7]}
my_basket = 0
while 1:
    print("1. Просмотр описания: название – описание\n"
          "2. Просмотр цены: название – цена\n"
          "3. Просмотр количества: название – количество\n"
          "4. Всю информацию\n"
          "5. Покупка\n"
          "6. Выход\n")
    i = input()
    if i == '1':
        for item, info in jewelery.items():
            print(f"{item} – {info[0]}")
    elif i == '2':
        for item, info in jewelery.items():
            print(f"{item} – {info[1]}")
    elif i == '3':
        for item, info in jewelery.items():
            print(f"{item} – {info[2]}")
    elif i == '4':
        for item, info in jewelery.items():
            print(f"{item} – {info[0]}, Цена: {info[1]} руб., Количество: {info[2]} шт.")
    elif i == '5':
        if my_basket != 0:
            print(f"Вы купили вещей на {my_basket} р.")
        good = input("Введите желаемый к покупке товар\n")
        if good in jewelery:
            amount = input("Введите количество товара\n")
            if amount == 'n':
                break
            elif not amount.isdigit():
                print("Неверное количество")
            else:
                amount = int(amount)
                if amount > jewelery[good][2]:
                    print("Товара в таком количестве нет в наличии")
                elif amount == jewelery[good][2]:
                    my_basket = jewelery[good][1] * amount
                    del jewelery[good]
                else:
                    my_basket = jewelery[good][1] * amount
                    jewelery[good][2] -= amount
            break
        else:
            print("Данного товара нет в наличии")
    elif i == '6':
        if my_basket != 0:
            print(f"Вы купили вещей на {my_basket} р.")
        print("До свидания")
        break
    else:
        print("Неверно выбран пункт меню")