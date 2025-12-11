# Kaung Khant Lin
# 6540131
# 542

# Version 1: Naive Recursive Brute Force
import sys
import time
sys.setrecursionlimit(2000)

A = input().strip()
B = input().strip()

def editDistance(i, j):
    # BASE CASES
    # If A is empty, insert all remaining chars of B
    if i == len(A):
        return len(B) - j
    
    # If B is empty, delete all remaining chars of A
    if j == len(B):
        return len(A) - i

    # RECURSIVE CASES
    # Case 1: Match
    if A[i] == B[j]:
        return editDistance(i + 1, j + 1)
    
    # Case 2: Mismatch
    else:
        # Calculate cost for all 3 options
        insert_cost = 1 + editDistance(i, j + 1)      # Insert
        delete_cost = 1 + editDistance(i + 1, j)      # Delete
        sub_cost    = 1 + editDistance(i + 1, j + 1)  # Substitute
        
        return min(insert_cost, delete_cost, sub_cost)
    
start = time.time()
result = editDistance(0, 0)
end = time.time()

print(f'Minimum Edit Distance: {result}')
print(f"Time: {end - start:.6f} seconds")
