# Autor: Gerson Loaiza Vásquez
# Carné: 2020207712
# Objetivo: Función que cuenta los ceros de un número
# E: Un número entero
# S: Un número que indica el número de ceros del dígito ingresado
# R: Números enteros únicamente

def contarCeros (numero):
    if isinstance (numero, int):
        if numero == 0:
            return True
        elif numero < 0:
            numero *= -1
            return contarCeros_aux (numero)
        else:
            return contarCeros_aux (numero)
    else:
        return "Error, los elementos de entrada son incorrectos"


def contarCeros_aux (p_numero):
    if p_numero == 0:
        return 0
    else:
        if p_numero % 10 == 0:
            return contarCeros_aux (p_numero // 10) + 1
        else:
            return contarCeros_aux (p_numero // 10)
