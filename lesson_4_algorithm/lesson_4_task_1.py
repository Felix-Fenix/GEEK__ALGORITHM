"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.

Примечание. Идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),

● написать 3 варианта кода (один у вас уже есть),

● проанализировать 3 варианта и выбрать оптимальный,

● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),

● написать общий вывод: какой из трёх вариантов лучше и почему.

 ------------------ Задача урок 3 упражнение 7 --------------------------
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
между собой (оба являться минимальными), так и различаться.

"""
import timeit
import cProfile


array = [85, 18, 51, 32, 22, 90, 65, 74, 76, 34]

"""
    Вариант № 1
"""


def min_n(a, b):
    return a if a < b else b


def sort_min_1(arr):
    min_list = []
    for i in range(len(arr)):
        if i != '':
            min_number = arr[0]
            for elem in arr:
                min_number = min_n(min_number, elem)

            arr.remove(min_number)
            min_list.append(min_number)
    return min_list


sort_LIST = sort_min_1(array.copy())
print("********************************************")
print(f'Вариант № 1: {sort_LIST[0]}, {sort_LIST[1]}')
cProfile.run('sort_min_1(array.copy())')

"""
    Вариант № 2
"""


def sort_min_2(arr):
    my_list = sorted(arr)
    return my_list


sort_list = sort_min_2(array.copy())
print("********************************************")
print(f'Вариант № 2: {sort_list[0]}, {sort_list[1]}')
cProfile.run('sort_min_2(array)')

"""
    Вариант № 3
"""


def sort_min_3(arr):
    number_1 = min(arr)
    arr.remove(number_1)
    number_2 = min(arr)
    return [number_1, number_2]


sort_list = sort_min_3(array.copy())
print("********************************************")
print(f'Вариант № 3: {sort_list[0]}, {sort_list[1]}')
cProfile.run('sort_min_3(array.copy())')

print('Вариант № 1 через timeit()')
print(timeit.timeit(f'a = sort_min_1(array)', number=100000, globals=globals()))

print('Вариант № 2 через timeit()')
print(timeit.timeit(f'a = sort_min_2(array)', number=100000, globals=globals()))
# print(timeit.timeit(f'a = sort_min_3(array)', number=10000, globals=globals()))

"""
КОММЕНТАРИЙ.

********************************************
Вариант № 1: 18, 22
         81 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       55    0.000    0.000    0.000    0.000 lesson_4_task_1.py:33(min_n)
        1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:37(sort_min_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}


********************************************
Вариант № 2: 18, 22
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:60(sort_min_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


********************************************
Вариант № 3: 18, 22
         8 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:75(sort_min_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}


Вариант № 1 через timeit()
0.05112114900111919
Вариант № 2 через timeit()
0.031144580003456213

Вывод:
 Вариант № 2 самый оптимальный вызов всего 5 функций в сравнении с Варинтом № 1 
 где вызываються функции 81 раз. Вариант №3 средний результат.
 По времени через timeit очевидно быстродейсвие Варианта №2.
 Не смог понять почему не запускаеться timeit с алгоритмом Вариант № 3, хотя пробывал по разному.
 
"""