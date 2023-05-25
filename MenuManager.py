from Menu import Menu
from DBManager import DBManager

class MenuManager:
    def __init__(self):
        self.DBManager = DBManager()
        self.menuList = self.DBManager.LoadMenuList()

    def DisplayMenu(self):
        testmenu = Menu(1, 2 ,3, 4)
        tp = 0
        for menu in self.menuList:
            tp += menu.price

        pass

    def RemoveMenu(menu):
        pass

    def AddMenu():
        pass

    def EditMenu(menu):
        pass

    def CreateMenu():
        pass

