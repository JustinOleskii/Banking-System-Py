# Import Modules
import sys
import auth as authFunctions
import utils

def main():
    choice = 1

    ascii_banner = '''
██████╗  █████╗ ███╗   ██╗██╗  ██╗     ██████╗ ███████╗    ██╗███╗   ██╗██████╗ ██╗ █████╗ 
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ██╔═══██╗██╔════╝    ██║████╗  ██║██╔══██╗██║██╔══██╗
██████╔╝███████║██╔██╗ ██║█████╔╝     ██║   ██║█████╗      ██║██╔██╗ ██║██║  ██║██║███████║
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗     ██║   ██║██╔══╝      ██║██║╚██╗██║██║  ██║██║██╔══██║
██████╔╝██║  ██║██║ ╚████║██║  ██╗    ╚██████╔╝██║         ██║██║ ╚████║██████╔╝██║██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═════╝ ╚═╝         ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝
                                                                                           '''
    
    while choice != 0:
        print(ascii_banner)
        print("\nWelcome to the Bank of India Portal\n\n1. First Time User\n2. Returning User\n0. Exit\n\n")
        print("Enter Choice: ", end="")

        try:
            choice = int(input())
        except:
            choice = 1
            utils.clear()
            continue

        if choice == 1:
            print("Signing up")
            authFunctions.signUp()
        elif choice == 2:
            print("Signing in")
            authFunctions.login()
        elif choice == 0:
            sys.exit()
        else:
            print("Invalid Choice!")
            utils.clear()
main()