# Autor: Gerson Loaiza Vásquez
# Carné: 2020207712
# Objetivo: Función que retorna un número que indica la cantidad de veces que se repite un dígito dentro del otro
# E: Un número entero positivo
# S: El número con la cantidad de veces que se repite el dígito
# R: Solo ingresan números enteros positivos

def numeroRepetido (numero, digito):
    if isinstance (numero, int) and (numero >= 0) and isinstance (digito, int) and (digito >= 0):
        return numeroRepetido_aux (numero, digito)
    else:
        return "Error, los elementos de entrada deben ser números enteros positivos, intente de nuevo"


def numeroRepetido_aux (p_numero, p_digito):
    if p_numero < 10 and p_numero != p_digito:
        return 0
    else:
        if (p_numero % 10) == p_digito:
            return numeroRepetido_aux (p_numero // 10, p_digito) + 1
        else:
            return numeroRepetido_aux (p_numero // 10, p_digito)