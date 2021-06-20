"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Сами минимальный и максимальный элементы в сумму не включать.

"""
array = [59, 17, 40, 29, 68, 29, 39, 9, 71, 50, 20, 17, 29]


def min_n(a, b):
    return a if a < b else b


def max_n(a, b):
    return a if a > b else b


def addition(a, b):
    return a + b


max_number = array[0]
min_number = array[0]
sum_n = 0

for elem in array:
    min_number = min_n(min_number, elem)
    max_number = max_n(max_number, elem)


array.remove(min_number)
array.remove(max_number)

for i in array:
    sum_n = addition(i, sum_n)


print(f'Число min = {min_number}, число max = {max_number}')
print(f'Сумма элементов = {sum_n}')
