# **Lab 4: Numerical Integration Methods**  

## **Objective**  
The goal of this lab is to study the basic methods for computing definite integrals.  

---

## **Overview**  

### **Definite Integral Approximation**  
We compute the definite integral of a function \( f(x) \) over an interval \([a, b]\):  

```
Integral = ∫[a,b] f(x) dx
```

Since many functions do not have elementary antiderivatives or are given in tabular form, numerical methods such as the **rectangle method** are used.  

---

## **Task 5: Left Rectangle Method**  

### **Algorithm**  

1. **Initialize parameters:**  
   ```
   Integral = 0  
   h = (b - a) / n  
   x = a  
   ```
2. **Iterate over subintervals:**  
   ```
   for i = 0 to n - 1:
       Integral = Integral + f(x)  
       x = x + h  
   ```
3. **Multiply by step size:**  
   ```
   Integral = Integral * h
   ```

---


## **Expected Results**  
- Approximate integral value.  
- Comparison with the Newton-Leibniz formula for verification.  

---

## **References**  
1. Numerical Integration Methods.  
2. Newton-Leibniz Theorem.  

---
