import numpy as np
 
 
def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
 
    matriz = np.array(lista).reshape(3, 3)
 
    funciones = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }
 
    resultado = {}
    for nombre, f in funciones.items():
        resultado[nombre] = [
            f(matriz, axis=0).tolist(),  # axis1: por columnas
            f(matriz, axis=1).tolist(),  # axis2: por filas
            f(matriz).item(),            # flattened: toda la matriz
        ]
 
    return resultado