import numpy as np

# Coefficients of the equations
A = np.array([[3, 4], [2, -1]])

# Constants on the right-hand side
B = np.array([10, 3])

# Solve the system of equations
solution = np.linalg.solve(A, B)
print(solution)  # This will give the values for x and y
