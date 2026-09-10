def estimar_et0(temp_max, temp_min):
    temp_media = (temp_max + temp_min) / 2
    et0 = 0.0023 * (temp_media + 17.8) * ((temp_max - temp_min) ** 0.5) * 15
    return et0

registros_temperatura = [
    {"dia": "Lunes", "tmax": 24.5, "tmin": 11.2},
    {"dia": "Martes", "tmax": 26.0, "tmin": 12.5},
    {"dia": "Miércoles", "tmax": 21.0, "tmin": 10.0}
]

print("=== ESTIMACIÓN DE EVAPOTRANSPIRACIÓN (ET0) ===")
for reg in registros_temperatura:
    evapo = estimar_et0(reg["tmax"], reg["tmin"])
    print(f"{reg['dia']}: {evapo:.2f} mm/día de pérdida de agua")