#Yanyu Xu
#ITP_115, FALL 2019
#Final Project
#yanyuxu@usc.edu

#MenuItem Class
from MenuItem import MenuItem

# variable: MENU_ITEM_TYPES
MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree","Dessert"]
class Menu(object):
    #Methods
    #__init__
    def __init__(self, menu):
        menuItemDictionary = {}
        self.menuItemDictionary = menuItemDictionary
        fileIn = open(menu, "r")
        for line in fileIn:  # one LINE of the file
            line = line.strip()
            wordList = line.split(",")  # words of a SINGLE in a list
            itemObject = MenuItem(wordList[0],wordList[1],wordList[2],wordList[3])
        #extra credit
            if wordList[1] not in menuItemDictionary:  # we have NOT SEEN this word before
                menuItemDictionary[wordList[1]] = [itemObject]
            else:  # word is ALREADY in disctionary
                menuItemDictionary[wordList[1]].append(itemObject)

            #item += 1

        keys = list(menuItemDictionary.keys())
        keys.sort()

        #for word in keys:
        #    print(word)
        #    for item in menuItemDictionary[word]:
        #        print(item)


    #getMenuItem
    def getMenuItem(self, ItemType, pos):
        if ItemType == MENU_ITEM_TYPES[0]:
            return self.menuItemDictionary.get(ItemType)[pos]

        if ItemType == MENU_ITEM_TYPES[1]:
            return self.menuItemDictionary.get(ItemType)[pos]

        if ItemType == MENU_ITEM_TYPES[2]:
            return self.menuItemDictionary.get(ItemType)[pos]

        if ItemType == MENU_ITEM_TYPES[3]:
            return self.menuItemDictionary.get(ItemType)[pos]


    #printMenuItemsByType
    def printMenuItemsByType(self, ItemType):
        count = 0
        if ItemType == MENU_ITEM_TYPES[0]:
            print("----- DRINKS -----")
            for item in self.menuItemDictionary.get("Drink"):
                print(count, ")", item)
                count += 1

        elif ItemType == MENU_ITEM_TYPES[1]:
            print("----- APPETIZERS -----")
            for item in self.menuItemDictionary.get("Appetizer"):
                print(count,")", item)
                count += 1


        elif ItemType == MENU_ITEM_TYPES[2]:
            print("-----ENTREES-----")
            for item in self.menuItemDictionary.get("Entree"):
                print(count,")", item)
                count += 1

        elif ItemType == MENU_ITEM_TYPES[3]:
            print("-----DESSERTS-----")
            for item in self.menuItemDictionary.get("Dessert"):
                print(count,")", item)
                count += 1


    #getNumMenuItemsByType
    def getNumMenuItemsByType(self,ItemType):
        if ItemType == MENU_ITEM_TYPES[0]:
            num = len(self.menuItemDictionary[ItemType])
            return num-1

        #for word in keys:
        #    print(word)
        #    for item in menuItemDictionary[word]:
        #        print(item)

        elif ItemType == MENU_ITEM_TYPES[1]:
            num1 = len(self.menuItemDictionary[ItemType])
            return num1-1

        elif ItemType == MENU_ITEM_TYPES[2]:
            num2 = len(self.menuItemDictionary[ItemType])
            return num2-1

        elif ItemType == MENU_ITEM_TYPES[3]:
            num3 = len(self.menuItemDictionary[ItemType])
            return num3-1