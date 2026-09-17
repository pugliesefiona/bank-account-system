from src.account import Account


class SavingsAccount(Account):
    def __init__(self, owner_name, account_number, balance=0, interest_rate=0.02):
        # usamos el constructor de Account para los datos básicos
        super().__init__(owner_name, account_number, balance)

        # guardamos la tasa de interés propia de la cuenta de ahorro
        self.interest_rate = interest_rate

    def add_interest(self):
        # calculamos el interés usando el saldo actual
        interest = self._balance * self.interest_rate

        # agregamos el interés al saldo
        self._balance += interest

        return interest

    def withdraw(self, amount):
        # una cuenta de ahorro mantiene un saldo mínimo de 100
        if amount <= 0:
            raise ValueError("el monto a retirar debe ser mayor que cero")

        if self._balance - amount < 100:
            raise ValueError("la cuenta debe mantener un saldo mínimo de $100")

        self._balance -= amount