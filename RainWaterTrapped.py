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
