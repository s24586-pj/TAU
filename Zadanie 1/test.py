# WYMAGANIA Z ZAJĘC ODNOŚNIE TESTÓW:
# - 10 testów z różnymi danymi
# - obojętnie jaka funkcjonalność
# - wykorzystujące 3 różne asercje
# - Różne przypadki,Rzutowanie wartości (int, float), ujemne wartosci
# - język dowolny

import unittest
from main import *

class TestFunkcje(unittest.TestCase):

    def test_dodaj_liczby_dodatnie(self):
        wynik = dodaj(2, 3)
        print(f'Dodawanie liczb dodatnich: 2 + 3 = {wynik}')
        self.assertEqual(wynik, 5)

    def test_dodaj_liczby_ujemne(self):
        wynik = dodaj(-2, -3)
        print(f'Dodawanie liczb ujemnych: -2 + -3 = {wynik}')
        self.assertEqual(wynik, -5)

    def test_dodaj_zero(self):
        wynik = dodaj(0, 5)
        print(f'Dodawanie z zerem: 0 + 5 = {wynik}')
        self.assertEqual(wynik, 5)

    def test_czy_parzysta_true(self):
        liczba = 4
        wynik = czy_parzysta(liczba)
        print(f'Czy liczba {liczba} jest parzysta? {wynik}')
        self.assertTrue(wynik)

    def test_czy_parzysta_false(self):
        liczba = 5
        wynik = czy_parzysta(liczba)
        print(f'Czy liczba {liczba} jest parzysta? {wynik}')
        self.assertTrue(not wynik)

    def test_dziel_przez_liczbe_niezerowa(self):
        wynik = dziel(10, 2)
        print(f'Dzielenie: 10 / 2 = {wynik}')
        self.assertEqual(wynik, 5)

    def test_dziel_przez_zero(self):
        print(f'Próba dzielenia przez zero dla wartości: 10 / 0')
        with self.assertRaises(ValueError):
            dziel(10, 0)

    def test_dziel_liczby_ujemne(self):
        wynik = dziel(-10, 2)
        print(f'Dzielenie liczby ujemnej: -10 / 2 = {wynik}')
        self.assertEqual(wynik, -5)

    def test_dodaj_float_int(self):
        wynik = dodaj(2.5, 2)
        print(f'Dodawanie float i int: 2.5 + 2 = {wynik}')
        self.assertEqual(wynik, 4.5)

    def test_dodaj_duze_liczby(self):
        wynik = dodaj(10**18, 10**18)
        print(f'Dodawanie dużych liczb: 10^18 + 10^18 = {wynik}')
        self.assertEqual(wynik, 2 * 10**18)

    def test_dziel_float(self):
        wynik = dziel(7.5, 2.5)
        print(f'Dzielenie liczb float: 7.5 / 2.5 = {wynik}')
        self.assertEqual(wynik, 3.0)

    def test_dziel_mala_liczba(self):
        wynik = dziel(1, 3)
        print(f'Dzielenie: 1 / 3 = {wynik}')
        self.assertEqual(wynik, 1/3)

