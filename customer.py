import utils
import sys

def customerMenu(account):
    choice = 1

    while choice != 0:
        utils.clear()
        print(f"1. Deposit Money\n2. Transfer Money\n3. Close Account\n0. Logout\n\n\nCard Number: {account.getCard()}\nBalance: {account.getBalance()}")
        print("Enter choice: ", end=" ")

        try:
            choice = int(input())
        except:
            choice = 1
            utils.clear()
            continue

        if choice == 1:
            print("Deposit money")
            account.depositMoney()
        elif choice == 2:
            account.transferMoney()
        elif choice == 3:
            print("Close Account")
            account.closeAccount()
            pass
        elif choice == 0:
            print("Logout")
            pass
        else:
            print("Invalid choice!")