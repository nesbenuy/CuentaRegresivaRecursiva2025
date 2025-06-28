# main.py

import contador

def solicitar_entero_positivo():
    while True:
        entrada = input("Ingrese un número entero positivo: ")
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Entrada inválida. por favor, ingrese solo números enteros positivos.")

# Solicita un número válido
n = solicitar_entero_positivo()

# Ejecuta la cuenta regresiva
contador.cuenta_regresiva(n)

# Mensaje 
print("¡LANZAMIENTO!")
