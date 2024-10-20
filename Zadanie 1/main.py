def dodaj(a, b):
    return a + b

def czy_parzysta(n):
    return n % 2 == 0

def dziel(a, b):
    if b == 0:
        raise ValueError("Dzielenie przez zero jest niedozwolone")
    return a / b