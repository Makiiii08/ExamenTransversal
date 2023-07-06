## 10 X 10

import numpy as np
from Cliente import *
from Funciones import *

cliente = np.full((10,10),'---')

ciclo = True
llenar(arreglo)

def salir():
    print("Nicolas Miranda")
    return False

def agregarCliente(lista_cliente,num_asiento):
    p = Cliente()
    p.run = int(input("Ingrese Rut"))
    p.nombre = input("Ingrese Nombre")
    p.apellido = input("Ingrese Apellido")
    p.num_asiento = num_asiento
    if num_asiento>=1 and num_asiento<=20:
        p.valor =120000
    if num_asiento>=21 and num_asiento<=50:
        p.valor = 80000
    if num_asiento>=51 and num_asiento<=10:
        p.valor = 50000
    lista_cliente.append(p)
    print("Cliente Agregado")

def comprarAsiento(arreglo):
    try:
        ubicaciones=int(input("Ingrese Cantidad a comprar 1-3 "))
        if ubicaciones>=1 and ubicaciones<=3:
            compra=0
            while compra < ubicaciones:
                mostrar(arreglo)
                num_asiento=int(input("Numero de Zona"))
                if num_asiento>=1 and num_asiento<=100:
                    disponible = comprobar(arreglo,num_asiento)
                    if disponible == True:
                        agregarCliente(lista_cliente,num_asiento)
                        comprar(arreglo,num_asiento)
                        compra = compra + 1
                    else:
                        print("No esta Disponible")
                else:
                    print("Ubicaciones del 1 al 100")
        else:
            print("Cantidad de 1 a 3")
    except BaseException as error:
        print(f"Error : {error}")


def totales(lista_cliente):
    pla=0
    g=0
    s=0
    tot_pla=0
    tot_g=0
    tot_s=0
    for p in lista_cliente:
        if p.valor == 120000:
            pla +=1
            tot_pla+= 120000
        if p.valor == 80000:
            g +=1
            tot_g+= 80000
        if p.valor == 50000:
            s +=1
            tot_s += 50000
    print(f"Platino: Cantidad: {pla} total: {tot_pla}")
    print(f"Oro: Cantidad: {g} total: {tot_g}")
    print(f"Plata: Cantidad: {s} total: {tot_s}")


def listarClientes(lista_cliente):
    for p in lista_cliente:
        print(f"run: {p.run}")
        print(f"Nombre: {p.nombre}")
        print(f"Valor {p.valor}")
        print(f"Numero asiento: {p.num_asiento}")


while ciclo:

    print("Creativos.cl")
    print("1) Comprar entradas")
    print("2) Mostrar Ubicaciones Disponibles")
    print("3) Ver Listado de Asistentes")
    print("4) Mostrar ganancias Totales")
    print("5) Salir")
    try:
        op=int(input("Seleccione"))
        match op:
            case 1:
                print("comprar")
                comprarAsiento(arreglo)
            case 2:
                mostrar(arreglo)
            case 3:
                print("listado")
                listarClientes(lista_cliente)
            case 4:
                print("ganancias")
                totales(lista_cliente)
            case 5:
                ciclo = salir()

            case _:
                print("operacion incorrecta")
    except BaseException as error:
        print(f"Error: {error}")
