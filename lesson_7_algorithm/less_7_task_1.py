"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

Примечания:

● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,

● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

"""

import random


MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(MIN_ITEM, MAX_ITEM - 1) ]
print(array)


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


print(bubble_sort(array))
