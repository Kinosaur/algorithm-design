"""
Memoized Recursive Approach for Weightlifting (Top-Down DP)
We added a 'notepad' to our naive approach so we don't repeat work!
"""

def get_shared_weights(exercises, start_idx, end_idx):
    """
    Helper function (Exactly the same as before).
    Finds how many weights are shared by all exercises in the range.
    """
    if start_idx > end_idx:
        return 0
    shared = list(exercises[start_idx])
    for i in range(start_idx + 1, end_idx + 1):
        for weight_type in range(len(shared)):
            shared[weight_type] = min(shared[weight_type], exercises[i][weight_type])
    return sum(shared)


def solve_memoized(exercises, start_idx, end_idx, notepad):
    """
    Our upgraded recursive function. It now carries a 'notepad' (a dictionary).
    """
    
    # --- UPGRADE 1: Check the notepad! ---
    # We use the tuple (start_idx, end_idx) as the "name" of the chunk.
    if (start_idx, end_idx) in notepad:
        # We already did this math! Just hand over the answer.
        return notepad[(start_idx, end_idx)]


    # BASE CASE (Same as before)
    if start_idx == end_idx:
        total_weights_needed = sum(exercises[start_idx])
        ans = 2 * total_weights_needed
        
        # --- UPGRADE 2: Write base case to notepad before returning ---
        notepad[(start_idx, end_idx)] = ans
        return ans

    
    # RECURSIVE STEP (Same logic as before)
    shared_count = get_shared_weights(exercises, start_idx, end_idx)
    savings = 2 * shared_count
    
    best_cost = float('inf')
    
    # Try all slices
    for k in range(start_idx, end_idx):
        
        # Pass the notepad down to the left and right halves!
        cost_left = solve_memoized(exercises, start_idx, k, notepad)
        cost_right = solve_memoized(exercises, k + 1, end_idx, notepad)
        
        total_cost = cost_left + cost_right - savings
        
        if total_cost < best_cost:
            best_cost = total_cost
            

    # --- UPGRADE 3: Write the final best cost to the notepad! ---
    notepad[(start_idx, end_idx)] = best_cost
    
    return best_cost


# --- Let's run it! ---
if __name__ == "__main__":
    # Test case from Sample 1
    test_exercises = [[1], [2], [1]]
    
    # Create an empty dictionary to act as our blank notepad
    my_notepad = {}
    
    # Call the solver, handing it the blank notepad
    result = solve_memoized(test_exercises, 0, 2, my_notepad)
    
    print(f"Minimum operations needed: {result}") 
    
    # If we want to peek at the robot's brain, we can print the notepad!
    print(f"Look at the notepad: {my_notepad}")