def get_matrix(n, m, value):

    matrix_1 = []

    for i in range(n):
        matrix_2 = []
        for j in range(m):
            matrix_2.append(value)
        matrix_1.append(matrix_2)
    return matrix_1

print(get_matrix(int(input('Введите количество столбцов: ')),
                 int(input('Введите количество строк: ')),
                 int(input('Введите значение: '))))


