# factorial.py
# Programa para calcular factoriales.
# Puede trabajar de estas formas:
# 1) Un solo número: 5
# 2) Un rango completo: 4-8
# 3) Un rango sin límite inferior: -10   -> calcula de 1 a 10
# 4) Un rango sin límite superior: 5-    -> calcula de 5 a 60
# Si no se pasa argumento por consola, lo solicita por teclado.

import sys


def factorial(n):
    # Calcula el factorial de un número entero positivo
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i

    return resultado


def mostrar_factoriales(desde, hasta):
    # Muestra los factoriales entre dos extremos, inclusive
    for i in range(desde, hasta + 1):
        print(f"{i}! = {factorial(i)}")


# Si el usuario pasó un argumento, lo usamos.
# Si no, lo pedimos por teclado.
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese un número o rango: ")


# Caso 1: rango sin límite inferior, por ejemplo -10
# Calcula desde 1 hasta 10
if entrada.startswith("-") and len(entrada) > 1:
    hasta = int(entrada[1:])
    mostrar_factoriales(1, hasta)

# Caso 2: rango sin límite superior, por ejemplo 5-
# Calcula desde 5 hasta 60
elif entrada.endswith("-") and len(entrada) > 1:
    desde = int(entrada[:-1])
    mostrar_factoriales(desde, 60)

# Caso 3: rango completo, por ejemplo 4-8
elif "-" in entrada:
    partes = entrada.split("-")
    desde = int(partes[0])
    hasta = int(partes[1])
    mostrar_factoriales(desde, hasta)

# Caso 4: número simple, por ejemplo 6
else:
    num = int(entrada)
    print(f"{num}! = {factorial(num)}")