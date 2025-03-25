# Метод скалярних добутків \ Степеневий метод із скалярними добутками
from helpingFunctions import scalar_product
import numpy as np
from scipy import linalg

def stepin_scalar(A, x0, eps=1e-5, max_iter=150):
    if (np.all(x0 == 0)):
        print("Неправильний початковий вектор")
        return None, None
    else:
        x = x0.copy()
        alpha = 0
        for i in range(max_iter):
            x_next = A @ x
            alpha_next = scalar_product(x_next, x) / scalar_product(x, x)
            x_next = x_next / linalg.norm(x_next, ord = 2)
            
            if abs(alpha_next - alpha) <= eps:
                return x_next, alpha_next
            
            alpha = alpha_next
            x = x_next
    
        print("Досягнуто максимальну кількість ітерацій")
        return x_next, alpha_next
    