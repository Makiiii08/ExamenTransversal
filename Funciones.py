import numpy as np

from Cliente import *

arreglo = np.full((10,10),'---')

lista_cliente = []
def llenar(arreglo):
    x = 0
    for f in range(10):
        for c in range (10):
            x = x+1
            if len(str(x))<2:
                arreglo[f][c]= '0' + str(x)
            else:
                arreglo[f][c] = '0' + str(x)


def mostrar(arreglo):
    x = 0
    for f in range(10):
        fila =''
        for c in range(10):
            if c == 2:
                fila = fila + ' |'   + \
                       arreglo[f][c]
            else:
                fila = fila + ' | '  + \
                       arreglo[f][c]
        print(fila)



def comprar(arreglo,num_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x+1
            if str(x) == str(num_asiento):
                arreglo[f][c] = 'X'


def comprobar(arreglo,num_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x+1
            if str(x) == str(num_asiento):
                if arreglo[f][c] == 'X':
                    return False
    return True

