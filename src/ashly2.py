import matplotlib.pyplot as plt

# Datos
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
ventas = [10, 15, 8, 20, 25]

# Crear gráfica
plt.plot(dias, ventas, marker="o")

# Títulos y etiquetas
plt.title("Ventas de la semana")
plt.xlabel("Días")
plt.ylabel("Ventas")

# Mostrar gráfica
plt.show()