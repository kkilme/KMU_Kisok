from OrderDAO import OrderDAO
from MenuDAO import MenuDAO
from Singleton import SingletonInstance
from Menu import Menu, Menutype, stringToMenutype

class MenuManager(SingletonInstance):

    def __init__(self):
        self.OrderDAO = OrderDAO.instance()
        self.MenuDAO = MenuDAO.instance()
        # self.menuListDB = self.DBManager.getMenuDB()  # menu db 가져오기
        self.menuList = []
        self.loadMenu()
    
    # menuDAO로부터 메뉴를 읽어와 menu list 생성
    def loadMenu(self):
        self.menuList.clear()
        data = self.MenuDAO.getMenuDB()
        for menuid, name, price, menutype, islegacy in data:
            if islegacy: continue
            menu = Menu(menuid, name, price, stringToMenutype(menutype))
            self.menuList.append(menu)

    def getMenuList(self) -> list[Menu]:
        return self.menuList
    