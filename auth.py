from mysql.connector import IntegrityError
import os
import time
import customer
import utils
from account import Account
from getpass import getpass
import globals

def signup():
    cursor, connection = utils.dbConnect()

    utils.printBanner()
    print("Please enter the following information to register for an account.")
    firstName = input("First name: ")
    lastName = input("Last name: ")
    username = input("Username: ")
    password = getpass()
    address = input("Address: ")
    panID = input("PAN ID:")
    aadhaarID = input("Adhaar ID: ")

    try:
        query = "INSERT INTO users (FirstName, LastName, Username, Password, Address, PAN, Aadhaar) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        value = (firstName, lastName, username, password, address, panID, aadhaarID)
        cursor.execute(query, value)
        connection.commit()
        print("Proceeding to card creation...", end="\n\n")
        time.sleep(5)
        utils.clear()

        utils.printBanner()
    except IntegrityError:
        print("Username is already in use!", end="\n\n")
        connection.rollback()
        time.sleep(5)
        utils.clear()
    except:
        if len(panID) > 10:
            print("Invalid PAN ID!")
        elif len(aadhaarID) > 12:
            print("Invalid Aadhaar ID!")
        time.sleep(5)
        connection.rollback()
        utils.clear()

def login():
    cursor, _ = utils.dbConnect()

    utils.printBanner()
    username = input("Username: ")
    password = getpass()

    query = "SELECT * FROM users WHERE username = %s"
    results = [ ]
    cursor.execute(query)

    for x in cursor:
        results.append(x)

    if len(results) <= 0:
        print("No such username exists!")
        time.sleep(5)
        utils.clear()
        login()
    else:
        for i in range(len(credentials)):
            if username === credentials[i][2]:
                if password === credentials[i][3]:
                    print("Successfully logged in!")
                    customer.customerMenu()
                else:
                    print("Invalid password...")
