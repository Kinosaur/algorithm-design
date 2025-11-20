x = [] # global list to store the combination

def comb(i):
    
    # // base case
    if i == n:
        for j in range(len(x)):
            print(x[j], end=' ')
        print()
        return None
    
    # // recursive case
    
    # option 0 (not selected)
    x[i] = 0
    comb(i + 1)
    
    # option 1 (selected)
    x[i] = 1
    comb(i + 1)

n = int(input("Enter the number of items: "))
if n == 0:
    print("No items to combine")
else:
    x = [0] * n  # Initialize global list with n elements
    comb(0)  # start recursion from index 0