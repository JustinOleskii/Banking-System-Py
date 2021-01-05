import utils
import sys
import account

fn = account.reg()
balance = fn.getBalance()

def customerMenu():
    choice = 1

    while choice != 0:
        utils.clear()
        print("\n1. Register for Card\n2. Deposit Money\n3. Withdraw Money\n4. Transfer Money\n5. Print Statement\n6. Close Account\n7. Logout\n\n")
        print("Please note: You must register for a card before you are able to deposit, withdraw etc.\n")
        print(f"Balance: {balance}\n")
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
            print("Deposit money")
            fn.depositMoney()
        elif choice == 3:
            print("Withdraw Money")
        elif choice == 4:
            print("Transfer Money")
        elif choice == 5:
            print("Close Account")
        elif choice == 0:
            print("Logout")
            pass
        else:
            print("Invalid choice!")
            utils.clear()
