import pyfiglet
import utils
from sys import exit
import auth as authFunctions
import globals

def main():
    choice = -1

    while choice == -1:
        utils.printBanner()
        print("""Welcome to the Bank of India Portal!

    1. Register
    2. Login
    3. Administrator Login
    0. Exit""", end="\n\n")
        choiceStr = input("Enter choice: ")

        try:
            choice = int(choiceStr)
        except:
            choice = -1
            utils.clear()
            continue

        if choice == 1:
            print("Registering...")
            authFunctions.signup()
        elif choice == 2:
            print("Signing in...")
            authFunctions.login()
        elif choice == 3:
            print("Administrator Login")
        elif choice == 0:
            sys.exit("Exiting...")
        else:
            print("Invalid choice, please try again!")
            utils.clear()

if __name__ == "__main__":
    main()
