#Yanyu Xu
#ITP_115, FALL 2019
#Final Project
#yanyuxu@usc.edu

#MenuItem Class
from Menu import Menu
from Diner import Diner

class Waiter(object):
    #Methods
    #__init__
    def __init__(self, Menu):
        # self.diners
        # self.menu
        self.diners = []
        self.menu = Menu
    #addDiner
    def addDiner(self, diner):
        self.diners.append(diner)
    #getNumDiners
    def getNumDiners(self):
        len(self.diners)
    #printDinerStatuses
    def printDinerStatuses(self):
        for diner in self.diners:
            if Diner.STATUSES[diner.getStatus()] == "seated":
                print("Diner who are seated: ")
                print("\t", diner.getName(), "is currently seated.")

        for diner1 in self.diners:
            if Diner.STATUSES[diner1.getStatus()] == "ordering":
                print("Diner who are ordering: ")
                print("\t", diner1.getName(), "is currently ordering.")

        for diner2 in self.diners:
            if Diner.STATUSES[diner2.getStatus()] == "eating":
                print("Diner who are eating: ")
                print("\t", diner2.getName(), "is currently eating.")

        for diner3 in self.diners:
            if Diner.STATUSES[diner3.getStatus()] == "paying":
                print("Diner who are paying: ")
                print("\t", diner3.getName(), "is currently paying.")

        for diner4 in self.diners:
            if Diner.STATUSES[diner4.getStatus()] == "leaving":
                print("Diner who are leaving: ")
                print("\t", diner4.getName(), "is currently leaving.")


    #takeOrders
    def takeOrders(self):
        for people in self.diners:
            if Diner.STATUSES[people.getStatus()] == "ordering":
                self.menu.printMenuItemsByType("Drink")
                ask = int(input("Please order a menu item by selecting a number"))
                while ask > self.menu.getNumMenuItemsByType("Drink") or ask < 0:
                    ask = int(input("Please order a menu item by selecting a number"))
                if ask <= self.menu.getNumMenuItemsByType("Drink"):
                    people.addToOrder(self.menu.getMenuItem("Drink", ask))




                self.menu.printMenuItemsByType("Appetizer")
                ask = int(input("Please order a menu item by selecting a number"))
                while ask > self.menu.getNumMenuItemsByType("Appetizer") or ask < 0:
                    ask = int(input("Please order a menu item by selecting a number"))
                if ask <= self.menu.getNumMenuItemsByType("Appetizer"):
                    people.addToOrder(self.menu.getMenuItem("Appetizer", ask))


                self.menu.printMenuItemsByType("Entree")

                ask = int(input("Please order a menu item by selecting a number"))
                while ask > self.menu.getNumMenuItemsByType("Entree") or ask < 0:
                    ask = int(input("Please order a menu item by selecting a number"))
                if ask <= self.menu.getNumMenuItemsByType("Entree"):
                    people.addToOrder(self.menu.getMenuItem("Entree", ask))

                self.menu.printMenuItemsByType("Dessert")

                ask = int(input("Please order a menu item by selecting a number"))
                while ask > self.menu.getNumMenuItemsByType("Dessert") or ask < 0:
                    ask = int(input("Please order a menu item by selecting a number"))
                if ask <= self.menu.getNumMenuItemsByType("Dessert"):
                    people.addToOrder(self.menu.getMenuItem("Dessert", ask))

                print(people.getName(),"ordered:")
                people.printOrder()


    # ringUpDiners
    def ringUpDiners(self):
        for check in self.diners:
            if Diner.STATUSES[check.getStatus()] == "paying":
                mealCost = check.calculateMealCost()
                print(check.getName(), "your meal cost $", mealCost)


    #removeDoneDiners
    def removeDoneDiners(self):
        for leave in self.diners:
            if Diner.STATUSES[leave.getStatus()] == "leaving":
                print(leave.getName(), "thank you for dining with us! Come again soon!")
            #loop through the list od inners backwards (use a range-based loop)
            for people in range(len(self.diners) - 1,-1,-1):
                if Diner.STATUSES[self.diners[people].getStatus()] == "leaving":
                    del self.diners[people]


    #advanceDiners
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for dinerstatus in self.diners:
            dinerstatus.updateStatus()