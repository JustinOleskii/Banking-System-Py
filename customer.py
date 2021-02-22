import utils
import sys
import account

fn = account.reg()
def customerMenu():
    choice = 1

    while choice != 0:
        utils.clear()
        print("\n1. Register for Card\n2. View Balance\n3. Deposit Money\n4. Transfer Money\n5. Close Account\n0. Logout\n\n")
        print("Please note: You must register for a card before you are able to deposit, withdraw etc.\n")
        print('Card Number:', fn.getCard())
        print("Enter choice: ", end=" ")

        try:
            choice = int(input())
        except:
            choice = 1
            utils.clear()
            continue

        if choice == 1:
            print("Register for Card")
            fn.createCard()
        elif choice == 2:
            fn.getBalance()
        elif choice == 3:
            print("Deposit money")
            fn.depositMoney()
        elif choice == 4:
            fn.transferMoney()
        elif choice == 5:
            print("Close Account")
        elif choice == 0:
            print("Logout")
            pass
        else:
            print("Invalid choice!")
