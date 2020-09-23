# Objetivo: Función que calcula la potencia de otro número sin utilizar el operador de potencia
# E: Un número entero
# S: El número ingresado elevado
# R: Solo ingresan números enteros positivos

def potencia (numero, exponente):
    if isinstance (numero, int) and (numero >= 0) and isinstance (exponente, int) and (exponente >= 0):
        return potencia_aux (numero, exponente, 1)
    else:
        return "Error, los lementos de entrada son incorrectos, deben ser números enteros positivos"

    
def potencia_aux (p_numero, p_potencia, p_aumento):
    if p_aumento == p_potencia:
        return p_numero
    else:
        return potencia_aux (p_numero, p_potencia, p_aumento + 1) * p_numero