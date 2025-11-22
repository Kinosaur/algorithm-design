# Kaung Khant Lin
# 6540131
# 542

import sys
import time
sys.setrecursionlimit(10000) # set recursion-stack depth

# Global variables
items = []
n = 0
total_sum = 0  # Total sum of all items
min_diff = 999999999 # Initialize with a huge number

def solve(i, sum_a):
    global min_diff
    
    # BASE CASE: All items have been assigned a basket
    if i == n:
        # sum_a is the sum of group A
        # sum_b can be calculated as total_sum - sum_a
        sum_b = total_sum - sum_a
        
        # Calculate difference
        diff = abs(sum_a - sum_b)
        
        # Update global minimum if this is the best split so far
        if diff < min_diff:
            min_diff = diff
        return

    # RECURSIVE CASE
    
    # Option 0: Put item[i] in Group A
    solve(i + 1, sum_a + items[i])
    
    # Option 1: Put item[i] in Group B
    solve(i + 1, sum_a)

items = list(map(int, input().split()))
n = len(items)
total_sum = sum(items)

start_time = time.time()
solve(0, 0) # Start recursion with sum_a = 0
end_time = time.time()

print(f"Minimal Difference: {min_diff}")
print(f"Time: {end_time - start_time:.6f} seconds")
