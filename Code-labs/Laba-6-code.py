import numpy as np
import matplotlib.pyplot as plt

R1 = 30  
R2 = 20  
R3 = 333  
R4 = 77  
C1 = 13e-3  
L_max = 17  
L_min = 1.7  
L2 = 23  
i_min = 1  
i_max = 2  
a = 0.001  

T = 6 * a
dt = T / 5000  
num_steps = int(T / dt)  

def input_voltage(t):
    period = T
    t_mod = t % period
    if t_mod < a:
        return 10 * (t_mod / a)
    elif t_mod < 2 * a:
        return 10
    elif t_mod < 3 * a:
        return 10 * (1 - ((t_mod - 2 * a) / a))
    elif t_mod < 4 * a:
        return 10 * (1 - ((t_mod - 2 * a) / a))
    elif t_mod < 5 * a:
        return -10
    else:
        return -10 + 10 * ((t_mod - 5 * a) / a)

def calculate_L_coefficients():
    A = np.array([
        [1, i_min, i_min ** 2, i_min ** 3],
        [1, i_max, i_max ** 2, i_max ** 3],
        [0, 1, 2 * i_min, 3 * i_min ** 2],
        [0, 1, 2 * i_max, 3 * i_max ** 2]
    ])
    b = np.array([L_max, L_min, 0, 0])
    return np.linalg.solve(A, b)

def L(i):
    i_abs = abs(i)
    if i_abs <= i_min:
        return L_max
    elif i_abs >= i_max:
        return L_min
    else:
        a0, a1, a2, a3 = L_coeffs
        return a0 + a1 * i_abs + a2 * i_abs ** 2 + a3 * i_abs ** 3

def derivatives(t, y):
    u_C1, i_L1, i_L2 = y  
    u1 = input_voltage(t)

    i1 = (u1 - u_C1) / R1
    i3 = u_C1 / R3

    du_C1_dt = (i1 - i3 - i_L1) / C1  
    di_L1_dt = (u_C1 - R2 * i_L1) / L(i_L1)  
    di_L2_dt = (u_C1 - R4 * i_L2) / L2

    return np.array([du_C1_dt, di_L1_dt, di_L2_dt])

def runge_kutta_4th_knuth(y, x, h):
    K1 = h * derivatives(x, y)
    K2 = h * derivatives(x + 0.5 * h, y + 0.5 * K1)
    sqrt_2 = np.sqrt(2)
    K3 = h * derivatives(x + 0.5 * h, y - (0.5 - 1/sqrt_2) * K1 + (1 - 1/sqrt_2) * K2)
    K4 = h * derivatives(x + h, y - (1/sqrt_2) * K2 + (1 + 1/sqrt_2) * K3)
    y_next = y + (K1 + (2 - sqrt_2) * K2 + (2 + sqrt_2) * K3 + K4) / 6
    return y_next

L_coeffs = calculate_L_coefficients()

y = np.zeros(3)  

time = np.linspace(0, T, num_steps)
results = np.zeros((num_steps, 3))  
u1_values = np.zeros(num_steps)

for i in range(num_steps):
    t = time[i]
    results[i] = y
    u1_values[i] = input_voltage(t)
    y = runge_kutta_4th_knuth(y, t, dt)

plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(time * 1000, u1_values, 'b-', label='u1(t)')
plt.grid(True)
plt.legend()
plt.ylabel('Напруга (В)')
plt.title('Результати моделювання')

plt.subplot(3, 1, 2)
plt.plot(time * 1000, results[:, 0], 'g-', label='u_C1(t)')
plt.grid(True)
plt.legend()
plt.ylabel('Напруга (В)')

plt.subplot(3, 1, 3)
plt.plot(time * 1000, results[:, 1], 'k-', label='i_L1(t)')
plt.plot(time * 1000, results[:, 2], 'r-', label='i_L2(t)')
plt.grid(True)
plt.legend()
plt.xlabel('Час (мс)')
plt.ylabel('Струм (А)')

plt.tight_layout()
plt.show()

i_range = np.linspace(0, 2.5, 1000)
L_values = [L(i) for i in i_range]

plt.figure(figsize=(10, 6))
plt.plot(i_range, L_values)
plt.grid(True)
plt.title('Залежність L(i)')
plt.xlabel('Струм i (А)')
plt.ylabel('Індуктивність L (Гн)')
plt.axvline(x=i_min, color='r', linestyle='--', label=f'i_min = {i_min} A')
plt.axvline(x=i_max, color='g', linestyle='--', label=f'i_max = {i_max} A')
plt.axhline(y=L_max, color='b', linestyle='--', label=f'L_max = {L_max} H')
plt.axhline(y=L_min, color='y', linestyle='--', label=f'L_min = {L_min} H')
plt.legend()
plt.show()
