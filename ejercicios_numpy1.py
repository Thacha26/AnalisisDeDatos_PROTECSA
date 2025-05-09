## TENER QUE SER CUIDADOSA CON LA IDENTACIÓN ES HORRIBLEEEEEEEE

import numpy as np

#Ejercicio 1 - Crear un array de ceros:
#Crea un array de tamaño (3, 4) lleno de ceros.

def ejercicio_1():
    arr_ceros = np.zeros((3, 4)) #matriz de 3x4
    print("\n ________ Ejercicio 1 ________ \n")
    print("Array de ceros:\n", arr_ceros)


#Ejercicio 2- Suma de elementos:
#Dado el array [1, 2, 3, 4, 5], calcula la suma de todos sus elementos usando NumPy.

def ejercicio_2():
    arr_suma = np.array([1, 2, 3, 4, 5])
    suma = np.sum(arr_suma) #module 'numpy' has no attribute 'suma'. Did you mean: 'sum'?
    print("\n ________ Ejercicio 2 ________ \n")
    print("El resultado de la sumita es:", suma, "\n")


#Ejercicio 3 - Encontrar el máximo y mínimo:
#   Dado el array [10, 20, 30, 40, 50], encuentra el valor máximo y mínimo.

def ejercicio_3():
    array = np.array([10, 20, 30, 40, 50])
    maximo = np.max(array)
    minimo = np.min(array)
    print("\n ________ Ejercicio 3 ________ \n")
    print("El máximo es: ", maximo, "\n")
    print("El mínimo es: ", minimo, "\n")


# EStaba repetido el ejercicio 4

#Ejercicio 5 - Generar números aleatorios: 
#Genera un array de 5 números aleatorios entre 0 y 1.

def ejercicio_4():
    arr_aleatorio = np.random.rand(5)
    print("\n ________ Ejercicio 4 ________ \n")
    print("Los números aleatorios son: ", arr_aleatorio, "\n")


#Ejercicio 6 - Promedio de un array:
#Dado el array [5, 10, 15, 20, 25], calcula su promedio usando NumPy.

def ejercicio_5():
    arr_promedio = np.array([5, 10, 15, 20, 25])
    promedio = np.mean(arr_promedio)
    print("\n ________ Ejercicio 5 ________ \n")
    print("Promedio:", promedio, "\n")

#Ejercicio 7 - Concatenar dos arrays
#Dados los arrays A = [1, 2, 3] y B = [4, 5, 6], concaténalos en un solo array.

def ejercicio_6():
    array_A = np.array([1, 2, 3])
    array_B = np.array([4, 5, 6])
    array_C = np.concat([array_A, array_B]) #concat une los arrays
    print("\n ________ Ejercicio 6 ________ \n")
    print( array_C, "\n")

#Ejercicio 8 - Reshape de un Array
#Dado el array [1, 2, 3, 4, 5, 6], cámbialo a una matriz de 2x3.

def ejercicio_7():
    array_matriz = np.array([1, 2, 3, 4, 5, 6])
    arr_2x3 = array_matriz.reshape(2, 3)  
    print("\n ________ Ejercicio 7 ________ \n")
    print("Original\n", array_matriz)
    print("\n El cambio a una matriz de 2x3 se ve así: \n", arr_2x3, "\n")

#Ejercicio 9 - Producto punto (dot product):
#Dados dos arrays A = [1, 2, 3] y B = [4, 5, 6], calcula su producto punto

#numpy.dot() calcula el producto de puntos de dos matrices de entrada.
def ejercicio_8():
    A = np.array([1, 2, 3])
    B = np.array([4, 5, 6])
    dot_product = np.dot(A, B)
    print("\n ________ Ejercicio 8 ________ \n")
    print("Array A: ", A)
    print("Array B: ", B)   
    print("El producto es: ", dot_product, "\n")

#Ejercicio 10 - Reorganizar un array:
#Dado el array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], conviértelo en una matriz (2, 5).
#reshape, su función es la de modificar la forma de un array sin cambiar sus datos

def ejercicio_9():
    array_reorganizar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    matriz = array_reorganizar.reshape(2, 5)
    print("\n ________ Ejercicio 8 ________ \n")
    print("El array original es: ", array_reorganizar)
    print("La matriz de 2x5 es: \n", matriz, "\n")

def calculoDe_ROI():
    inversion = np.array([1000, 1500, 2000])
    retorno = np.array([1200, 1650, 1800])
    ROI = (retorno - inversion) / inversion * 100
    print("\n ________ Cálculo de ROI ________ \n")
    print("El Retorno de Inversión es: ", ROI, "\n")

#Ejercicio: Normalización de Datos
#Tienes un dataset de precios de productos (en USD): [250, 320, 150, 500, 210]. Normaliza los valores al rango [0, 1] para compararlos en una escala común.
#Formulita de la normalización: (x - min) / (max - min): Para una escala valores entre 0 y 1.

def NormalizaciónDe_Datos():
    preciosUSD = np.array([250, 320, 150, 500, 210])

    minimo = np.min(preciosUSD)
    maximo = np.max(preciosUSD)  
    valores_normalizados = (preciosUSD - minimo) / (maximo - minimo)
    print("\n ________ Normalización de valores ________ \n")
    print(preciosUSD)
    print("Precios normalizados:", valores_normalizados, "\n")

#Ejercicio: Filtrado de Datos
#En un array de ventas diarias ([1200, 0, 750, 2400, 0, 1800]), reemplaza los ceros (días sin ventas) por el promedio de los días con ventas.

def FiltradoDe_Datos():
    ventasDiarias = np.array([1200, 0, 750, 2400, 0, 1800])
    print("\n ________ Filtrado de Datos ________ \n")
    print("Ventas antes de remplazar los ceros", ventasDiarias)
    Días_conventas = ventasDiarias[ventasDiarias != 0]
    promedio = np.mean(Días_conventas) #mean se usa para calcular el promedio
    ventasDiarias[ventasDiarias == 0] = promedio #pa' remplazar dondes estén los ceros
    print("Ventas con los ceros remplaazados por el promedio de las ventas diarias", ventasDiarias, "\n")


#Ejercicio - Análisis de Presión Arterial
#Tenemos un dataset de mediciones de presión arterial sistólica (mmHg) de 10 pacientes: [120, 135, 140, 118, 150, 130, 160, 125, 142, 128].

#Calculen:

#Media y desviación estándar.
#Identifiquen valores fuera del rango normal (90–140 mmHg).

def Análisis_de_Presión_Arterial():
    precionesDe_pacientes= np.array([120, 135, 140, 118, 150, 130, 160, 125, 142, 128])
    media = np.mean(precionesDe_pacientes)
    desviacion_estandar = np.std(precionesDe_pacientes) #std calcula la desviación estándar de un array (matriz) NumPy
    valores_fuera_del_rangoNormal = precionesDe_pacientes[(precionesDe_pacientes < 90) | (precionesDe_pacientes > 140)]
    print("\n ________ Análisis de Presión Arterial ________ \n")
    print("Presión de 10 pacientes", precionesDe_pacientes)
    print("Media y desviación estandar:", media, desviacion_estandar)
    print("Valores fuera del rango normal:", valores_fuera_del_rangoNormal, "\n")

#Ejercicio - Cálculo del PIB per Cápita
#Dados el PIB (en millones de USD) [500, 320, 700, 450] y la población (en millones) [10, 8, 12, 9] de 4 países, calculen el PIB per cápita y determinen el país con el mayor valor.

def Cálculo_del_PIB_per_Cápita():
    PIB = np.array([500, 320, 700, 450]) 
    poblacion = np.array([10, 8, 12, 9])
    PIB_per_capita = PIB / poblacion 
    indice_max = np.argmax(PIB_per_capita) #argmax devuelve los índices del valor máximo dentro de un array, o a lo largo de un eje especificado
    max_pib_per_capita = PIB_per_capita[indice_max]
    print("\n ________ Cálculo del PIB per Cápita ________ \n")
    print("Datos del PIB: ", PIB)
    print("Población: ", poblacion)
    print("PIB per cápita :", PIB_per_capita)
    print("País con mayor PIB per cápita: País", indice_max + 1, "\n") #El array inicia con 0, por eso se le pone el +1

#Ejercicio - Sistema de Drops (Probabilidades)
def Sistema_de_Drops():
    opciones_Para_Dropear = [0, 1, 2, 3]
    probabilidad = [0.5, 0.3, 0.15, 0.05]
    drops = np.random.choice(opciones_Para_Dropear, size=100, p=probabilidad)
    artefactos = np.sum(drops == 3)
    print("\n ________ Sistema de Drops (Probabilidades)________ \n")
    print("Artefactos obtenidos:", artefactos, "\n")

ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()
ejercicio_6()
ejercicio_7()
ejercicio_8()
ejercicio_9()
calculoDe_ROI()
NormalizaciónDe_Datos()
FiltradoDe_Datos()
Análisis_de_Presión_Arterial()
Cálculo_del_PIB_per_Cápita()