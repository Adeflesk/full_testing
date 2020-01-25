"""This Module is to serve bank accounts on local hoset
"""
import os
import sys
FILE_DIR = os.path.dirname(__file__)
sys.path.append(FILE_DIR)

from bank import Bank
from flask import Flask, render_template, request  # pylint: disable=E0401

#from account import Account needed when cProfile is used below




APP = Flask(__name__, template_folder="templates")
APP.config.update(TESTING=True, EXPLAIN_TEMPLATE_LOADING=True)
BANK = Bank()


@APP.route("/")
def hello_world():
    """This calls the home page and renders it index.html
    """
    account_number = request.args.get("account_number")
    balance = BANK.get_account_balance(account_number)
    return render_template("index.html", balance=balance)


if __name__ == "__main__":
    #import cProfile

    # ACCOUNT = Account("1111", 50)
    #  BANK.add_account(ACCOUNT) needed to run cProfile
    #    cProfile.run("APP.run(debug=True)", sort="time")
    APP.run(debug=True)
