import random

def generuj_plansze(wiersze, kolumny, liczba_przeszkod):

    """Tworzenie zarysu mapy"""
    plansza = [['#' if i == 0 or i == wiersze - 1 or j == 0 or j == kolumny - 1
                else ' ' for j in range(kolumny)] for i in range(wiersze)]

    """Wylosowanie pozycji startowej jak i mety (A,B),losujemy miejce na pustym polu"""
    while True:
        start = (random.randint(1, wiersze - 2), random.randint(1, kolumny - 2))
        if plansza[start[0]][start[1]] == ' ':
            plansza[start[0]][start[1]] = 'A'
            break

    while True:
        stop = (random.randint(1, wiersze - 2), random.randint(1, kolumny - 2))
        if plansza[stop[0]][stop[1]] == ' ' and abs(stop[0] - start[0]) + abs(stop[1] - start[1]) > 1:
            plansza[stop[0]][stop[1]] = 'B'
            break

    """ Losujemy podobnie jak dla startu i mety (A,B),miejce na przeszkodę (X) """
    przeszkody = 0
    while przeszkody < liczba_przeszkod:
        wiersz, kolumna = random.randint(1, wiersze - 2), random.randint(1, kolumny - 2)
        if plansza[wiersz][kolumna] == ' ':
            plansza[wiersz][kolumna] = 'X'
            przeszkody += 1

    return plansza, start, stop


def wypisz_plansze(plansza):
    """Funkcja do wyprintowania planszy"""
    print("\n".join(" ".join(wiersz) for wiersz in plansza))
    print("\n")


if __name__ == "__main__":
    """Ustawienia gry,dostosowanie ilości wierszy kolumn i liczby przeszkod"""
    wiersze = 10
    kolumny = 50
    liczba_przeszkod = 70

    plansza, start, stop = generuj_plansze(wiersze, kolumny, liczba_przeszkod)

    wypisz_plansze(plansza)

