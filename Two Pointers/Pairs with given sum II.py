"""The problem "Pairs with Given Sum II" involves finding pairs of elements in a sorted array that add up to a given target sum. The challenge is to efficiently find all such pairs, taking advantage of the fact that the array is sorted.

 Problem Statement:
- You are given a sorted array of integers `arr` and an integer `target`.
- Your task is to find all pairs `(i, j)` such that `arr[i] + arr[j] == target`, where `i < j`.

Approach:
Given that the array is sorted, a two-pointer approach is particularly efficient. You can use one pointer starting from the beginning of the array and another pointer starting from the end. Depending on the sum of the elements at these two pointers, you can adjust the pointers accordingly.

 Steps:
Initialize Two Pointers:
   - Set `left` to the start of the array (`0`) and `right` to the end of the array (`len(arr) - 1`).

Check Sum:
   - If `arr[left] + arr[right]` equals the target, you've found a pair.
   - If `arr[left] + arr[right]` is less than the target, increment `left` to increase the sum.
   - If `arr[left] + arr[right]` is greater than the target, decrement `right` to decrease the sum.

Continue Until the Pointers Cross:
   - Repeat the process until `left` is no longer less than `right`."""


# Python Implementation:


def find_pairs_with_given_sum(arr, target):
    left, right = 0, len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1

            # Skip duplicates (if required)
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs


# Example usage:
arr = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
target = 8
result = find_pairs_with_given_sum(arr, target)
print(f"Pairs with sum {target}: {result}")

"""
Explanation:
Two Pointers: 
  `left` starts at the beginning, and `right` starts at the end.
   Depending on the sum of `arr[left]` and `arr[right]`, the pointers are moved to either find a matching pair or adjust the search range.

Handling Duplicates:
 The code includes an optional step to skip duplicates to ensure that only unique pairs are added. This step can be omitted if the array doesn't contain duplicates or if you want to include duplicate pairs.

Example:
For the array `[1, 2, 3, 4, 4, 5, 6, 7, 8, 9]` and `target = 8`:
The pairs that sum up to `8` are `(1, 7)`, `(2, 6)`, `(3, 5)`, and `(4, 4)`.

 Complexity:
Time Complexity: O(n), where n is the number of elements in the array. Each element is considered at most once by either pointer.
Space Complexity: O(1) if we ignore the space needed to store the pairs. Otherwise, O(k) where Kis the number of pairs.

This approach is efficient and takes advantage of the sorted nature of the array to find all pairs with the given sum in linear time.
"""