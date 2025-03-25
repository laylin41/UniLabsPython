# Степеневий метод 
from helpingFunctions import is_symmetric_positive
import numpy as np
from scipy import linalg

def stepin(A, x0, eps=1e-5, max_iter=150):
    if (np.all(x0 == 0)):
        print("Неправильний початковий вектор")
        return None, None
    else:
        x = x0.copy()
        alpha = 0
        for i in range(max_iter):
            x_next = A @ x
            #alpha_next = x_next[0] / x[0] if x[0] != 0 else 0
            alpha_next = linalg.norm(x_next, ord=np.inf) / linalg.norm(x, ord=np.inf)  # Краще наближення власного значення
            x_next = x_next / linalg.norm(x_next, ord = 2)  # Нормалізація

            if abs(alpha_next - alpha) <= eps:
                return x_next, alpha_next
            
            alpha = alpha_next
            x = x_next
        
        print("Досягнуто максимальну кількість ітерацій")
        return x_next, alpha_next

def stepin_min(A):
    n,n = A.shape
    if (is_symmetric_positive(A)):
      #print("Метод через ||A||_∞:")

      norm_A = np.linalg.norm(A, np.inf)
      B = norm_A * np.eye(n) - A

      #print("B:")
      e_vec_B, e_val_B = stepin()
      e_val_A_min = norm_A - e_val_B

      #print(f"Мінімальне власне значення: {e_val_A_min}")
      return e_vec_B, abs(e_val_A_min)
    else:
        print("Умова A = A.T > 0 не виконана")
        return None, None