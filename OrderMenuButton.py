# from PySide2.QtCore import *
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QPushButton

class OrderMenuButton(QPushButton):
    def __init__(self, text='', parent=None):
        super(OrderMenuButton, self).__init__(text, parent)
        self.initUI()

    def initUI(self):
        self.setMinimumSize(120, 120)
        
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        
        self.setStyleSheet(u"background-color:white")