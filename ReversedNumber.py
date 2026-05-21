# Задача
# Напишите программу, которая развернет число / строку / список / матрицу.
# Напишите функцию, которая принимает целое число и возвращает число, записанное в обратном порядке.

# Вариант 1
num = int(input("Введите число: "))

while num != 0:
   last_digit = num % 10
   num //= 10
   print(last_digit, end='')

print()

# Вариант 2
def rotated_num_while(num: int) -> None:
    while num != 0:
        last_digit = num % 10
        num //= 10
        print(last_digit, end='')
    print()

# Вариант 3
def rotated_num_for(num: int) -> int:
    result = 0

    for _ in range(num):
        if num == 0:
            break

        result = result * 10 + num % 10
        num //= 10

    return result

num = int(input("Введите число: "))
rotated_num_while(num)
print(rotated_num_for(num))
