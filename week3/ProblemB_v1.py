# Kaung Khant Lin
# 6540131
# 542

import sys
import time
sys.setrecursionlimit(10000) # set recursion-stack depth

prices = list(map(int, input().split()))
L = len(prices)  # Rod length is determined by the number of prices

call_count = 0

def MaxRevenue(L, prices):
    global call_count
    call_count += 1
    
    # BASE CASE
    if L == 0:
        return 0
    
    v = float('-inf')
    
    # RECURSIVE CASE
    # 1 + MaxRevenue(9) if L=10 and cut at 1
    for i in range(1, L + 1):
        result = prices[i - 1] + MaxRevenue(L - i, prices)
        
        v = max(result, v)
    
    return v

start_time = time.time()
result = MaxRevenue(L, prices)
end_time = time.time()

print(f"Maximum revenue: {result}")
print(f"Recursive calls: {call_count}")
print(f"Time: {end_time - start_time:.6f} seconds")