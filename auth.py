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

    query = "select rowid,username,password from users"
    credentials = []
    cursor.execute(query)

    for x in cursor:
        credentials.append(x)

    loggedIn = False
    
    for i in range(len(credentials)):
        if username == credentials[i][1]:
            if password == credentials[i][2]:
                loggedIn = True
                print("Successfully logged in!")
                acc = account.reg(credentials[i][0])
            else:
                print("Invalid password")

    if loggedIn:
        customer.customerMenu(acc)
    else
        print("No such username exists!")
            
