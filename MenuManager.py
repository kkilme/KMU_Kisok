from MenuDAO import MenuDAO
from Singleton import SingletonInstance
from Menu import Menu, Menutype, stringToMenutype

class MenuManager(SingletonInstance):

    def __init__(self):
        self.MenuDAO = MenuDAO.instance()
        self.menuList = []
        self.menutypeList = []
        self.loadMenu()
        self.loadMenutype()
    
    def refresh(self):
        self.loadMenu()
        self.loadMenutype()
    
    # menuDAO로부터 메뉴를 읽어와 menu list 생성
    def loadMenu(self):
        self.menuList.clear()
        data = self.MenuDAO.getMenuDB()
        for menuid, name, price, menutype, islegacy in data:
            if islegacy: continue
            menu = Menu(menuid, name, price, stringToMenutype(menutype))
            self.menuList.append(menu)

    def editMenu(self, id, name, price, menutype):
        self.MenuDAO.editMenu(id, name, price, menutype)
        self.refresh()
        
    def deleteMenu(self, id):
        self.MenuDAO.deleteMenu(id)
        self.refresh()
    
    def createMenu(self, name, price, menutype):
        self.MenuDAO.createMenu(name, price, menutype)
        self.refresh()
        
    def loadMenutype(self):
        self.menutypeList.clear()
        self.menutypeList = list(Menutype)
    
    def getMenuList(self) -> list[Menu]:
        return self.menuList
    
    def getMenutypeList(self) -> list[Menutype]:
        return self.menutypeList

if __name__ == "__main__":
    l = list(Menutype)
    for i in l:
        print(i)
    print(li for li in l)