¡Readme para graficar funciones, derivadas e integrales con Python!
Introducción
Este código tiene como objetivo enseñar a graficar funciones, sus derivadas e integrales utilizando la biblioteca matplotlib en Python. Es una herramienta útil para visualizar el comportamiento de funciones matemáticas y comprender sus propiedades.

Descripción del código
Importación de librerías
Se importan las librerías numpy como np y matplotlib.pyplot como plt.

Python
import numpy as np
import matplotlib.pyplot as plt
Usa el código con precaución.
content_copy
Definición de la función f(x)
Se define una función f(x) que representa la expresión x**3 + x**2 + x.

Python
def f(x):
  return x**3 + x**2 + x
Usa el código con precaución.
content_copy
Definición del intervalo de integración
Se establecen las variables x_min y x_max para definir el intervalo de integración [0, 2].

Python
x_min = 0  # Límite inferior del intervalo
x_max = 2  # Límite superior del intervalo
Usa el código con precaución.
content_copy
Generación de valores de x
Se crea un vector x_values con 1000 puntos distribuidos uniformemente entre x_min y x_max usando np.linspace.

Python
x_values = np.linspace(x_min, x_max, 1000)  # Generamos 1000 puntos entre x_min y x_max
Usa el código con precaución.
content_copy
Evaluación de la función y su derivada
Se evalúa la función f en los puntos de x_values y se guarda el resultado en y_values.
Se calcula la derivada de f usando np.gradient y se almacena en df.

Python
y_values = f(x_values)
integral = np.trapz(y_values, x_values)

print("Integral de f(x) en el intervalo [", x_min, ",", x_max, "]:", integral)

df = np.gradient(y_values, x_values)
Usa el código con precaución.
content_copy
Cálculo de la integral
Se calcula la integral definida de f en el intervalo [x_min, x_max] usando np.trapz y se guarda en integral.
Se imprime el valor de la integral.

Python
integral = np.trapz(y_values, x_values)

print("Integral de f(x) en el intervalo [", x_min, ",", x_max, "]:", integral)
Usa el código con precaución.
content_copy
Creación de la figura y los ejes
Se crea una figura con tamaño (10, 6) usando plt.figure.
Se generan los ejes para la gráfica.

Python
plt.figure(figsize=(10, 6))
Usa el código con precaución.
content_copy
Graficado de la función original
Se grafica la función f con una línea azul y una etiqueta f(x) = x**3 + x**2 + x.

Python
plt.plot(x_values, y_values, label='f(x) = x**3 + x**2 + x', color='blue')
Usa el código con precaución.
content_copy
Graficado de la derivada
Se grafica la derivada df con una línea roja discontinua y una etiqueta f'(x) = 3x**2 + 2x + 1.

Python
plt.plot(x_values, df, label="f'(x) = 3x**2 + 2x + 1", linestyle='--', color='red')
Usa el código con precaución.
content_copy
Graficado del área bajo la curva (integral)
Se rellena el área bajo la curva de f con un color naranja transparente (alpha=0.3) y una etiqueta Integral.

Python
plt.fill_between(x_values, 0, y_values, alpha=0.3, color='orange', label='Integral')
Usa el código con precaución.
content_copy
Configuración del título y las etiquetas
Se establece un título descriptivo para la gráfica: "Función Original, Derivada e Integral".
Se etiquetan los ejes x e y con las etiquetas "x" e "y", respectivamente.
Se añade una leyenda para identificar las curvas graficadas: "f(x)", "f'(x)" e "Integral".

Python
plt.title('Función Original, Derivada e Integral')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
Usa el código con precaución.
content_copy
