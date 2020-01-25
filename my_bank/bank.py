"""Bank is an object to represent a bank
"""


class Bank:
    """ Bank is an object to represent a bank which holds
        Accounts
    """

    def __init__(self):
        self._accounts = {}

    @property
    def accounts(self):
        """Returns the private dictionary of accounts
        """
        return self._accounts

    def add_account(self, account):
        """ Setter method to add accounts to the account dictionary
        """
        print("creating an account")
        self._accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):
        """ Public interface to find account by number (keyword)
            in dictionary
        """

        return self.accounts.get(account_number)
