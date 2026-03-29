# factorial_OOP.py
# Versión orientada a objetos del cálculo de factorial

import sys


class Factorial:

    def __init__(self):
        # Constructor (no necesita parámetros por ahora)
        pass

    def calcular(self, n):
        # Calcula el factorial de un número
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    def run(self, minimo, maximo):
        # Calcula factoriales entre minimo y maximo
        for i in range(minimo, maximo + 1):
            print(f"{i}! = {self.calcular(i)}")


def main():
    f = Factorial()

    # Si hay argumento
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
    else:
        entrada = input("Ingrese número o rango: ")

    # 🔥 mismos casos que antes

    if entrada.startswith("-"):
        hasta = int(entrada[1:])
        f.run(1, hasta)

    elif entrada.endswith("-"):
        desde = int(entrada[:-1])
        f.run(desde, 60)

    elif "-" in entrada:
        partes = entrada.split("-")
        desde = int(partes[0])
        hasta = int(partes[1])
        f.run(desde, hasta)

    else:
        num = int(entrada)
        f.run(num, num)


main()