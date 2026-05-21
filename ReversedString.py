# Задача
# Напишите программу, которая развернет число / строку / список / матрицу.
# Напишите функцию, которая принимает строку и возвращает её в обратном порядке.

# Вариант 1
def revert_str_1(some_str: str) -> str:
   return ''.join(reversed(some_str))

# Вариант 2
def revert_str_2(some_str: str) -> str:
   return some_str[::-1]

some_string = input("Введите строку: ")
print(revert_str_1(some_string))
print(revert_str_2(some_string))
