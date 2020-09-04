#Yanyu Xu
#ITP_115, FALL 2019
#Final Project
#yanyuxu@usc.edu

#MenuItem Class
from MenuItem import MenuItem
class Diner(object):
    #class variable
    #STATUSES
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    #Methods

    #__init__
    def __init__(self, potentialDiner):
        # instance attributes
        # self.name
        self.name = potentialDiner
        # self.order
        self.order = []
        # self.status
        self.status = 0
        Diner.STATUSES

    #define getters and setters
    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

    def getStatus(self):
        return self.status

    def setStatus(self,s):
        self.status = s

    #updateStatus
    def updateStatus(self):
        self.status += 1

    #addToOrder
    def addToOrder(self, item):
        self.order.append(item)

    #printOrder
    def printOrder(self):
        for item in self.order:
            print("-",item)
    #calculateMealCost
    def calculateMealCost(self):
        totalCost = 0
        for price in self.order:
            totalCost += (price.getPrice())
        return float(totalCost)

    #__str__
    def __str__(self):
        msg = "Diner " + self.name + " is currently " + STATUSES[self.status]
        msg += "\n\t Diner " + self.name + " is currently " + STATUSES[self.status]