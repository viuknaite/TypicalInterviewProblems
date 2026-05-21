# Задача
# Напишите программу, которая развернет число / строку / список / матрицу.
# Напишите функцию, которая принимает список и возвращает новый список с элементами в обратном порядке.

# Вариант 1
def reverse_slice(numbers):
    return numbers[::-1]

# Вариант 2
def reverse_method(numbers):
    numbers.reverse()
    return numbers

numbers = [1, 2, 3, 4, 5]
print(reverse_slice(numbers))
print(reverse_method(numbers))
