# collatz.py
# Calcula, para cada número entre 1 y 10000,
# cuántas iteraciones tarda la secuencia de Collatz en llegar
# a una repetición (en este caso, cuando entra al ciclo 4 -> 2 -> 1).

import matplotlib.pyplot as plt


def collatz_iteraciones(n):
    iteraciones = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        iteraciones += 1

    return iteraciones


numeros_inicio = []
cant_iteraciones = []

for n in range(1, 10001):
    numeros_inicio.append(n)
    cant_iteraciones.append(collatz_iteraciones(n))


plt.figure(figsize=(10, 6))
plt.plot(cant_iteraciones, numeros_inicio)
plt.xlabel("Cantidad de iteraciones hasta llegar a 1")
plt.ylabel("Número inicial n")
plt.title("Conjetura de Collatz para números entre 1 y 10000")
plt.grid(True)
plt.show()