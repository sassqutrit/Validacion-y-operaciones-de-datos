# Validacion-y-operaciones-de-datos
El proyecto consta de dos programas que demuestran la comprensión y aplicación de estructuras de control y colecciones de datos en Python.
## Programa 1. Longitud de una Frase:
   * El programa solicita una palabra al usuario y verificar que su longitud esté entre 4 y 8 caracteres.
   * Si la palabra tiene menos de 4 caracteres, debe informar cuántos caracteres faltan.
   * Si la palabra tiene más de 8 caracteres, debe informar cuántos caracteres sobran.
   * Si la palabra tiene entre 4 y 8 caracteres, debe informar que la palabra es correcta.

## Programa 2. Encuentra el Cuadrante:
   * El programa solicita dos números al usuario que representan las coordenadas XX y YY de un punto en un plano cartesiano.
   * Verifica que ninguna de las coordenadas sea 0.
   * Basándose en los valores de XX y YY, el programa determina y muestra en cuál de los cuatro cuadrantes se encuentra el punto.

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
* Finalmente, en el método `validar_longitud`, se obtiene la frase ingresada por el usuario, se agrega a la lista `frases_ingresadas`, se calcula su longitud y se muestra el resultado correspondiente en la etiqueta `self.resultado`.

#### En conclusión, la clase `LongitudFraseApp` hereda de la clase `QMainWindow` de PyQt6 y se encarga de crear y administrar la interfaz gráfica de usuario para el programa de validación de longitud de frases. Además, utiliza una lista (`frases_ingresadas`) para almacenar las frases ingresadas por el usuario durante la ejecución del programa.


### Explicación del desarrollo del Programa 2. Encuentra el Cuadrante.
   * Uso correcto de las estructuras de control:
      - Se utiliza






