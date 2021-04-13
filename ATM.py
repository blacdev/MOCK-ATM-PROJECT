# register
# -supply username
# - generate user id

#Login
# - (account number or email) and pasword

# banking operations

# Initializing the system
import random, time
from babel import numbers

database = {}

def init():
    print("welcome to bank OOO")
    isValidOption = False
    while isValidOption == False:

        existingUser = int(input("Do you have an account with us:\n 1. (yes)\n 2. (no)\n"))

        if (existingUser == 1):
            isValidOption = True
            login()

        elif existingUser == 2:
            isValidOption = True
            register()
            if register() == False:
                print("Thank you for opening an account with us today")
                init()
            else:
                login()
        else:
            print("You have selected an invalid option")



def login():
    print("Login to your account")
    loginError = 0
    isLoginSuccesful = False

    while loginError < 4:
        loginError += 1
        accountNumberFromUser = int(input("Please enter your account number\n"))
        userPassword = input("Please enter your password\n")
        for accountNumber, userDetails in database.items():

            if (accountNumber == accountNumberFromUser) and (userDetails[4] == userPassword):
                isLoginSuccesful = True
                bankingOperation(userDetails)



    forgotPassword()



def register():
    Y = ['Y','y',"Yes","yes", 'YES']
    N = ['N', 'n', 'No','no', 'NO']
    print("Input in your details to register")
    Fname = input("Please enter your first name:\n")
    Lname = input("Please enter your last name:\n")
    userName = input("What would you like to use as your username?\n")
    email = input("What is your email address?\n")
    password = input("Please enter your preferred password\n")
    accountNumber = generateAccountNumber()
    bank_bal = 0

    database[accountNumber] = [Fname, Lname, userName, email, password, bank_bal]
    print("Saving your details...")
    time.sleep(3)
    print("Your account has been created")
    print("Your account number is", accountNumber)
    print("Please copy your account number")
    time.sleep(2)

    askToLogin = input("Would you like to login to your account?(Yes/No)\n")

    if askToLogin in Y:
        login()
    elif askToLogin in N:
        init()

def bankingOperation(user):
    print("welcome %s %s" % (user[0], user[1]))
    time.sleep(1)

    print("What will you be doing today?")
    time.sleep(1)
    print("Press 1 to check balance")
    print("Press 2 to withdraw")
    print("Press 3 to deposit cash")
    print("Press 4 to lodge a complaint")
    print("Press 5 to logout")
    print("Press 6 to exit")

    select_Operation = int(input("please select an option:\n"))

    if select_Operation == 1:
        balance(user)

    elif select_Operation == 2:
        withdrawalOperation(user)


    elif select_Operation == 3:
        depositOperation(user)

    elif select_Operation == 4:
        Complaint(user)

    elif select_Operation == 5:
        Logout()

    elif select_Operation == 6:
        exit()


def withdrawalOperation(user):
    time.sleep(1)
    withdrawal_amount = int(input("How much would you like to withdraw?\n"))

    time.sleep(3)
    print("please take your cash")
    bankingOperation(user)


def depositOperation(user):
    print("Loading...")
    time.sleep(2)
    deposit_amount = int(input("How much would you like to deposit?\n"))
    balance_allowed_users = user[5]
    balance = deposit_amount + int(balance_allowed_users)
    babell = str(numbers.format_currency(balance, 'NGN', locale = "en_NG"))
    time.sleep(2)

    print("Thank you for banking with us", user[0] + ".")
    time.sleep(1)
    bankingOperation(user)

def Complaint(user):
    time.sleep(1)
    comp_laint = input("Enter your complaint\n")
    time.sleep(1)
    print("Thank you for your feedback")
    bankingOperation(user)

def balance(user):
    print("Your balance is ", user[5])
    bankingOperation(user)

def Logout():
    print("Thank you for banking with us")
    time.sleep(3)
    login()

def forgotPassword():
    print("invalid user")
    time.sleep(2)
    forgotPasswordOption = int(input("Please press \n1. to use 'Forgot Password'\n2. to go back to login page\n"))

    if (forgotPasswordOption == 1):
        forgotPassword()
    elif (forgotPasswordOption == 2):
        login()
    else:
        init()

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)




init()
