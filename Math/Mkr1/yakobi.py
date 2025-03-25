# Метод Якобі
import numpy as np

def jacobi_rotation(A, epsilon=1e-10, max_iterations = 1000):        
    def max_off_diagonal(A):
        max_val = -np.inf
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > max_val:
                    max_val = abs(A[i, j])
                    p, q = i, j
        print(f"p: {p+1}, q: {q+1}, max_val: {max_val}")
        return p, q, max_val
    
    def rotation_matrix(A, p, q):
        if A[p, q] == 0:
            return np.eye(n)
        phi = 0.5 * np.arctan2(2 * A[p, q], A[p, p] - A[q, q])
        print(f"phi: {phi}")
        cos_phi = np.cos(phi)
        sin_phi = np.sin(phi)
        U_k = np.eye(n)
        U_k[p, p] = cos_phi
        U_k[q, q] = cos_phi
        U_k[p, q] = -sin_phi
        U_k[q, p] = sin_phi
        print(f"U_k: {U_k}")
        return U_k
    
    n = A.shape[0]
    U = np.eye(n)
    A_k = A.copy()

    for iteration in range(max_iterations):
        print(f"iteration: {iteration}")
        p, q, max_val = max_off_diagonal(A_k)
        if max_val < epsilon:
            break
        U_k = rotation_matrix(A_k, p, q)
        A_k = U_k.T @ A_k @ U_k
        U = U @ U_k
    else:
        print("Досягнуто максимальну кількість ітерацій ", max_iterations)

    eigenvalues = np.diag(A_k)
    eigenvectors = U
    return eigenvalues, eigenvectors