# Kaung Khant Lin
# 6540131
# 542

import sys
import math

input_data = sys.stdin.read().split()
iterator = iter(input_data)

N = int(next(iterator))
coordinate = []
for _ in range(N):
    x = int(next(iterator))
    y = int(next(iterator))
    coordinate.append((x, y)) # Store as (start, finish)

print(N, coordinate)

distances = []

for i in range(N):
    for j in range(i, N):
        x1, y1 = coordinate[i]
        x2, y2 = coordinate[j]

        sum = (x2 -x1)**2  + (y2 -y1)**2
        result = round(math.sqrt(sum), 2)
        if result > 0.0:
            distances.append(result)


print(min(distances))

# i = 0
# j = 3

# x1, y1 = coordinate[i]
# x2, y2 = coordinate[j]

# sum = (x2 -x1)**2  + (y2 -y1)**2
# result = round(math.sqrt(sum), 2)

# print(result)
