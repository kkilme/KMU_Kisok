from MenuManager import MenuManager
from OrderManager import OrderManager
from AdminUI import AdminUI
from AdminPresenter import AdminPresenter
from CustomWidgetCreator import CustomWidgetCreator
from functools import partial

class KioskPresenter():
    def __init__(self, ui) -> None:
        self.ui = ui
        self.MenuManager = MenuManager.instance()
        self.OrderManager = OrderManager.instance()
        self.WidgetCreator = CustomWidgetCreator.instance()
        
        self.adminUI = AdminUI()
        adminPresenter = AdminPresenter(self.adminUI)
        self.adminUI.assignPresenter(adminPresenter)
        self.adminUI.initStartUI()

    # 관리자 도구 창 염
    def openAdminWindow(self):
        if not self.adminUI.isVisible():
            self.adminUI.show()
    
    # 메뉴를 불러와 UI에 표시    
    def loadMenu(self):
        menulist = self.MenuManager.getMenuList()
        food_x = 0; food_y = 0
        drink_x = 0; drink_y = 0
        set_x = 0; set_y = 0

        def increase_xy(x, y):
            x = x + 1 if y == self.ui.menugridSize - 1 else x
            y = y + 1 if y < self.ui.menugridSize - 1 else 0
            return x, y

        # 알맞은 탭에 메뉴 삽입
        for menu in menulist:
            button = self.WidgetCreator.menuButton(f'{menu.name}\n\n₩{menu.price}', menu)
            button.clicked.connect(partial(self.WidgetCreator.enterNumWindow, menu, self))
            
            if str(getattr(menu, "menutype")) == "Menutype.Food":
                self.ui.replaceWidget(self.ui.FoodGrid, button, food_y, food_x)
                food_x, food_y = increase_xy(food_x, food_y)
            elif str(getattr(menu, "menutype")) == "Menutype.Drink":
                self.ui.replaceWidget(self.ui.DrinkGrid, button, drink_y, drink_x)
                drink_x, drink_y = increase_xy(drink_x, drink_y)
            elif str(getattr(menu, "menutype")) == "Menutype.Set":
                self.ui.replaceWidget(self.ui.SetGrid, button, set_y, set_x)
                set_x, set_y = increase_xy(set_x, set_y)
    
    # 장바구니에 메뉴 추가
    def addToCart(self, menu, quantity):
        table = self.ui.cartTable
        if quantity == '': quantity = 1
        else: quantity = int(quantity)
        row = self.findRowbyString(table, menu.name)
        # 이미 장바구니에 해당 메뉴 있는경우 중첩
        if row != -1:
            current_quantity = int(table.item(row, 2).text())
            new_quantity = current_quantity + quantity
            table.item(row, 2).setText(str(new_quantity))
        else:
            current_row_count = table.rowCount()
            table.setRowCount(current_row_count + 1)
            print(menu.name, menu.price, quantity)
            table.setItem(current_row_count, 0, self.WidgetCreator.tableWidgetItem(menu.name))
            table.setItem(current_row_count, 1, self.WidgetCreator.tableWidgetItem(str(menu.price)))
            table.setItem(current_row_count, 2, self.WidgetCreator.tableWidgetItem(str(quantity)))
            table.setItem(current_row_count, 3, self.WidgetCreator.tableWidgetItem(menu.name))
            
        self.OrderManager.addToCart(menu, quantity)
    
    # 테이블에서 특정 스트링이 들어간 행의 번호를 찾음. 없으면 -1 리턴
    # 메뉴 이름으로 찾기때문에 column은 0번 고정
    def findRowbyString(self, table, string):
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item and string == item.text():
                return row
        return -1