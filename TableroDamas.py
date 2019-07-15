#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:39:52 2019

@author: diegorivera
"""
'''
PROBLEMA:
Según Wikipedia, las damas es un juego de mesa para dos contrincantes que 
consiste en mover las piezas en diagonal a través de los cuadros negros o 
blancos de un tablero de 64 cuadros con la intención de capturar las piezas del
jugador contrario pasando por encima de dichas piezas.

a) El primer paso consiste en crear el tablero. Utilizando una matriz (arreglo 
bidimensional) en numpy como base, cree un programa que dibuje el tablero 
inicial colocando:
- Un 0 si la casilla es blanca y está desocupada
- Un 1 si es negra y está desocupada y
- Un 2 donde hay fichas rojas, que son básicamente todas las casillas negras en
  las 3 primeras filas
- Un 3 donde hay fichas blancas, que son básicamente todas las casillas negras 
  en las 3 últimas filas
Nota: No debe utilizar asignaciones individuales a cada elemento de la matriz

Un compañero ha creado el siguiente trozo de código para comprobar si se puede
mover una ficha roja un casillero en diagonal. Una ficha se puede mover un 
casillero en diagonal si solo si el casillero se encuentra vacío.
_______________________________________________________________________________
pos_x = int(input("Ingrese la fila de la ficha roja (de 0 a 7): "))
pos_y = int(input("Ingrese la columna de la ficha roja (de 0 a 7): "))
if tablero_damas[pos_x, pos_y] == 2:
    if tablero_damas[pos_x+1, pos_y+1] != 2 or tablero_damas[pos_x-1, pos_y+1] != 2:
        print("Puedes mover la ficha")
    else:
        print("No puedes mover la ficha")
else:
    print("No hay ficha en esa posición")
_______________________________________________________________________________

b) Modifique el código de forma que ahora esté dentro de una función que RECIBA 
el tablero, la fila y la columna, realice la verificación de la misma forma 
actual, y luego retorne TRUE si es que el movimiento es válido y FALSE en caso 
contrario.

c) A pesar de que un usuario se comporte en forma correcta, es decir, el 
usuario ingresa índices entre 0 y 7, el código anterior no funciona para algunos 
casos. Describa al menos 2 casos.
'''
# a) Display de tablero, de acuerdo a enunciado:
# https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.r_.html
# https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.ma.row_stack.html
# Importando paquete numpy con alias "np" para tener un mejor soporte de vectores 
# y matrices por medio de sus funciones matemáticas de manera computar de manera 
# más efectiva.
import numpy as np

def armar_tablero (ancho):
    fila_r_par = np.r_[ancho * [0,2]] # para crear fila par fichas rojas
    fila_r_impar = np.r_[ancho * [2,0]] # para crear fila impar fichas rojas
    fila_par = np.r_[ancho * [0,1]] # para crear fila par vacias
    fila_impar = np.r_[ancho * [1,0]] # para crear fila impar vacias
    fila_b_impar = np.r_[ancho * [3,0]] # para crear fila impar fichas blancas
    fila_b_par = np.r_[ancho * [0,3]] # para crear fila par fichas blancas
    # retorno concatencion de filas creadas en la secuencia descrita.
    return np.row_stack((fila_r_par,fila_r_impar,fila_r_par, fila_impar, fila_par,
                         fila_b_impar,fila_b_par,fila_b_impar))
    
tablero_damas = armar_tablero(4)
print(tablero_damas)

# b) se dejará en un ciclo continuo la ejecución del programa para poder realizar 
# varias pruebas seguidas para contestar las siguientes preguntas.
ejecucion = "s"

while (ejecucion != "n"):
    pos_x = int(input("Ingrese la fila de la ficha roja (de 0 a 7): "))
    pos_y = int(input("Ingrese la columna de la ficha roja (de 0 a 7): "))
    respuesta = ""

    def mover_ficha_roja(tablero_damas,pos_x,pos_y):
        if tablero_damas[pos_x, pos_y] == 2:
            if tablero_damas[pos_x+1, pos_y+1] != 2 or tablero_damas[pos_x-1, pos_y+1] != 2:
                respuesta = "\nTRUE, Puedes mover la ficha"
            else:
                respuesta = "\nFALSE, No puedes mover la ficha"
        else:
            respuesta = "\nFALSE, No hay ficha en esa posición"
        return respuesta
    
    # Invocando a la funcion "mover_ficha_roja", de acuerdo a enunciado para 
    # validar movimiento de fichas rojas dentro de una funcion print para 
    # desplegar el retorno
    print(mover_ficha_roja(tablero_damas,pos_x,pos_y))
    
    # consulta al usuario para seguir ejecutando el programa
    ejecucion = input("Deseas seguir moviendo fichas rojas?: s/n ")
    print(tablero_damas)

'''
basado en reglas de damas -> https://www.youtube.com/watch?v=jA-zevc2fao

Respuesta:
c) En la primera condición (tablero_damas[pos_x, pos_y] == 2), el código únicamente 
valida la presencia o no de fichas rojas, sin embargo no valida la presencia de 
fichas blancas, Simplemente entrega el print de "No hay ficha en esa posición", 
cuando la validacion correcta en caso de haber presencia de ficha blanca 
(tablero_dama[5,0]) debiese ser que "Existe una ficha blanca".

En la segunda condición, (tablero_damas[pos_x+1, pos_y+1] != 2 or 
tablero_damas[pos_x-1, pos_y+1] != 2), no hay una correcta validacion para las
fichas rojas de la fila 0, ya que el print indica que "Puedes mover la ficha", 
cuando toda la fila se ecuentra bloqueada. La valición se realiza correctamente 
cuando las fichas se encuentran en la fila 1 ("No puedes mover la ficha") y fila 
2 ("Puedes mover la ficha").
Otro error en esta validacion es cuando se valida una ficha roja en la columna
7, ya que al validar la posisibilidad de movimiento a la izquierda, perspectiva
jugador fichas rojas, el porgrama arroga el siguiente error:
    IndexError: index 8 is out of bounds for axis 1 with size 8.
Esto debido a que el argumento de la condición valida un eventual movimiento
hacia una inexistente columna 8. 
'''
