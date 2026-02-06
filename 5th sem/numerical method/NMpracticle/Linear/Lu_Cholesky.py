import numpy as np

# Symmetric positive definite matrix
A = np.array([
    [3, 2, 1],
    [2, 3, 2],
    [1, 2, 3]
], dtype=float)
B = np.array([10, 14, 14], dtype=float)

# Cholesky decomposition
L = np.linalg.cholesky(A)

# Round L for nice viewing
L_rounded = np.round(L, 3)
print("L  =\n", L_rounded)

# Solve Ly = B (forward substitution)
y = np.linalg.solve(L, B)

# Solve L^T x = y (back substitution)
x = np.linalg.solve(L.T, y)

# Round solution
x_rounded = np.round(x, 3)
print("\nSolution :")
print("x =", x_rounded[0])
print("y =", x_rounded[1])
print("z =", x_rounded[2])
