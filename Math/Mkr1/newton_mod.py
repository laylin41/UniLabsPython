# Модифікований метод Ньютона для розв'язання систем нелінійних рівнянь

from Math.Mkr1.helpingFunctions import *
import numpy as np
from scipy import linalg

def newton_mod_2d(f_0, f_1, x_0, y_0, error_tolerance=1.0e-15, max_iterations=500):
    J = np.zeros((2, 2))

    J[0][0] = df_dx_2d(f_0, x_0, y_0)
    J[0][1] = df_dy_2d(f_0, x_0, y_0)
    J[1][0] = df_dx_2d(f_1, x_0, y_0)
    J[1][1] = df_dy_2d(f_1, x_0, y_0)

    J_invert = linalg.inv(J)

    k = 0

    while k < max_iterations:
        x = x_0 - (J_invert[0, 0] * f_0(x_0, y_0) + J_invert[0, 1] * f_1(x_0, y_0))
        y = y_0 - (J_invert[1, 0] * f_0(x_0, y_0) + J_invert[1, 1] * f_1(x_0, y_0))

        k = k + 1

        if np.max([np.abs(f_0(x, y)), np.abs(f_1(x, y))]) < error_tolerance:
            print("root found within tolerance", error_tolerance, "using", k, "iterations")
            return [x, y]

        x_0 = x
        y_0 = y

        #print ([x,y])

    raise RuntimeError("no root found within tolerance", error_tolerance, "using", max_iterations, "iterations")

def newton_mod_3d(f_0, f_1, f_2, x_0, y_0, z_0, error_tolerance=1.0e-15, max_iterations=500):
    J = np.zeros((3, 3))

    J[0][0] = df_dx_3d(f_0, x_0, y_0, z_0)
    J[0][1] = df_dy_3d(f_0, x_0, y_0, z_0)
    J[0][2] = df_dz_3d(f_0, x_0, y_0, z_0)

    J[1][0] = df_dx_3d(f_1, x_0, y_0, z_0)
    J[1][1] = df_dy_3d(f_1, x_0, y_0, z_0)
    J[1][2] = df_dz_3d(f_1, x_0, y_0, z_0)

    J[2][0] = df_dx_3d(f_2, x_0, y_0, z_0)
    J[2][1] = df_dy_3d(f_2, x_0, y_0, z_0)
    J[2][2] = df_dz_3d(f_2, x_0, y_0, z_0)

    J_invert = linalg.inv(J)

    k = 0

    while k < max_iterations:
        x = x_0 - (J_invert[0, 0] * f_0(x_0, y_0, z_0) + J_invert[0, 1] * f_1(x_0, y_0, z_0) + J_invert[0, 2] * f_2(x_0, y_0, z_0))
        y = y_0 - (J_invert[1, 0] * f_0(x_0, y_0, z_0) + J_invert[1, 1] * f_1(x_0, y_0, z_0) + J_invert[1, 2] * f_2(x_0, y_0, z_0))
        z = z_0 - (J_invert[2, 0] * f_0(x_0, y_0, z_0) + J_invert[2, 1] * f_1(x_0, y_0, z_0) + J_invert[2, 2] * f_2(x_0, y_0, z_0))

        k = k + 1

        if np.max([np.abs(f_0(x, y, z)), np.abs(f_1(x, y, z)), np.abs(f_2(x, y, z))]) < error_tolerance:
            print("root found within tolerance", error_tolerance, "using", k, "iterations")
            return [x, y, z]

        x_0 = x
        y_0 = y
        z_0 = z

        #print ([x, y, z])

    raise RuntimeError("no root found within tolerance", error_tolerance, "using", max_iterations, "iterations")

