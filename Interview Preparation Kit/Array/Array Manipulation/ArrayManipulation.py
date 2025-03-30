# Time Complexity: O(m + n)
# Space Complexity: O(n)
# Where m is the number of queries, and n is the number of elements
def array_manipulation(n, queries):
    # Initialize a difference array with zeros
    temp = [0] * (n + 1)

    # Apply the difference array technique
    for first_i, last_i, to_add in queries:
        temp[first_i - 1] += to_add  # Convert to 0-based index
        if last_i < n:  # Prevent out-of-bounds
            temp[last_i] -= to_add  

    # Compute the maximum value using prefix sum
    max_value = 0
    current_sum = 0
    for value in temp[:-1]:  # Ignore the extra element
        current_sum += value
        max_value = max(max_value, current_sum)

    return max_value