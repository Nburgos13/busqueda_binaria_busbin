import random

import time

# Busqueda Binaria


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        # range(len(lista)) -> 0, 1, 2, 3, 4, ....., len(lista)-1
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 # Inicio de la lista
    if limite_superior is None:
        limite_superior = len(lista)-1 # Final de la lista
    if limite_superior < limite_inferior:
        return -1

    punto_medio = (limite_inferior + limite_superior) // 2

    # [1, 3, 5, 10, 12]
    #  0  1  2   3   4
    # punto_medio = (0 + 4) // 2 = 4 // 2 => 2 en la posicion 2 esta el 5

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio + 1, limite_superior)



if __name__=="__main__":
    # Crear una lista ordenada con 10000 numeros aleatorios.
    tamano = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamano:
        conjunto_inicial.add(random.randint(-3*tamano, 3 * tamano))

    lista_ordenada = sorted(list(conjunto_inicial))

    # Medir el tiempo de busqueda ingenua

    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")

    # Medir el tiempo de busqued binaria

    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos.")
