# Kaung Khant Lin
# 6540131
# 542

# Problem link: https://www.spoj.com/problems/INVCNT/cstart=90

def merge_and_count(arr, temp, left, mid, right):
    # Merge two halves and count inversions
    i = left        # pointer for left half
    j = mid + 1     # pointer for right half
    k = left        # pointer for temp array
    count = 0
    
    # Merge while counting inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            # arr[i] > arr[j], so this is an inversion
            # all remaining elements in left half are also greater than arr[j]
            temp[k] = arr[j]
            count += (mid - i + 1)
            j += 1
        k += 1
    
    # Copy remaining elements from left half
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    # Copy remaining elements from right half
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    # Copy sorted elements back to original array
    for i in range(left, right + 1):
        arr[i] = temp[i]
    
    return count

def merge_sort_count(arr, temp, left, right):
    # Divide and conquer: count inversions using merge sort
    count = 0
    if left < right:
        mid = (left + right) // 2
        
        # Count inversions in left half
        count += merge_sort_count(arr, temp, left, mid)
        
        # Count inversions in right half
        count += merge_sort_count(arr, temp, mid + 1, right)
        
        # Count inversions while merging
        count += merge_and_count(arr, temp, left, mid, right)
    
    return count

def count_inversions(arr):
    n = len(arr)
    temp = [0] * n  # temporary array for merging
    return merge_sort_count(arr, temp, 0, n - 1)

t = int(input())  # number of test cases
for _ in range(t):
    input()  # blank line
    n = int(input())  # array size
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    
    print(count_inversions(arr))