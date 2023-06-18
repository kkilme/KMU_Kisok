from Menu import Menu
from DBManager import DBManager
from Singleton import SingletonInstance
from MenuFactory import MenuFactory

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
            menutype = self.menuListDB[menuname]['menutype']
            item = MenuFactory.CreateMenu(name, id, price, description, menutype)
            self.menuList.append(item)

    def DisplayMenu(self, idx=-1):
        if idx == -1:
            for i in range(len(self.menuList)):
                item = self.menuList[i]
                print(f"{i+1}. ({item.menutype}) [{item.name}] {item.price}원\n   : {item.description}")
        else:
            item = self.menuList[idx]
            print(f"{idx+1}. [{item.name}] {item.price}원\n   : {item.description}")

    def CreateMenu(self, name, price, desc, menutype):
        newmenu = MenuFactory.CreateMenu(name, self.nextmenuid, price, desc, menutype)
        self.menuList.append(newmenu)
        self.nextmenuid +=1
        self.DBManager.SaveMenuDB(self.menuList)

    def RemoveMenu(self, idx):
        del self.menuList[idx]
        self.DBManager.SaveMenuDB(self.menuList)

    def EditMenu(self, idx, name, price, desc, menutype):
        self.menuList[idx].UpdateMenu(name, price, desc,menutype)
        self.DBManager.SaveMenuDB(self.menuList)

    def getMenu(self, idx):
        return self.menuList[idx]

    def getMenuListLength(self):
        return len(self.menuList)
