"""
Naive Recursive Approach for Weightlifting (Google Code Jam)
This code tries EVERY possible way to split the exercises.
"""

def get_shared_weights(exercises, start_idx, end_idx):
    """
    Helper function to find out how many weights are shared by 
    ALL exercises in the range from start_idx to end_idx.
    """
    if start_idx > end_idx:
        return 0
        
    # Start by assuming the first exercise's weights are the shared ones
    shared = list(exercises[start_idx])
    
    # Check every other exercise in the range
    for i in range(start_idx + 1, end_idx + 1):
        for weight_type in range(len(shared)):
            # The shared amount is the minimum required by anyone in the group
            shared[weight_type] = min(shared[weight_type], exercises[i][weight_type])
            
    # Return the total number of shared plates
    return sum(shared)


def solve_naive(exercises, start_idx, end_idx):
    """
    The main recursive function. It finds the minimum operations
    needed for the chunk of exercises between start_idx and end_idx.
    """
    
    # BASE CASE: We have shrunk the chunk down to just 1 exercise!
    if start_idx == end_idx:
        total_weights_needed = sum(exercises[start_idx])
        # We must push them all on, and pop them all off.
        return 2 * total_weights_needed

    
    # RECURSIVE STEP: We have multiple exercises. Let's try splitting them!
    
    # 1. Figure out how many weights this entire chunk shares.
    shared_count = get_shared_weights(exercises, start_idx, end_idx)
    savings = 2 * shared_count
    
    # 2. Keep track of the best (minimum) cost we find.
    # We start it at infinity so any real number will beat it.
    best_cost = float('inf')
    
    # 3. Try slicing the chunk into two halves at every possible split point (k).
    for k in range(start_idx, end_idx):
        
        # Calculate cost of Left half (from start to k)
        cost_left = solve_naive(exercises, start_idx, k)
        
        # Calculate cost of Right half (from k+1 to end)
        cost_right = solve_naive(exercises, k + 1, end_idx)
        
        # The total cost for this specific way of splitting
        total_cost = cost_left + cost_right - savings
        
        # Is this the best way we've found so far?
        if total_cost < best_cost:
            best_cost = total_cost
            
    return best_cost


# --- Let's run Case 3 (Sample 1) to prove it works! ---
if __name__ == "__main__":
    # 3 exercises, 1 type of weight.
    # Ex 0: [1] (One plate)
    # Ex 1: [2] (Two plates)
    # Ex 2: [1] (One plate)
    test_exercises = [[1], [2], [1]]
    
    # Call the naive solver for the whole list (index 0 to 2)
    result = solve_naive(test_exercises, 0, 2)
    
    print(f"Minimum operations needed: {result}") 
    # This will print 4!