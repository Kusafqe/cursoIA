# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:06:07 2023

@author: Kusafqe

Escribir una función que tenga como entrada por
parámetro un entero positivo y devuelva con return si es primo o no
"""

def esPrimo(numero):
    primo = "No es primo"
    if numero <= 1:
        primo = "No es primo"
    elif numero == 2:
        primo = "Es primo"
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = "No es primo"
                break
        else:
            primo = "Es primo"
    return primo 


print("El numero 3 ", esPrimo(3))
print("El numero 4 ", esPrimo(4))
print("El numero 22 ", esPrimo(22))
print("El numero 27 ", esPrimo(27))