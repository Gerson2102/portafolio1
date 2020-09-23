# Autor: Gerson Loaiza Vásquez
# Carné: 2020207712
# Objetivo: Determinar si un número es impar
# E: Un número
# S: True si es impar, False si es par
# R: Los números deben ser enteros positivos

def impar (numero):
    if isinstance (numero, int) and (numero >= 0):
        return impar_aux (numero)
    else:
        return "Error, el elemento de entrada debe ser un número entero positivo, intente de nuevo por favor"


def impar_aux (p_numero):
    if p_numero % 2 != 0:
        return True
    else:
        return False
