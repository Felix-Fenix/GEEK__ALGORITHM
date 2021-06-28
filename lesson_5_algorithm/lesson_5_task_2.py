"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
from collections import deque

number1 = input('Введите шестнацатеричное число: ').lower()
number2 = input('Введите шестнацатеричное число: ').lower()
fac_list = []
der1 = deque(number1)
der2 = deque(number2)

list_t = '0123456789abcdef0123456789abcdef'
result = []
one = 0
while True:

    if der1 == deque([]):
        if der2 == deque([]):
            break
        last = list_t.index(der2.pop())
        res = last + one
        r = list_t[res]
        result.append(r)
        break
    elif der2 == deque([]):
        last = list_t.index(der1.pop())
        res = last + one
        r = list_t[res]
        result.append(r)
        break

    first = list_t.index(der1.pop())
    second = list_t.index(der2.pop())
    res = first + second + one
    r = list_t[res]
    result.append(r)
    if res > 16 or res > 20:
        one = 1
    elif res < 16:
        one = 0

result.reverse()
print(*result)
