# Objetivo: Función que multiplica solo los números pares de un número
# E: Un número entero positivo
# S: Un resultado que será la multiplicación de solo números pares
# R: Solo ingresan números enteros positivos

def multiplicatoria (numero):
    if isinstance (numero, int) and (numero >= 0):
        return multiplicatoria_aux (numero)
    else:
        return "Error, el elemento de entrada debe ser un número entero positivo, intente de nuevo por favor"


def multiplicatoria_aux (p_numero):
    if p_numero == 1:
        return p_numero
    else:
        if p_numero % 2 == 0:
            return multiplicatoria_aux (p_numero - 1) * p_numero
        else:
            return multiplicatoria_aux (p_numero - 1)