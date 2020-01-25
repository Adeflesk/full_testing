from flask import Flask, render_template, request
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from bank import Bank


app = Flask(__name__,template_folder='templates')
app.config.update(
   TESTING=True,
   EXPLAIN_TEMPLATE_LOADING=True
)
BANK = Bank()


@app.route("/")
def hello_world():
    #return 'Hello World!'
    account_number = request.args.get('account_number')
    balance = BANK.get_account_balance(account_number)
    return render_template('index.html', balance=balance)


if __name__ == "__main__":
    app.run(debug=True)
