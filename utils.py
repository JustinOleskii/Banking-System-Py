import mysql.connector
import os
from pyfiglet import figlet_format

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

def printBanner():
    ascii_banner = figlet_format("Bank of India")
    print(ascii_banner, end="\n\n")
