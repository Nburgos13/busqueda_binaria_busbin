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