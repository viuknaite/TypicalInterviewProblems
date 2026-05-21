# Задача
# Напишите функцию, которая принимает строку и проверяет, является ли она палиндромом.
# Напишите функцию, которая проверяет, является ли строка палиндромом, игнорируя:
#     регистр символов
#     пробелы
#     знаки препинания

def is_palindrome(some_str):
    cleaned = some_str.replace(" ", "")

    if cleaned == cleaned[::-1]:
        return 'YES'
    return 'NO'

phrase = "А роза упала на лапу Азора".lower()
print(is_palindrome(phrase))
