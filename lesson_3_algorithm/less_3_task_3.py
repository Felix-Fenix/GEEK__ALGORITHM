"""
В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.

"""

array = [59, 17, 40, 29, 68, 39, 9, 71, 50, 20]
print(array)
numberMAX = 0
numberMIN = 0
for j in range(len(array)):
    if array[j] > numberMAX:
        numberMAX = array[j]
    for i in range(len(array)):
        if array[i] < array[j]:
            numberMIN = array[i]

arMAX_index = array.index(numberMAX)
arMIN_index = array.index(numberMIN)
array.pop(arMAX_index)
array.insert(arMAX_index, numberMIN)
array.pop(arMIN_index)
array.insert(arMIN_index, numberMAX)
print(array)
print(numberMAX, numberMIN)
