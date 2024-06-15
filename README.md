# Validacion-y-operaciones-de-datos
El proyecto consta de dos programas que demuestran la comprensión y aplicación de estructuras de control y colecciones de datos en Python.
## Programa 1. Longitud de una Frase:
   * El programa solicita una palabra al usuario y verificar que su longitud esté entre 4 y 8 caracteres.
   * Si la palabra tiene menos de 4 caracteres, debe informar cuántos caracteres faltan.
   * Si la palabra tiene más de 8 caracteres, debe informar cuántos caracteres sobran.
   * Si la palabra tiene entre 4 y 8 caracteres, debe informar que la palabra es correcta.

## Programa 2. Encuentra el Cuadrante:
   * El programa solicita dos números al usuario que representan las coordenadas X e Y de un punto en un plano cartesiano.
   * Verifica que ninguna de las coordenadas sea 0.
   * Basándose en los valores de X e Y, el programa determina y muestra en cuál de los cuatro cuadrantes se encuentra el punto.

### Explicación del desarrollo del Programa 1. Longitud de una Frase.
   * Uso correcto de las estructuras de control:
      - Se utiliza la estructura de control `if-elif-else` para validar la longitud de la frase y mostrar el mensaje correspondiente.
   * Uso correcto de variables y colecciones de datos:
      - Se utiliza la variable `frase` para almacenar la cadena de texto ingresada por el usuario.
      - Se utiliza la función `len()` para obtener la longitud de la cadena de texto almacenada en `frase`.
      - Se ha creado una lista llamada `frases_ingresadas` dentro de la clase `LongitudFraseApp`.
      - Cada vez que el usuario ingresa una frase y hace clic en el botón "Validar", la frase se agrega a la lista `frases_ingresadas` mediante el método `append()`.
   * Uso correcto de la sintaxis y características de Python:
      - Se utiliza la indentación adecuada según las buenas prácticas de Python.
      - Se utiliza el casting implícito al comparar la longitud de la cadena con números enteros.
   * Comentarios dentro del archivo explicando el funcionamiento:
      - Se han agregado comentarios en el código explicando el propósito de cada bloque de código.
#### Con estos pasos, el programa utiliza una colección de datos (una lista) para almacenar las frases ingresadas por el usuario.

### Explicación del uso y funcionamiento de la clase creada:
* Primeramente, como podemos observar se define una clase llamada `LongitudFraseApp` que hereda de la clase `QMainWindow` proporcionada por el módulo `PyQt6.QtWidgets`. La clase `QMainWindow` es una clase base que proporciona una ventana principal para una aplicación de interfaz gráfica de usuario (GUI) en PyQt6.
* Cuando se crea una instancia de la clase `LongitudFraseApp`, se llama al método `__init__`, que es el método constructor de la clase. Dentro de este método, se realiza lo siguiente:
  - `super().__init__()`: Se llama al constructor de la clase base (`QMainWindow`) para inicializar los atributos y métodos básicos de la ventana principal.
  - `self.initUI()`: Se llama al método `initUI`, que se encarga de configurar y crear la interfaz de usuario de la aplicación.
  - `self.frases_ingresadas = []`: Se crea una lista vacía llamada `frases_ingresadas`, que se utilizará para almacenar las frases ingresadas por el usuario durante la ejecución del programa.
* Luego, en el método `initUI`, se configura la ventana principal, se crean los widgets (etiquetas, campo de entrada de texto y botón) y se organizan en un layout vertical utilizando la clase `QVBoxLayout`.
* En el método `validar_longitud`, se obtiene la frase ingresada por el usuario, se agrega a la lista `frases_ingresadas`, se calcula su longitud y se muestra el resultado correspondiente en la etiqueta `self.resultado`.
* En el método `validar_entrada` se conecta al evento textChanged del QLineEdit. Este método verifica si la entrada ingresada por el usuario contiene números. Si hay números, se limpia el campo de entrada y se muestra un mensaje de error en la etiqueta `self.resultado`.

#### En conclusión, la clase `LongitudFraseApp` hereda de la clase `QMainWindow` de PyQt6 y se encarga de crear y administrar la interfaz gráfica de usuario para el programa de validación de longitud de frases. Además, utiliza una lista (`frases_ingresadas`) para almacenar las frases ingresadas por el usuario durante la ejecución del programa.


### Explicación del desarrollo del Programa 2. Encuentra el Cuadrante.
#### Programa que identifica el cuadrante en el que se encuentra un punto dado por sus coordenadas (X, Y), utilizando PyQt6 para la interfaz gráfica y matplotlib para visualizar el punto en el plano cartesiano.
#### Incluí comentarios en el código para explicar cada bloque y al final detallé cómo hice el programa y mis reflexiones sobre el bootcamp.

### Explicación del código:
* Importamos los módulos necesarios de PyQt6 y matplotlib.
* Creamos la clase `CuadranteApp` que hereda de `QMainWindow`.
* En el método `__init__` llamamos al método `initUI` para inicializar la interfaz de usuario.
* El método `initUI` configura la ventana principal, crea los widgets (etiquetas, campos de entrada de texto y botón), los organiza en un layout vertical y crea un lienzo (`FigureCanvas`) para graficar el punto en el plano cartesiano.
* Cuando se hace clic en el botón "Encontrar Cuadrante", se llama al método `encontrar_cuadrante`.
* El método `encontrar_cuadrante` obtiene las coordenadas ingresadas por el usuario, verifica que ninguna coordenada sea 0, identifica el cuadrante en el que se encuentra el punto según las reglas dadas, muestra el resultado y grafica el punto en el plano cartesiano utilizando matplotlib.
* Finalmente, creamos una instancia de la aplicación Qt, creamos una instancia de la ventana `CuadranteApp` y la mostramos.

### Detalles de cómo hice el programa:
* Para hacer este programa, primero entendí los requisitos y separé las tareas en partes más pequeñas. Decidí utilizar PyQt6 para crear la interfaz gráfica de usuario y matplotlib para visualizar el punto en el plano cartesiano.
* Comencé por crear la ventana principal y los widgets necesarios (etiquetas, campos de entrada de texto y botón) en el método `initUI`. Luego, conecté el botón "Encontrar Cuadrante" al método `encontrar_cuadrante`, donde se realiza la lógica principal del programa.
* En el método `encontrar_cuadrante`, obtuve las coordenadas ingresadas por el usuario, verifiqué que ninguna coordenada fuera 0 (utilizando una estructura condicional `if`), identifiqué el cuadrante en el que se encuentra el punto según las reglas dadas (utilizando una estructura condicional `if-elif-else`), y mostré el resultado en la etiqueta `self.resultado`.
* Finalmente, utilicé matplotlib para graficar el punto en el plano cartesiano. Primero, creé un lienzo (`FigureCanvas`) en el método `initUI` para asignar un área de dibujo. Luego, en el método `encontrar_cuadrante`, limpié el lienzo (`self.figure.clear()`), creé un nuevo subplot (`ax = self.figure.add_subplot(111)`), dibujé los ejes X e Y (`ax.axhline(y=0, color='k')` y `ax.axvline(x=0, color='k')`), establecí los límites del plano cartesiano (`ax.set_xlim([-10, 10])` y `ax.set_ylim([-10, 10])`), grafiqué el punto (`ax.scatter(x, y, color='r', marker='o')`), agregué un título (`ax.set_title(f"Punto ({x}, {

### Este proyecto me ha dejado varias reflexiones sobre el Bootcamp hasta ahora:
*Aprendizaje práctico: El bootcamp ha sido una excelente oportunidad para aplicar los conocimientos adquiridos en proyectos prácticos. Al tener que crear programas funcionales, he podido reforzar los conceptos aprendidos y enfrentar desafíos reales, lo que ha mejorado significativamente mi comprensión y habilidades de programación.
*Resolución de problemas: Cada proyecto ha representado un reto en cuanto a la resolución de problemas. He tenido que analizar los requisitos, dividir las tareas en pasos más pequeños, investigar y buscar soluciones a los obstáculos que se han presentado. Esta experiencia ha fortalecido mi capacidad para resolver problemas de manera efectiva y sistemática.
*Integración de herramientas y bibliotecas: En estos proyectos, he aprendido a integrar diferentes herramientas y bibliotecas, como PyQt6 para la interfaz gráfica de usuario y matplotlib para la visualización de gráficos. Esto me ha permitido comprender cómo diferentes componentes pueden trabajar juntos para crear soluciones completas.
*Documentación y comentarios: La importancia de una buena documentación y comentarios claros en el código ha sido enfatizada en el bootcamp. Al tener que explicar detalladamente mi enfoque y el funcionamiento del código, he mejorado mis habilidades para comunicar ideas de manera efectiva y crear código más legible y mantenible.
*Trabajo individual y colaborativo: Algunos proyectos han sido individuales, mientras que otros han requerido trabajo colaborativo. Esta combinación me ha permitido desarrollar habilidades tanto para trabajar de manera autónoma como para colaborar en equipo, lo cual es invaluable en el mundo laboral.

#### En general, este bootcamp ha sido una experiencia enriquecedora y desafiante. He adquirido conocimientos sólidos en programación y he podido aplicarlos en proyectos prácticos. Además, he desarrollado habilidades importantes como la resolución de problemas, la integración de herramientas, la documentación efectiva y la capacidad de trabajar tanto de forma individual como en equipo. Estoy emocionado por continuar aprendiendo y enfrentando nuevos desafíos en el futuro.
