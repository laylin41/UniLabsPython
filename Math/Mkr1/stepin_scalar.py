# Метод скалярних добутків \ Степеневий метод із скалярними добутками
from helpingFunctions import scalar_product
import numpy as np
from scipy import linalg

def stepin_scalar():
    # while true loop
    # break loop when alpha_next - alpha <= epsilon
    # have A parameter - matrix,
    # have max_iter parameter
    # break loop when max_iter
    # have epsilon parameter for checking
    # have x_0 vector. cant be 0 vector
    # x = x_0.copy()
    # in loop:
    # x_next = A @ x
    # alpha = scalar_product(x_next, x) / (x, x)
    # check for breaks. prints for when max_iter break. no print for when just epsilon
    # if not breaks x = x_next
    # after the loop. return x_next, alpha_next
    pass

def stepin():
    # while true loop
    # break loop when alpha_next - alpha <= epsilon
    # have A parameter - matrix,
    # have max_iter parameter
    # break loop when max_iter
    # have epsilon parameter for checking
    # have x_0 vector. cant be 0 vector
    # x = x_0.copy()
    # in loop:
    # x_next = A @ x
    # alpha = pow(x[0], i+1) / pow(x[0], i)
    # check for breaks. prints for when max_iter break. no print for when just epsilon
    # if not breaks x = x_next
    # after the loop. return x_next, alpha_next
    pass

"""
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
"""