# Autor: Gerson Loaiza Vásquez
# Carné: 2020207712
# Objetivo: Determinar si un número es par
# E: Un número
# S: True si es par, False si es impar
# R: Los números deben ser enteros positivos

def par (numero):
    if isinstance (numero, int) and (numero >= 0):
        return par_aux (numero)
    else:
        return "Error, el elemento de entrada debe ser un número entero positivo, intente de nuevo por favor"


def par_aux (p_numero):
    if p_numero % 2 == 0:
        return True
    else:
        return False
