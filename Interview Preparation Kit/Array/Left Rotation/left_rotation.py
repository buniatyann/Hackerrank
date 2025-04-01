from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n) 
def rotLeft(a: List[int], d: int) -> List[int]:
    if not a:  # Handle empty list
        return a
        
    d %= len(a)  # Adjust d for values larger than n
    return a[d:] + a[:d]  # Rotate left by slicing