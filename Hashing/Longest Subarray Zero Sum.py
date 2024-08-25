"""The problem "Longest Subarray with Zero Sum" asks us to find the length of the longest contiguous subarray within a given array where the sum of the elements is zero.

 Approach:
To solve this problem efficiently, we can use a hashing technique to track the cumulative sum at each index of the array. The key idea is based on the observation that if two indices have the same cumulative sum, the elements between these indices must sum to zero.

 Steps:
1. Cumulative Sum: As we iterate through the array, we maintain a cumulative sum of the elements.
2. Hash Map: We use a hash map (or dictionary) to store the first occurrence of each cumulative sum.
    If the cumulative sum has been seen before, it means the subarray between the previous index (where this sum was seen) and the current index has a sum of zero.
    If the cumulative sum is zero, then the subarray from the start of the array to the current index has a sum of zero.
3. Calculate the Length: Each time we find a subarray with zero sum, we calculate its length and update the maximum length found so far."""


# Python Implementation:


def longest_zero_sum_subarray(arr):
    # Dictionary to store the first occurrence of cumulative sum
    sum_map = {}

    max_length = 0
    cumulative_sum = 0

    for i, num in enumerate(arr):
        cumulative_sum += num

        if cumulative_sum == 0:
            max_length = i + 1  # Subarray from start to current index has zero sum

        if cumulative_sum in sum_map:
            # If cumulative sum was seen before, there's a zero-sum subarray
            max_length = max(max_length, i - sum_map[cumulative_sum])
        else:
            # Store the first occurrence of this cumulative sum
            sum_map[cumulative_sum] = i

    return max_length



#Example usage:
arr = [1, 2, -2, 4, -4, 1, -1, 3, -3]
result = longest_zero_sum_subarray(arr)
print(f"Length of the longest subarray with zero sum: {result}")
'''
Explanation:
Cumulative Sum: We calculate the cumulative sum as we iterate through the array.
Hash Map:
   The hash map `sum_map` stores the first occurrence of each cumulative sum.
   If the cumulative sum repeats, it indicates that the subarray between the previous index and the current index has a sum of zero.
Update Maximum Length: Each time a zero-sum subarray is found, the length is compared to the current maximum length, and the maximum is updated.

Example:
For the array `[1, 2, -2, 4, -4, 1, -1, 3, -3]`:
The longest subarray with zero sum is `[2, -2, 4, -4]`, `[1, -1, 3, -3]`, etc., each with a length of `4`.

 Complexity:
Time Complexity: O(n), where n is the number of elements in the array.
Space Complexity:O(n), because we store the cumulative sums and their indices in a hash map.

This approach efficiently finds the length of the longest subarray with a zero sum using hashing, allowing for a linear-time solution.
'''