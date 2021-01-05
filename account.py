import random
import mysql.connector
import utils

accountLog = open('acLog.txt', 'w')

class reg:
    def __init__(self):
        self.FirstName = None
        self.LastName = None
        self.cardNo = None
        self.pin = None
        self.balance = 0
    
    def createCard(self):
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        pin = int(input("Enter 4 digit PIN: "))
        bal = float(input("Enter starting balance: (min 500)"))
        self.FirstName = firstName
        self.LastName = lastName
        self.pin = pin
        self.cardNo = '400000' + "".join([str(random.randrange(10)) for i in range(9)])
        self.cardNo = self.luhnAlgo(self.cardNo, 1)
        self.balance = bal
        accountLog.write("{} {} has been registed with Account No. {}").format(firstName, lastName, self.cardNo)
        cursor, connection = utils.dbConnect()
        querystring = "INSERT into cards(CardNumber, FirstName, LastName, PIN, Balance) VALUES ({}, {}, {}, {}, {})".format(self.cardNo, self.FirstName, self.LastName, self.pin, self.balance)
        cursor.execute(querystring)
        connection.commit()
        print(f"Your card has been created! The details are as follows: \n\nAccount Number: {self.cardNo}\nFirst Name: {self.FirstName}\nLast Name: {self.LastName}\nPIN: {self.pin}\nBalance: ${self.balance}")
        connection.close()

    def getBalance(self):
        if self.balance == 0:
            bal = "NIL"
        else:
            bal = self.balance
        return bal

    def depositMoney(self):
        cardNo = input("Enter your card number: ")
        val = float(input("How much money would you like to deposit: "))
        cursor, connection = utils.dbConnect()
        querystring = f"UPDATE cards SET Balance = Balance + {val} WHERE CardNumber = {cardNo}"
        cursor.execute(querystring)
        connection.commit()
        print(f"{val} was credited into your account.")
        connection.close()

    @staticmethod
    def luhnAlgo(cardNum, mode):
        if len(cardNum) != 15 and len(cardNum) != 16:
            return False
        init = cardNum
        cardNum = list(cardNum)
        sumNo = 0

        for i in range(15):
            if int(i + 1) % 2 != 0:
                cardNum[i] = int(cardNum[i]) * 2
            if int(cardNum[i]) > 0:
                cardNum[i] = int(cardNum[i]) - 9
            sumNo += int(cardNum[i])
        
        if mode == 0:
            return (sumNo + int(cardNum[-1])) % 10 == 0
        elif mode == 1:
            return "".join(map(str, init)) + str((1000 - sumNo) % 10)
    