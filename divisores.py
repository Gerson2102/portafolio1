# Autor: Gerson Loaiza Vásquez
# Carné: 2020207712
# Objetivo: Función que imprime los divisores de un número de forma descendente
# E: Un número entero
# S: Los divisores impresos
# R: Solo ingresan números enteros menores a mil

def divisores (numero):
    if isinstance (numero, int):
        if (numero <= 999):
            return divisores_aux (numero, numero)
        else:
            return "Error, solo ingresan números menores a 1000"
    else:
        return "Error, los elementos de entrada son incorrectos, deben ser números enteros"


def divisores_aux (p_numero, p_divisor):
    if p_divisor == 1:
        print (p_divisor)
    else:
        if p_numero % p_divisor == 0:
            print (p_divisor)
            return divisores_aux (p_numero, p_divisor - 1)
        else:
            return divisores_aux (p_numero, p_divisor - 1)
