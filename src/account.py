class Account:
    # contador general para saber cuántas cuentas se crearon
    _account_count = 0

    def __init__(self, owner_name, account_number, balance=0):
        # guardamos los datos básicos de la cuenta
        self.owner_name = owner_name
        self.account_number = account_number

        # usamos _balance para indicar que es un atributo interno
        self._balance = balance

        # cada vez que se crea una cuenta, aumentamos el contador
        Account._account_count += 1

    @property
    def balance(self):
        # permite consultar el saldo sin acceder directamente a _balance
        return self._balance

    def deposit(self, amount):
        # no permitimos depósitos de cero o valores negativos
        if amount <= 0:
            raise ValueError("el monto a depositar debe ser mayor que cero")

        # sumamos el monto al saldo actual
        self._balance += amount

    def withdraw(self, amount):
        # no permitimos retiros de cero o valores negativos
        if amount <= 0:
            raise ValueError("el monto a retirar debe ser mayor que cero")

        # verificamos que haya suficiente saldo para retirar
        if amount > self._balance:
            raise ValueError("saldo insuficiente")

        # restamos el monto del saldo
        self._balance -= amount

    def show_balance(self):
        # devuelve el saldo con un formato más fácil de leer
        return f"saldo: ${self._balance:.2f}"

    @classmethod
    def get_account_count(cls):
        # devuelve la cantidad total de cuentas creadas
        return cls._account_count

    def __str__(self):
        # define cómo se muestra la cuenta cuando usamos print()
        return (
            f"cuenta {self.account_number} - "
            f"titular: {self.owner_name} - "
            f"saldo: ${self._balance:.2f}"
        )

    def __add__(self, other):
        # permite sumar los saldos de dos cuentas
        if not isinstance(other, Account):
            return NotImplemented

        return self._balance + other._balance

    def __lt__(self, other):
        # permite comparar los saldos de dos cuentas
        if not isinstance(other, Account):
            return NotImplemented

        return self._balance < other._balance

    def __getitem__(self, key):
        # permite acceder a algunos datos de la cuenta usando []
        data = {
            "owner": self.owner_name,
            "account_number": self.account_number,
            "balance": self._balance
        }

        return data[key]