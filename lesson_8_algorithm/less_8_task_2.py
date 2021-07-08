"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.


"""
import collections

str_ = 'salamandra'

klist = collections.deque(str_)
klist = collections.Counter(klist)
klist2 = {}
# for i in range(len(klist)):
klist2.update(klist)
print((klist2))
print(sorted(klist2.items()))




