# Метод простої ітерації для системи нелінійних рівнянь
import numpy as np
from scipy import linalg
from helpingFunctions import *

def simple_iteration_2d(phi1, phi2, x0, y0, eps=0.2 , max_iter=150):
    A0 = jacobian_matrix_2d(phi1, phi2, x0, y0)
    if (check_convergence(A0)):
        x, y = x0, y0
        for i in range(max_iter):
            x_new, y_new = [phi1(x, y), phi2(x, y)]
            if linalg.norm([x_new - x, y_new - y], ord=np.inf) < eps:
                return x_new, y_new
            x, y = x_new, y_new
    else:
        print("Не збігається метод простих ітерацій")
        return None, None

def jacobian_matrix_2d(phi1, phi2, x, y):
    return np.array([
        [df_dx_2d(phi1, x, y), df_dy_2d(phi1, x, y)],
        [df_dx_2d(phi2, x, y), df_dy_2d(phi2, x, y)]
    ])

def check_convergence(jacob):
    convergence_check = linalg.norm(jacob, ord=1)

    if convergence_check < 1:
        return True
    else:
        return False

# ці функції записуються вже у вигляді x = ... ; y = ...
def phi1(x, y):
    return np.sin((x - y) / 2) / 2

def phi2(x, y):
    return np.cos((x + y) / 2) / 2

def example_simple_iteration():
    x0, y0 = 0, 0
    x, y = simple_iteration_2d(phi1, phi2, x0, y0, eps=0.2)
    print(x, y)
