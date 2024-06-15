#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget


""" Programas: 1. Longitud de una frase y 2. Encuentra el cuadrante. """
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


# Creación o definición de una clase, que hereda de la clase principal QMainWindow
# Se utilizan esta clase y funciones para desarrollar una GUI.
class LongitudFraseApp(QMainWindow):
    # Cuando se crea una instancia de la clase LongitudFraseApp, se llama al método:
    # __init__, que es el método constructor de la clase.
    def __init__(self):
        super().__init__()
        self.initUI()

        # Creación de una lista para almacenar las frases ingresadas
        self.frases_ingresadas = []

    # En este método initUI, se configura la ventana principal, se crean los widgets
    # (etiquetas, campo de entrada de texto y botón) y se organizan en un layout
    # vertical utilizando la clase QVBoxLayout.
    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle("Longitud de Frase")
        self.setGeometry(500, 100, 400, 200)

        # Creación de los widgets, usando la clase QVBoxLayout()
        layout = QVBoxLayout()
        self.label = QLabel("Ingrese una frase (sin números):")
        layout.addWidget(self.label)
        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.validar_entrada)
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

    # El método validar_entrada se conecta al evento textChanged del QLineEdit.
    # Este método verifica si la entrada ingresada por el usuario contiene números.
    # Si hay números, se limpia el campo de entrada y se muestra un mensaje de
    # error en la etiqueta self.resultado.
    def validar_entrada(self):
        # Obtener la entrada del usuario
        entrada = self.lineEdit.text()

        # Verificar si la entrada contiene números
        if any(char.isdigit() for char in entrada):
            self.lineEdit.clear()
            self.resultado.setText("No se permiten números en la entrada.")

    # En este método validar_longitud, se obtiene la frase ingresada por el usuario,
    # se agrega a la lista frases_ingresadas, se calcula su longitud y se muestra el
    # resultado correspondiente en la etiqueta self.resultado.
    # Solo se ejecutará cuando el usuario ingrese una frase válida Sin números.
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


# Cuando el intérprete ejecuta un módulo, la variable __name__ se establecerá como __main__
# si el módulo que se está ejecutando es el programa principal.
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


