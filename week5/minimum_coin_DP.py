# Kaung Khant Lin
# 6540131
# 542

# Minimum Coin Change Problem using Dynamic Programming
import time

C = list(map(int, input().split()))
n = int(input())

# Initialize DP table: dp[i] = minimum coins needed for amount i
dp = [float('inf')] * (n + 1)

# BASE CASE: 0 coins needed for amount 0
dp[0] = 0

# Fill table bottom-up from 1 to n
for current_amount in range(1, n + 1):
    
    # Try using each coin denomination
    for c in C:
        if c <= current_amount:
            # Use coin c: 1 coin + min coins for remaining amount
            dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount - c])

start_time = time.time()
result = dp[n]
end_time = time.time()

# Check if solution exists
if result == float('inf'):
    print("Change not possible")
else:
    print(f"Minimum coins needed: {result}")

print(f"Time: {end_time - start_time:.6f} seconds")