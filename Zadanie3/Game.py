import random
import time

def generuj_plansze(wiersze, kolumny, liczba_przeszkod):
    """Tworzenie zarysu mapy"""
    plansza = [['#' if i == 0 or i == wiersze - 1 or j == 0 or j == kolumny - 1
                else ' ' for j in range(kolumny)] for i in range(wiersze)]

    """Wylosowanie pozycji startowej jak i mety (A,B), losujemy miejsce na pustym polu"""
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

    """Losujemy podobnie jak dla startu i mety (A,B), miejsce na przeszkodę (X)"""
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
        else:
            print('Nie poprawny ruch trafiłeś na przeszkodę lub granice mapys')
    return pozycja


if __name__ == "__main__":
    """Ustawienia gry, dostosowanie ilości wierszy, kolumn i liczby przeszkód
    oraz pętla gry,opiera się na sprawdzeniu czy gracz dotarł do mety jesli nie 
     przyjmuje kierunek gracza a nastepnie odpala funkcje wykonaj_ruch
     na sam koniec liczy czas"""
    wiersze = 10
    kolumny = 10
    liczba_przeszkod = 3
    start_gry = time.time()
    plansza, start, stop = generuj_plansze(wiersze, kolumny, liczba_przeszkod)

    pozycja_gracza = start
    wypisz_plansze(plansza)

    while pozycja_gracza != stop:
        ruch = input("Wybierz ruch (w, a, s, d): ").strip().lower()

        if ruch == 'w':
            pozycja_gracza = wykonaj_ruch(plansza, pozycja_gracza, (-1, 0))
        elif ruch == 's':
            pozycja_gracza = wykonaj_ruch(plansza, pozycja_gracza, (1, 0))
        elif ruch == 'a':
            pozycja_gracza = wykonaj_ruch(plansza, pozycja_gracza, (0, -1))
        elif ruch == 'd':
            pozycja_gracza = wykonaj_ruch(plansza, pozycja_gracza, (0, 1))
        else:
            print("Niepoprawny ruch. Spróbuj ponownie.")
            continue

        wypisz_plansze(plansza)
        koniec_gry = time.time()
        czas_trwania = koniec_gry - start_gry
        print(f"Pozycja gracza: {pozycja_gracza}")

    print("===========KONIEC GRY==============")
    print(f"Gra trwała: {czas_trwania:.2f} sekund.")
