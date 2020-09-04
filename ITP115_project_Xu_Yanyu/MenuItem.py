#Yanyu Xu
#ITP_115, FALL 2019
#Final Project
#yanyuxu@usc.edu

#MenuItem Class

class MenuItem(object):

    #Methods
    #__init__
    def __init__(self, name, ItemType, price, description):
        self.name = name
        self.type = ItemType
        self.price = float(price)
        self.description = description

    # Instance attributes
    # self.name:a string representing the name of the MenuItem
    # self.type: a string presenting the type of item
    # self.price: a float representing the price of the item
    # self.description: a string containing a description of the item
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def setDescription(self):
        return self.description
    #__str__
    def __str__(self):
        msg = self.name + " ( " + self.type + " ) : $" + str(self.price)
        msg += "\n\t" + self.description

        return  msg
