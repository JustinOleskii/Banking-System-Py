import random
import mysql.connector
import utils

accountLog = open("acLog.txt", "a+")

class Account:
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.cardNo = None
        self.pin = None
        self.balance = 0

    def getCard(self, cardNo, pin):
        cursor, _ = utils.dbConnect()
        query = "SELECT * FROM cards WHERE CardNumber = %s AND PIN = %s"
        values = (cardNo, pin)
        results = [ ]
        cursor.execute(query, values)

        card = None
        
        for x in cursor:
            results.append(x)

        if len(results) <= 0:
            return None
        else:
            return results[0]

    def createCard(self, firstName, lastName, pin, balance):
        self.firstName = firstName
        self.lastName = lastName
        self.pin = pin
        self.cardNo = "400000" + "".join([str(random.randrange(10)) for i in range(9)])
        self.cardNo = self.luhnAlgo(self.cardNo, 1)
        self.balance = balance
        
        accountLog.write("{} {} has been registered with Account No. {}".format(firstName, lastName, self.cardNo))

        cursor, connection = utils.dbConnect()
        query = "INSERT INTO cards(CardNumber, FirstName, LastName, PIN, Balance) VALUES (%s, %s, %s, %s, %s)"
        values = (self.cardNo, self.firstName, self.lastName, self.pin, self.balance)
        cursor.execute(query, values)
        connection.commit()
        #print(f"Your card has been created! The details are as follows:\n\nAccount Number: {self.cardNo}\nFirst Name: {self.firstName}\nLast Name: {self.lastName}\nPIN: {self.pin}\nBalance: {self.balance}")
        connection.close()
        return True

    def getBalance(self):
        return "NIL" if self.balance <= 0 else self.balance

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
