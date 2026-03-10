# Kaung Khant Lin
# 6540131
# 542

import sys

# Read all standard input at once
input_data = sys.stdin.read().split()
if not input_data:
    exit()
    
iterator = iter(input_data)

N = int(next(iterator))
M = int(next(iterator))
S = int(next(iterator))
T = int(next(iterator))

# Build Adjacency List
graph = {i: [] for i in range(N)}

for _ in range(M):
    u = int(next(iterator))
    v = int(next(iterator))
    energy = int(next(iterator))
    graph[u].append((v, energy))
    graph[v].append((u, energy)) 

current = S
total_energy = 0
visited = [False] * N
visited[current] = True

while current != T:
    next_node = -1
    min_energy = float('inf')
    
    for neighbor, cost in graph[current]:
        if not visited[neighbor] and cost < min_energy:
            min_energy = cost
            next_node = neighbor
            
    if next_node == -1:
        break 
        
    total_energy += min_energy
    current = next_node
    visited[current] = True

if current == T:
    print(total_energy)
else:
    print("Impossible to reach the relic")