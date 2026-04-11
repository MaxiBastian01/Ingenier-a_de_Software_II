import math


class RPNError(Exception):
    """Error específico de la calculadora RPN."""


def convertir_numero(token):
    """Convierte un token a int o float."""
    try:
        if "." in token:
            return float(token)
        return int(token)
    except ValueError as exc:
        raise RPNError(f"Token inválido: {token}") from exc


def sacar_uno(pila, mensaje="Pila insuficiente"):
    """Extrae un elemento de la pila o lanza RPNError."""
    if len(pila) < 1:
        raise RPNError(mensaje)
    return pila.pop()


def sacar_dos(pila, mensaje="Pila insuficiente para operar"):
    """Extrae dos elementos de la pila o lanza RPNError."""
    if len(pila) < 2:
        raise RPNError(mensaje)
    b = pila.pop()
    a = pila.pop()
    return a, b


def evaluar_rpn(expresion):
    pila = []
    memoria = [0] * 10  # posiciones 0 a 9
    tokens = expresion.split()

    for token in tokens:

        # COMANDOS DE PILA
        if token == "dup":
            if not pila:
                raise RPNError("Pila insuficiente para dup")
            pila.append(pila[-1])

        elif token == "swap":
            if len(pila) < 2:
                raise RPNError("Pila insuficiente para swap")
            pila[-1], pila[-2] = pila[-2], pila[-1]

        elif token == "drop":
            if not pila:
                raise RPNError("Pila insuficiente para drop")
            pila.pop()

        elif token == "clear":
            pila.clear()

        # FUNCIONES
        elif token == "sqrt":
            a = sacar_uno(pila)
            if a < 0:
                raise RPNError("Raíz negativa")
            pila.append(math.sqrt(a))

        elif token == "log":
            a = sacar_uno(pila)
            if a <= 0:
                raise RPNError("Log inválido")
            pila.append(math.log10(a))

        elif token == "ln":
            a = sacar_uno(pila)
            if a <= 0:
                raise RPNError("Ln inválido")
            pila.append(math.log(a))

        elif token == "ex":
            a = sacar_uno(pila)
            pila.append(math.exp(a))

        elif token == "10x":
            a = sacar_uno(pila)
            pila.append(10**a)

        elif token == "yx":
            a, b = sacar_dos(pila, "Pila insuficiente para yx")
            pila.append(a**b)

        elif token == "1/x":
            a = sacar_uno(pila)
            if a == 0:
                raise RPNError("División por cero")
            pila.append(1 / a)

        elif token == "CHS":
            a = sacar_uno(pila, "Pila insuficiente para CHS")
            pila.append(-a)

        # TRIGONOMÉTRICAS (GRADOS)
        elif token == "sin":
            a = sacar_uno(pila)
            pila.append(math.sin(math.radians(a)))

        elif token == "cos":
            a = sacar_uno(pila)
            pila.append(math.cos(math.radians(a)))

        elif token == "tg":
            a = sacar_uno(pila)
            pila.append(math.tan(math.radians(a)))

        elif token == "asin":
            a = sacar_uno(pila)
            pila.append(math.degrees(math.asin(a)))

        elif token == "acos":
            a = sacar_uno(pila)
            pila.append(math.degrees(math.acos(a)))

        elif token == "atg":
            a = sacar_uno(pila)
            pila.append(math.degrees(math.atan(a)))

        # MEMORIAS
        elif token == "STO":
            if len(pila) < 2:
                raise RPNError("Pila insuficiente para STO")
            idx = int(pila.pop())
            val = pila.pop()
            if not 0 <= idx <= 9:
                raise RPNError("Memoria inválida")
            memoria[idx] = val

        elif token == "RCL":
            idx = sacar_uno(pila, "Pila insuficiente para RCL")
            idx = int(idx)
            if not 0 <= idx <= 9:
                raise RPNError("Memoria inválida")
            pila.append(memoria[idx])

        # OPERACIONES
        elif token in {"+", "-", "*", "/"}:
            a, b = sacar_dos(pila, "Pila insuficiente para operar")

            if token == "+":
                pila.append(a + b)
            elif token == "-":
                pila.append(a - b)
            elif token == "*":
                pila.append(a * b)
            elif token == "/":
                if b == 0:
                    raise RPNError("División por cero")
                pila.append(a / b)

        # CONSTANTES
        elif token == "p":
            pila.append(math.pi)

        elif token == "e":
            pila.append(math.e)

        elif token == "j":
            pila.append((1 + 5**0.5) / 2)

        # NÚMEROS
        else:
            pila.append(convertir_numero(token))

    if len(pila) != 1:
        raise RPNError("Resultado inválido")

    return pila[0]


def main():
    expresion = input("Ingrese una expresión RPN: ")
    try:
        resultado = evaluar_rpn(expresion)
        print("Resultado:", resultado)
    except RPNError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
