def f1(x1, x2):
    return (x1 / (x1 ** 2 + x2 ** 2)) + 0.4 - x1

def f2(x1, x2):
    return -(x2 / (x1 ** 2 + x2 ** 2)) - 1.4 - x2

def system_of_equations(x):
    x1, x2 = x
    return [f1(x1, x2), f2(x1, x2)]

def compute_jacobian(x, h=1e-5):
    n = len(x)
    jacobian_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            x_temp = x[:]
            x_temp[j] += h
            jacobian_matrix[i][j] = (system_of_equations(x_temp)[i] - system_of_equations(x)[i]) / h
            
    return jacobian_matrix

def gaussian_elimination(A, B):
    n = len(B)

    for i in range(n):
        max_value = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_value][i]):
                max_value = k

        A[i], A[max_value] = A[max_value], A[i]
        B[i], B[max_value] = B[max_value], B[i]

    
        pivot = A[i][i]
        for j in range(i, n):
            A[i][j] /= pivot
        B[i] /= pivot

    return eliminate_below_diagonal(n, A, B)


def eliminate_below_diagonal(n, A, B):
    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]

    return A, B

def back_substitution(A, B):
    n = len(B)
    A, B = gaussian_elimination(A, B)
    solution = [0] * n

    for i in range(n - 1, -1, -1):
        solution[i] = B[i]
        for j in range(i + 1, n):
            solution[i] -= A[i][j] * solution[j]

    return solution


def newton_method(x0, epsilon=1e-6, max_iter=100):
    x = x0[:]

    for _ in range(max_iter):
        Fx = system_of_equations(x)
        jacobian_matrix = compute_jacobian(x)
        delta_x = back_substitution(jacobian_matrix, [-fx for fx in Fx])

        x = [x[i] + delta_x[i] for i in range(len(x))]

        
        if all(abs(dx) < epsilon for dx in delta_x):
            return [round(val, 5) for val in x]

    return x

initial_guess = [0.5, 0.5]

solution = newton_method(initial_guess)

x1, x2 = solution
print(f"Розв'язок: {solution}")
print(f"Перевірка підстановкою значень: f1 = {round(f1(x1, x2), 5)}, f2 = {round(f2(x1, x2), 5)}")
