import pytest

from src.account import Account
from src.savings_account import SavingsAccount
from src.account_manager import AccountManager


def test_deposit():
    # verificamos que un depósito aumente el saldo
    account = Account("fiona", "001", 1000)

    account.deposit(500)

    assert account.balance == 1500


def test_withdraw():
    # verificamos que un retiro disminuya el saldo
    account = Account("fiona", "001", 1000)

    account.withdraw(300)

    assert account.balance == 700


def test_withdraw_insufficient_balance():
    # verificamos que no se pueda retirar más dinero del disponible
    account = Account("fiona", "001", 1000)

    with pytest.raises(ValueError, match="saldo insuficiente"):
        account.withdraw(1500)


def test_savings_interest():
    # verificamos que se calcule correctamente el interés
    account = SavingsAccount("fiona", "002", 1000, 0.05)

    interest = account.add_interest()

    assert interest == 50
    assert account.balance == 1050


def test_savings_minimum_balance():
    # verificamos que la cuenta de ahorro mantenga el saldo mínimo
    account = SavingsAccount("fiona", "002", 1000)

    with pytest.raises(
        ValueError,
        match="la cuenta debe mantener un saldo mínimo de \\$100"
    ):
        account.withdraw(950)


def test_find_account():
    # verificamos que se pueda encontrar una cuenta por su número
    manager = AccountManager()
    account = Account("fiona", "001", 1000)

    manager.add_account(account)

    found_account = manager.find_account("001")

    assert found_account is account


def test_total_balance():
    # verificamos que se calcule correctamente el saldo total
    manager = AccountManager()

    account_1 = Account("fiona", "001", 1000)
    account_2 = Account("martina", "002", 1500)

    manager.add_account(account_1)
    manager.add_account(account_2)

    assert manager.get_total_balance() == 2500