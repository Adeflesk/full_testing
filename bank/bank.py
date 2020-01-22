class Bank(object):
    def __init__(self):
        self._accounts = {}

    @property
    def accounts(self):
        return self._accounts

    def add_account(self, account):
        self._accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):
        return self.accounts.get(account_number)