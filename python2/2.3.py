def find_and_reduce(matrix):
    found_zero_row = False
    zero_row_index = None
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for i in range(num_rows):
        if all(element == 0 for element in matrix[i]):
            found_zero_row = True
            zero_row_index = i
            break
    if found_zero_row:

        for j in range(num_cols):
            if j == zero_row_index:
                for i in range(num_rows):
                    matrix[i][j] /= 2
    return matrix


def input_matrix():
    while True:
        try:
            num_rows = int(input("Введите количество строк матрицы: "))
            num_cols = int(input("Введите количество столбцов матрицы: "))
            matrix = []
            for i in range(num_rows):
                row = []
                for j in range(num_cols):
                    element = float(input(f"Введите элемент матрицы ({i + 1}, {j + 1}): "))
                    row.append(element)
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка: Некорректный ввод числа. Пожалуйста, попробуйте снова.")


try:
    matrix = input_matrix()
    print("Исходная матрица:")
    for row in matrix:
        print(row)
    result = find_and_reduce(matrix)
    print("Матрица после обработки:")
    for row in result:
        print(row)
except KeyboardInterrupt:
    print("Процесс ввода прерван пользователем.")
