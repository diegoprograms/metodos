# Estimación rápida de DBO en una planta de tratamientono
nombre = "Adriana"
edad = 20
print("Hola soy Adriana:)", nombre)
dbo_Entrada = float(input("Ingresa la DBO a la entrada (mg/L): "))
dbo_Salida = float(input("Ingresa la DBO a la salida (mg/L): "))
#Calculo del porcentaje de eficiencia
eficiencia = ((dbo_Entrada - dbo_Salida / dbo_Entrada))* 100
print(f"\nEficiencia de remocion del sistema: {eficiencia:.1f}%")
              