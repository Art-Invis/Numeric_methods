import math

def integrand(x):
    return 1 / (x * math.log(x))

def left_rectangle_method(a, b, n):
    h = (b - a) / n  
    integral_sum = 0
    x = a
    for i in range(n):
        integral_sum += integrand(x)  
        x += h  
    return integral_sum * h  

def exact_integral_value(a, b):
    def F(x):
        return math.log(math.log(x))  
    
    return F(b) - F(a)

def calculate_integral():
    a = 2
    b = 4
    n = 100

    approx_value = left_rectangle_method(a, b, n)
    exact_value = exact_integral_value(a, b)
    difference = abs(approx_value - exact_value)

    print(f"Приблизне значення методом лівих прямокутників: {approx_value:.6f}")
    print(f"Точне значення за допомогою функції F(x): {exact_value:.6f}")
    print(f"Різниця між значеннями: {difference:.6f}")

calculate_integral()
