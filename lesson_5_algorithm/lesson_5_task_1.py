"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.

"""
from collections import defaultdict

# company = [
#     ('steeper', 12), ('steeper', 2), ('steeper', 88), ('steeper', 13),
#     ('racer', 11), ('racer', 22), ('racer', 21), ('racer', 45),
#     ('raid', 45), ('raid', 34), ('raid', 5), ('raid', 27)
# ]

company = []
while True:

    print('Закончить ввод нажмите `q`')
    company_name = input('Введите наименование предприятия: ')
    if company_name == 'q':
        break

    number = 1
    while number < 5:

        quarter = int(input(f'Введите прибыль за {number}-й квартал: '))
        number += 1
        company.append((company_name, quarter))

print('---------------------------------------')

comp = defaultdict(list)
for i, k in company:
    comp[i].append(k)

avg = []
for i in comp.values():
    avg.append(sum(i))

result = round(sum(avg) / len(avg), 2)

for j in comp.items():
    if sum(j[1]) >= result:
        print(f"У предприятия: `{j[0]}` прибыль выше среднего")
    else:
        print(f"У предприятия: `{j[0]}` прибыль ниже среднего")

print(f"Средняя годовая прибыль: `{result}`")
