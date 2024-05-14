Introducción:

Este código tiene como objetivo enseñar a graficar funciones, sus derivadas e integrales utilizando la biblioteca matplotlib en Python. Es una herramienta útil para visualizar el comportamiento de funciones matemáticas y comprender sus propiedades.

Descripción del código:

Importación de librerías:

Se importan las librerías numpy como np y matplotlib.pyplot como plt.
Definición de la función f(x):

Se define una función f(x) que representa la expresión x**3 + x**2 + x.
Definición del intervalo de integración:

Se establecen las variables x_min y x_max para definir el intervalo de integración [0, 2].
Generación de valores de x:

Se crea un vector x_values con 1000 puntos distribuidos uniformemente entre x_min y x_max usando np.linspace.
Evaluación de la función y su derivada:

Se evalúa la función f en los puntos de x_values y se guarda el resultado en y_values.
Se calcula la derivada de f usando np.gradient y se almacena en df.
Cálculo de la integral:

Se calcula la integral definida de f en el intervalo [x_min, x_max] usando np.trapz y se guarda en integral.
Se imprime el valor de la integral.
Creación de la figura y los ejes:

Se crea una figura con tamaño (10, 6) usando plt.figure.
Se generan los ejes para la gráfica.
Graficado de la función original:

Se grafica la función f con una línea azul y una etiqueta f(x) = x**3 + x**2 + x.
Graficado de la derivada:

Se grafica la derivada df con una línea roja discontinua y una etiqueta f'(x) = 3x**2 + 2x + 1.
Graficado del área bajo la curva (integral):

Se rellena el área bajo la curva de f con un color naranja transparente (alpha=0.3) y una etiqueta Integral.
Configuración del título y las etiquetas:
Se establece un título descriptivo para la gráfica: "Función Original, Derivada e Integral".
Se etiquetan los ejes x e y con las etiquetas "x" e "y", respectivamente.
Se añade una leyenda para identificar las curvas graficadas: "f(x)", "f'(x)" e "Integral".
Visualización de la gráfica:
Se activa la cuadrícula para mejorar la visualización de la gráfica.
Se muestra la gráfica usando plt.show.
Explicación del código:

El código primero define la función f(x) que se desea graficar. Luego, se establece el intervalo de integración y se generan los valores de x dentro de ese intervalo. La función f se evalúa en estos valores de x y el resultado se almacena en y_values. La derivada de f se calcula usando np.gradient y se almacena en df. La integral de f se calcula usando np.trapz y se almacena en integral.

A continuación, se crea una figura y se generan los ejes para la gráfica. La función f se grafica con una línea azul, su derivada se grafica con una línea roja discontinua y el área bajo la curva de f se rellena con un color naranja transparente. El título y las etiquetas de los ejes se establecen, y se añade una leyenda para identificar las curvas. Finalmente, la gráfica se muestra usando plt.show.

Recursos adicionales:

Documentación de NumPy: https://numpy.org/
Documentación de Matplotlib: https://readthedocs.org/projects/matplotlib/
Tutorial de Matplotlib para principiantes: https://realpython.com/courses/python-plotting-matplotlib/
