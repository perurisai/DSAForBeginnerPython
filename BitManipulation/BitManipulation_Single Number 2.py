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

"""
Explanation:
ones and twos are used to store bits of the numbers that have appeared once and twice respectively.
For each number in the array, update ones and twos:
ones: XOR the current number with ones and then AND it with the negation of twos. This ensures that if the number appears the second time, it is removed from ones.
twos: XOR the current number with twos and then AND it with the negation of ones. This ensures that if the number appears the third time, it is removed from twos.
After processing all numbers, ones will hold the bits of the number that appears exactly once.
Example:
For the array [2, 2, 3, 2], the output will be 3, because 3 is the number that appears exactly once, while all other numbers appear three times.

Complexity:
Time Complexity: 
𝑂(𝑛)
O(n), where 
n is the number of elements in the array.
Space Complexity: 
𝑂(1)
O(1), since no extra space is used other than a few variables.
This solution efficiently finds the single number that does not appear three times using bitwise operations.
"""
