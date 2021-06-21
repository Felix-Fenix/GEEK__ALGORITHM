"""
Определить, какое число в массиве встречается чаще всего.

"""

array = [59, 17, 40, 29, 68, 29, 39, 9, 71, 50, 20, 17, 29]
array2 = []
for i in array:
    if array.count(i) > 1:
        array2.append(i)

set_t = set(array2)

result = {}
for i in set_t:
    result[i] = array2.count(i)
print(result)


# from collections import Counter
# c = Counter(array)
# print(c)

