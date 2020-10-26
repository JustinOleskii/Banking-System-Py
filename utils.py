import mysql.connector
import os

def dbConnect():
    connection = mysql.connector.connect(
        user='root',
        password='12345678',
        host='localhost',
        database='banking'
    )

    cursor = connection.cursor()
    return cursor, connection

def closeConnection():
    _, connection = dbConnect()
    connection.close()

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')