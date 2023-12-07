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