# Objetivo: Función que divide 2 factores sin utilizar el operador de división entera
# E: Un divisor y dividendo
# S: El resultado de la división entre los factores
# R: Los números que ingresan solo pueden ser enteros

def divisionRecursivo (divisor, dividendo):
    if isinstance (dividendo, int) and isinstance (divisor, int):
        if dividendo == 0:
            return "Error por división entre cero"
        else:
            return divisionRecursivo_aux (dividendo, divisor)
    else:
        return "Error, elementos incorrectos, deben ser números enteros"


def divisionRecursivo_aux (p_divisor, p_dividendo):
    if p_dividendo == p_divisor:
        return 1
    elif p_divisor < p_dividendo:
        return 0
    else:
        return divisionRecursivo_aux (p_divisor - p_dividendo, p_dividendo) + 1
