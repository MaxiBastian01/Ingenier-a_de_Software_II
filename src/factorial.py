# factorial.py
import sys

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# 🔥 Entrada (argumento o teclado)
if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese un número o rango (ej: 4-8): ")


# 🔥 Procesar entrada
if "-" in entrada:
    partes = entrada.split("-")
    inicio = int(partes[0])
    fin = int(partes[1])

    for i in range(inicio, fin + 1):
        print(f"{i}! = {factorial(i)}")
else:
    num = int(entrada)
    print(f"{num}! = {factorial(num)}")