def process_input(data):
    try:
        if isinstance(data, list):
            product_of_odd_elements = 1
            max_element = float('-inf')
            for i, element in enumerate(data):
                if i % 2 != 0:
                    product_of_odd_elements *= element
                if element > max_element:
                    max_element = element
            data.remove(max_element)
            return {
                "Произведение элементов": product_of_odd_elements,
                "Новый список": data
            }
        elif isinstance(data, dict):
            sorted_dict = dict(sorted(data.items(), key=lambda item: item[0]))
            return sorted_dict
        elif isinstance(data, int):
            if data < 2:
                return "Число не простое"
            for i in range(2, int(data ** 0.5) + 1):
                if data % i == 0:
                    return "Число не простое"
            return "Число простое"
        elif isinstance(data, str):
            vowels = "AEIOUaeiou"
            consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
            vowel_count = sum(1 for char in data if char in vowels)
            consonant_count = sum(1 for char in data if char in consonants)
            return {
                "Глвсных": vowel_count,
                "Соглвсных": consonant_count
            }
        else:
            raise TypeError("Тип данных не поддерживается")
    except TypeError as e:
        return f"Ошибка: {str(e)}"


print(process_input([1, 2, 3, 4, 5, 6]))
print(process_input({"b": 2, "a": 1, "c": 3}))
print(process_input(7))
print(process_input("Hello, World!"))
print(process_input(1.1))
