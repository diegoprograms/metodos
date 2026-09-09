import matplotlib.pyplot as plt

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
ventas = [120, 150, 90, 200, 170, 220]

plt.figure(figsize=(8, 5))
plt.bar(meses, ventas, color='steelblue')

plt.title("Ventas mensuales 2026")
plt.xlabel("Mes")
plt.ylabel("Unidades vendidas")
plt.grid(axis='y', alpha=0.3)

plt.show()