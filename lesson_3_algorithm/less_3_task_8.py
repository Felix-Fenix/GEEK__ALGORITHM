"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в
последнюю ячейку строки. В конце следует вывести полученную матрицу.

"""


def addition(arr):
    sum_s = 0
    for i in arr:
        sum_s += i
    return sum_s


a = [int(i) for i in input('Введите 4 натуральных числа : ')]
b = [int(i) for i in input('Введите 4 натуральных числа : ')]
c = [int(i) for i in input('Введите 4 натуральных числа : ')]
d = [int(i) for i in input('Введите 4 натуральных числа : ')]

array = [a, b, c, d]

for i in array:
    sum_l = []
    for j in i:
        sum_l.append(j)
        print("%3s" % j, end=' ')
    print("%3s" % addition(sum_l))
