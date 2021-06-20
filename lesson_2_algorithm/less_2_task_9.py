"""
9.Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.

"""
answer = input('Введите последовательность чисел : ')
chars = '1234567890'
for char in chars:
    count = answer.count(char)
    if count > 1:
        res = int(count) * int(char)
        print(f" Цифра {char} повторяется {count} раз , сумма : {res}")
