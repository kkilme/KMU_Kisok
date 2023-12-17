from MenuManager import MenuManager
from OrderManager import OrderManager
from AdminPresenter import AdminPresenter
from CustomWidgetCreator import CustomWidgetCreator
from PresenterTemplate import PresenterTemplate
from functools import partial

class UserPresenter(PresenterTemplate):
    def __init__(self, ui) -> None:
        self.ui = ui
        self.MenuManager = MenuManager.instance()
        self.OrderManager = OrderManager.instance()
        self.WidgetCreator = CustomWidgetCreator.instance()
        
        self.adminPresenter = AdminPresenter(self)
        self.nextnumticketnum = int(self.OrderManager.getTodayOrderCount()) + 1

    # 관리자 도구 창 염
    def openAdminWindow(self):
        self.adminPresenter.openUI()
    
    # 메뉴를 불러와 UI에 표시    
    def loadMenu(self):
        menulist = self.MenuManager.getMenuList()
        self.ui.clearGridLayout()
        self.ui.fillDummyWidgetOnGrid()
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
            button.clicked.connect(partial(self.enterMenuQuantity, menu))
            
            if str(menu.menutype) == "Menutype.Food":
                self.ui.replaceWidget(self.ui.FoodGrid, button, food_y, food_x)
                food_x, food_y = increase_xy(food_x, food_y)
            elif str(menu.menutype) == "Menutype.Drink":
                self.ui.replaceWidget(self.ui.DrinkGrid, button, drink_y, drink_x)
                drink_x, drink_y = increase_xy(drink_x, drink_y)
            elif str(menu.menutype) == "Menutype.Set":
                self.ui.replaceWidget(self.ui.SetGrid, button, set_y, set_x)
                set_x, set_y = increase_xy(set_x, set_y)
    
    def enterMenuQuantity(self, menu):
        window = self.WidgetCreator.menuQuantityWindow()
        def sendsignal():
            self.addToCart(menu, window.num.text())
            window.close()
        window.okbutton.clicked.connect(lambda: sendsignal())
        window.exec_()
        
    
    # 장바구니에 메뉴 추가
    def addToCart(self, menu, quantity):
        table = self.ui.cartTable
        if quantity == '': quantity = 1
        else: quantity = int(quantity)
        row_cur = self.ui.findRowinCart(menu.name)
        # 이미 장바구니에 해당 메뉴 있는경우 중첩
        if row_cur != -1:
            current_quantity = int(table.item(row_cur, 2).text())
            new_quantity = current_quantity + quantity
            table.item(row_cur, 2).setText(str(new_quantity))
        else:
            current_row_count = table.rowCount()
            table.setRowCount(current_row_count + 1)
            table.setItem(current_row_count, 0, self.WidgetCreator.tableWidgetItem(menu.name))
            table.setItem(current_row_count, 1, self.WidgetCreator.tableWidgetItem(str(menu.price)))
            table.setItem(current_row_count, 2, self.WidgetCreator.tableWidgetItem(str(quantity)))
            decreaseButton = self.WidgetCreator.cartItemManageButton(managetype="decrease")
            decreaseButton.clicked.connect(lambda: self.decreaseCartItem(decreaseButton))
            increaseButton = self.WidgetCreator.cartItemManageButton(managetype="increase")
            increaseButton.clicked.connect(lambda: self.increaseCartItem(increaseButton))
            table.setCellWidget(current_row_count, 3, decreaseButton)
            table.setCellWidget(current_row_count, 4, increaseButton)
            
        self.OrderManager.addToCart(menu, quantity)
        
        self.updateTotalPrice()
    
    # 장바구니 메뉴 개수 감소
    def decreaseCartItem(self, signal_sender):
        table = self.ui.cartTable
        row = -1
        # 버튼이 들어있는 행 찾음
        for i in range(table.rowCount()):
            if table.cellWidget(i, 3) == signal_sender:
                row = i
        if row == -1:
            print("Couldn't find row")
            return
        
        menuname = table.item(row, 0).text()
        cur = table.item(row, 2).text()
        if cur == "1":
            table.removeRow(row)
        else:
            added = int(cur) - 1
            table.item(row, 2).setText(str(added))
        
        self.OrderManager.decreaseCartItem(menuname)
        self.updateTotalPrice()
    
    # 장바구니 메뉴 개수 증가
    def increaseCartItem(self, signal_sender):
        table = self.ui.cartTable
        row = -1
        # 버튼이 들어있는 행 찾음
        for i in range(table.rowCount()):
            if table.cellWidget(i, 4) == signal_sender:
                row = i
        if row == -1:
            print("Couldn't find row")
            return
        
        cur = table.item(row, 2).text()
        added = int(cur) + 1
        table.item(row, 2).setText(str(added))
        
        menuname = table.item(row, 0).text()
        self.OrderManager.increaseCartItem(menuname)
        self.updateTotalPrice()
        
    
    # 장바구니 초기화
    def clearCart(self):
        table = self.ui.cartTable
        for i in range(table.rowCount()-1,-1,-1):
            table.removeRow(i)
        self.OrderManager.clearCart()
        self.updateTotalPrice()
    
    # 현재 총 가격 업데이트
    def updateTotalPrice(self):
        tprice = self.OrderManager.calculateTotalPrice()
        self.ui.totalPriceLabel.setText(f"총 가격: {tprice} ₩")

    # 주문 진행
    def processOrder(self):
        cart = self.OrderManager.getCart()
        if len(cart) == 0: return
        self.OrderManager.processOrder()
        
        num = self.nextnumticketnum
        tprice = self.OrderManager.calculateTotalPrice()
        self.adminPresenter.addOrderQueueItem(cart, num, tprice)
        window = self.WidgetCreator.numTicket(num, tprice, cart)
        self.nextnumticketnum += 1
        window.exec_()
        self.ui.changeUI()