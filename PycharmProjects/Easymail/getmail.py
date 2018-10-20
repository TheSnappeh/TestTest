import os

f_start = True
am_accs = 0


def check_accounts():
    check_path("C:\\Users\\Evan PC")
    accounts = open("Text.txt")
    content = accounts.readlines(1)
    if content != "":
        f_start = False
    else:
        add_accounts()


def add_accounts():
    print("First start detected. Please enter your details.")
    print("Enter your email ")
    email = input()
    accounts = open("Text.txt", "w")
    print("Enter your password")
    password = input()
    print("Are these details correct? email: " + str(email) + " pass: " + str(password))
    accounts.writelines("Email: " + email, am_accs * 2 + 2)
    accounts.writelines("Password: " + email, am_accs * 2 + 3)
    am_accs += 1


def check_path(input_string):
    os.chdir(input_string)
    if os.path.exists(input_string + "\\easymail"):
        os.chdir(input_string + "\\easymail")
    else:
        os.makedirs(input_string + "\\easymail")
        os.chdir(input_string + "\\easymail")


check_accounts()
add_accounts()
