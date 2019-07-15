#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:04:16 2019

@author: diegorivera
"""
'''
Utilizando como base de datos el "archivo athlete_events.csv". Ubicado en el 
mismo directorio de trabajo que el presente archivo.

Los deportes se caracterizan mucho por el físico de los deportistas. En algunos 
deportes como el Basketball, la mayoría de los deportistas son bastantes altos. 
Por ejemplo, al comparar la altura de esos jugadores con los participantes de 
judo, existe una clara diferencia. Sin embargo, para determinar si hay una 
diferencia significativa entre alturas no basta comparar el valor medio, 
también hay que comparar la variación de la altura de los jugadores con respecto 
a su media, es decir la varianza.
En este problema, se pide crear una función que determine si la altura de los 
jugadores de dos disciplinas son significativamente distintas. Específicamente, 
deberá calcular:

    D = XA - XB/(VA/NA + VB/NB)^0.5
    
donde XA y XB son las alturas promedios de los jugadores de las disciplina A y 
B respectivamente; VA y VB son las varianzas promedios de la altura de los 
jugadores de las disciplina A y B respectivamente; NA y NB son el número de 
jugadores de las disciplinas A y B respectivamente. Si D es menor a -1.96 o 
mayor a 1.96 entonces las diferencias de alturas son significativas.

Crear un programa en Python donde una persona seleccione dos deportes (ingreso 
por teclado) y determine si la diferencia entre las alturas de los jugadores es 
significativamente distintas. Para hacer justa la comparación, considere 
solamente los datos de los deportes en los juegos olímpicos donde ambos deportes 
estuvieron presentes en el mismo año.

Ejemplo de ejecución:
    
    Ingrese un deporte: Taekwondo
    
    Ingrese otro deporte: Judo
    
    Año 2000 D: 1.6848 No hay diferencia significativa 
    Año 2004 D: 2.2484 Hay diferencia significativa 
    Año 2008 D: 3.0102 Hay diferencia significativa 
    Año 2012 D: 3.0322 Hay diferencia significativa 
    Año 2016 D: 5.6742 Hay diferencia significativa

'''
# Importando paquete pandas con alias "pd" para manejar estructura de datos (data
# frames) de manera más efectiva y eficiente por medio de sus funciones.
# Importando paquete numpy con alias "np" para tener un mejor soporte de vectores 
# y matrices por medio de sus funciones matemáticas de manera computar de manera 
# más efectiva.
import pandas as pd
import numpy as np

# definiendo df como data frame de datos athlete_events. Este archivo de formato 
# csv contiene data de los deportistas participantes (nombre, género, edad, 
# altura, peso, equipo, medalla) por disciplinas y evento de los juegos olimpicos 
# modernos en sus versiones de verano e invierno, con detalle de años y sede.
df = pd.read_csv('athlete_events.csv')

# Para tener una idea del número de deportes disponibles para el ingreso de los 
# parametros solicitados por el programa
unique_sports = df['Sport'].unique()

# se dejará en un ciclo continuo la ejecución del programa para poder realizar 
# las consultas que el usuario estime conveniente.
ejecucion = "s" # variable para iniciar el ciclo de ejecución del programa

while (ejecucion != "n"):

    # Desplegando las opciones de deportes disponibles en el data frame, de esta 
    # manera de evitará errores de tipeo y/o el ingreso de deportes que no pertenecen 
    # a los deportes del listado.
    print("Deportes disponibles:",unique_sports)
    
    # capturando variables de ingreso de deportes A y B.
    deporte_A = input("Ingrese un deporte: ")
    deporte_B = input("Ingrese otro deporte: ")
    
    # Una vez definidos los deportes a analizar, de calcularán los indicadores 
    # respectivos, para un mismo año o edición de juego:
    
    # Primero identifico las ediciones en comun para ambos deportes.
    # Con filtro_A y filtro_B acoto el data frame a la data exclusiva de los deportes 
    # ingresados por el usuario del programa.
    # Con ediciones_A y ediciones_B obtengo las ediciones (años) de los juegos en 
    # los cuales estuvieron los deportes selecccionados para asi iniciar la respectiva 
    # seleccion y análisis de la data solicitada y a la vez validar de que se pueda 
    # realizar el respectivo análisis.
    filtro_A = df[df['Sport'] == deporte_A]
    ediciones_A = filtro_A['Year'].unique()
    
    filtro_B = df[df['Sport'] == deporte_B]
    ediciones_B = filtro_B['Year'].unique()
    
    # agrupando por años para obtener los indicadores correspondientes a cada deporte
    # por año. 
    grupoA = filtro_A.groupby('Year')
    grupoB = filtro_B.groupby('Year')
    
    # XA y XB son las alturas promedios de los jugadores de las disciplina A y B 
    # respectivamente
    XA = grupoA['Height'].mean()
    XB = grupoB['Height'].mean()
    
    # VA y VB son las varianzas promedios de la altura de los jugadores de las 
    # disciplina A y B respectivamente
    VA = grupoA['Height'].var()
    VB = grupoB['Height'].var()
    
    # NA y NB son el número de jugadores de las disciplinas A y B respectivamente.
    NA = grupoA['Height'].count()
    NB = grupoB['Height'].count()
    
    # Un vez obtenidos losindicadores necesarios, se podra estimar el diferencial de 
    # estaturas entre los deportes A y B en base a las alturas promedio y las respectivas 
    # varianzas. 
    D = (XA - XB)/((VA/NA) + (VB/NB))**0.5
    
    # Por conceptos de formato y presentación de resultados, éstos serán redondeados 
    # a 5 cifras significativas. Además consideraré únicamente los campos con 
    # registro que es donde ambos deportes estuvieron presentes en el mismo año, 
    # para asegurarme de ello incluiré método dropna().
    D = D.round(4).dropna()
    
    # Para el despliegue correcto de los años de las ediciones de los juegos 
    # correspondiente al análisis, guardamos en la variable ediciones_analisis el 
    # index de la serie D que contiene el año correspondiente.
    ediciones_analisis = D.index
    
    # Guardamos la serie D como arreglo para facilitar el despliegue del resultado 
    # final.
    D_array = np.asarray(D)
    
    # espacio generado por fin de linea para desplegar mejor el resultado
    print("\n")
    
    # ciclo para desplegar resultado en el formato propuesto en el ejemplo del 
    # enunciado, mostrando cada diferencial de estaturas y respuesta de si hay o no 
    # diferencia significativa entre las esturas de los deportistas de las disciplinas 
    # en cuestión por edición correspondiente de análisis.
    for i in range(0,D.size):
        if ((D_array[i] < -1.96) | (D_array[i] > 1.96)):
            analisis = "Hay diferencia significativa"
        else:
            analisis = "No hay diferencia significativa"
        print("Año:",ediciones_analisis[i],"D:",D_array[i]," ",analisis)
    
    # En caso de no haber información que cruzar en los deportes seleccionados, ya 
    # sea porque no hay match en los deportes por años, o no existen los deportes o
    # no hay registros de alturas (data = NA)
    if (D.size == 0):
        print("No existe información disponible para el análisis de",deporte_A,"y",
              deporte_B)
    
    # consulta al usuario para seguir ejecutando el programa
    ejecucion = input("Deseas consultar otros deportes?: s/n ")
