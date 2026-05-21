# Задача
# Напишите программу, которая развернет число / строку / список / матрицу.
# Напишите функцию, которая принимает матрицу (список списков) и возвращает ее в перевернутом виде.

# Вариант 1
def reverse_matrix_1(matrix):
    return matrix[::-1]

# Вариант 2
def reverse_matrix_2(matrix):
    return [row[::-1] for row in matrix[::-1]]

# result = []
# for row in matrix[::-1]:
#     reversed_row = row[::-1]
#     result.append(reversed_row)

m = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(reverse_matrix_1(m))
print(reverse_matrix_2(m))
