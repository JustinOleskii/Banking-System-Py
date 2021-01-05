import mysql.connector
import os
import time
import customer
import utils
import account

fn = account.reg()

def signUp():
    cursor, connection = utils.dbConnect()
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    address = input("Enter address: ")
    panID = input("Enter PAN ID: ")
    aadhaarID = input("Enter Aadhaar ID: ")

    try:
        query = "INSERT INTO users (FirstName, LastName, Username, Password, Address, PAN, Aadhaar) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        value = (firstName, lastName, username, password, address, panID, aadhaarID)
        cursor.execute(query, value)
        connection.commit()
        print("Proceeding to card creation...\n\n\n")
        fn.createCard()
        time.sleep(5)
        utils.clear()
    except mysql.connector.IntegrityError:
        print("Username is already in use!\n\n")
        connection.rollback()
        time.sleep(5)
        utils.clear()
    except:
        if len(panID) > 10:
            print("Invalid PAN ID!")
        elif len(aadhaarID) > 12:
            print("Invalid Aadhaar ID!")
        connection.rollback()
        utils.clear()

def login():
    cursor, _ = utils.dbConnect()
    username = input("Enter username: ")
    password = input("Enter password: ")

    query = "select * from users"
    credentials = []
    cursor.execute(query)

    for x in cursor:
        credentials.append(x)
    
    for i in range(len(credentials)):
        if username == credentials[i][2]:
            if password == credentials[i][3]:
                print("Successfully logged in!")
                customer.customerMenu()
            else:
                print("Invalid password")
        else:
            print("No such username exists!")
            