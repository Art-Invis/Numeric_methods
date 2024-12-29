### **Lab #2 Task**

**Topic:** Root-finding methods for nonlinear equations

---

### **Objective:**

The objective of this lab is to study the primary methods for refining the roots of nonlinear equations with one unknown, specifically the *False Position Method* (also known as the method of chords), and to implement it for finding the root of a given nonlinear equation.

---

### **False Position Method (Method of Chords):**

The *False Position Method* is an iterative method used to find the root of a nonlinear equation \( f(x) = 0 \). The method is applicable when the function \( f(x) \) is continuous on a given interval \([a, b]\), and the function values at the ends of the interval have opposite signs (i.e., \( f(a) \cdot f(b) < 0 \)).

The process of the False Position Method involves:

1. **Initial Conditions:**
   - A segment \([a, b]\) is provided where the root of the equation is expected to be located.
   - It is verified that the function at the ends of the interval has opposite signs, i.e., \( f(a) \cdot f(b) < 0 \), ensuring that a root exists within this interval.

2. **Chord Calculation:**
   - The method approximates the root by drawing a straight line (chord) connecting the points \((a, f(a))\) and \((b, f(b))\).
   - The root approximation is obtained by calculating the intersection of the chord with the x-axis using the following formula:
     \[
     x_{\text{new}} = x_{\text{prev}} - \frac{f(x_{\text{prev}}) \cdot (b - a)}{f(b) - f(a)}
     \]

3. **Updating the Interval:**
   - After each iteration, the method checks which side of the interval contains the root.
   - If \( f(x_{\text{new}}) \cdot f(a) > 0 \), the left boundary is updated: \( a = x_{\text{new}} \).
   - Otherwise, the right boundary is updated: \( b = x_{\text{new}} \).

4. **Stopping Criteria:**
   - The process continues until the desired accuracy \( \epsilon \) is reached. The iterations stop when the relative error between two successive approximations is less than the specified tolerance:
     \[
     \frac{|x_{\text{new}} - x_{\text{prev}}|}{|x_{\text{new}}|} < \epsilon
     \]
   - Alternatively, the method can stop when the function value at the new approximation is sufficiently close to zero:
     \[
     |f(x_{\text{new}})| < \epsilon
     \]

5. **Result:**
   - Once the stopping criteria are met, the new approximation \( x_{\text{new}} \) is considered the root of the equation.

---

### **Example:**

Find the root of the equation:
\[
f(x) = \cos(x) + \frac{1}{x + 2} = 0
\]
on the interval \( [0, 3] \) with an accuracy of \( \epsilon = 0.0001 \).

### **Solution:**

The equation can be written as:
\[
f(x) = \cos(x) + \frac{1}{x + 2}
\]

Apply the False Position Method to find the root of this function on the interval \( [0, 3] \).

---

### **Expected Outcome:**

After applying the method, the root will be found, and the function value at the root will be very close to zero, confirming the correctness of the method.

---

### **Conclusion:**

In this lab, the False Position Method (Method of Chords) was studied and applied to find the root of a nonlinear equation. By using this method, I was able to find the root of the equation \( f(x) = \cos(x) + \frac{1}{x + 2} = 0 \) on the given interval with a high degree of accuracy. This iterative method proves effective and accurate for solving nonlinear equations when appropriate initial conditions are given.
