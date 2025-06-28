# contador.py

def es_par(numero):
    """
    Determina si un número es par o impar.
    Devuelve un string: 'par' o 'impar'.
    """
    return "par" if numero % 2 == 0 else "impar"

def cuenta_regresiva(n):
    """
    Función recursiva que imprime los números desde n hasta 0,
    indicando si cada número es par o impar.
    """
    if n < 0:
        return
    print(f"{n} - {es_par(n)}")
    cuenta_regresiva(n - 1)
