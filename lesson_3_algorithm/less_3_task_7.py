"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
между собой (оба являться минимальными), так и различаться.

"""
array = [85, 18, 51, 32, 22, 90, 65, 74, 76, 34]

def min_n(a, b):
    return a if a < b else b


def mysort_MIN(array):
    min_list = []
    for i in range(len(array)):
        if i != []:
            min_number = array[0]
            for elem in array:
                min_number = min_n(min_number, elem)

            array.remove(min_number)
            min_list.append(min_number)
    return min_list


sort_LIST = mysort_MIN(array.copy())
print(array)
print(f'Два минимальных числа из списка: {sort_LIST[0]}, {sort_LIST[1]}')
