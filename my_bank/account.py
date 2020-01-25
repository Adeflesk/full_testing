""" Class Account is to represent a bank account
"""


class Account:
    """ set up with an account number and balance
        a = Account("1111',50)
    """

    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        """ getter method to return the private variable 
            .account_number
        """
        return self._account_number

    @property
    def balance(self):
        """ geter method to return the private variable
            ._balance
        """
        return self._balance
