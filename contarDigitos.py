# Objetivo: Función que cuenta los dígitos de un número
# E: Un número
# S: Un número con la cantidad de dígitos del número ingresado
# R: None

def contarDigitos (num):
    if num < 10:
        return 1
    else:
        return contarDigitos (num // 10) + 1