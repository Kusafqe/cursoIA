# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:47:21 2023

@author: Kusafqe

Escribir un programa que lea un entero positivo por
teclado e indique si el número es primo o no
"""

numero1 = int(input("Introduzca un numero positivo: "))

def esPrimo(numero):
    primo = False
    if numero <= 1:
        primo = False
    elif numero == 2:
        primo = True
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break
        else:
            primo = True
    return primo
            
            
if esPrimo(numero1):
    print("El número ", numero1, " es primo")
else:
    print("El número ", numero1, " no es primo")