import numpy as np

# 1D arr
arr = np.array([1, 2, 3, 4, 5])
# print(arr[0])  # Imprime 1
# print(arr[3])  # Imprime 4

# arr multi dim
arr = np.array([[1, 2, 3, 12], [4, 5, 6, 23], [0, 5, 6, 12], [23, 2, 6, 13]])


# print(arr[0:-1, 1:3])
# print(arr[[0, -1],])

# Inhomogeneous list of lists
arr2 = [
    [1, 2, 3, 12],
    [4, 5, 6, 23],
    [0, 5, 6, 12],
    [23, 2, 6, 13],
    ["a", "b", "c"],  # Inhomogeneous element (different length)
]

# no np to obtain only 1st and last item
print([arr2[0], arr2[-1]])

print([arr2[i] for i in [0, -1]])

print(list(filter(lambda x: arr2.index(x) in [0, len(arr2)-1], arr2)))