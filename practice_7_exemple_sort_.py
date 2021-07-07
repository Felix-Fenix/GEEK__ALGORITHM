import random

"""
    Быстрая сортировка
"""

def quick_sort(data, first, last):
    print(data[first:last + 1])
    if first >= last:
        print(data)
        return

    pivot = data[random.randint(first, last)]
    i = first
    j = last
    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i, j = i + 1, j - 1

    quick_sort(data, first, j)
    quick_sort(data, i, last)


array = [1, 9, 5, 8, 2, 4, 0, 7, 6, 3]
# print(array)
quick_sort(array, 0, len(array) - 1)

# sorted()
"""
    Сортировка
    сложных
    структур c
    использованием ключа
    
"""
from collections import namedtuple
from operator import attrgetter
from random import randint

import names

Person = namedtuple('Person', 'age, name')

people = [Person(randint(15, 50), names.get_full_name()) for _ in range(10)]
print(*people, sep='\n')
print('-'*50)
res = sorted(people)
print(*res, sep='\n')
res = sorted(people, key=attrgetter('name'))
print('-'*50)
print(*res, sep='\n')
new_res = sorted(res, key=attrgetter('age'))
print('-'*50)
print(*new_res, sep='\n')


"""
    Сортировка Шелла
"""

array = [1, 9, 5, 8, 2, 4, 0, 7, 6, 3]
print(array)


def shell_sort(data):
    assert len(data) < 4_000, 'Попробуй другую сортировку :Р'

    def new_inc(inp):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(inp) <= inc[-1]:
            inc.pop()
        while inc:
            yield inc.pop()

    for cur_inc in new_inc(data):
        for i in range(cur_inc, len(data)):
            for j in range(i, cur_inc - 1, -cur_inc):
                if data[j - cur_inc] <= data[j]:
                    break
                data[j], data[j - cur_inc] = data[j - cur_inc], data[j]
            print(data)


shell_sort(array)

"""
    Алгоритм сортировки вставками
"""
array = [1, 9, 5, 8, 2, 4, 0, 7, 6, 3]
print(array)


def insertion_sort(data):
    for i in range(len(data)):
        spam = data[i]
        j = i
        while data[j - 1] > spam and j > 0:
            data[j] = data[j - 1]
            j -= 1
        data[j] = spam
        print(data)


insertion_sort(array)
# ---------------------------------------------------


"""
    Алгоритм сортировки выбором
"""

array = [1, 9, 5, 8, 2, 4, 0, 7, 6, 3]
print(array)


def selection_sort(data):
    for i in range(len(data)):
        spam = i
        for j in range(i + 1, len(data)):
            if data[j] < data[spam]:
                spam = j
        data[spam], data[i] = data[i], data[spam]
        print(data)


selection_sort(array)

"""
    Алгоритм сортировки пузырьком
"""


array = [1, 9, 5, 8, 2, 4, 0, 7, 6, 3]
print(array)
n = 1
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
    print(array)

"""
    Сортировка слиянием
"""
import operator


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        print(left)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
