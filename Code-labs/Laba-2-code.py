import math

def f(x):
    return math.cos(x) + 1 / (x + 2)

def chord_method(a, b, epsilon):
    x_prev = a  

    while True:
        f_a = f(a)
        f_b = f(b)

        x_next = x_prev - (f(x_prev) * (b - a)) / (f_b - f_a)
        
        if f(x_next) * f_a > 0:
            a = x_next
        else:
            b = x_next

        if (abs(x_next - x_prev) / abs(x_next)) < epsilon:
                    break
        
        x_prev = x_next

    return x_next

a = 0
b = 3
epsilon = 0.0001

root = chord_method(a, b, epsilon)
rounded_value = round(f(root), 6)  

print(f"Корінь рівняння: {root}")
print(f"Значення функції в корені: {f(root)} ~ {rounded_value}")
