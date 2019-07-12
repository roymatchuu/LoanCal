from datetime import datetime


class Loan:
    def __init__(self, name, type, amount, interest, dateBorrowed):
        self.name = name
        self.type = type
        self.amount = amount
        self.interest = interest
        self.dateBorrowed = dateBorrowed

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAmount(self):
        return self.amount

    def getInterest(self):
        return self.interest

    def getDate(self):
        return self.dateBorrowed

    def compundedInt(self):
        return self.interest/365;




