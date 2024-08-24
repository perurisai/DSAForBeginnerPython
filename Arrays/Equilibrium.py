"""
Explanation:
total_sum: Initially, the total sum of the array is calculated.
left_sum: This variable keeps track of the sum of elements on the left side of the current index.
We iterate through each element in the array.
For each element, we update total_sum to represent the sum of elements to the right of the current index.
We then compare left_sum with total_sum. If they are equal, the current index is an equilibrium index.
If no equilibrium index is found, the function returns -1.
Example:
For the array [1, 3, 5, 2, 2], the equilibrium index is 2, as the sum of elements on the left (1 + 3 = 4) is equal to the sum on the right (2 + 2 = 4).
"""
def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        total_sum -= num  # Right sum for index i

        if left_sum == total_sum:
            return i

        left_sum += num

    return -1  # If no equilibrium index is found


# Example usage:
arr = [1, 8, 5, 2, 2]
index = find_equilibrium_index(arr)
if index != -1:
    print(f"Equilibrium index found at: {index}")
else:
    print("No equilibrium index found.")
