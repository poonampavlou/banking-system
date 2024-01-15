import random as rd


def pin_verification():
    while True:
        pin_check = input("\nPlease enter your pin to proceed: ")
        if pin_check != pin_number:
            print("That is incorrect, please try again")
            continue
        else:
            break
    print(f"\nYour pin has been successfully verified")
    return


print("Welcome to Pavlou Banking."
      "To proceed, please provide the following information: ")

while True:
    email_address = input("Please enter your email address: ")
    if "@" not in email_address or "." not in email_address:
        print("Please enter a valid email address")
        continue
    else:
        break

while True:
    phone_number = input("Please enter your phone number (please leave no spaces: ")
    if len(phone_number) != 11 or phone_number.isalpha():
        print("Please enter a valid phone number")
        continue
    else:
        break

while True:
    pin_number = input("Please enter your pin number: ")
    if len(pin_number) == 4 and pin_number.isdigit():
        print("You have successfully logged in!")
        break
    else:
        print("Your pin is not correct, please try again")
        continue

banking_dropdown = ["Checking Balance", "Transferring Funds", "Depositing Money", "Withdrawing Money", "Account Limit"]

while True:
    print("\nPlease select one of the following options:")
    for i in enumerate(banking_dropdown, start=1):
        print(i)
    try:
        user_selection = int(input("Please enter your selection (1 - 5) here or 0 to log off: "))
        if user_selection >= 0 and user_selection <= 5:
            break
        else:
            print("\nPlease enter a valid choice")
            continue
    except ValueError:
        print("\nPlease enter a valid choice")
        continue


if user_selection == 1:
    pin_verification()
    print(f"Your current balance is £{rd.randint(100, 99999)} and your savings balance is £{rd.randint(100, 99999)}")

elif user_selection == 2:
    current_balance = rd.randint(100, 99999)
    saving_balance = rd.randint(100, 99999)
    while True:
        try:
            funds_transfer_selection = int(input('''Select 1 if you are transferring from your current to your 
            savings account. Or press 2 if you are transferring from your savings account to your current 
            account: '''.rjust(10)))
            if funds_transfer_selection == 1 or funds_transfer_selection == 2:
                break
            else:
                print("\nPlease type either (option) 1 or 2 only:")
                continue
        except ValueError:
            print("\nPlease enter a valid choice")
            continue
    while True:
        try:
            transfer_amount = int(input("How much do you wish to transfer to your account: "))
            if transfer_amount < 0:
                print("We cannot action your request. Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number to transfer: ")
            continue

    if funds_transfer_selection == 1:
        if transfer_amount > current_balance:
            print(f"Unfortunately you cannot proceed. You wish to transfer £{transfer_amount} from your current account"
                  f" but you only have £{current_balance} available.")
        else:
            pin_verification()
            new_current_balance = current_balance + transfer_amount
            print(f"You had £{current_balance} in your account. Your new balance is £{new_current_balance}")

    if funds_transfer_selection == 2:
        if transfer_amount > saving_balance:
            print(f"Unfortunately you cannot proceed. You wish to transfer £{transfer_amount} from your savings account"
                  f" but you only have £{saving_balance} available.")
        else:
            pin_verification()
            new_saving_balance = saving_balance + transfer_amount
            print(f"You had £{saving_balance} in your account. Your new balance is £{new_saving_balance}")

elif user_selection == 3:
    current_balance = rd.randint(100, 99999)
    saving_balance = rd.randint(100, 99999)
    while True:
        try:
            funds_deposit_selection = int(
                input("Select 1 if you are depositing into your current account or 2 for your savings: "))
            if funds_deposit_selection == 1 or funds_deposit_selection == 2:
                break
            else:
                print("Please type either (option) 1 or 2 only:")
                continue
        except ValueError:
            print("Please enter a valid number to transfer: ")
            continue

    while True:
        try:
            deposit_amount = int(input("How much do you wish to deposit into your account: "))
            break
        except ValueError:
            print("Please enter a valid number to deposit: ")
            continue

    if funds_deposit_selection == 1:
        pin_verification()
        new_current_balance = current_balance + deposit_amount
        print(f"You had £{current_balance} in your account. Your new balance is £{new_current_balance}")

    elif funds_deposit_selection == 2:
        pin_verification()
        new_saving_balance = saving_balance + deposit_amount
        print(f"You had £{saving_balance} in your account. Your new balance is £{new_saving_balance}")


elif user_selection == 4:
    current_balance = rd.randint(100, 99999)
    saving_balance = rd.randint(100, 99999)
    while True:
        try:
            funds_withdraw_selection = int(input('''\nSelect 1 if you are withdrawing from your current account. 
            Or press 2 if you are withdrawing from your savings account: '''))
            if funds_withdraw_selection == 1 or funds_withdraw_selection == 2:
                break
            else:
                print("\nPlease type either (option) 1 or 2 only: ")
                continue
        except ValueError:
            print("\nPlease enter a valid number to withdraw: ")
            continue
    while True:
        try:
            withdraw_amount = int(input("How much do you wish to withdraw from your account: "))
            break
        except ValueError:
            print("Please enter a valid number to withdraw: ")
            continue

    if funds_withdraw_selection == 1:
        if withdraw_amount > current_balance:
            print(f"Unfortunately you cannot proceed. You wish to withdraw £{withdraw_amount} from your current account"
                  f" but you only have £{current_balance} available.")
        else:
            pin_verification()
            new_current_balance = current_balance - withdraw_amount
            print(f"You had £{current_balance} in your account. Your new balance is £{new_current_balance}")

    if funds_withdraw_selection == 2:
        if withdraw_amount > saving_balance:
            print(f"Unfortunately you cannot proceed. You wish to withdraw £{withdraw_amount} from your savings account"
                  f" but you only have £{saving_balance} available.")
        else:
            pin_verification()
            new_saving_balance = saving_balance - withdraw_amount
            print(f"You had £{saving_balance} in your account. Your new balance is £{new_saving_balance}")


elif user_selection == 5:
    pin_verification()
    limit = rd.randint(1000, 100000)
    print(f"Your account limit is £{round(limit, -3)}")


else:
    print("Logging off, goodbye!")
