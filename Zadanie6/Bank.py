import asyncio
from typing import Dict


class InsufficientFundsError(Exception):
    pass


class Account:
    """"
        Klasa konta która zawiera pola takie jak:
        -saldo konta
        -numer konta
        -właściciel konta

        Oraz metody:
        - Wpłata na konto (wartość wpłaty musi być wieksza od zera)
        - Wypłata z konta (wartość wypłaty musi być mniejsza niż aktualne środki)
        - Przeniesienie środków na inne konta (podobnie jak z wypłata środków tylko że operacja przelewu jest wykonywana
        asynchronicznie (await asyncio.sleep(1))

        """
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Wartość wpłaty musi wynosić więcej niż 0!!")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError  ("Niewystarczające środki na koncie!")
        self.balance -= amount

    async def transfer(self, to_account: 'Account', amount: float):
        if amount > self.balance:
            raise InsufficientFundsError ("Niewystarczające środki na koncie!")
        await asyncio.sleep(1)
        self.withdraw(amount)
        to_account.deposit(amount)


class Bank:
    """"
        Klasa Banku która zawiera pola takie jak:
        -Accounts przechowywany (jako dict,klucz wartosc)

        Oraz metody:
        - Utworzenie konta
        - Znalezienie konta na podstawie numeru konta.
        - Pzeprowadzenie tranzakcji używa asynchronicznych operacji

        """
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def create_account(self, account_number: str, owner: str, initial_balance: float = 0.0):
        if account_number in self.accounts:
            raise ValueError("Konto już istnieje.")
        self.accounts[account_number] = Account(account_number, owner, initial_balance)

    def get_account(self, account_number: str) -> Account:
        if account_number not in self.accounts:
            raise ValueError("Nie znaleziono konta")
        return self.accounts[account_number]

    async def process_transaction(self, transaction_function):
        await transaction_function()


