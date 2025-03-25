# Використання усіх методів які будуть на мкр. Умови - ті що у файлі з прикладом МКР.
import numpy as np
import iteration
import newton
import newton_mod
import stepin
import stepin_scalar
import yakobi
from scipy import linalg

def main():
    # Всі приклади із теоретичних матеріалів до мкр

    print("=" * 50)

    # Метод простої ітерації 
    def iter_phi1(x, y): # не умова, потрібно руками перетворити
        return np.sin((x - y) / 2) / 2
    def iter_phi2(x, y): # не умова, потрібно руками перетворити
        return np.cos((x + y) / 2) / 2 
    x0, y0 = 0, 0 # умова
    print("Метод простих ітерацій: ")
    x, y = iteration.simple_iteration_2d(iter_phi1, iter_phi2, x0, y0, eps=0.2)
    try:
        np.testing.assert_almost_equal([x, y], [-0.12, 0.48], decimal=2)
        print(f"Розв'язок: x = {x}, y = {y}")
    except AssertionError:
        print("Implementation is NOT correct")

    print("=" * 50)

    # метод ньютона 
    def newton_f_1(x, y):
        return x - 0.5 * np.sin((x - y) / 2)
    def newton_f_2(x, y):
        return y - 0.5 * np.cos((x + y) / 2)
    x0, y0 = 0, 0
    print("Метод Ньютона: ")
    x, y = newton.newton_2d(newton_f_1, newton_f_2, x0, y0, error_tolerance=0.2)
    try:
        np.testing.assert_almost_equal([x, y], [-0.16, 0.49], decimal=2)
        print(f"Розв'язок: x = {x}, y = {y}")
    except AssertionError:
        print("Implementation is NOT correct")

    print("=" * 50)

    # модифікований метод ньютона
    def newton_mod_f_1(x, y):
        return x - 0.5 * np.sin((x - y) / 2)
    def newton_mod_f_2(x, y):
        return y - 0.5 * np.cos((x + y) / 2)
    x0, y0 = 0, 0
    print("Модифікований метод Ньютона: ")
    x, y = newton_mod.newton_mod_2d(newton_mod_f_1, newton_mod_f_2, x0, y0, error_tolerance=0.2)
    try:
        np.testing.assert_almost_equal([x, y], [-0.17, 0.49], decimal=2)
        print(f"Розв'язок: x = {x}, y = {y}")
    except AssertionError:
        print("Implementation is NOT correct")

    print("=" * 50)

    # скалярний метод 
    A = np.array([[5.0, 1, 2], [1, 4, 1], [2, 1, 3]])
    x0 = np.array([1,1,1])
    e_vec, e_val = stepin_scalar.stepin_scalar(A, x0)
    try:
        np.testing.assert_almost_equal(np.float64(e_val), np.max(np.abs(linalg.eigvals(A))), decimal=5)
        print("Скалярний метод:")
        print("Вектор: ", e_vec)
        print("Значення: ", e_val)
    except AssertionError:
        print("Implementation is NOT correct")
   
    print("=" * 50)

    # степеневий метод
    
    A = np.array([[5.0, 1, 2], [1, 4, 1], [2, 1, 3]])
    x0 = np.array([1,1,1])
    e_vec, e_val = stepin.stepin(A, x0)
    try:
        np.testing.assert_almost_equal(np.float64(e_val), np.max(np.abs(linalg.eigvals(A))), decimal=5)
        print("Скалярний метод:")
        print("Вектор: ", e_vec)
        print("Значення: ", e_val)
    except AssertionError:
        print("Implementation is NOT correct")

    print("=" * 50)

    # метод якобі 

if __name__ == "__main__":
    main()