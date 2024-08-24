"""
Merge Sort is a classic sorting algorithm that follows the divide-and-conquer paradigm. It divides the input array into two halves, recursively sorts them, and then merges the two sorted halves.

Key Steps in Merge Sort:
Divide: Split the array into two halves.
Conquer: Recursively sort both halves.
Combine: Merge the two sorted halves to produce the sorted array.
Here’s the Python implementation of Merge Sort:
"""


def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2

        # Divide the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Initialize pointers for left_half, right_half, and the main array
        i = j = k = 0

        # Merge the left and right halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements are left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any elements are left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(f"Sorted array: {arr}")

# Output: Sorted array: [3, 9, 10, 27, 38, 43, 82]

# The merge_sort function takes an array arr as input and sorts it in ascending order using the Merge Sort algorithm.
# The function first checks if the length of the array is greater than 1 to proceed with the sorting process.
# It then divides the array into two halves, left_half and right_half, and recursively sorts them.
# After sorting the two halves, the function merges them by comparing elements and updating the main array arr.
# The example usage demonstrates sorting an array using the merge_sort function and prints the sorted array.
# Merge Sort has a time complexity of O(n log n) and is a stable sorting algorithm. It is widely used for sorting large datasets efficiently.
#   1. Merge Sort is a stable sorting algorithm, meaning that the relative order of equal elements is preserved in the sorted output.