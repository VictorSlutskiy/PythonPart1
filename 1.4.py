text = input("Введите текст: ")
point_counter=0
one = set("aeioulnstr")
two = set("dg")
three = set("bcmp")
four = set("fhvwy")
five = set("k")
six = set("jx")
ten = set("qz")
for letter in text: #подсчет очков
    if letter in one:
        point_counter+=1
    elif letter in two:
        point_counter += 2
    elif letter in three:
        point_counter += 3
    elif letter in four:
        point_counter += 4
    elif letter in five:
        point_counter += 5
    elif letter in six:
        point_counter += 6
    elif letter in ten:
        point_counter += 10
print("Количество очков - ", point_counter)
