"""
The problem "Single Number III" involves finding two numbers in an array where every other number appears exactly twice. The two numbers that appear only once should be returned.

Approach:
To solve this problem efficiently, you can use bitwise operations. The basic idea is:

XOR all the numbers. The result will be the XOR of the two unique numbers because the XOR of any number with itself is 0.
Find a bit that is set (i.e., 1) in the XOR result. This bit will differ between the two unique numbers.
Divide the numbers into two groups based on whether they have that bit set or not. Each group will contain one of the unique numbers, and XOR-ing all numbers in each group will give the two unique numbers.
Here's the Python code to implement this approach:
"""


def single_number(nums):
    # Step 1: XOR all the numbers
    xor_result = 0
    for num in nums:
        xor_result ^= num

    # Step 2: Find a bit that is set in the xor_result
    # The bit will help us differentiate the two unique numbers
    diff_bit = xor_result & -xor_result  # This isolates the rightmost set bit

    # Step 3: Divide the numbers into two groups and find the unique numbers
    num1, num2 = 0, 0
    for num in nums:
        if num & diff_bit:
            num1 ^= num  # Group with the set bit
        else:
            num2 ^= num  # Group without the set bit

    return [num1, num2]


# Example usage:
nums = [1, 2, 1, 3, 2, 5]
result = single_number(nums)
print(f"The two unique numbers are: {result}")


# Output: The two unique numbers are: [3, 5]

# The time complexity of this solution is O(n), where n is the number of elements in the input array. The space complexity is O(1) since we are using a constant amount of extra space.

# This approach is efficient and does not require any extra memory. It leverages bitwise operations to find the two unique numbers in the array. By XOR-ing all the numbers and isolating a bit that is set in the XOR result, we can divide the numbers into two groups and find the unique numbers in linear time complexity.

