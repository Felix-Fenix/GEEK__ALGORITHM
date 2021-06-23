
import random

SIZE_ROW = 5
SIZE_COL = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_COL)]
          for _ in range(SIZE_ROW)]

for line in matrix:
    print(*line, sep='\t')

max_ = None
print(max_)
for j, min_ in enumerate(matrix[0]):
    print(j, min_)
    # for i in range(len(matrix)):
    #     if matrix[i][j] < min_:
    #         min_ = matrix[i][j]
    for i, line in enumerate(matrix):
        print(i, line)
        if line[j] < min_:
            min_ = line[j]
    print(min_)
    if max_ is None or max_ < min_:
        max_ = min_
        print(f"if max_ :{max_}")

print(f'Max in min = {max_}')