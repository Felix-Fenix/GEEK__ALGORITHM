"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на
уроках (сортировка слиянием также недопустима).

"""

import random

MIN_ITEM = 0
MAX_ITEM = 10
rand = random.randint(MIN_ITEM, MAX_ITEM)
array = [random.randint(0, i) for i in range((2 * rand) + 1)]

print(array)
print(sorted(array))
print('=' * 60)


def median(array):
    middle = len(array) // 2
    array.sort()
    if not len(array) % 2:

        return (array[middle - 1] + array[middle]) / 2.0
    return array[middle]


print(f'Медиана равна = {median(array)}')

