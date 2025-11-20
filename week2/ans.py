# Global list to store the combination
x = []

def comb(i):
    """
    Recursive function to generate all binary combinations.
    i: current index in the combination
    """
    # Base case: if we've assigned all positions, print the combination
    if i == len(x):
        print(' '.join(map(str, x)))
        return
    
    # Try option 0 (not selected)
    x[i] = 0
    comb(i + 1)
    
    # Try option 1 (selected)
    x[i] = 1
    comb(i + 1)

# Main program
n = int(input("Enter the number of items: "))
x = [0] * n  # Initialize global list with n elements
comb(0)  # Start recursion from index 0
