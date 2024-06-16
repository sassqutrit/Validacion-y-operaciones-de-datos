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
- Programa que valida la longitud de una frase ingresada por el usuario.
- La frase correcta debe tener entre 4 y 8 caracteres.

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



# TODO NOTA: PARA EJECUTAR ESTE PROGRAMA 2, SE DEBE COMENTAR EL ANTERIOR (TODO DE ARRIBA) O
#   EJECUTARLO DIRECTAMENTE CON EL OTRO SCRIPT/ARCHIVO QUE SE CREO EN EL REPO.
"""
Programa 2. Encuentra el Cuadrante.
- Programa que identifica el cuadrante en el que se encuentra un punto dado por sus
coordenadas (X, Y).
- El programa verifica que ninguna coordenada sea 0.
- No se permiten ingresar letras, solo números.
- El usuario solo podrá ingresar números en los campos de entrada de las coordenadas.
- Si el usuario intenta ingresar letras, el campo de entrada se limpiará y se mostrará
un mensaje de error.
- Se utiliza PyQt6 para la interfaz gráfica y matplotlib para visualizar el punto en el
plano cartesiano.

Criterios de evaluación:
A. Uso correcto de las estructuras de control
B. Uso correcto de variables y colecciones de datos
C. Entrega de ambos programas según las indicaciones
D. Uso correcto de la sintaxis y características de Python
E. Comentarios dentro del archivo explicando el funcionamiento
"""

"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QWidget
import matplotlib
matplotlib.use('QT5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


# Creación o definición de una clase, que hereda de la clase principal QMainWindow
# Se utilizan esta clase y funciones para desarrollar una GUI.
class CuadranteApp(QMainWindow):
    # Cuando se crea una instancia de la clase CuadranteApp, se llama al método:
    # __init__, que es el método constructor de la clase.
    def __init__(self):
        super().__init__()
        self.initUI()

    # En este método initUI, se configura la ventana principal, se crean los widgets
    # (etiquetas, campo de entrada de texto y botón) y se organizan en un layout
    # vertical utilizando la clase QVBoxLayout.
    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle("Encuentra el Cuadrante")
        self.setGeometry(500, 100, 600, 600)

        # Creación de los widgets
        layout = QVBoxLayout()
        self.label_x = QLabel("Ingrese la coordenada X (distinta de 0, sin letras):")
        layout.addWidget(self.label_x)
        self.lineEdit_x = QLineEdit()
        self.lineEdit_x.textChanged.connect(self.validar_entrada_x)
        layout.addWidget(self.lineEdit_x)
        self.label_y = QLabel("Ingrese la coordenada Y (distinta de 0, sin letras):")
        layout.addWidget(self.label_y)
        self.lineEdit_y = QLineEdit()
        self.lineEdit_y.textChanged.connect(self.validar_entrada_y)
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

    # Métodos: validar_entrada_x y validar_entrada_y que se conectan al evento textChanged
    # de los QLineEdit correspondientes. Estos métodos verifican si la entrada ingresada por
    # el usuario contiene letras. Si hay letras, se limpia el campo de entrada y se muestra
    # un mensaje de error en la etiqueta self.resultado.
    def validar_entrada_x(self):
        # Obtener la entrada del usuario
        entrada_x = self.lineEdit_x.text()

        # Verificar si la entrada contiene letras
        if any(char.isalpha() for char in entrada_x):
            self.lineEdit_x.clear()
            self.resultado.setText("No se permiten letras en la coordenada X.")

    def validar_entrada_y(self):
        # Obtener la entrada del usuario
        entrada_y = self.lineEdit_y.text()

        # Verificar si la entrada contiene letras
        if any(char.isalpha() for char in entrada_y):
            self.lineEdit_y.clear()
            self.resultado.setText("No se permiten letras en la coordenada Y.")

    # En el método `encontrar_cuadrante`, se obtienen las coordenadas ingresadas por el usuario,
    # verifica que ninguna coordenada fuera 0 (utilizando una estructura condicional `if`),
    # identifica el cuadrante en el que se encuentra el punto según las reglas dadas
    # (utilizando una estructura condicional `if-elif-else`), y muestra el resultado en la
    # etiqueta `self.resultado`.
    def encontrar_cuadrante(self):
        # Obtener las coordenadas ingresadas por el usuario
        x_str = self.lineEdit_x.text()
        y_str = self.lineEdit_y.text()

        # Bloque try-except para verificar que las coordenadas ingresadas sean números válidos.
        # Si no son números válidos, se muestra un mensaje de error en la etiqueta self.resultado.
        try:
            x = float(x_str)
            y = float(y_str)
        except ValueError:
            self.resultado.setText("Las coordenadas deben ser números válidos.")
            return

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
"""
