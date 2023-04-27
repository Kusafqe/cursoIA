# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:08:47 2023

@author: Kusafqe

Escriba una función que tenga como entrada dos números
mínimo y máximo, y pida al usuario introducir un valor en ese rango.
Deberá devolver el valor introducido (previa comprobación de que es
válido).
"""

def pedirNumeroEnRango(minimo, maximo):
    numero = int(input("Introduzca un número entre {} y {} ".format(minimo,maximo)))
    while numero < minimo or numero > maximo:
        numero = int(input("No está en el rango. Introduzca un número entre {} y {} ".format(minimo,maximo)))
    print("El numero introducido, que es correcto, es: ", numero)
    
pedirNumeroEnRango(3,7)
