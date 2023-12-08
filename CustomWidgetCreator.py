from CustomWidgets import *
from Singleton import SingletonInstance

class CustomWidgetCreator(SingletonInstance):
    def __init__(self) -> None:
        pass
    
    def menuButton(self, text, menu):
        return MenuButton(text, menu)
    
    def enterNumWindow(self, menu, presenter):
        window = EnterNumWindow()
        def sendsignal():
            presenter.addToCart(menu, window.num.text())
            window.close()
        window.okbutton.clicked.connect(lambda: sendsignal())
        window.exec_()
        
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
        
    def numTicketDialog(self, num, tprice, cart):
        window = NumTicketDialog()
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
    