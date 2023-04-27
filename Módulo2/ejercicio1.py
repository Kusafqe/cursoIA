# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:34:14 2023

@author: Kusafqe
"""

numero1 = int(input("Introduzca el primer número: "))
numero2 = int(input("Introduzca el segundo número: "))
numero3 = int(input("Introduzca el tercer número: "))

maximo = numero1
if numero2 > maximo:
    maximo = numero2
if numero3 > maximo:
    maximo = numero3

minimo = numero1
if numero2 < minimo:
    minimo = numero2
if numero3 < minimo:
    minimo = numero3


print("El máximo es: ", maximo)
print("El mínimo es: ", minimo)