# Kaung Khant Lin
# 6540131
# 542

import sys
import time
sys.setrecursionlimit(10000) # set recursion-stack depth

C = list(map(int, input().split()))
n = int(input())

call_count = 0

def MinChange(n, C):
    global call_count
    call_count += 1
    
    # BASE CASE
    if n == 0:
        return 0
    
    v = float('inf')
    
    # RECURSIVE CASE
    for c in C:
        if c <= n:  # Only try valid coins
            # Recursive call
            result = MinChange(n - c, C)
            
            # Update minimum
            v = min(result + 1, v)
    
    return v

start_time = time.time()
result = MinChange(n, C)
end_time = time.time()

print(f"Minimum coins needed: {result}")
print(f"Recursive calls: {call_count}")
print(f"Time: {end_time - start_time:.6f} seconds")