"""
To solve this problem efficiently without using extra memory, you can use bitwise operations.
The idea is to count the bits at each position for all numbers in the array.
Since every number except one appears three times,
the sum of bits at each position will be a multiple of three, except for the bits of the number that appears once.
"""


def single_number(nums):
    ones, twos = 0, 0

    for num in nums:
        # Appears once
        ones = (ones ^ num) & ~twos

        # Appears twice
        twos = (twos ^ num) & ~ones

    return ones


# Example usage:
nums = [2, 2, 3, 2]
result = single_number(nums)
print(f"The single number is: {result}")
