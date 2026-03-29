# factorial.py
import sys

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# 🔥 Acá está la modificación
if len(sys.argv) > 1:
    num = int(sys.argv[1])
else:
    num = int(input("Ingrese un número: "))

print(f"{num}! = {factorial(num)}")