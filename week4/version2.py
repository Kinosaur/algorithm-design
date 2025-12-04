# Kaung Khant Lin
# 6540131
# 542

import sys
import time
sys.setrecursionlimit(10000)

# Number_of_items(N) Max_capacity(M)
N, M = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

call_count = 0

def maxVal(i, C):
    global call_count
    call_count += 1
    
    # BASE CASE
    if i == N:
        return 0
    else:
        # RECURSIVE CASE
        skip = maxVal(i + 1, C)
        if weights[i] <= C:
            take = values[i] + maxVal(i + 1, C - weights[i])
        else:
            take = -1
        return max(skip, take)

start_time = time.time()
result = maxVal(0, M)
end_time = time.time()

print(f"Maximum profit: {result}")
print(f"Recursive calls: {call_count}")
print(f"Time: {end_time - start_time:.6f} seconds")