import random
import mysql.connector
import utils

accountLog = open('acLog.txt', 'w')

class reg:
    def __init__(self, userID = None):
        self.FirstName = None
        self.LastName = None
        self.cardNo = None
        self.pin = None
        self.balance = 0
        
        if userID is not None:
            cursor, _ = utils.dbConnect()
            cursor.execute(f"SELECT CardNumber FROM users WHERE rowid = {userID}")
            self.cardNo = cursor.fetchone()[0]
            
            cursor.execute(f"SELECT FirstName,LastName,PIN,Balance FROM cards WHERE CardNumber = '{self.cardNo}';")
            while True:
                row = cursor.fetchone()
                if row === None:
                    break
                self.FirstName = row[0]
                self.LastName = row[1]
                self.pin = row[2]
                self.balance = row[3]
        
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
        
        accountLog.write(f"{firstName} {lastName} has been registed with Account No. {self.cardNo}")
        
        cursor, connection = utils.dbConnect()
        cursor.execute(f"INSERT into cards(CardNumber, FirstName, LastName, PIN, Balance) VALUES ({self.cardNo}, '{self.FirstName}', '{self.LastName}', {self.pin}, {self.balance})")
        connection.commit()
        connection.execute(f"UPDATE users SET CardNumber = '{self.cardNo}' WHERE FirstName = '{self.firstName}' AND LastName = '{self.LastName}';")
        connection.commit()
        print(f"Your card has been created! The details are as follows: \n\nAccount Number: {self.cardNo}\nFirst Name: {self.FirstName}\nLast Name: {self.LastName}\nPIN: {self.pin}\nBalance: ${self.balance}")
        connection.close()

    def getBalance(self):
        cursor, _ = utils.dbConnect()
        cursor.execute(f'SELECT Balance FROM cards WHERE CardNumber={self.cardNo}')
        balance = cursor.fetchone()[0]
        return balance

    def getCard(self):
        cardNo = self.cardNo
        return cardNo

    def depositMoney(self):
        val = float(input("How much money would you like to deposit: "))
        cursor, connection = utils.dbConnect()
        cursor.execute(f"UPDATE cards SET Balance = Balance + {val} WHERE CardNumber = '{self.cardNo}'")
        connection.commit()
        print(f"{val} was credited into your account.")
        connection.close()

    def transferMoney(self):
        cursor, connection = utils.dbConnect()
        recv = input("Enter card number to transfer money to: ")
        cursor.execute(f"SELECT COUNT(*) FROM cards WHERE CardNumber = '{recv}';")
        if self.luhnAlgo(recv, 0) is False:
            print("Invalid Card Number!")
        elif recv == self.cardNo:
            print("You can't transfer money to yourself!")
        elif cursor.fetchone()[0] == 0:
            print("No such card exists!")
        else:
            cursor.execute(f"SELECT Balance FROM cards WHERE CardNumber='{self.cardNo}'")
            senderBal = cursor.fetchone()[0]
            cursor.execute(f"SELECT Balance FROM cards WHERE CardNumber='{recv}'")
            receiverBal = cursor.fetchone()[0]
            amount = int(input("Enter how much money you want to transfer: "))
            if amount > senderBal:
                print('Value is greater than amount in your savings!')
            else:
                cursor.execute(f"UPDATE cards SET balance={senderBal - amount} WHERE CardNumber='{self.cardNo}'")
                connection.commit()
                cursor.execute(f"UPDATE cards SET balance={receiverBal + amount} WHERE CardNumber='{recv}'")
                connection.commit()
                print("Transfer successful!")
    
    def closeAccount(self):
        cursor, connection = utils.dbConnect()
        cursor.execute(f"DELETE from cards WHERE CardNumber='{self.cardNo}'")
        cursor.execute(f"DELETE from users WHERE CardNumber='{self.cardNo}'")
        connection.commit()
        print("Account has been closed!")

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
    
