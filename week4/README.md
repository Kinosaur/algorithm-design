# Week 4: Dynamic Programming - 0-1 Knapsack Problem

## Problem A: 0-1 Knapsack

Given a maximum weight you can carry in a knapsack and items, each with a weight and a value, find a set of items you can carry in the knapsack so as to maximize the total value.

### Input/Output
- **Input**: 
  - Line 1: Number of items (N) and maximum capacity (M)
  - Line 2: Weights of each item
  - Line 3: Values of each item
- **Output**: Maximum total value achievable

### Example
```
Input:
5 8
4 3 5 6 2
9 8 10 9 3

Output:
Maximum profit: 18
```

### Implementations

#### version1.py - Brute Force (Binary Combinations)
- Uses global decision array `x[]` to track item selection
- Generates all 2^N combinations using binary choices (0 or 1)
- At base case, calculates total weight and value from decision array
- Returns -1 for invalid combinations (weight > capacity)
- Time complexity: O(2^N × N)

#### version2.py - Brute Force with Two State Variables
- Uses two state variables: item index `i` and remaining capacity `C`
- No global decision array needed
- Cleaner recursive structure with skip/take decisions
- Pruning: only considers "take" if item weight ≤ remaining capacity
- Time complexity: O(2^N)

#### version3.py - Memoization (Top-Down DP)
- Builds on version2 with memoization dictionary
- Caches results for each unique (item_index, remaining_capacity) pair
- Avoids redundant calculations for overlapping subproblems
- Time complexity: O(N × M)
- Space complexity: O(N × M) for memo table

### Recursive Structure

```
maxVal(i, C):
    if i == N:                          # Base case: no more items
        return 0
    
    skip = maxVal(i + 1, C)             # Option 1: Skip item i
    
    if weights[i] <= C:                 # Option 2: Take item i (if fits)
        take = values[i] + maxVal(i + 1, C - weights[i])
    else:
        take = -1
    
    return max(skip, take)
```

---

## Performance Results

### Version 1: Brute Force

| Test Case | Recursive Calls | Time (s) |
|-----------|-----------------|----------|
| knapsack0.in | 63 | 0.000017 |
| knapsack1.in | 2097151 | 0.704563 |
| knapsack2.in | 65535 | 0.021793 |
| knapsack3.in | 33554431 | 13.663992 |
| knapsack4.in | 2047 | 0.000555 |
| knapsack5.in | - | - |
| knapsack6.in | - | - |
| knapsack7.in | - | - |

### Version 2: Brute Force with Two State Variables

| Test Case | Recursive Calls | Time (s) |
|-----------|-----------------|----------|
| knapsack0.in | 32 | 0.000006 |
| knapsack1.in | 506469 | 0.036397 |
| knapsack2.in | 44448 | 0.003811 |
| knapsack3.in | 17770698 | 1.178952 |
| knapsack4.in | 249 | 0.000023 |
| knapsack5.in | - | - |
| knapsack6.in | - | - |
| knapsack7.in | - | - |

### Version 3: Memoization

| Test Case | Recursive Calls | Time (s) |
|-----------|-----------------|----------|
| knapsack0.in | 32 | 0.000009 |
| knapsack1.in | 2446 | 0.000333 |
| knapsack2.in | 6373 | 0.001245 |
| knapsack3.in | 12064216 | 2.852295 |
| knapsack4.in | 208 | 0.000041 |
| knapsack5.in | 152601 | 0.02985 |
| knapsack6.in | - | - |
| knapsack7.in | 311991 | 0.059377 |

---

## Test Cases

Located in `knapsacktests/` directory:

| Test File | N Items | Capacity | Expected Answer | Notes |
|-----------|---------|----------|-----------------|-------|
| knapsack0.in | 5 | 8 | 18 | Small test case |
| knapsack1.in | 20 | 500 | 59 | Medium test case |
| knapsack2.in | 15 | 750 | 1458 | Medium test case |
| knapsack3.in | 24 | 6404180 | 13549094 | Large capacity - unlikely to solve fast with DP |
| knapsack4.in | 10 | 165 | 171 | Small test case |
| knapsack5.in | 100 | 1000 | 3403 | Large N, moderate capacity |
| knapsack6.in | 200 | 100000000 | 7134 | Very large - unlikely to solve fast with DP |
| knapsack7.in | 200 | 1000 | 6491 | Large N, small capacity |

### Input Format
```
Number_of_items(N) Max_capacity(M)
weight_0 weight_1 . . . weight_N-1
value_0  value_1  . . . value_N-1
```

---

## Key Concepts

### Optimal Substructure
The 0-1 Knapsack problem exhibits optimal substructure:
- $maxVal(i, C) = \max(skip, take)$
- $skip = maxVal(i+1, C)$
- $take = values[i] + maxVal(i+1, C - weights[i])$ if $weights[i] \leq C$

### Version Comparison

| Version | Approach | State | Pruning | Memoization |
|---------|----------|-------|---------|-------------|
| v1 | Binary combinations | Global array `x[]` | Weight check at leaf | No |
| v2 | Two state variables | `(i, C)` parameters | Weight check before take | No |
| v3 | Top-down DP | `(i, C)` parameters | Weight check + memo | Yes |

### Performance Analysis
- **v1 → v2**: State variable approach reduces calls by avoiding invalid branches earlier
- **v2 → v3**: Memoization provides dramatic improvement for test cases with overlapping subproblems
- **Note**: knapsack3.in and knapsack6.in have very large capacities, making even memoization slow due to sparse memo table utilization

---

## Usage

### Run Knapsack Solutions
```bash
# Version 1: Brute Force
python3 version1.py < knapsacktests/knapsack0.in

# Version 2: Two State Variables
python3 version2.py < knapsacktests/knapsack0.in

# Version 3: Memoization
python3 version3.py < knapsacktests/knapsack0.in
```

### Expected Output
```
Maximum profit: 18
Recursive calls: 32
Time: 0.000009 seconds
```

---

## Additional Resources

- **Week4_answers.pdf**: Contains answers to worksheet questions
- **knapsacktests.zip**: Extract to get all test case files

---

## 👤 Author

[Kinosaur](https://github.com/Kinosaur)
