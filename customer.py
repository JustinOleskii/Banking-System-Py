import utils
import sys

def customerMenu(account):
    choice = 1

    while choice != 0:
        utils.clear()
        print("\n1. View Balance\n2. Deposit Money\n3. Transfer Money\n4. Close Account\n0. Logout\n\n")
        print('Card Number:', account.getCard())
        print("Enter choice: ", end=" ")

        try:
            choice = int(input())
        except:
            choice = 1
            utils.clear()
            continue

        if choice == 1:
            balance = account.getBalance()
            print(f"Your current balance is: {balance}")
        elif choice == 2:
            print("Deposit money")
            account.depositMoney()
        elif choice == 3:
            account.transferMoney()
        elif choice == 4:
            print("Close Account")
            account.closeAccount()
        elif choice == 0:
            print("Logout")
            pass
        else:
            print("Invalid choice!")
