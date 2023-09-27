try:
    with open("grades.txt", "r", encoding="utf-8") as grades:
        for line in grades:
            data = line.split()
            surname = data[0]
            scores = [int(score) for score in data[1:]]
            average_score = sum(scores) / len(scores)
            if average_score > 8:
                print("Фамилия: ", surname, "Средний балл: ", round(average_score, 2))
except IOError:
    print("Произошла ошибка ввода-вывода!")
