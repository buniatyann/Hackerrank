# Time Complexity: O(n)
# Space Complexty: O(1)
def reverse_array(arr):
    l, r = 0, len(arr) - 1  # Initialize left and right pointers
    
    # Swap elements from both ends towards the middle
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]  # Swap elements
        l += 1  # Move left pointer forward
        r -= 1  # Move right pointer backward
    
    return arr  # Return the reversed array
