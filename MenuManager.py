from Menu import Menu
from DBManager import DBManager
from Singleton import SingletonInstance

class MenuManager(SingletonInstance):
    def __init__(self):
        self.DBManager = DBManager.instance()
        self.menuListDB = self.DBManager.getMenuDB()  # menu dictionary 리턴
        self.menuList = []

    def GenerateMenu(self):
        for i in self.menuListDB:
            name = i
            id = self.menuListDB[i]['id']
            price = self.menuListDB[i]['price']
            description = self.menuListDB[i]['description']

            item = Menu(name, id, price, description)
            self.menuList.append(item)
        return self.menuList

    def DisplayMenu(self, UIDict):
        print(UIDict['menuscreen'], end="")
        for i in range(len(self.menuList)):
            item = self.menuList[i]
            print("{}. [{}] {}원\n   : {}".format(i+1, item.name, item.price, item.description))
        print("*****************************")

    def RemoveMenu(menu):
        pass

    def AddMenu():
        pass

    def EditMenu(menu):
        pass

    def CreateMenu():
        pass

