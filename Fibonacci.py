# Задача
# Напишите функцию, которая принимает целое число n и возвращает n-е число последовательности Фибоначчи.
# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.

# Вариант 1
def print_fibonacci(n: int) -> None:
    f1, f2 = 0, 1
    for _ in range(n):
        f1, f2 = f2, f1 + f2
        print(f1, end=' ')
    print()

# Вариант 2
def get_fibonacci(n: int) -> list[int]:
    result = []
    f1, f2 = 0, 1
    for _ in range(n):
        f1, f2 = f2, f1 + f2
        result.append(f1)
    return result

n = int(input("Введите количество итераций: "))
print_fibonacci(n)
print(get_fibonacci(n))