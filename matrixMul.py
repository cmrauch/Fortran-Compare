import numpy as np

rows = 10
columns = 10

A = np.array([[i+j for i in range(rows)] for j in range(columns)])
B = np.array([[i+j for i in range(rows)] for j in range(columns)])
C = np.array([[0 for i in range(rows)] for j in range(columns)])

for i in range(rows):
  for j in range(columns):
    for k in range(columns):
      C[i][j] += A[i][k] * B[k][j]
      
print("Matrix A:\n",A)
print("Matrix B:\n",B)
print("Matrix C:\n",C)
