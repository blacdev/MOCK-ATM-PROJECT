import time,sys
from babel import numbers

wrong_password = 0


allowed_users = ['seye', 'ryan', 'hakeem']
allowed_password = ['pseye', 'pryan', 'phakeem']
allowed_input = [1, 2, 3]
balance_allowed_users = [0, 0, 0]

while (1):
    username = input("What is your name? \n")

    if (username not in allowed_users):
        time.sleep(.5)
        print("Name does not exist. please try again.")
        time.sleep(.5)
        continue

    else:
        allowed_users_position = allowed_users.index(username)
        password = input("Please enter your password")
        if password != allowed_password[allowed_users_position]:
            print("Wrong password")
            wrong_password += 1
            if wrong_password == 5:
                sys.exit("wrong password. pleases try again later")


        else:
            print( "Logging in...")
            time.sleep(2)
            print("welcome %s" % username)
            time.sleep(2)
            print("These are the available options:")
            print("1. Withdrawal")
            print("2. Deposit")
            print("3. Complaint")

            selection = int(input("Enter a number\n"))
            if selection not in allowed_input:
                print("wrong entry")
                time.sleep(.5)
                continue

            elif selection == 1:
                time.sleep(1)
                withdrawal_amount = int(input("How much would you like to withdraw?"))
                time.sleep(3)
                print("please take your cash")

            elif selection == 2:
                time.sleep(1)
                deposit_amount = int(input("How much would you like to deposit?"))
                balance = deposit_amount + balance_allowed_users[allowed_users_position]
                babell = str(numbers.format_currency(balance, 'NGN', locale = "en_NG"))
                print(babell, "sh")
                time.sleep(2)
                print("your balance is",babell[0:1],babell[1:])

            elif selection == 3:
                time.sleep(1)
                comp_laint = input("Enter your complaint")
                time.sleep(1)
                print("Thank you for your feedback")
