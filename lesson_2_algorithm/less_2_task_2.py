""""
2.Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

answer = input('Введите набор чисел :')

a = 0
b = 0
for i in range(len(answer)):
    if int(answer[i]) % 2 == 0:
        a += 1
    else:
        b += 1
print(f"Нечётных : {b}")
print(f"Чётных : {a}")



