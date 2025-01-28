# Lab 3: Newton's Method and ε-Algorithm  

## **Objective**  
The goal of this lab is to solve nonlinear systems of equations using:  
1. Newton's method with a finite-difference Jacobian matrix.  
2. ε-algorithm for improving convergence.  

---

## **Overview**  

### **Nonlinear Systems of Equations**  
We solve systems of `n` nonlinear equations:  

```
F(X):  
f1(x1, x2, ..., xn) = 0  
f2(x1, x2, ..., xn) = 0  
...  
fn(x1, x2, ..., xn) = 0  
```  

Newton's method requires calculating the Jacobian matrix `J(X)` and solving linear systems iteratively to find the solution `X = [x1, x2, ..., xn]`.  

---

## **Tasks**  

### **Task 5:**  
- Implement Newton's method with a finite-difference Jacobian matrix.  
- Use Gaussian elimination with pivoting for solving the linear system.  
- Apply relative error tolerance `ε = 10^-5`.  

---

## **Implementation Steps**  

1. **Initialize values:**  
   - Set the initial approximation `X0`.  
   - Define convergence tolerance `ε`.  

2. **Jacobian Matrix Calculation:**  
   The Jacobian matrix is approximated using finite differences:  

   ```
   Jij(X) ≈ [fi(X + h * ej) - fi(X)] / h
   ```  

   Here:  
   - `h` is a small step.  
   - `ej` is the unit vector in the `j-th` direction.  

3. **Solve the Linear System:**  
   At each iteration, solve:  
   ```
   J(X^(k)) * ΔX^(k) = -F(X^(k))
   ```  

4. **Update Approximation:**  
   Update the solution:  
   ```
   X^(k+1) = X^(k) + ΔX^(k)
   ```  

5. **Check Convergence:**  
   Stop if:  
   ```
   ||F(X)|| < ε
   ```  

---

## **Requirements**  
- **Programming Language:** Python  
- **Libraries:**  
  - NumPy for matrix operations.  

---

## **Expected Results**  
- Approximation of the solution `X = [x1, x2, ..., xn]`.  
- Convergence details and error values.  

---

## **References**  
1. Newton-Raphson Method.  
2. Numerical Methods for Nonlinear Systems.  
