# Kaung Khant Lin
# 6540131
# 542

import sys

sys.setrecursionlimit(10**7)

H, T = map(int, input().split())

grid = []
for _ in range(T):
    grid.append(list(map(int, input().split())))


def solve(t, h):
    # Base Case 1: Out of bounds (bird hit the floor or ceiling)
    if h < 0 or h >= H:
        return False

    # Base Case 2: Hit an obstacle
    if grid[t][h] == 1:
        return False

    # Base Case 3: Reached the last interval successfully!
    if t == T - 1:
        return True

    # Recursive Case: Try possible moves (Up, Straight, Down)
    if solve(t + 1, h):
        return True  # Move Straight
    if solve(t + 1, h + 1):
        return True  # Move Up
    if solve(t + 1, h - 1):
        return True  # Move Down

# Try starting the bird at every possible height at interval 0
for start_h in range(H):
    if solve(0, start_h):
        
        print(start_h + 1)
        break