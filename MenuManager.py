from Menu import Menu
from DBManager import DBManager
from Singleton import SingletonInstance

class MenuManager(SingletonInstance):
    def __init__(self):
        self.DBManager = DBManager.instance()
        self.menuList = self.DBManager.LoadMenuList()

    def DisplayMenu(self):
        pass

    def RemoveMenu(menu):
        pass

    def AddMenu():
        pass

    def EditMenu(menu):
        pass

    def CreateMenu():
        pass

