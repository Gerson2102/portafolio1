# Objetivo: Determinar si todos los dígitos de un número ingresado son pares
# E: Un número
# S: True si todos los dígitos son pares, de lo contrario, False
# R: Los números deben ser enteros positivos

def sonPares (numero):
    if isinstance (numero, int) and (numero >= 0):
        return sonPares_aux (numero)
    else:
        return "Error, el elemento de entrada debe ser un número entero positivo, intente de nuevo por favor"


def sonPares_aux (p_numero):
    if p_numero == 0:
        return True
    else:
        if (p_numero % 10) % 2 == 0:
            return sonPares_aux (p_numero // 10)
        else:
            return False