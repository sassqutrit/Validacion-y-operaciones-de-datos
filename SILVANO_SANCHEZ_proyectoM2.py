#!/usr/bin/python3
#-*- coding: utf-8 -*-


""" Programas: Longitud de una frase y Encuentra el cuadrante. """
__author__      =   '©"SILVANO SANCHEZ SANCHEZ"®'
__copyright__   =   'Copyright 2024, Proyecto: Validación y operaciones de datos.'
__credits__     =   ["ChatGPT", "Yo", "nada más"]
__license__     =   'GPL'
__version__     =   '0.0.1.0.0'
__email__       =   'sass74050505@hotmail.com'
__status__      =   'Desarrollo-Development'
__date__        =   '2024-06-14 12:00:00'
__changed__     =   '2024-06-15 12:00:00'

# Programa 1. Longitud de una frase.
# Programa para verificar la longitud de una palabra

# Solicita al usuario que ingrese una palabra
palabra = input("Introduce una palabra: ")

# Verifica la longitud de la palabra y proporciona la respuesta adecuada
if len(palabra) < 4:
    print(f"Hacen falta letras. Solo tiene {len(palabra)} letras")
elif len(palabra) > 8:
    print(f"Sobran letras. Tiene {len(palabra)} letras")
else:
    print("La palabra es correcta")


# Programa 2. Encuentra el cuadrante.
# Programa para encontrar el cuadrante de un punto en el plano cartesiano.

# Solicita al usuario que ingrese las coordenadas X e Y
x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

# Verifica que ninguna de las coordenadas sea 0 y determina el cuadrante
if x == 0 or y == 0:
    print("Las coordenadas no pueden ser 0")
elif x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I")
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II")
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III")
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuadrante IV")


