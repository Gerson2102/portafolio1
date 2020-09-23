# Autor: Gerson Loaiza Vásquez
# Carné: 2020207712
# Objetivo: Función que desarrolla la sumatoria de un número dependiendo de un rango dado
# E: Un número de inicio, un número de parada y un rango
# S: La sumatoria de un número dependiendo de un rango dado por el usuario
# R: Solo ingresan números enteros

def sumatoriaRangos (numero_inicio, numero_parada, rango):
    if isinstance (numero_inicio, int) and isinstance (numero_parada, int) and isinstance (rango, int):
        return sumatoriaRangos_aux (numero_inicio, numero_parada, rango)
    else:
        return "Error, los elementos de entrada son incorrectos, deben ser números enteros"


def sumatoriaRangos_aux (p_numero_inicio, p_numero_parada, p_rango):
    if p_numero_inicio > p_numero_parada:
        return 0
    else:
        return sumatoriaRangos_aux (p_numero_inicio + p_rango, p_numero_parada, p_rango) + p_numero_inicio
