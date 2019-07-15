#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:57:39 2019

@author: diegorivera
"""

'''
PROBLEMA:
Un problema común en física corresponde al cálculo de la trayectoria de un 
proyectil. En particular, cuando se dispara un proyectil desde una altura h 
sobre un plano horizontal con velocidad inicial v0 y ángulo θ (respecto a la 
horizontal). Para una mejor visualización del problema observe la figura 
(enunciado original):

El alcance, o distancia horizontal, entre el origen y el punto de impacto, R, 
está dado por la ecuación:

R = v0^2/g(sin(θ)+(sin^2(θ)+2z)^1/2)*cos(θ)
z = gh/v0^2

Escriba un programa en Python que:
a) Cree dos arreglos de 1 dimensión:
    i) Uno llamado velocidades_iniciales, con valores de velocidad entre 10 y 
       100 m/s, con paso i, donde i es entregado por el usuario. Ejemplo: 
       range(10,100,2), en este caso el paso es 2.
    ii) Otro llamado ángulos, con ángulos entre 20 y 70 grados, con paso j, 
        donde j es entregado por el usuario. Recuerde que debe pasarlo a 
        radianes (multiplicar por Pi y dividir por 180 cada valor)
        
b) Cree una matriz llamada distancias, que contenga un valor de R por cada par 
   de velocidad y ángulo (es decir, en la posición [0,0] debe tener el valor de 
   R para la velocidad [0] y el ángulo [0], en la [1,0] debe tener R para la 
   velocidad [0] y el ángulo [1], y así sucesivamente)
   
c) Muestre la mayor distancia alcanzada.

Asuma que h es 10 metros, y recuerde que g es 9.8 m/s^2

Un ejemplo de ejecución es el siguiente:

Ingresa el paso de las velocidades: 10 
Ingrese el paso de los ángulos: 5
La distancia máxima es 1331.2853548710866    

'''
# Importando paquete numpy con alias "np" para tener un mejor soporte de vectores 
# y matrices por medio de sus funciones matemáticas de manera computar de manera 
# más efectiva.
# Importando paquete math con alias "m" para computar de mejor forma variables y 
# operaciones matemáticas por medio de funciones específicas.
import numpy as np
import math as m

# Dejaré como input variable el ingreso de los steps para los arreglos de 
# velocidad inicial y angulos
step_velocidades = int(input("Ingresa el paso de las velocidades: "))
step_angulos = int(input("Ingresa el paso de las velocidades: "))

# a) Arreglos de 1 dimesión. Arreglo velocidades_iniciales, start = 10, 
# stop = 100 y un step arbitrario segun ingreso de usuario. Arreglo angulos con 
# start = 20, stop = 70 y se repite criterio de stepanterior. Para ambos ranges, 
# el stop tendrá + 1, para que sea considerado 100 y 70, respectivamente en sus 
# arreglos.
# a.i) velocidades_iniciales
velocidades_iniciales = np.array(range(10,100+1,step_velocidades))

# a.ii) angulos
angulos = np.array(range(20,70+1,step_angulos))

# llevando el valor de los angulos de grados a radianes.
angulos = angulos * m.pi/180

# b) Primero decidí realizar el producto cartesiano, entre los arreglos 
# anteriores y asi poder tener la relacion de cada velocidad inicial para cada 
# angulo definido
# (http://elclubdelautodidacta.es/wp/2013/05/python-el-producto-cartesiano/)

# producto cartesiano entre velocidades_iniciales y angulos
producto = [(v, a) for v in velocidades_iniciales for a in angulos]
    
# el resultado del producto es una lista que deberé pasar a una matriz o arreglo
# de lista 
v0_angulo = np.array(producto)

# Una vez obtenida la matriz v0_angulo, donde col(0) = velocidad_inicial 
# y col(1) = grados. Procederé a calcular R para cada fila (par de velocidad y 
# ángulo).
# R = v0^2/g(sin(θ)+(sin^2(θ)+2z)^1/2)*cos(θ)
# z = gh/v0^2

# Defino R como una matriz de ceros de "v0_angulo.shape[0]" filas (en este caso 
# 180 filas) para luego ingresar el resultado para cada par de velocidad y ángulo.
R = np.zeros([v0_angulo.shape[0],])
for i in range(0,v0_angulo.shape[0]):
    R[i] = ((v0_angulo[i,0]**2)/9.8)*(m.sin(v0_angulo[i,1])+m.sqrt(pow(m.sin(v0_angulo[i,1]),2)+(2*9.8*10/v0_angulo[i,0]**2)))*m.cos(v0_angulo[i,1])

# finalmente defino la matriz distancias como matriz de ceros con 
# "v0_angulo.shape[0]" filas (en este caso 180 filas) y 3 columnas donde 
# incorporaré los valores de velocidad inicial, angulos y R
# respectivamente
distancias = np.zeros([v0_angulo.shape[0],3])

# ciclo iterativo para poblar matriz distancias
for j in range(0,v0_angulo.shape[0]):
    distancias[j] = [v0_angulo[j,0], v0_angulo[j,1], R[j]]

# c) Mostrando la mayor distancia alcanzada, valor maximo para variable R.
mayor_distancia = distancias[:,2].max()

# para ver a qué valores de velocidad inicial y ángulo de elevación 
# corresponden la mayor distancia alcanzada, chequeare el index del valor 
# obtenido en mayor_distancia
# https://es.stackoverflow.com/questions/24577/obtener-las-posiciones-del-array-donde-encuentre-un-valor-con-numpy-where
index_mayor_distancia = np.where(distancias[:,2] == mayor_distancia)[0]

# mostrando resultados correspondiente a la mayor distancia alcanzada por el 
# proyectil:

# Para desplegar angulo en grdos:
ang_grados = distancias[index_mayor_distancia,1]*180/m.pi

print("La mayor distancia alcanzada en el lanzamiento del proyectil fue:",
      distancias[index_mayor_distancia,2],"metros.")
print("Con una velocidad inicial de:",distancias[index_mayor_distancia,0],
      "metros/segundos.")
print("Con un ángulo de elevación de:",distancias[index_mayor_distancia,1],
      "radianes. ->",ang_grados,"grados")
