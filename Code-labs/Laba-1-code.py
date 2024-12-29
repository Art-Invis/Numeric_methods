import numpy as np

def simple_gauss_determinant(A):
    V = np.array(A, dtype=float)  
    n = V.shape[0]  
    det = 1  

    for k in range(n):
        if V[k][k] == 0:
            return 0  
 
        det *= V[k][k]  
        
        
        for j in range(k + 1, n):
            Cj = V[j][k] / V[k][k]  
            for i in range(k, n):
                V[j][i] -= V[k][i] * Cj
    
    return det

A = [
    [8.3, 2.72, 4.1, 1.9],
    [3.92, 8.45, 7.68, 2.46],
    [3.77, 7.31, 8.04, 2.28],
    [2.21, 3.55, 1.69, 6.69]
]

result = simple_gauss_determinant(A)
print(f"Визначник матриці: {result}")
