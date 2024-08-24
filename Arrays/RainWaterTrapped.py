def trap_rain_water(heights):
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    trapped_water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            trapped_water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            trapped_water += right_max - heights[right]

    return trapped_water


# Example usage:
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = trap_rain_water(heights)
print(f"Total trapped rain water: {result}")

"""
Explanation:
left_max and right_max store the maximum heights encountered from the left and right sides, respectively.
left and right pointers start from the two ends of the array and move towards each other.
Depending on which side's maximum height is lower, the corresponding pointer moves inward. The water trapped above each building is calculated by subtracting the building's height from the current maximum height of that side.
The process continues until the pointers meet.
Example:
For the array [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], the algorithm calculates the trapped water as follows:

From left to right: The left pointer moves, updating left_max and accumulating trapped water.
From right to left: The right pointer moves, updating right_max and accumulating trapped water.
Finally, the total trapped rainwater will be 6.
"""
