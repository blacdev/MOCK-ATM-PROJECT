import random, time, sys
from babel import numbers





def database_listing():
    w = list()
    k = list()

    for p_id, p_info in user_database.items():

        for key in p_info:
            w.append(key)
            k.append(p_info[key])

    return k





def login():
    global p # used to take password out

    acc = input("Please your account number?\n")
    password = input("Please enter your password?\n")
    p = password

    L = database_listing()

    if acc and password in L:

        allowed_acc = L.index(acc)
        allowed_password = L.index(password)
        # c = ""
        Account_name = L[allowed_password - 1]
        print("welcome", Account_name)
        time.sleep(2)
        banking_Operation()

    #checks if account number already exist in database
    elif acc in L:
        print("Password or Username Incorrect. Try to login again")

    else:
        print("User does not exist. Register account")


    return False




def get_Password(): # returns password
    return p





def banking_Operation():

    print("What will you be doing today?")
    print("Press 1 to withdraw")
    print("Press 2 to deposit cash")
    print("Press 3 to lodge a complaint")
    print("Press 4 to logout")

    select_Operation = int(input("please select an option:\n"))

    if select_Operation == 1:

        time.sleep(1)
        withdrawal_amount = int(input("How much would you like to withdraw?\n"))

        time.sleep(3)
        print("please take your cash")

    if select_Operation == 2:
        print("Loading...")
        time.sleep(2)
        deposit_amount = int(input("How much would you like to deposit?\n"))
        L = database_listing()
        F = get_Password()
        balance_allowed_users = L[L.index(F) + 1]
        balance = deposit_amount + int(balance_allowed_users)
        babell = str(numbers.format_currency(balance, 'NGN', locale = "en_NG"))
        time.sleep(2)

        print("your balance is",babell[0:1],babell[1:])
        time.sleep(1)
        print("Thank you for banking wiht us.")
        time.sleep(1)

    if select_Operation == 3:

        time.sleep(1)
        comp_laint = input("Enter your complaint\n")
        time.sleep(1)
        print("Thank you for your feedback")

    if select_Operation == 4:
        print("Thank you for banking with us")
        time.sleep(3)
        return False





def register():

    print("Please fill the following to create an account")

    name = input("Please enter your name\n")
    d = 0

    if name.isalpha()== False:
        return True
    else:
        password = input("Please enter your password\n")
        s = ['1','2','3','4','5','6','7','8','9','0']
        w = list()
        c = ""
        random.shuffle(s)
        Account_num =c.join(s)

        for d,v in user_database.items():
            w.append(d)

        if d not in w:
            user_database[d] = {"account":Account_num,"name":name, "password":password, "balance_allowed_users":0}


            print("Saving your details...")
            time.sleep(3)
            print("Your account number is")
            print(Account_num)
            print("Please copy your account number")
            time.sleep(1)
            Y = ['Y','y',"Yes","yes", 'YES']
            N = ['N', 'n', 'No','no', 'NO']

            In = input("Would you like to login to your account?(Y/N)\n")

            if In in Y:
                return True
            elif In in N:
                return False
            else:
                return False
        elif d in w:
            user_database[d+1] = {"account":Account_num,"name":name, "password":password, "balance_allowed_users":0}


            print("Saving your details...")
            time.sleep(3)
            print("Your account number is")
            print(Account_num)
            print("Please copy your account number")
            time.sleep(1)
            Y = ['Y','y',"Yes","yes", 'YES']
            N = ['N', 'n', 'No','no', 'NO']

            In = input("Would you like to login to your account?(Y/N)\n")

            if In in Y:
                return True
            elif In in N:
                return False
            else:
                return False


user_database = {}

while(1):

    print("Welcome. What would you like to do today?\n")
    time.sleep(2)
    print("1. to login")
    print("2. to register")

    entered_num = input("please select a number:\n")
    failed = 0

    print("Loading...")
    time.sleep(2)

    if entered_num == "1":
        Log_in = False

        while Log_in == False:
            Log_in = login()


            if Log_in == False:
                break
            else:
                banking_Operation()
            break



    elif entered_num == "2":
        Reg_ister = False

        while Reg_ister == False:
            Reg_ister = register()

            if Reg_ister == False:
                break

            elif Reg_ister == True:
                login()

            else:
                continue

    else:
        print("Login failed, username or password incorrect")
