class Account:
    __balance = 0

    def __init__(self,balance):
        self.__balance = balance

    def getbalance(self):
        return self.__balance

    def deposit(self,amt):
        if amt > 0:
            self.__balance = self.__balance + amt
            return True
        else:
            return False

    def withdraw(self,amt):
        if amt <= self.__balance:
            self.__balance = self.__balance - amt
            return True
        else:
            return False

class Customer:
    __firstname = ""
    __lastname = ""
    __account = Account(10000)

    def __init__(self,firstname,lastname):
        self.__firstname = firstname
        self.__lastname = lastname

    def getfirstname(self):
        return self.__firstname

    def getlastname(self):
        return self.__lastname

    def getaccount(self):
        return self.__account

    def setaccount(self,acct):
        self.__account = acct

class Bank:
    __customers = []
    __numberofcustomers = 0
    __bankname = ""

    def __init__(self,bankname):
        self.__bankname = bankname

    def addcustomers(self,firstname,lastname):
        self.__customers.append(Customer(firstname,lastname))
        self.__numberofcustomers += 1

    def getnumberofcustomers(self):
        return self.__numberofcustomers

    def getcustomers(self,index):
        return self.__customers[index]