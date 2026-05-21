# Задача
# Напишите функцию, которая принимает два списка и возвращает новый список, содержащий все элементы обоих списков.
# Напишите функцию, которая объединяет два списка и возвращает новый список без повторяющихся элементов, сохраняя порядок первого появления элементов.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Вариант 1
def merge_lists_plus(lst1: list[int], lst2: list[int]) -> list[int]:
    return lst1 + lst2

result_plus = merge_lists_plus(list1, list2)
print(result_plus)

# Вариант 2
def merge_lists_method(lst1: list[int], lst2: list[int]) -> list[int]:
    lst1.extend(lst2)
    return lst1

result_method = merge_lists_method(list1, list2)
print(result_method)

# Вариант 3
def merge_unique_ordered(lst1: list[int], lst2: list[int]) -> list[int]:
    return list(dict.fromkeys(lst1 + lst2))

result_unique = merge_unique_ordered(list1, list2)
print(result_unique)
