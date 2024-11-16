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

def wykonaj_ruch(plansza, pozycja, ruch):
    """Funkcja przyjmuje 3 parametry plansze,pozycje graczaa i ruch w dany kierunek
        sprawdza czy ruch nie powoduje kolizje ze ścianą # albo z przeszkodą X, jeśli oba warunki przechodzą
        Zmienia A na nowe pole a starą pozycje zamienia na puste pole
    """
    x, y = pozycja
    dx, dy = ruch

    nowy_x, nowy_y = x + dx, y + dy

    if 0 <= nowy_x < len(plansza) and 0 <= nowy_y < len(plansza[0]):
        if plansza[nowy_x][nowy_y] not in ('#', 'X'):
            plansza[x][y] = ' '
            plansza[nowy_x][nowy_y] = 'A'
            return nowy_x, nowy_y
    return pozycja


if __name__ == "__main__":
    """Ustawienia gry, dostosowanie ilości wierszy, kolumn i liczby przeszkód"""
    wiersze = 10
    kolumny = 50
    liczba_przeszkod = 70

    plansza, start, stop = generuj_plansze(wiersze, kolumny, liczba_przeszkod)

    wypisz_plansze(plansza)

    pozycja_gracza = start

    pozycja_gracza = wykonaj_ruch(plansza, pozycja_gracza, (0, 1)  )

    wypisz_plansze(plansza)
    print(f"Nowa pozycja : {pozycja_gracza}")


