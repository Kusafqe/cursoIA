# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:28:30 2023

@author: Kusafqe
"""

# Ejercicio 4

def media(listaNumeros):
    for i in listaNumeros:
        sumaTotal = 0
        sumaTotal += i
    media = sumaTotal/len(listaNumeros)
    return media

listaNumeros = []
i = 0
while i < 10:
    entrada = int(input("Introduce un número positivo o 0 para salir: "))
    if entrada == 0:
        break
    if entrada > 0:
        listaNumeros.append(entrada)
        i += 1

if len(listaNumeros) == 0:
    print("No se han introducido números positivos.")
else:
    media = media(listaNumeros)
    print("La media de los números positivos introducidos es:", media)



    
    