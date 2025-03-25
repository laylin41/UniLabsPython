def df_dx_3d(f, x, y,z, h=1.0e-7):
    return (f(x + h, y, z) - f(x, y, z)) / h
def df_dy_3d(f, x, y,z, h=1.0e-7):
    return (f(x, y + h, z) - f(x, y, z)) / h
def df_dz_3d(f,x,y,z,h=1.0e-7):
    return (f(x, y, z + h) - f(x, y, z)) / h

def df_dx_2d(f, x, y, h=1.0e-7):
    return (f(x + h, y) - f(x, y)) / h
def df_dy_2d(f, x, y, h=1.0e-7):
    return (f(x, y + h) - f(x, y)) / h

