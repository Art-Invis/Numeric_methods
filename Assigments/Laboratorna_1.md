## Lab Assignment #1: Direct and Iterative Methods for Solving Systems of Linear Equations

### Objective
Familiarize yourself with basic direct and iterative methods for solving systems of linear equations, as well as methods for calculating determinants and matrix rotations.

### Assignment
1. Solve a system of linear equations using the Gaussian elimination method to calculate the determinant of a matrix.
2. Implement an algorithm for calculating the determinant of a matrix by transforming it into upper triangular form and multiplying the elements along the main diagonal.
3. Compare the results with other methods for calculating determinants.
4. Develop a program to compute the determinant of a matrix using Gaussian elimination.

### Algorithm Description

The Gaussian elimination method for calculating the determinant of a matrix involves the following steps:
1. Perform elimination to transform the matrix into upper triangular form.
2. The determinant is the product of the diagonal elements.
3. If a zero element appears on the main diagonal during the elimination process, the determinant of the matrix is zero.

### Input Data
Matrix:
```
A = [
    [8.3, 2.72, 4.1, 1.9],
    [3.92, 8.45, 7.68, 2.46],
    [3.77, 7.31, 8.04, 2.28],
    [2.21, 3.55, 1.69, 6.69]
]
```

Variables:
- `s = 0.02k` (where `k` is the task number).
- `p = 21` (group number).

### Expected Outcome
Implement the calculation of the determinant of the matrix using the Gaussian elimination method and compute the determinant for the given matrix.
