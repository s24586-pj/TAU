import pytest
import asyncio
from unittest.mock import AsyncMock
from Bank import Bank, Account, InsufficientFundsError


@pytest.fixture
def sample_account():
    """"Tworzenie fixture który będziie nam służył jako konto do testów"""
    return Account("s24586", "Krystian Jank", 100)


@pytest.fixture
def bank():
    return Bank()


def test_deposit(sample_account):
    """Testowanie poprawności wpłat."""
    sample_account.deposit(50.0)
    assert sample_account.balance == 150.0


def test_withdraw(sample_account):
    """Testowanie wypłat, w tym sytuacji, gdy saldo jest niewystarczające."""
    sample_account.withdraw(50.0)
    assert sample_account.balance == 50.0


def test_withdraw_insufficient_funds(sample_account):
    with pytest.raises(InsufficientFundsError):
        sample_account.withdraw(200.0)


@pytest.mark.asyncio(scope="function")
async def test_transfer():
    """"Testowanie transferów między kontami, w tym testowanie operacji asynchronicznych."""

    account1 = Account("666", "s21234", 100.0)
    account2 = Account("444", "s45354", 50.0)

    await account1.transfer(account2, 50.0)

    assert account1.balance == 50.0
    assert account2.balance == 100.0


def test_create_account(bank):
    """"Testowanie tworzenia konta."""
    bank.create_account("123", "Alice", 200.0)
    assert bank.get_account("123").balance == 200.0


def test_get_nonexistent_account(bank):
    """"Testowanie pobierania konta,złapanie błedu."""
    with pytest.raises(ValueError):
        bank.get_account("999")

def test_get_existent_account(bank):
    bank.create_account("s24586", "Krystian Jank", 100.0)
    account = bank.get_account("s24586")
    print(f"Numer konta: {account.account_number}, Właściciel: {account.owner}, balans: {account.balance}")
    assert account.owner == "Krystian Jank"
    assert account.balance == 100.0


@pytest.mark.asyncio(scope="function")
async def test_process_transaction(bank):
    """"Testowanie procesowania transakcji (z użyciem asynchronicznych funkcji).
        Sprawdzane jest, czy transakcja została oczekiwana dokładnie raz"""
    mock_transaction = AsyncMock()
    await bank.process_transaction(mock_transaction)
    mock_transaction.assert_awaited_once()


def test_deposit_negative_amount(sample_account):
    with pytest.raises(ValueError):
        sample_account.deposit(-100.0)
