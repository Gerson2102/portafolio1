# Objetivo: Función que determina la sumatoria desde un inicio hasta un fin
# E: Un número de inicio y un número de parada
# S: La sumatoria del número hasta donde el usuario quiso
# R: Solo ingresan números enteros positivos

def sumatoria (numero_inicio, numero_parada):
    if isinstance (numero_inicio, int) and (numero_inicio >= 0) and isinstance (numero_parada, int) and (numero_parada >= 0):
       return sumatoria_aux (numero_inicio, numero_parada)
    else:
        return "Error, los lementos de netrada son incorrectos, intente de nuevo"


def sumatoria_aux (p_numero_inicio, p_numero_parada):
    if p_numero_inicio >= p_numero_parada:
        return 0
    else:
        if p_numero_inicio != p_numero_parada:
            return sumatoria_aux (p_numero_inicio + 1, p_numero_parada) + p_numero_inicio
