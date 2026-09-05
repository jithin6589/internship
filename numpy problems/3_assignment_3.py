import numpy as np
A = np.array([
    [2, 4],
    [1, 3]
])
B = np.array([
    [5, 1],
    [2, 6]
])
element_wise = A * B
print("Element-wise multiplication:")
print(element_wise)
matrix_multiplication = A @ B
print("\nMatrix multiplication:")
print(matrix_multiplication)
x = np.array([2, 3, 4])
y = np.array([1, 0, 2])
print("\nx * y:")
print(x * y)
print("\nnp.dot(x, y):")
print(np.dot(x, y))