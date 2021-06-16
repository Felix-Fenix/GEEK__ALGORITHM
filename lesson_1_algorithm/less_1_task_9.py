# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input(' Введите первое число :'))
b = int(input(' Введите второе число :'))
c = int(input(' Введите третье число :'))
var = 0
if a > b:
    var = a
    if var > c:
        var = c
        if var > b:
                var = c
                print(f'Среднее число {var}')
        else:
                var = b
                print(f'Среднее число {var}')
    else:
        var = a
        print(f'Среднее число {var}')
elif a < b:
    var = b
    if var > c:
        var = c
        print(f'Среднее число {var}')
    else:
        var = b
        print(f'Среднее число {var}')

