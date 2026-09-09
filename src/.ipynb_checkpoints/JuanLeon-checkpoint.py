import math
import time


def simular_dbo_oxigeno():
    # Parámetros ambientales / de diseño
    L0 = 250.0  # DBO última inicial (mg/L)
    k = 0.23  # Tasa de desoxigenación (1/día)
    dias = 15  # Período de simulación

    print("==================================================")
    print("  SIMULACIÓN AMBIENTAL: CINÉTICA DE DBO (mg/L)   ")
    print("==================================================\n")
    time.sleep(0.5)

    print(f"{'Día':<6} | {'DBO Remanente (L)':<20} | {'DBO Removida (y)':<20} | 'Gráfica'")
    print("-" * 75)

    for t in range(dias + 1):
        # Modelo cinético de primer orden: L(t) = L0 * e^(-k*t)
        L_t = L0 * math.exp(-k * t)
        y_t = L0 - L_t  # DBO ejercida/removida

        # Generar barra gráfica ASCII basada en DBO removida
        barra = "█" * int(y_t / 8)

        print(f"{t:<6} | {L_t:<20.2f} | {y_t:<20.2f} | {barra}")
        time.sleep(0.08)

    print("-" * 75)
    print("\n[ÉXITO] Simulación de degradación materia orgánica completada.")


if __name__ == "__main__":
    simular_dbo_oxigeno()