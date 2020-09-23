# Objetivo: Función que busca si un número tiene ceros
# E: Un número entero
# S: True si tiene ceros, False de lo contrario
# R: Solo números enteros

def tieneCeros (numero):
    if isinstance (numero, int):
        return tieneCeros_aux (numero)
    elif numero == 0:
        return True
    else:
        return "Error, el elemento de entrada debe ser un número entero, intente de nuevo por favor"


def tieneCeros_aux (p_numero):
    if p_numero == 0:
        return False
    else:
        if (p_numero % 10) != 0:
            return tieneCeros_aux (p_numero // 10)
        else:
            return True