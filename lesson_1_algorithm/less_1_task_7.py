# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования
# треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.
print('Введите длину стороны треугольника')
a = int(input('Введите первое число : '))
b = int(input('Введите первое число : '))
c = int(input('Введите первое число : '))
if a == b and a == c:
    print(f'Треугольник равносторонний')
elif a == b and a != c:
    print(f'Треугольник равнобедренный')
elif a != b and a != c:
    print(f'Треугольник разносторонний')
else:
    print(f'Треугольник равнобедренный')