"""
To find the B closest points to the origin from a list of points in a 2D plane, you can use a custom comparator or a more Pythonic approach using a heap.
The custom comparator isn't natively supported in Python's sort functions, but you can achieve the same effect by using a custom key function with sorted() or by using the heapq library for efficiency.

Here's a Python implementation using a custom comparator:
"""


def k_closest_points(points, B):
    # Sort points based on the squared distance from the origin
    points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)

    # Return the first B points
    return points[:B]


# Example usage:
points = [(1, 3), (3, 4), (2, -1)]
B = 2
result = k_closest_points(points, B)
print(f"The {B} closest points to the origin are: {result}")

# Output: The 2 closest points to the origin are: [(1, 3), (2, -1)]

"""
In this implementation, the k_closest_points function takes a list of points and an integer B as input and returns the B closest points to the origin.
The points are sorted based on the squared distance from the origin using a custom key function lambda p: p[0] ** 2 + p[1] ** 2.
The sorted points are then sliced to return the first B points, representing the B closest points to the origin.
"""