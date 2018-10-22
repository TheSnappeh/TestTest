import json, requests, smtplib

# PARAMETERS , LIST OF CRYPTO, CRYPTO, TAGGED CRYPTOS
currencies = [[], [], {}, []]


def read_api(name):
    api_url = "https://api.coinmarketcap.com/v1/ticker/{}/".format(name)
    response = requests.get(api_url)
    response_json = response.json()
    return response_json[0]


def setup():
    global currencies
    # Open text file and load into a data list (of dictionary).
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    #  Grab coin market cap information, and read into dictionary dic
    dic = read_api("bitcoin")

    # Check if there's any data. data[0] is PARAMETERS.
    if not data[0]:
        # Create new list of parameters.
        print("No parameters found. Getting appropriate information.")
        for parameters in dic:
            data[0].append(parameters)
    if not data[1]:
        # Create new list of crypto. TODO -> Grab a list of top 100.
        print("No list of crypto found.")
    if not data[2]:
        # Information of crypto hasn't been found.
        for crypto_currency in data[1]:
            data[2][crypto_currency] = {}
    currencies = data
    write_to()


def update_list():
    for name in currencies[2]:
        try:
            info = read_api(name)
            currencies[2][name] = info
        except:
            print("Failed to identify.")
    write_to()


def write_to():
    with open('data.json', 'w') as json_file:
        json.dump(currencies, json_file)


def send_mail(msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("cryptopython000@gmail.com", "theshow2")
        server.sendmail("cryptopython000@gmail.com", "evan.hofmann@hotmail.com",msg)
    except:
        print("Something went wrong.")



# Main loop
setup()
update_list()
print(currencies[2])
send_mail("Hello")
