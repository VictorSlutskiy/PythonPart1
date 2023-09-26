try:
    with open("F1.txt", "w") as F1:
        while 1:
            line = input("Введите строку (пустая строка для завершения ввода): ")
            if not line:
                break
            F1.write(line + "\n")
    with open("F1.txt", "r") as F1, open("F2.txt", "w") as F2:
        lines = F1.readlines()
        for num,line in enumerate(lines):
            if num % 2 != 1:
                F2.write(line)
    with open("F2.txt", "r") as F2:
        first_line = F2.readline()
        words_count = len(first_line.split())
except IOError:
    print("Произошла ошибка ввода-вывода!")

print(f"Количество слов в первой строке файла F2: {words_count}")
with open('F2.txt', 'r') as F2:
    for line in F2:
        print(line)