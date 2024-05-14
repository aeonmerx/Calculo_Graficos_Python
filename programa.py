import numpy as np
import matplotlib.pyplot as plt

# Definimos la función original f(x)
def f(x):
    return x**3 + x**2 + x

# Definimos el intervalo de integración
x_min = 0  # Límite inferior del intervalo
x_max = 2  # Límite superior del intervalo

# Definimos el rango de valores de x dentro del intervalo
x_values = np.linspace(x_min, x_max, 1000)  # Generamos 1000 puntos entre x_min y x_max

# Evaluamos la función y su derivada en los puntos x dentro del intervalo
y_values = f(x_values)
integral = np.trapz(y_values, x_values)

print("Integral de f(x) en el intervalo [", x_min, ",", x_max, "]:", integral)

# Calculamos la derivada de la función original f'(x)
df = np.gradient(y_values, x_values)

# Creamos la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficamos la función original
plt.plot(x_values, y_values, label='f(x) = x**3 + x**2 + x', color='blue')

# Graficamos la derivada de la función original
plt.plot(x_values, df, label="f'(x) = 3x**2 + 2x + 1", linestyle='--', color='red')

# Graficamos la integral de la función original (área bajo la curva)
plt.fill_between(x_values, 0, y_values, alpha=0.3, color='orange', label='Integral')

# Configuramos el título y las etiquetas de los ejes
plt.title('Función Original, Derivada e Integral')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Mostramos la gráfica
plt.grid(True)
plt.show()
