from factorial import factorial

x = [] # global list to store the combination

def comb1(i):
    
    # // base case
    if i == n:
        for j in range(len(x)):
            print(x[j], end=' ')
        print()
        return 1
    
    # // recursive case
    
    # option 0 (not selected)
    x[i] = 0
    count1 = comb1(i + 1)
    
    # option 1 (selected)
    x[i] = 1
    count2 = comb1(i + 1)
    
    return count1 + count2

def comb2(i):
    
    # // base case
    if i == n:
        # Count how many 1's in the combination
        ones_count = sum(x)
        if ones_count == k:
            for j in range(len(x)):
                print(x[j], end=' ')
            print()
            return 1
        else:
            return 0
    
    # // recursive case
    
    # option 0 (not selected)
    x[i] = 0
    count1 = comb2(i + 1)
    
    # option 1 (selected)
    x[i] = 1
    count2 = comb2(i + 1)
    
    return count1 + count2

n = int(input("Enter the number of items: "))
if n == 0:
    print("No items to combine")
else:
    
    # Test comb1
    x = [0] * n  # Initialize global list with n elements
    total = comb1(0)
    print(f"Total combinations: {total} (2^{n} = {2**n})")
    
    # Test comb2
    k = int(input("Enter k (number of 1's): "))
    print(f"\nCombinations with exactly {k} ones:")
    total_k = comb2(0)
    
    # Calculate C(n,k)
    c_n_k = factorial(n) // (factorial(n - k) * factorial(k))
    print(f"Total: {total_k} (C({n},{k}) = {c_n_k})")