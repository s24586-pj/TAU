import unittest
import time
from Game import generuj_plansze, wykonaj_ruch


class TestGry(unittest.TestCase):

    def test_generuj_plansze(self):
        wiersze = 10
        kolumny = 10
        liczba_przeszkod = 3
        plansza, start, stop = generuj_plansze(wiersze, kolumny, liczba_przeszkod)

        self.assertNotEqual(start, stop, "Pozycje startowa i końcowa powinny być różne.")

        self.assertTrue(0 <= start[0] < wiersze, "Pozycja startowa jest poza planszą.")
        self.assertTrue(0 <= start[1] < kolumny, "Pozycja startowa jest poza planszą.")
        self.assertTrue(0 <= stop[0] < wiersze, "Pozycja stopu jest poza planszą.")
        self.assertTrue(0 <= stop[1] < kolumny, "Pozycja stopu jest poza planszą.")

        przeszkody = sum(row.count('X') for row in plansza)
        self.assertEqual(przeszkody, liczba_przeszkod, f"Powinno być {liczba_przeszkod} przeszkód.")

    def test_plansza_zablokowana_przeszkodami(self):
        wiersze = 5
        kolumny = 5
        liczba_przeszkod = 26

        with self.assertRaises(ValueError):
            plansza, start, stop = generuj_plansze(wiersze, kolumny, liczba_przeszkod)
            print("Plansza:")
            for wiersz in plansza:
                print(" ".join(wiersz))

    def test_plansza_z_jednym_polem(self):
        """"Nie wiem czy to poprawny test, wygenerowało z jednym pustym polem jak oczekiwałem
         ale start i meta są ustawione w taki sposób ze nie da się tam dotrzeć
        """
        wiersze = 5
        kolumny = 5
        liczba_przeszkod = 6

        plansza, start, stop = generuj_plansze(wiersze, kolumny, liczba_przeszkod)
        print("Plansza:")
        for wiersz in plansza:
            print(" ".join(wiersz))

        puste_pola = sum(row.count(' ') for row in plansza)

        print(puste_pola)
        self.assertEqual(puste_pola, 1, "Wszystkie komórki oprócz startu i mety powinny być zajęte.")

        self.assertNotEqual(start, stop, "Start i meta nie mogą być w tym samym miejscu.")

        liczba_przeszkod = sum(row.count('X') for row in plansza)
        self.assertEqual(liczba_przeszkod, 6, f"Liczba przeszkód powinna wynosić 6, ale jest {liczba_przeszkod}.")

    def test_ruch_w_gore(self):
        plansza = [
            ['#', '#', '#', '#', '#'],
            ['#', ' ', 'X', ' ', '#'],
            ['#', ' ', 'A', ' ', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#'],
        ]
        start = (2, 2)
        pozycja_gracza = start

        print("Plansza przed ruchem:")
        for wiersz in plansza:
            print(" ".join(wiersz))

        nowa_pozycja = wykonaj_ruch(plansza, pozycja_gracza, (-1, 0))
        print("\nPlansza po ruchu w górę (na przeszkodę):")
        for wiersz in plansza:
            print(" ".join(wiersz))
        self.assertEqual(nowa_pozycja, pozycja_gracza, "Gracz wykonał nieprawidłowy ruch w górę na przeszkodę.")

        plansza[1][2] = ' '
        plansza[2][2] = 'A'
        pozycja_gracza = (2, 2)

        nowa_pozycja = wykonaj_ruch(plansza, pozycja_gracza, (-1, 0))
        print("\nPlansza po ruchu w górę (na puste pole):")
        for wiersz in plansza:
            print(" ".join(wiersz))
        self.assertNotEqual(nowa_pozycja, pozycja_gracza, "Gracz nie wykonał ruchu w górę na puste pole.")
        self.assertEqual(nowa_pozycja[0], pozycja_gracza[0] - 1, "Gracz nie przeszedł o 1 w górę na puste pole.")


    def test_ruch_w_dol(self):
        plansza = [
            ['#', '#', '#', '#', '#'],
            ['#', ' ', 'A', ' ', '#'],
            ['#', ' ', 'X', ' ', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#'],
        ]
        start = (1, 2)  # Początkowa pozycja gracza
        pozycja_gracza = start

        print("Plansza przed ruchem:")
        for wiersz in plansza:
            print(" ".join(wiersz))

        nowa_pozycja = wykonaj_ruch(plansza, pozycja_gracza, (1, 0))
        print("\nPlansza po ruchu w dół (na przeszkodę):")
        for wiersz in plansza:
            print(" ".join(wiersz))
        self.assertEqual(nowa_pozycja, pozycja_gracza, "Gracz wykonał nieprawidłowy ruch w dół na przeszkodę.")

        plansza[2][2] = ' '
        plansza[1][2] = 'A'
        pozycja_gracza = (1, 2)

        nowa_pozycja = wykonaj_ruch(plansza, pozycja_gracza, (1, 0))
        print("\nPlansza po ruchu w dół (na puste pole):")
        for wiersz in plansza:
            print(" ".join(wiersz))
        self.assertNotEqual(nowa_pozycja, pozycja_gracza, "Gracz nie wykonał ruchu w dół na puste pole.")
        self.assertEqual(nowa_pozycja[0], pozycja_gracza[0] + 1, "Gracz nie przeszedł o 1 w dół na puste pole.")

    def test_ruch_w_prawo(self):
        plansza = [
            ['#', '#', '#', '#', '#'],
            ['#', ' ', 'A', 'X', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#'],
        ]
        start = (1, 2)
        pozycja_gracza = start

        print("Plansza przed ruchem:")
        for wiersz in plansza:
            print(" ".join(wiersz))

        nowa_pozycja = wykonaj_ruch(plansza, pozycja_gracza, (0, 1))

        print("\nPlansza po ruchu w prawo:")
        for wiersz in plansza:
            print(" ".join(wiersz))
        self.assertEqual(nowa_pozycja, pozycja_gracza, "Gracz wykonał nieprawidłowy ruch w prawo na przeszkodę.")

        plansza[1][3] = ' '
        plansza[1][2] = ' '
        pozycja_gracza = (1, 2)
        plansza[1][2] = 'A'

        nowa_pozycja = wykonaj_ruch(plansza, pozycja_gracza, (0, 1))

        print("\nPlansza po ruchu w prawo na puste pole:")

        for wiersz in plansza:
            print(" ".join(wiersz))


        self.assertNotEqual(nowa_pozycja, pozycja_gracza, "Gracz nie wykonał ruchu w prawo na puste pole.")
        self.assertEqual(nowa_pozycja[1], pozycja_gracza[1] + 1, "Gracz nie przeszedł o 1 w prawo na puste pole.")

    def test_czas_trwania_gry(self):
        """Test sprawdzajacy czas trwania gry,zamockowana plansza aby moc wykonac sekwencje ruchów i dotrzec do mety"""
        start_gry = time.time()
        print('')
        plansza = [
            ['#', '#', '#', '#', '#'],
            ['#', 'A', ' ', ' ', '#'],
            ['#', ' ', 'X', ' ', '#'],
            ['#', ' ', ' ', 'B', '#'],
            ['#', '#', '#', '#', '#'],
        ]
        start = (1, 1)
        stop = (3, 3)
        pozycja_gracza = start

        ruchy = [(0, 1), (0, 1), (1, 0), (1, 0),(1, 0)]
        for ruch in ruchy:
            for wiersz in plansza:
                print(" ".join(wiersz))
            pozycja_gracza = wykonaj_ruch(plansza, pozycja_gracza, ruch)

        koniec_gry = time.time()
        czas_trwania = koniec_gry - start_gry
        print(czas_trwania)

        self.assertEqual(pozycja_gracza, stop, "Gracz nie dotarł do mety.")
        self.assertGreater(czas_trwania, 0, "Czas gry powinien być większy niż 0.")
        print(f"Czas gry wynosił: {czas_trwania:.6f} sekund.")

    if __name__ == "__main__":
        unittest.main()

