# Задача
# Напишите программу, которая принимает два целых числа a и b (a ≤ b) и выводит все простые числа в этом диапазоне.
# Выведите все простые числа до n включительно.

# Вариант 1
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

        return True

# Вариант 2
def primes_in_range_cycle(a, b):
    result = []
    for num in range(a, b + 1):
        if is_prime(num):
            result.append(num)
    return result

# Вариант 3
def primes_in_range(a, b):
    return [n for n in range(a, b + 1) if is_prime(n)]

print(primes_in_range_cycle(1, 10))
print(primes_in_range(1, 20))