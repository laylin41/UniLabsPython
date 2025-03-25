import numpy as np
from scipy import linalg

# максимальне власне значення та вектор до нього
def power_iteration(A, max_it):
    n, n = A.shape
    e_vec = np.random.rand(n)
    for i in range(max_it):
        e_vec_new = A @ e_vec
        e_vec = e_vec_new / linalg.norm(e_vec_new)
        #e_val = linalg.norm(A @ e_vec)
        #print(f"{i}: {e_vec}, {e_val}")

    e_val = linalg.norm(A @ e_vec)
    #print (e_vec, e_val)
    return e_vec, e_val

# мінімальне власне значення та вектор до нього
def power_iteration_min(A, max_it):
    n,n = A.shape
    if (is_symmetric_positive(A)):
      #print("Метод через ||A||_∞:")

      norm_A = np.linalg.norm(A, np.inf)
      B = norm_A * np.eye(n) - A

      #print("B:")
      e_vec_B, e_val_B = power_iteration(B, max_it)
      e_val_A_min = norm_A - e_val_B

      #print(f"Мінімальне власне значення: {e_val_A_min}")
      return e_vec_B, abs(e_val_A_min)
    else:
        print("Умова A = A.T > 0 не виконана")
        return None, None

# умова для знаходження мінімального власного значення
def is_symmetric_positive(A):
    # Перевірка симетричності
    if not np.allclose(A, A.T):
        return False

    # Перевірка позитивної визначеності (всі головні мінори > 0)
    for i in range(1, A.shape[0] + 1):
        if np.linalg.det(A[:i, :i]) <= 0:
            return False

    return True