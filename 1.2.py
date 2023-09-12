text = input("Введите текст: ")
vowels_count = 0
consonants_count = 0
vowels = set("eyuioa")
for letter in text: #подсчет гласных
    if letter in vowels:
        vowels_count += 1
    else: #подсчет согласных
        if letter != ' ':
            consonants_count += 1
if vowels_count == consonants_count: #если количество согласных равно гласным то выводятся все гласные
    for letter in text:
        if letter in vowels:
            print(letter)
word_list = text.split() #создаем список слов
print("Количество слов - ", len(word_list))
print("Количество гласных в тексте - ", vowels_count, " Количество согласных - ", consonants_count)
