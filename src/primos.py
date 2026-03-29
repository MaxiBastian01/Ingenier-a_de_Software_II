# primos.py

def es_primo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print("Numeros primos del 1 al 100:")

for num in range(1, 101):
    if es_primo(num):
        print(num, end=" ")
