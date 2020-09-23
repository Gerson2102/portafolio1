# Objetivo: Función que calculará el producto de 2 números
# E: Factor A y Factor B
# S: El resultado del producto de los números ingresados por el usuario
# R: Solo ingresan números enteros

def multiplicarRecursivo (numero_1, numero_2):
    if isinstance (numero_1, int) and isinstance (numero_2, int):
        return multiplicarRecursivo_aux (numero_1, numero_2, 0)
    else:
        return "Error, los elementos de entrada deben ser números enteros"


def multiplicarRecursivo_aux (p_numero_1, p_numero_2, p_contador):
    if p_contador == p_numero_2:
        return 0
    else:
        return multiplicarRecursivo_aux (p_numero_1, p_numero_2, p_contador + 1) + p_numero_1