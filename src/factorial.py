# factorial.py
# Programa para calcular factoriales

import sys

def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def procesar_entrada(entrada):
    # Caso 1: número simple (ej: 10)
    if "-" not in entrada:
        n = int(entrada)
        print(f"{n}! = {calcular_factorial(n)}")

    # Caso 2: rango completo (ej: 4-8)
    elif "-" in entrada and entrada[0] != "-" and entrada[-1] != "-":
        partes = entrada.split("-")
        inicio = int(partes[0])
        fin = int(partes[1])

        for i in range(inicio, fin + 1):
            print(f"{i}! = {calcular_factorial(i)}")

    # Caso 3: -hasta (ej: -10 → de 1 a 10)
    elif entrada.startswith("-"):
        fin = int(entrada[1:])
        for i in range(1, fin + 1):
            print(f"{i}! = {calcular_factorial(i)}")

    # Caso 4: desde- (ej: 5- → de 5 a 60)
    elif entrada.endswith("-"):
        inicio = int(entrada[:-1])
        for i in range(inicio, 61):
            print(f"{i}! = {calcular_factorial(i)}")


def main():
    # Si viene argumento por consola
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
    else:
        entrada = input("Ingrese un número o rango: ")

    procesar_entrada(entrada)


main()