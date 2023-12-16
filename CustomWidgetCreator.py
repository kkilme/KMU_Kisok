from CustomWidgets import *
from Singleton import SingletonInstance

class CustomWidgetCreator(SingletonInstance):
    def __init__(self) -> None:
        pass
    
    def menuButton(self, text, menu):
        return MenuButton(text, menu)
    
    def menuQuantityWindow(self):
        window = MenuQuantityWindow()
        return window
        
        
    def tableWidgetItem(self, text):
        widget = QTableWidgetItem(text)
        widget.setTextAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(7)
        widget.setFont(font)
        return widget
    
    def cartItemManageButton(self, managetype):
        if managetype == "decrease":
            return CartItemManageButton("-")
        elif managetype == "increase":
            return CartItemManageButton("+")
        elif managetype == "remove":
            return CartItemManageButton("x")
        elif managetype == "edit":
            return CartItemManageButton("수정")
        
    def numTicket(self, num, tprice, cart):
        window = NumTicket()
        table = window.orderitemTable
        window.numticket.setText(str(num))
        window.totalprice.setText(f'합계: {tprice} ₩')
        table.setRowCount(len(cart))
        
        for i, data in enumerate(cart.values()):
            menu = data['menu']
            table.setItem(i, 0, self.tableWidgetItem(menu.name))
            table.setItem(i, 1, self.tableWidgetItem(str(menu.price)))
            table.setItem(i, 2, self.tableWidgetItem(str(data['quantity'])))
            
        return window
    
    def menuEditor(self, name, price, type, menutypes):
        window = MenuEditor(name, price, type, menutypes)
        return window
        
    def menuCreator(self, menutypes):
        window = MenuCreator(menutypes)
        return window