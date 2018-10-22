import requests
import bs4
import json

""" Includes all the global variables used throughout the program.

    param_list: List of all the different parameters, like price of the coin, total supply, etc... (List)
    list_of_cryptos: Every coin/currency of which information will be gathered. (List)
    cryptos: The main dictionary which includes all the information. [#NAME_OF_COIN][#PARAMETER_OF_COIN]
"""

param_list = []
list_of_cryptos = ['bitcoin', 'ethereum', 'ripple', 'iota']
cryptos = {}

""" Quite evident, this function creates a dictionary inside the main dictionary (each coin individually).

    Takes a string (name), which is the name of a coin, as input, which will then create a dictionary of (name) in cryptos.
"""

def create_crypto(name):
    if name in cryptos:
        print("This crypto currency is already in your list.")
    else:
        cryptos[name] = cryptos.get("Example")


def delete_crypto(name):
    if name in cryptos:
        cryptos.pop(name)
    else:
        print("Sorry, this crypto currency isn't in your list.")


def list_crypto():
    for name in cryptos:
        print("{}: at a price of {} USD and {} BTC.".format(name, cryptos[name]["price_usd"], cryptos[name]["price_btc"]))

def update_crypto(name, param, value):
    if param in param_list:
        if name in cryptos:
            cryptos[name][param] = value
            print("Sorry, the parameter is not valid.")
        else:
            print("Creating crypto currency, since it hasn't been added yet.")
            create_crypto(name)
            update_crypto(name, param, value)
    else:
        print("Sorry, this parameter does not exist.")


def html_grab(name):
    api_url = "https://api.coinmarketcap.com/v1/ticker/{}/".format(name)
    response = requests.get(api_url)
    response_json = response.json()
    dic = response_json[0]

    for items in param_list:
        if items in dic:
            cryptos[name][items] = dic[items]


def setup():
    # CHECK IF THE FILE IS EMPTY, IF IT IS, WE HAVE TO GATHER INFO FIRST.
    json_file = open('data.json')
    data = json.load(json_file)
    if data[0]:
        print("Empty. Getting appropriate information.")
        api_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
        response = requests.get(api_url)
        response_json = response.json()
        dic = response_json[0]

        for parameters in dic:
            data[0].append(parameters)
        #  param_list.append(parameters)
        for crypto_currency in list_of_cryptos:
            create_crypto(crypto_currency)
            cryptos[crypto_currency] = {}




setup()
for x in list_of_cryptos:
    html_grab(x)
list_crypto()


