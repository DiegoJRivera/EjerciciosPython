#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:45:18 2019

@author: diegorivera
"""
'''
PROBLEMA:
El profesor de cálculo le ha pedido aproximar el volumen generado por la 
diferencia entre un cubo de lado L=10 y un cono de radio r=3 de altura h = L 
(es decir, la misma altura que el cubo).

El profesor les explica que dividiendo el problema en infinitos cálculos de 
áreas de una lámina, puede calcular el volumen de la figura sumando las áreas 
de las láminas. Para ayudarlos, el profesor les hace ver que a medida que 
“subimos” en la altura del cono (variable h), el radio r de la circunferencia 
decrece en función de esta altura h, según presenta la figura que sigue:
    
r = 3 * (10 - h)/ 10

Hacer esto manualmente sería muy complicado, por lo que les pide desarrollar un 
programa en Python de forma que podamos variar la altura (variable h) con un 
valor muy pequeño, calcular el valor del radio r para cada altura h, hacer al 
cálculo del área y finalmente sumar.

Para ello debe cumplir los siguientes requerimientos:
a) Escribir una función que reciba la altura h como parámetro y retorne el 
   radio r.
b) Escribir una función que calcule el área de una lámina según el parámetro 
   radio r.
c) Escribir un programa que incremente la altura h para estimar el volumen del 
   cubo. Utilice las dos funciones anteriores para dicho cálculo. Muestre el 
   resultado del volumen final por pantalla. Nota: considere que el valor de h 
   aumenta en 0.001.
   
Recuerde que el área del círculo se calcula como pi * r^2, donde r es el radio, 
y el área del cuadrado está dada por l^2, donde l es la longitud del lado.
'''
# Importando paquete math con alias "m" para computar de mejor forma variables y 
# operaciones matemáticas por medio de funciones específicas.
# Importando paquete numpy con alias "np" para tener un mejor soporte de vectores 
# y matrices por medio de sus funciones matemáticas de manera computar de manera 
# más efectiva.
import math as m
import numpy as np

# a) función que recibe la altura h (cono) como parámetro y retorna el radio r.
def radio_funcion_h(h):
    r = (3*(10-h))/10
    return r

# b) función que calcula el área de una lámina según el parámetro radio r.
def area_lamina(r):
    a_lamina = 10**2 - (m.pi*r**2)
    return a_lamina

# c) incremento de altura (h) en 0.001 unidades asignadas al arreglo rango.
rango = np.arange(0,10,0.001)

# inicializando variable al que será asignado el valor de la suma total de las
# areas laminares
sum_areas_laminares = 0

# ciclo para calcular las 10000 iteraciones correspondiente a los respectivos 
# radios, areas laminares de cada lámina de cubo con incremento en 0.001
for h in rango:
    # asignando valor del radio el retorno de la función radio_funcion_h, donde 
    # el parámetro de entrada es la altura asignada en el arreglo rango, que es 
    # la altura h, con incremento en 0.001.
    radio = radio_funcion_h(h)
    
    # asignando valor de area_laminar el retorno de la función area_lamina, donde 
    # el parámetro de entrada es el valor del radio definido anteriormente, 
    # correspondiente a la altura h, con incremento en 0.001.
    area_laminar = area_lamina(radio)
    
    # sumatoria de las areas laminares. (unidades cuadradas)
    sum_areas_laminares = sum_areas_laminares + area_laminar
    
# Ya teniendo el resultado del total de las sumas de las areas laminares, que 
# que contempla la diferencia entre el cubo y el cono, es necesario multiplicarlo 
# por la altura de cada lámina (0.001) para obtener el volumen estimado del cubo.
volumen_cubo = sum_areas_laminares * 0.001

# Mostrando resultado final redondeado a 4 decimales.
print("El volumen estimado del cubo es:",round(volumen_cubo,4),"unidades cúbicas")
