def evaluar_ph(ph_valor):
    if ph_valor < 6.5:
        return "Ácido (Requiere tratamiento alcalinizante)"
    elif 6.5 <= ph_valor <= 8.5:
        return "Óptimo / Neutro"
    else:
        return "Alcalino (Requiere ajuste de pH)"

muestras = [5.8, 7.2, 8.9, 6.8]

print("=== EVALUACIÓN DE MUESTRAS DE AGUA ===")
for i, muestra in enumerate(muestras, start=1):
    resultado = evaluar_ph(muestra)
    print(f"Muestra {i} (pH {muestra}): {resultado}") 