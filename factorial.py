# Objetivo: Función que calcula el factorial de un número
# E: Un número entero positivo
# S: El resultado del factorial del número ingresado
# R: Solo ingresan números enteros positivos

def factorial (numero):
    if isinstance (numero , int) and (numero >= 0):
        return factorial_aux (numero)
    else:
        return "Error, el elemento de entrada debe ser un número entero positivo, intente de nuevo"


def factorial_aux (p_numero):
    if p_numero == 1:
        return p_numero
    else:
        return factorial_aux (p_numero - 1) * p_numero