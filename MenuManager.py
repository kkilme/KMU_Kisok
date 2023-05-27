from Menu import Menu
from DBManager import DBManager
from Singleton import SingletonInstance

class MenuManager(SingletonInstance):

    def __init__(self):
        self.DBManager = DBManager.instance()
        self.menuListDB = self.DBManager.getMenuDB()  # menu db 가져오기
        self.menuList = []
        self.nextmenuid = self.DBManager.getNextMenuID()
        self.GenerateMenulist()
    
    # menuDB로부터 menu객체를 생성하여 list 형성
    def GenerateMenulist(self):
        for menuname in self.menuListDB:
            name = menuname
            id = self.menuListDB[menuname]['id']
            price = self.menuListDB[menuname]['price']
            description = self.menuListDB[menuname]['description']

            item = Menu(name, id, price, description)
            self.menuList.append(item)

    def DisplayMenu(self):
        for i in range(len(self.menuList)):
            item = self.menuList[i]
            print(f"{i+1}. [{item.name}] {item.price}원\n   : {item.description}")

    def RemoveMenu(menu):
        pass

    def AddMenu():
        pass

    def EditMenu(menu):
        pass

    def CreateMenu():
        pass

    def getMenu(self, idx):
        return self.menuList[idx]

