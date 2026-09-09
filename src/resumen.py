from pathlib import Path
import csv


ruta_proyecto = Path(__file__).resolve().parent.parent
ruta_datos = ruta_proyecto / "datos" / "mediciones.csv"

temperaturas = []

with ruta_datos.open(encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        temperaturas.append(float(fila["temperatura_c"]))

promedio = sum(temperaturas) / len(temperaturas)

temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)

print(f"Número de mediciones: {len(temperaturas)}")
print(f"Temperatura promedio: {promedio:.2f} °C")
print(f"Temperatura máxima: {temperatura_maxima:.2f} °C")
print(f"Temperatura mínima: {temperatura_minima:.2f} °C")

if promedio > 25:
    print("La temperatura promedio es alta.")
else:
    print("La temperatura promedio es normal.")
    # editado por Jeison Vanegas 
# juan estuvo aqui :p 
