from datetime import datetime, timedelta
import math
import random
import string
import sys

class randomGenerator:
    def __init__(self, initialID):
        self.id = initialID

    def generateRandomString(self, length = 0):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(length))

    def generateRandomHexString(self, length = 0):
        return ''.join(random.SystemRandom().choice(string.hexdigits) for _ in range(length)).lower()

    def generateRandomDatetime(self, min_year=1900, max_year=datetime.now().year):
        # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random.random()

    def getID(self):
        actualID = self.id
        self.id += 1
        return actualID

    def getUsername(self):
        length = random.randint(1, 20)
        return self.generateRandomString(length)

    def getFirstOrLastName(self):
        length = random.randint(1, 20)
        return self.generateRandomString(length).capitalize()

    def getEmail(self):
        length = random.randint(1, 20)
        return self.generateRandomString(length) + "@" + self.generateRandomString(length) + ".com"

    def getGender(self):
        return "F" if (random.randint(0, 1) == 0) else "M"

    def getIPV4(self):
        ip = str(random.randint(0, 255)) + "."
        ip += str(random.randint(0, 255)) + "."
        ip += str(random.randint(0, 255)) + "."
        ip += str(random.randint(0, 255))
        return ip

    def getIPV6(self):
        hexString = ""
        for i in range(8):
            if i != 0:
                hexString += ":"
            hexString += rng.generateRandomHexString(4)

        return hexString

    def getHash(self):
        return rng.generateRandomHexString(64)

    def getCompanyName(self):
        length = random.randint(5, 20)
        return rng.generateRandomString(length).capitalize()

    def getBackgroundColor(self):
        return "#" + rng.generateRandomHexString(6)

    def getCreateTime(self):
        return str(rng.generateRandomDatetime())

    def getUpdateTime(self):
        rng = random.randint(0, 9)
        return "'" + str(self.generateRandomDatetime()) + "');" if (rng >= 2) else "null);"


with open("../sql/randomDataInsert.sql", "w") as dataFile:
    rng = randomGenerator(int(sys.argv[1]))

    iterations = 0
    while True if len(sys.argv) <= 2 else (True if iterations < int(sys.argv[2]) + 1 else False):
        if(iterations % 1000 == 0):
            print(iterations, "random inserts generated.")
            

        sql = "insert into user_information "
        sql += "(id, username, first_name, last_name, email, gender, ip_address_v4, ip_address_v6, hash, company_name, background_color, create_time, update_time) "
        sql += "values ("
        sql += str(rng.getID()) + ", "
        sql += "'" + rng.getUsername() + "', "
        sql += "'" + rng.getFirstOrLastName() + "', "
        sql += "'" + rng.getFirstOrLastName() + "', "
        sql += "'" + rng.getEmail() + "', "
        sql += "'" + rng.getGender() + "', "
        sql += "'" + rng.getIPV4() + "', "
        sql += "'" + rng.getIPV6() + "', "
        sql += "'" + rng.getHash() + "', "
        sql += "'" + rng.getCompanyName() + "', "
        sql += "'" + rng.getBackgroundColor() + "', "
        sql += "'" + rng.getCreateTime() + "', "
        sql += rng.getUpdateTime()

        dataFile.write(sql + "\n")
        iterations += 1

dataFile.close()