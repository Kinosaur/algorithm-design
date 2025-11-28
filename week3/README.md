# Week 3: Dynamic Programming - Coin Change and Rod Cutting

## Problem A: Minimum Coin Change

A vending machine must give change with the minimum number of coins possible for any currency denomination set, as long as coin valued 1 does not run out.

### Input/Output
- **Input**: 
  - Line 1: List of coin denominators
  - Line 2: Amount of change needed
- **Output**: Minimum number of coins required

### Example
```
Input:
1 3 4 5
7

Output:
2
```

### Implementations

#### ProblemA_v1.py - Pure Brute Force (Recursive)
- Uses pure recursion without memoization
- Time complexity: O(C^n) where C is number of coins, n is the amount
- Exponential growth in recursive calls

#### ProblemA_v2.py - With Memoization
- Uses memoization (top-down dynamic programming)
- Stores computed results to avoid redundant calculations
- Time complexity: O(n × C)
- Dramatically reduces recursive calls

### Performance Results

| Test Case | Pure Brute Force | With Memoization |
|-----------|------------------|------------------|
|           | Calls / Time(s)  | Calls / Time(s)  |
| mincoin1.in | 1153677 / 0.132614 | 105 / 0.000016 |
| mincoin2.in | - / - | 527 / 0.000053 |
| mincoin3.in | 1308 / 0.000319 | 196 / 0.000039 |
| mincoin4.in | - / - | 16687 / 0.002101 |

---

## Problem B: Rod Cutting

Serling Enterprises cuts steel rods and sells them. Given a rod of length L and price table for lengths 1 to L, determine the maximum revenue obtainable by cutting up the rod.

### Input/Output
- **Input**: Sequence of prices p₁, p₂, ..., pₗ for rod lengths 1 to L
- **Output**: Maximum revenue obtainable

### Example
```
Input:
1 5 8 12 14 16 17 20 24 27

Output:
Maximum revenue: 30
```

For a rod of length 10:
- Length 1→10: prices [1, 5, 8, 12, 14, 16, 17, 20, 24, 27]
- Optimal: Cut into pieces that maximize total revenue

### Implementations

#### ProblemB_v1.py - Pure Brute Force (Recursive)
- Tries all possible cutting combinations
- Time complexity: O(2^L)
- Exponential recursive calls

#### ProblemB_v2.py - With Memoization
- Uses memoization to cache results for each rod length
- Time complexity: O(L²)
- Significant performance improvement

### Performance Results

| Test Case | Pure Brute Force | With Memoization |
|-----------|------------------|------------------|
|           | Calls / Time(s)  | Calls / Time(s)  |
| 1.in | 1024 / 0.001144 | 56 / 0.000012 |
| 2.in | 1048576 / 0.111297 | 211 / 0.000027 |
| 3.in | - / - | 821 / 0.000071 |
| 4.in | - / - | 5051 / 0.000429 |

---

## Key Concepts

### Recursive Structure
Both problems follow the optimal substructure property:
- **Coin Change**: MinChange(n) = min(MinChange(n-c) + 1) for all valid coins c
- **Rod Cutting**: MaxRevenue(L) = max(price[i] + MaxRevenue(L-i)) for all cuts i

### Memoization Benefits
- **Eliminates redundant calculations**: Stores results of subproblems
- **Reduces time complexity**: From exponential to polynomial
- **Trade-off**: Uses O(n) extra space for cache

### Performance Comparison
Memoization shows:
- **10-1000x fewer recursive calls**
- **100-1000x faster execution time**
- Essential for larger input sizes (marked with `-` in brute force columns indicate timeout/impractical runtime)

---

## Test Cases

### Coin Change (`mincointestcases/`)
- `mincoin1.in`, `mincoin2.in`, `mincoin3.in`, `mincoin4.in`
- Various coin denominations and change amounts

### Rod Cutting (`cutrodtestcases/`)
- `1.in` to `4.in`: Different rod lengths and price tables
- `answers.txt`: Expected outputs

---

## Usage

### Run Coin Change
```bash
# Brute force
python3 ProblemA_v1.py < mincointestcases/mincoin1.in

# With memoization
python3 ProblemA_v2.py < mincointestcases/mincoin1.in
```

### Run Rod Cutting
```bash
# Brute force
python3 ProblemB_v1.py < cutrodtestcases/1.in

# With memoization
python3 ProblemB_v2.py < cutrodtestcases/1.in
```

---

## 👤 Author

[Kinosaur](https://github.com/Kinosaur)
