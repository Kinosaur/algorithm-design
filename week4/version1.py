# Kaung Khant Lin
# 6540131
# 542

# Version 1: Naive Recursive Brute Force
import sys
import time
sys.setrecursionlimit(10000)

# Number_of_items(N) Max_capacity(M)
N, M = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

x = [0] * N         #  Global list
call_count = 0

def comb(i):
    global call_count
    call_count += 1
    
    # BASE CASE
    if i == N:
        current_weight = 0
        current_value = 0
        
        # Calculate totals based on x
        for j in range(N):
            if x[j] == 1:
                current_weight += weights[j]
                current_value += values[j]
        
        if current_weight > M:
            return -1
        else:
            return current_value
    else:
        # RECURSIVE CASE
        x[i] = 0
        a = comb(i + 1)
        x[i] = 1
        b = comb(i + 1)
        return max(a, b)
    
start_time = time.time()
result = comb(0)
end_time = time.time()

print(f"Maximum profit: {result}")
print(f"Recursive calls: {call_count}")
print(f"Time: {end_time - start_time:.6f} seconds")