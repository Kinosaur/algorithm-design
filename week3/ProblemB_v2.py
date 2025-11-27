# Kaung Khant Lin
# 6540131
# 542

import sys
import time
sys.setrecursionlimit(10000) # set recursion-stack depth

prices = list(map(int, input().split()))
L = len(prices)

call_count = 0
maxRev = {}  # Memoization dictionary

def MaxRevenue(L, prices):
    global call_count
    call_count += 1
    
    # CHECK in MEMO
    if L in maxRev:
        return maxRev[L]
    
    # BASE CASE
    if L == 0:
        return 0
    
    v = float('-inf')
    
    # RECURSIVE CASE
    for i in range(1, L + 1):
        v = max(prices[i - 1] + MaxRevenue(L - i, prices), v)
    
    # ADD to MEMO
    maxRev[L] = v
    
    return v

start_time = time.time()
result = MaxRevenue(L, prices)
end_time = time.time()

print(f"Maximum revenue: {result}")
print(f"Recursive calls: {call_count}")
print(f"Time: {end_time - start_time:.6f} seconds")
