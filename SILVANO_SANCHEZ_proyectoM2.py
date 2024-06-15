#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


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


"""
Programa 1. Longitud de Frase.
Programa que valida la longitud de una frase ingresada por el usuario.
La frase correcta debe tener entre 4 y 8 caracteres.

Criterios de evaluación:
A. Uso correcto de las estructuras de control.
B. Uso correcto de variables y colecciones de datos.
C. Entrega de ambos programas según las indicaciones.
D. Uso correcto de la sintaxis y características de Python.
E. Comentarios dentro del archivo explicando el funcionamiento.
"""

# Creación de una clase, pasándole 
class LongitudFraseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Creación de una lista para almacenar las frases ingresadas
        self.frases_ingresadas = []

    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle("Longitud de Frase")
        self.setGeometry(100, 100, 400, 200)

        # Creación de los widgets
        layout = QVBoxLayout()
        self.label = QLabel("Ingrese una frase:")
        layout.addWidget(self.label)
        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)
        self.button = QPushButton("Validar")
        self.button.clicked.connect(self.validar_longitud)
        layout.addWidget(self.button)
        self.resultado = QLabel("")
        layout.addWidget(self.resultado)

        # Organización de los widgets en un layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def validar_longitud(self):
        # Obtener la frase ingresada por el usuario
        frase = self.lineEdit.text()

        # Agregar la frase a la lista de frases ingresadas
        self.frases_ingresadas.append(frase)

        # Calcular la longitud de la frase
        longitud = len(frase)

        # Validar la longitud de la frase y mostrar el resultado correspondiente
        if longitud >= 4 and longitud <= 8:
            self.resultado.setText("La frase es correcta.")
        elif longitud < 4:
            self.resultado.setText(f"Hacen falta letras. Solo tiene {longitud} letras.")
        else:
            self.resultado.setText(f"Sobran letras. Tiene {longitud} letras.")

if __name__ == "__main__":
    # Creación de la aplicación Qt
    app = QApplication(sys.argv)

    # Creación de la ventana principal
    window = LongitudFraseApp()
    window.show()

    # Ejecución del loop de eventos de la aplicación
    sys.exit(app.exec())


"""
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

"""


