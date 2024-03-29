# from PySide2.QtCore import *
import typing
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

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
        
class MenuQuantityWindow(QDialog):
    def __init__(self, parent: QWidget=None) -> None:
        super(MenuQuantityWindow, self).__init__(parent=parent)
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
    
class CartItemManageButton(QPushButton):
    def __init__(self, text, parent=None):
        super(CartItemManageButton, self).__init__(text, parent)
        self.initUI()

    def initUI(self):
        font = QFont()
        font.setPointSize(7)
        self.setFont(font)
        
        self.setStyleSheet(u"background-color:yellow")


class NumTicket(QDialog):
    def __init__(self,):
        super(NumTicket, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.resize(480, 580)
        self.setWindowTitle("Order Complete")
        
        self.title = QLabel("주문이 완료되었습니다.", self)
        self.title.setGeometry(QRect(0, 30, 479, 45))
        font = QFont()
        font.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font.setPointSize(19)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        
        self.numticket = QLabel("1", self)
        self.numticket.setGeometry(QRect(0, 100, 479, 150))
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(52)
        font1.setBold(True)
        font1.setWeight(75)
        self.numticket.setFont(font1)
        self.numticket.setAlignment(Qt.AlignCenter)
        
        self.tabletitle = QLabel("주문 내역", self)
        self.tabletitle.setGeometry(QRect(0, 250, 481, 51))
        font2 = QFont()
        font2.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font2.setPointSize(16)
        self.tabletitle.setFont(font2)
        self.tabletitle.setAlignment(Qt.AlignCenter)
        
        self.orderitemTable = QTableWidget(self)
        self.orderitemTable.setGeometry(QRect(50, 310, 381, 201))
        self.orderitemTable.setColumnCount(3)
        self.orderitemTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.orderitemTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.orderitemTable.setHorizontalHeaderLabels(["품명", "가격", "수량"])
        
        self.totalprice = QLabel("총 가격: 0 ₩", self)
        self.totalprice.setGeometry(QRect(290, 520, 171, 31))
        font3 = QFont()
        font3.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font3.setPointSize(12)
        self.totalprice.setFont(font3)
        self.totalprice.setAlignment(Qt.AlignCenter)
        
class MenuEditor(QDialog):
    def __init__(self, menuname, menuprice, menutype, allmenutype):
        super(MenuEditor, self).__init__()
        self.initUI()
        self.menunameline.setText(menuname)
        self.menupriceline.setText(menuprice)
        for t in allmenutype:
            self.menutypecombobox.addItem(str(t)[9:])
        self.menutypecombobox.setCurrentText(menutype)
        
    def initUI(self):
        self.resize(700, 200)
        self.setWindowTitle("Menu Editor")
        font = QFont()
        font.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font.setPointSize(9)
        self.setFont(font)
        
        self.label = QLabel("수정 사항을 입력하세요", self)
        self.label.setGeometry(QRect(200, 20, 291, 21))
        
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.menunameline = QLineEdit(self)
        self.menunameline.setGeometry(QRect(100, 100, 113, 21))
        
        self.menunamelabel = QLabel("메뉴명", self)
        self.menunamelabel.setGeometry(QRect(100, 70, 111, 21))
        font2 = QFont()
        font2.setPointSize(9)
        self.menunamelabel.setFont(font2)
        self.menunamelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.menupriceline = QLineEdit(self)
        self.menupriceline.setGeometry(QRect(290, 100, 113, 21))
        validator = QIntValidator(self)
        self.menupriceline.setValidator(validator)
        
        self.menupricelabel = QLabel("메뉴 가격", self)
        self.menupricelabel.setGeometry(QRect(290, 70, 111, 21))
        self.menupricelabel.setFont(font2)
        self.menupricelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.menutypelabel = QLabel("메뉴 타입", self)
        self.menutypelabel.setGeometry(QRect(480, 70, 111, 21))
        self.menutypelabel.setFont(font2)
        self.menutypelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.menutypecombobox = QComboBox(self)
        self.menutypecombobox.setGeometry(QRect(480, 100, 111, 21))
        
        self.okButton = QPushButton("확인", self)
        self.okButton.setGeometry(QRect(210, 150, 93, 28))
        self.okButton.setFont(font2)
        
        self.cancelButton = QPushButton("취소", self)
        self.cancelButton.setGeometry(QRect(400, 150, 93, 28))
        self.cancelButton.setFont(font2)
        self.cancelButton.clicked.connect(self.close)

class MenuCreator(QDialog):
    def __init__(self, allmenutype):
        super(MenuCreator, self).__init__()
        self.initUI()
        for t in allmenutype:
            self.menutypecombobox.addItem(str(t)[9:])   
        self.menutypecombobox.setCurrentIndex(0)
        
    def initUI(self):
        self.resize(700, 200)
        self.setWindowTitle("Menu Editor")
        font = QFont()
        font.setFamily(u"\ub098\ub214\ubc14\ub978\uace0\ub515")
        font.setPointSize(9)
        self.setFont(font)
        
        self.label = QLabel("메뉴의 정보를 입력하세요", self)
        self.label.setGeometry(QRect(200, 20, 291, 21))
        
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.menunameline = QLineEdit(self)
        self.menunameline.setGeometry(QRect(100, 100, 113, 21))
        
        self.menunamelabel = QLabel("메뉴명", self)
        self.menunamelabel.setGeometry(QRect(100, 70, 111, 21))
        font2 = QFont()
        font2.setPointSize(9)
        self.menunamelabel.setFont(font2)
        self.menunamelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.menupriceline = QLineEdit(self)
        self.menupriceline.setGeometry(QRect(290, 100, 113, 21))
        validator = QIntValidator(self)
        self.menupriceline.setValidator(validator)
        
        self.menupricelabel = QLabel("메뉴 가격", self)
        self.menupricelabel.setGeometry(QRect(290, 70, 111, 21))
        self.menupricelabel.setFont(font2)
        self.menupricelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.menutypelabel = QLabel("메뉴 타입", self)
        self.menutypelabel.setGeometry(QRect(480, 70, 111, 21))
        self.menutypelabel.setFont(font2)
        self.menutypelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.menutypecombobox = QComboBox(self)
        self.menutypecombobox.setGeometry(QRect(480, 100, 111, 21))
        
        self.okButton = QPushButton("확인", self)
        self.okButton.setGeometry(QRect(210, 150, 93, 28))
        self.okButton.setFont(font2)
        
        self.cancelButton = QPushButton("취소", self)
        self.cancelButton.setGeometry(QRect(400, 150, 93, 28))
        self.cancelButton.setFont(font2)
        self.cancelButton.clicked.connect(self.close)
        
        self.errormessage = QLabel("", self)
        self.errormessage.setGeometry(QRect(213, 124, 281, 21))
        self.errormessage.setFont(font2)
        self.errormessage.setStyleSheet(u"color:red")
        self.errormessage.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = NumTicket()
    mywindow.show()
    app.exec_()