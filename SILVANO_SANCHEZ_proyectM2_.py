#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import matplotlib
matplotlib.use('QT5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

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


# Creación o definición de una clase, que hereda de la clase principal QMainWindow
# Se utilizan esta clase y funciones para desarrollar una GUI.
class CuadranteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Cuando se crea una instancia de la clase LongitudFraseApp, se llama al método:
    # __init__, que es el método constructor de la clase.
    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle("Encuentra el Cuadrante")
        self.setGeometry(500, 100, 600, 600)

        # Creación de los widgets
        layout = QVBoxLayout()
        self.label_x = QLabel("Ingrese la coordenada X (distinta de 0):")
        layout.addWidget(self.label_x)
        self.lineEdit_x = QLineEdit()
        layout.addWidget(self.lineEdit_x)
        self.label_y = QLabel("Ingrese la coordenada Y (distinta de 0):")
        layout.addWidget(self.label_y)
        self.lineEdit_y = QLineEdit()
        layout.addWidget(self.lineEdit_y)
        self.button = QPushButton("Encontrar Cuadrante")
        self.button.clicked.connect(self.encontrar_cuadrante)
        layout.addWidget(self.button)
        self.resultado = QLabel("")
        layout.addWidget(self.resultado)

        # Creación del lienzo para graficar el punto
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Organización de los widgets en un layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # En el método `encontrar_cuadrante`, obtienen las coordenadas ingresadas por el usuario,
    # verifiqué que ninguna coordenada fuera 0 (utilizando una estructura condicional `if`),
    # identifiqué el cuadrante en el que se encuentra el punto según las reglas dadas
    # (utilizando una estructura condicional `if-elif-else`), y mostré el resultado en la
    # etiqueta `self.resultado`.
    def encontrar_cuadrante(self):
        # Obtener las coordenadas ingresadas por el usuario
        x = float(self.lineEdit_x.text())
        y = float(self.lineEdit_y.text())

        # Verificar que ninguna coordenada sea 0
        if x == 0 or y == 0:
            self.resultado.setText("Las coordenadas no pueden ser 0.")
            return

        # Identificar el cuadrante
        if x > 0 and y > 0:
            cuadrante = "I"
        elif x < 0 and y > 0:
            cuadrante = "II"
        elif x < 0 and y < 0:
            cuadrante = "III"
        else:
            cuadrante = "IV"

        # Mostrar el resultado
        self.resultado.setText(f"El punto ({x}, {y}) se encuentra en el cuadrante {cuadrante}.")

        # Graficar el punto en el plano cartesiano
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.axhline(y=0, color='k')  # Eje X
        ax.axvline(x=0, color='k')  # Eje Y
        ax.set_xlim([-100, 100])
        ax.set_ylim([-100, 100])
        ax.scatter(x, y, color='r', marker='o')
        ax.set_title(f"Punto ({x}, {y}) en el cuadrante {cuadrante}")
        self.canvas.draw()

# Cuando el intérprete ejecuta un módulo, la variable __name__ se establecerá como __main__
# si el módulo que se está ejecutando es el programa principal.
if __name__ == "__main__":
    # Creación de la aplicación Qt
    app = QApplication(sys.argv)

    # Creación de la ventana principal
    window = CuadranteApp()
    window.show()

    # Ejecución del loop de eventos de la aplicación
    sys.exit(app.exec())
