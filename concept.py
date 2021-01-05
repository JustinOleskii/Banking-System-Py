import random

def randomNum():
    res = random.randint(1001, 9999)
    return res

accountLog = open('acLog.txt', 'r')

suitable = False
accNo = randomNum()
content = accountLog.readlines()

while not suitable:
    for i in content:
        if accNo == i:
            print("Exists.")
            accNo = randomNum()
        else:
            print("Success.")
            suitable = True

