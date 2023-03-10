from flask import Flask,request,jsonify
from web3 import Web3

node= 'Your node goes here'
web3 = Web3(Web3.HTTPProvider(node)) 

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to CodeWithJoe API"



@app.route("/blocknumber")
def blocknumber():
    return jsonify({"blocknumber": web3.eth.block_number})


@app.route("/nativeBalance/<address>")
def getBalance(address):
    return jsonify({"nativeBalance":web3.eth.get_balance(address) / 10**18})



@app.route("/getTransaction/<txHash>")
def getTransaction(txHash):
    transaction = web3.eth.get_transaction(txHash)
    transaction_dict = dict(transaction)

    # Convert bytes instances to hexadecimal string representations
    for key, value in transaction_dict.items():
        if isinstance(value, bytes):
            transaction_dict[key] = value.hex()

    return jsonify(transaction_dict)

if __name__ == '__main__':
    app.run(debug=True)
