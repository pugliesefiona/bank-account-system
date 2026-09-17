from src.account import Account


class AccountManager:
    def __init__(self):
        # guardamos todas las cuentas administradas
        self.accounts = []

    def add_account(self, account):
        # verificamos que el objeto sea una cuenta
        if not isinstance(account, Account):
            raise TypeError("solo se pueden agregar cuentas")

        # agregamos la cuenta a la lista
        self.accounts.append(account)

    def find_account(self, account_number):
        # buscamos una cuenta por su número
        for account in self.accounts:
            if account.account_number == account_number:
                return account

        # si no encontramos la cuenta, devolvemos None
        return None

    def remove_account(self, account_number):
        # buscamos la cuenta que queremos eliminar
        account = self.find_account(account_number)

        if account is None:
            raise ValueError("cuenta no encontrada")

        # eliminamos la cuenta de la lista
        self.accounts.remove(account)

    def get_total_balance(self):
        # sumamos los saldos de todas las cuentas
        return sum(account.balance for account in self.accounts)