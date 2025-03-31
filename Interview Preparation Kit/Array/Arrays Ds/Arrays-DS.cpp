#include <vector>
#include <algorithm> // For std::swap

/*
    Time Complexity: O(n)
    Space Complexity: O(1)
*/
std::vector<int> reverseArray(std::vector<int> a) {
    int l = 0;                   // Left pointer at the start of the array
    int r = a.size() - 1;         // Right pointer at the end of the array

    // Swap elements from both ends towards the middle
    while (l < r) {               
        std::swap(a[l], a[r]);    // Swap left and right elements
        l++;                      // Move left pointer forward
        r--;                      // Move right pointer backward
    }

    return a; // Return the reversed array
}
