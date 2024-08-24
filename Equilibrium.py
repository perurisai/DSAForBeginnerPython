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
