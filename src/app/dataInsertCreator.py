from datetime import datetime, timedelta
import math
import random
import string
import sys
import databaseConnection

class randomGenerator:
    def __init__(self, initialID):
        self.id = initialID

    def generateRandomString(self, length = 0):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(length))

    def generateRandomHexString(self, length = 0):
        return ''.join(random.SystemRandom().choice(string.hexdigits) for _ in range(length)).lower()

    def generateRandomDatetime(self, min_year=1970, max_year=datetime.now().year):
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
        length = random.randint(5, 20)
        return self.generateRandomString(length)

    def getFirstOrLastName(self):
        length = random.randint(5, 20)
        return self.generateRandomString(length).capitalize()

    def getEmail(self):
        length = random.randint(5, 20)
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
            hexString += self.generateRandomHexString(4)

        return hexString

    def getHash(self):
        return self.generateRandomHexString(64)

    def getCompanyName(self):
        length = random.randint(5, 20)
        return self.generateRandomString(length).capitalize()

    def getBackgroundColor(self):
        return "#" + self.generateRandomHexString(6)

    def getCreateTime(self):
        return str(self.generateRandomDatetime()).split(".")[0]

    def getUpdateTime(self):
        rng = random.randint(0, 9)
        return "'" + str(self.generateRandomDatetime()).split(".")[0] + "');" if (rng >= 2) else "null);"


rng = randomGenerator(int(sys.argv[2]))
db = databaseConnection.databaseConnection()

iterations = 0
while True if len(sys.argv) <= 3 else (True if iterations < int(sys.argv[3]) else False):
    if(iterations % 1000 == 0):
        print(iterations, "data inserted.")
        
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

    db.insert(sql)
    iterations += 1
