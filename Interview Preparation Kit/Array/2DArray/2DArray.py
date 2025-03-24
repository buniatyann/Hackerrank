"""
    Time Complexity: O(1)
    Space Complexity: O(1)
"""
def hourglass_sum(arr: list[list[int]]) -> int:
    # Initialize the maximum sum to a very low value
    max_sum = -float('inf')

    # Loop through the 2D list to find the top-left corner of each hourglass
    for i in range(4):  # Rows 0 to 3 (hourglass starts at these rows)
        for j in range(4):  # Columns 0 to 3 (hourglass starts at these columns)

            # Calculate the sum of the top part of the hourglass
            top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            # Calculate the middle part of the hourglass
            middle = arr[i + 1][j + 1]
            # Calculate the sum of the bottom part of the hourglass
            bottom = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

            # Compute the total hourglass sum
            hourglass = top + middle + bottom

            # Update max_sum if the current hourglass sum is greater
            max_sum = max(max_sum, hourglass)

    return max_sum
