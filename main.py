# Import Modules
import pyfiglet
import sys
import signup as registrationFunctions

def main():
    choice = 1

    ascii_banner = pyfiglet.figlet_format("Bank  of  India")
    
    while choice != 0:
        registrationFunctions.clear()
        print(ascii_banner)
        print("\nWelcome to the Bank of India Portal\n\n1. First Time User\n2. Returning User\n3. Administrator Login\n0. Exit\n\n")
        print("Enter Choice: ", end="")

        try:
            choice = int(input())
        except:
            choice = 1
            registrationFunctions.clear()
            continue

        if choice == 1:
            print("Signing up")
            registrationFunctions.signUp()
        elif choice == 2:
            print("Signing in")
        elif choice == 3:
            print("Admin Login")
        elif choice == 0:
            sys.exit()
        else:
            print("Invalid Choice!")
            registrationFunctions.clear() 
        
main()

