def calcular_caudal(velocidad, ancho, profundidad):
    """
    Calcula el caudal de un canal rectangular.

    Q = V * A
    A = ancho * profundidad
    """
    area = ancho * profundidad
    caudal = velocidad * area

    return area, caudal


def main():
    print("=" * 45)
    print("     CÁLCULO DE CAUDAL DE AGUA")
    print("=" * 45)

    try:
        velocidad = float(input("Ingrese la velocidad del agua (m/s): "))
        ancho = float(input("Ingrese el ancho del canal (m): "))
        profundidad = float(input("Ingrese la profundidad del agua (m): "))

        if velocidad < 0 or ancho <= 0 or profundidad <= 0:
            print("\nError: los valores deben ser positivos.")
            return

        area, caudal = calcular_caudal(
            velocidad,
            ancho,
            profundidad
        )

        print("\n--- RESULTADOS ---")
        print(f"Área de la sección: {area:.2f} m²")
        print(f"Caudal: {caudal:.2f} m³/s")

    except ValueError:
        print("\nError: ingrese únicamente valores numéricos.")



if __name__ == "__main__":
    main()