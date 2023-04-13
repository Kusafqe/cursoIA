# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:22:58 2023

@author: Kusafqe
"""

# Ejercicio 3
for i in range(0, 1001, 2):

    if i == 0:
        a = None
    else:
        a = (((-1)**i)*(i**2 - 1))/(2*i)
        print('El término es :', a )
        
