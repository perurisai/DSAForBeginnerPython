"""
The problem "Rotated Sorted Array Search" requires finding the index of a target value in a rotated sorted array. A rotated sorted array is an array that was originally sorted in ascending order but then rotated at some pivot. The goal is to perform this search in
O(logn) time complexity, which suggests using a modified binary search.
Approach:
To search for the target in a rotated sorted array using binary search, follow these steps:
Identify the Middle Element: Use binary search to determine the middle element.
Check if the Target is at the Middle: If the middle element is the target, return its index.
Determine the Sorted Half:
If the left half is sorted, check if the target lies within this range.
If the target is in the sorted left half, continue searching in this half. Otherwise, search in the other half.
If the right half is sorted, check if the target lies within this range.
If the target is in the sorted right half, continue searching in this half. Otherwise, search in the other half.
Repeat: Continue narrowing down the search range until the target is found or the range is exhausted.
"""


def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # If the target is found, return its index
        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:  # Target is in the sorted left half
                right = mid - 1
            else:  # Target is in the unsorted right half
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:  # Target is in the sorted right half
                left = mid + 1
            else:  # Target is in the unsorted left half
                right = mid - 1

    # If the target is not found
    return -1


# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search_rotated_array(nums, target)
print(f"Index of the target {target}: {result}")

"""
Explanation:
Initial Setup: The left and right pointers start at the beginning and end of the array, respectively.
Binary Search Loop: The loop continues as long as left <= right.
Midpoint Calculation: Calculate the middle index mid to check if the target is found at nums[mid].
Check Which Half is Sorted:
Left Half Sorted: If nums[left] <= nums[mid], the left half is sorted.
Right Half Sorted: Otherwise, the right half is sorted.
Narrowing the Search: Depending on whether the target is in the sorted half, adjust left or right to narrow down the search range.
Termination: If the target is found, its index is returned; otherwise, -1 is returned.
Example:
For the array [4, 5, 6, 7, 0, 1, 2] and target 0:

The function will identify that the right half is sorted and that the target lies within the range of the sorted half, leading it to narrow down and eventually find the target at index 4.
Complexity:
Time Complexity: 
O(logn) due to the binary search.
Space Complexity: 
O(1) as no additional space is required.
This approach efficiently finds the target in a rotated sorted array by leveraging the properties of binary search on a partially sorted array.
"""

