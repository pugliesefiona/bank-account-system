from src.account import Account


# creamos dos cuentas para probar las funcionalidades de la clase
account_1 = Account("fiona", "001", 1000)
account_2 = Account("martina", "002", 1500)


# mostramos la información de cada cuenta
print(account_1)
print(account_2)


# usamos __getitem__ para acceder al saldo usando []
print(f"saldo de account_1: ${account_1['balance']:.2f}")

# también podemos acceder al nombre del titular de la misma forma
print(f"titular de account_2: {account_2['owner']}")


# usamos __add__ para sumar los saldos de las dos cuentas
print(f"suma de saldos: ${account_1 + account_2:.2f}")

# usamos __lt__ para comparar los saldos de las dos cuentas
print(f"account_1 tiene menos saldo que account_2: {account_1 < account_2}")


# consultamos cuántas cuentas se crearon usando el class method
print(f"cuentas creadas: {Account.get_account_count()}")


# probamos qué pasa cuando intentamos retirar más dinero del disponible
try:
    account_1.withdraw(2000)

except ValueError as error:
    print(f"error: {error}")


# probamos qué pasa cuando intentamos hacer un depósito inválido
try:
    account_1.deposit(-100)

except ValueError as error:
    print(f"error: {error}")