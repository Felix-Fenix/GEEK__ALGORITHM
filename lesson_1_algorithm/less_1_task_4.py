# 4. Написать программу, которая генерирует в указанных пользователем границах:
#
#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.
#
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
a = int(input('Введите первое число : '))
b = int(input('Введите второе число : '))
res = random.randrange(a,b + 1)
print(res)
print(round(random.uniform(a,b),2))
if res >26:
    res = 26
print(chr(res + 96))