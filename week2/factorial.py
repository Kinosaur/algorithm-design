import sys
sys.setrecursionlimit(10000) # set recursion-stack depth

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)