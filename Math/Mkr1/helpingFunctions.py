# Обчислення похідних не використовуючи бібліотечні методи
# Скалярний добуток двох векторів

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

def scalar_product(a, b):
    """
    a: перший вектор
    b: другий вектор
    return: скалярний добуток a і b
    """
    if len(a) != len(b):
        print("Скалярний добуток: Вектори повинні мати однакову довжину.")
        return None
    
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]  # множимо відповідні елементи і додаємо їх до результату
    return result

