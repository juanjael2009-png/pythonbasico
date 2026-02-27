print("======== Mi Super Calculadora ==========")

# Entradas del usuario
num_1 = float(input("Escriba el valor del primer numero: "))
num_2 = float(input("Escriba el valor del segundo numero: "))
operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ")

# Función principal
def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        return num_1 + num_2
    elif operacion == "-":
        return num_1 - num_2
    elif operacion == "*":
        return num_1 * num_2
    elif operacion == "/":
        if num_2 != 0:
            return num_1 / num_2
        else:
            return "Error: No se puede dividir entre cero."
    else:
        return "Operación no válida."

# Llamado de la función
resultado = calculadora(num_1, num_2, operacion)

print("El resultado es:", resultado)