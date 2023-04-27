# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:43:39 2023

@author: Kusafqe
"""

numero1 = int(input("Introduzca el primer número: "))
numero2 = int(input("Introduzca el segundo número: "))

if numero1 % numero2 == 0:
    print("El número ", numero2, "divide a ", numero1)
    
elif numero2 % numero1 == 0:
    print("El número ", numero1, "divide a ", numero2)
else:
    print("Ninguno es divisible por el otro")
    