# from PySide2.QtCore import *
import typing
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class MenuButton(QPushButton):
    def __init__(self, text, menu, parent=None):
        super(MenuButton, self).__init__(text, parent)
        self.menu = menu
        self.initUI()

    def initUI(self):
        self.setMinimumSize(120, 120)
        
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        
        self.setStyleSheet(u"background-color:white")
        
class EnterNumWindow(QDialog):
    def __init__(self, parent: QWidget=None) -> None:
        super(EnterNumWindow, self).__init__(parent=parent)
        self.initUI()
    
    def initUI(self):
        self.resize(435,140)
        font = QFont()
        font.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        self.setFont(font)
        
        self.desc = QLabel("수량을 입력하세요 (최대 9): ", self)
        self.desc.setGeometry(QRect(20, 10, 281, 51))
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font1.setPointSize(14)
        self.desc.setFont(font1)
        
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(20, 80, 401, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.cancelbutton = QPushButton("취소", self.horizontalLayoutWidget)
        self.cancelbutton.setMaximumSize(QSize(120, 16777215))
        self.cancelbutton.clicked.connect(self.close)

        self.okbutton = QPushButton("확인",self.horizontalLayoutWidget)
        self.okbutton.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.okbutton)
        self.horizontalLayout.addWidget(self.cancelbutton)

        self.num = QLineEdit(self)
        self.num.setGeometry(QRect(310, 20, 111, 31))
        self.num.setAlignment(Qt.AlignCenter)
        self.num.setPlaceholderText("1")
        self.num.setValidator(QIntValidator(1,9,self))
        
        self.setWindowTitle("수량을 입력하세요")