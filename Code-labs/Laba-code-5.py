import numpy as np
import matplotlib.pyplot as plt

# Вхідні дані
U_max = 100  
f = 50  
R1 = 5 
R2 = 4  
R3 = 7  
R4 = 2  
L1 = 0.01  
L2 = 0.02  
C1 = 300e-6 
h = 0.00001  
t_end = 0.2  

i_L1 = 0  
i_L2 = 0  
V_C1 = 0  

# Часовий інтервал
t = np.arange(0, t_end, h)
U1 = U_max * np.sin(2 * np.pi * f * t)

i_L1_array = []
i_L2_array = []
V_C1_array = []
U2_array = []

for k in range(len(t)):
    di_L1_start = (U1[k] - R1 * i_L1 - V_C1) / L1
    di_L2_start = (V_C1 - R3 * i_L2) / L2
    dV_C1_start = ((i_L1 - i_L2) - V_C1 / R2) / C1

    i_L1_temp = i_L1 + di_L1_start * h
    i_L2_temp = i_L2 + di_L2_start * h
    V_C1_temp = V_C1 + dV_C1_start * h

    di_L1_end = (U1[k] - R1 * i_L1_temp - V_C1_temp) / L1
    di_L2_end = (V_C1_temp - R3 * i_L2_temp) / L2
    dV_C1_end = ((i_L1_temp - i_L2_temp) - V_C1_temp / R2) / C1

    i_L1 += h / 2 * (di_L1_start + di_L1_end)
    i_L2 += h / 2 * (di_L2_start + di_L2_end)
    V_C1 += h / 2 * (dV_C1_start + dV_C1_end)

    U2 = V_C1 * R4 / (R3 + R4)

    i_L1_array.append(i_L1)
    i_L2_array.append(i_L2)
    V_C1_array.append(V_C1)
    U2_array.append(U2)

# Графік
plt.plot(t, U2_array, label='Вихідна напруга U2')
plt.xlabel('Час (с)')
plt.ylabel('Напруга (В)')
plt.title('Перехідний процес вихідної напруги U2')
plt.legend()
plt.grid(True)
plt.show()
